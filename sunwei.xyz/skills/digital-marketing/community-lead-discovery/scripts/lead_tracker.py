#!/usr/bin/env python3
"""Window math and carry/cool/drop bookkeeping for a recurring lead digest.

  window  compute the scan window for this run (start = previous digest end)
  update  apply this window's observations to the lead state and propose
          status changes; you still review every proposal and record why

State file (JSON list), one object per tracked thread:
  {"id": "1abc2de", "source": "reddit/ObsidianMD", "url": "...", "title": "...",
   "score": 72, "status": "CARRY", "quiet": 0, "metric": 14,
   "last_activity_utc": "2026-09-27T15:54:10Z", "brand_mentioned": false, "own": false}
Observations (JSON object keyed by id), from this window's scan:
  {"1abc2de": {"metric": 14, "last_activity_utc": "...", "brand_mentioned": false,
               "rescore": 60},
   "9xyz": {"new": true, "score": 58, "source": "...", "url": "...", "title": "..."}}
`metric` is whatever measures activity on that source (comments, replies,
views, points). `rescore` is your fresh 0-100 score when something changed.

Default rules (from the digests this skill was distilled from; tune with flags):
  bands at discovery: >=90 URGENT candidate, 80-89 HIGH, 50-79 MEDIUM,
  <50 WEAK (not listed). A lead keeps its band while cooling until demoted.
  quiet window (no metric change, no newer activity): score -= --decay
  URGENT/HIGH: 3rd consecutive quiet window -> demote one band; 4th -> DROP
  MEDIUM: 1st quiet -> cooling; 2nd -> soft-DROP; 3rd -> DROP
  activity resumes on a soft-DROP -> soft-DROP cancelled, CARRY, rescore
  DROP + activity + rescore >= 50 -> REVIVE
  brand already mentioned in the thread -> LISTEN-ONLY (never post again)
  own posts -> OWN (track only, never a lead)

Examples:
  python3 lead_tracker.py window --prev-end 2026-09-27T16:11:55Z --tz Asia/Shanghai
  python3 lead_tracker.py update --state leads.json --obs obs.json --md changes.md
"""
import argparse, datetime as dt, json, sys

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None


def band(s):
    return "URGENT" if s >= 90 else "HIGH" if s >= 80 else "MEDIUM" if s >= 50 else "WEAK"


def parse(ts):
    return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")) if ts else None


def cmd_window(a):
    now = parse(a.now) if a.now else dt.datetime.now(dt.timezone.utc)
    start = parse(a.prev_end) if a.prev_end else now - dt.timedelta(hours=a.hours)
    tz = ZoneInfo(a.tz) if ZoneInfo else dt.timezone.utc
    local = now.astimezone(tz)
    slot = local.replace(minute=0, second=0, microsecond=0, hour=(local.hour // a.hours) * a.hours)
    print(f"AFTER={int(start.timestamp())}\nBEFORE={int(now.timestamp())}")
    print(f"PRIOR_DIGEST_END_UTC={start.strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print(f"NOW_UTC={now.astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    print(f"NOW_LOCAL={local.isoformat(timespec='seconds')}")
    print(f"LABEL={slot.strftime('%Y-%m-%d %H:%M')} {a.tz}")


def cmd_update(a):
    state = json.load(open(a.state, encoding="utf-8"))
    obs = json.load(open(a.obs, encoding="utf-8"))
    by = {l["id"]: l for l in state}
    changes = []
    for lid, o in obs.items():
        if o.get("new") and lid not in by:
            l = {"id": lid, "score": o.get("score", 0), "band": o.get("band") or band(o.get("score", 0)), "status": "NEW", "quiet": 0, "metric": o.get("metric", 0),
                 "last_activity_utc": o.get("last_activity_utc"), "brand_mentioned": o.get("brand_mentioned", False),
                 "own": o.get("own", False), **{k: o[k] for k in ("source", "url", "title") if k in o}}
            state.append(l); by[lid] = l
            changes.append((lid, "-", "NEW", f"score {l['score']} ({band(l['score'])})"))
    for l in state:
        if l["status"] == "NEW" and l["id"] in obs and obs[l["id"]].get("new"):
            continue
        o = obs.get(l["id"])
        l.setdefault("band", band(l["score"]))
        before = (l["status"], l["score"], l["band"])
        if l.get("own"):
            l["status"] = "OWN"
        if o is None:
            if l["status"] not in ("DROP", "OWN"):
                changes.append((l["id"], l["status"], l["status"], "NOT CHECKED this window: say so in Coverage"))
            continue
        if o.get("brand_mentioned"):
            l["brand_mentioned"] = True
        newer = o.get("last_activity_utc") and (not l.get("last_activity_utc") or parse(o["last_activity_utc"]) > parse(l["last_activity_utc"]))
        active = (o.get("metric", l.get("metric", 0)) > l.get("metric", 0)) or bool(newer)
        l["metric"] = o.get("metric", l.get("metric", 0))
        l["last_activity_utc"] = o.get("last_activity_utc") or l.get("last_activity_utc")
        note = []
        if l["status"] == "OWN":
            note.append("own post: track only")
        elif active:
            l["quiet"] = 0
            if "rescore" in o:
                l["score"] = o["rescore"]; l["band"] = band(l["score"])
            if l["status"] == "SOFT_DROP":
                l["status"] = "CARRY"; note.append("activity resumed: soft-DROP cancelled, rescore")
            elif l["status"] == "DROP":
                if l["score"] >= 50:
                    l["status"] = "CARRY"; note.append("REVIVE")
                else:
                    note.append("activity but still <50: archive-watch")
            else:
                l["status"] = "CARRY"; note.append("active")
            if "rescore" not in o:
                note.append("no rescore given: score unchanged")
            if l["score"] < 50 and l["status"] != "DROP":
                note.append("below 50: archive-listen only, do not engage")
        elif l["status"] != "DROP":
            l["quiet"] += 1
            l["score"] = max(0, l["score"] - a.decay)
            q, b0 = l["quiet"], l["band"]
            if b0 in ("URGENT", "HIGH"):
                if q >= 4:
                    l["score"] = min(l["score"], 49); l["status"] = "DROP"; note.append(f"quiet x{q}: DROP")
                elif q == 3:
                    l["band"] = "HIGH" if b0 == "URGENT" else "MEDIUM"
                    l["status"] = "CARRY"; note.append(f"quiet x{q}: demote {b0}->{l['band']}")
                else:
                    l["status"] = "CARRY"; note.append(f"quiet x{q}: cooling")
            else:
                if q >= 3 or l["score"] < 50:
                    l["status"] = "DROP"; note.append(f"quiet x{q}: DROP")
                elif q == 2:
                    l["status"] = "SOFT_DROP"; note.append("quiet x2: soft-DROP")
                else:
                    l["status"] = "CARRY"; note.append("quiet x1: cooling")
        if l.get("brand_mentioned") and l["status"] != "OWN":
            note.append("brand already in thread: LISTEN-ONLY, do not post again")
        if l["status"] == "DROP" or l["score"] < 50:
            l["band"] = "WEAK" if l["status"] != "OWN" else l["band"]
        changes.append((l["id"], f"{before[0]} {before[2]} {before[1]}", f"{l['status']} {l['band']} {l['score']}", "; ".join(note)))
    json.dump(state, open(a.out or a.state, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lines = ["| id | before | after | why |", "|---|---|---|---|"] + [f"| `{c[0]}` | {c[1]} | {c[2]} | {c[3]} |" for c in changes]
    table = {}
    for l in state:
        if l["status"] in ("DROP", "OWN") or l["score"] < 50:
            continue
        table.setdefault(l.get("band") or band(l["score"]), []).append(l)
    for b in ("URGENT", "HIGH", "MEDIUM"):
        lines.append(f"\n## {b}\n")
        rows = sorted(table.get(b, []), key=lambda l: -l["score"])
        lines += [f"- `{l['id']}` {l.get('source','')} ~{l['score']} {l['status']} {l.get('url','')}" for l in rows] or ["None."]
    md = "\n".join(lines)
    if a.md:
        open(a.md, "w", encoding="utf-8").write(md + "\n")
    print(md)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("window"); s.add_argument("--prev-end"); s.add_argument("--now"); s.add_argument("--hours", type=int, default=8); s.add_argument("--tz", default="UTC")
    s = sub.add_parser("update"); s.add_argument("--state", required=True); s.add_argument("--obs", required=True); s.add_argument("--decay", type=int, default=2); s.add_argument("--out"); s.add_argument("--md")
    a = ap.parse_args()
    (cmd_window if a.cmd == "window" else cmd_update)(a)


if __name__ == "__main__":
    main()
