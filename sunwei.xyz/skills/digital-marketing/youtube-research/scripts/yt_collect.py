#!/usr/bin/env python3
"""Collect YouTube search results, metadata and top comments with yt-dlp.

Pipeline (each step writes a file the next step reads):
  search   queries -> search.tsv   (views, id, title, channel, duration, queries)
  pick     search.tsv -> ids.txt   (relevance include/exclude regex, top N by views)
  fetch    ids.txt -> OUT/<id>.info.json  (metadata + comments; no video download)
  rows     OUT/*.info.json -> rows.json   (title, views, date, channel, subs,
                                           comment count, chapters, url)
  tag      OUT/*.info.json + taxonomy.json -> per-video pain tags and a
                                           comments.jsonl for manual reading

Requires yt-dlp on PATH (pip install yt-dlp). Use --dry-run to print the
yt-dlp commands without running them. Views are a snapshot: record the date.

Examples:
  python3 yt_collect.py search --queries queries.txt --per-query 30 --out search.tsv
  python3 yt_collect.py pick search.tsv --exclude "crystal|minecraft" --top 50 --out ids.txt
  python3 yt_collect.py fetch ids.txt --out comments --max-comments 100
  python3 yt_collect.py rows comments --out rows.json
  python3 yt_collect.py tag comments --taxonomy taxonomy.json --jsonl comments.jsonl
"""
import argparse, glob, json, os, re, shlex, subprocess, sys, collections


def run(cmd, dry):
    if dry:
        print(shlex.join(cmd)); return ""
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("yt-dlp error:", r.stderr.strip().splitlines()[-1:] or r.returncode, file=sys.stderr)
    return r.stdout


def cmd_search(a):
    qs = [l.strip() for l in open(a.queries, encoding="utf-8") if l.strip() and not l.startswith("#")]
    rows = {}
    for q in qs:
        out = run(["yt-dlp", f"ytsearch{a.per_query}:{q}", "--flat-playlist", "--print",
                   "%(view_count)s\t%(id)s\t%(title)s\t%(channel)s\t%(duration)s"], a.dry_run)
        for line in out.splitlines():
            p = line.split("\t")
            if len(p) < 5:
                continue
            r = rows.setdefault(p[1], {"views": int(p[0]) if p[0].isdigit() else 0, "id": p[1], "title": p[2],
                                      "channel": p[3], "duration": p[4], "queries": []})
            r["queries"].append(q)
    if a.dry_run:
        return
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("views\tid\ttitle\tchannel\tduration\tqueries\n")
        for r in sorted(rows.values(), key=lambda r: -r["views"]):
            fh.write(f"{r['views']}\t{r['id']}\t{r['title']}\t{r['channel']}\t{r['duration']}\t{'|'.join(r['queries'])}\n")
    print(f"{len(rows)} unique videos from {len(qs)} queries -> {a.out}")


def cmd_pick(a):
    rows = [l.rstrip("\n").split("\t") for l in open(a.tsv, encoding="utf-8")][1:]
    inc = re.compile(a.include, re.I) if a.include else None
    exc = re.compile(a.exclude, re.I) if a.exclude else None
    keep = [r for r in rows if (not inc or inc.search(r[2])) and not (exc and exc.search(r[2] + " " + r[3]))]
    keep.sort(key=lambda r: -int(r[0] or 0))
    open(a.out, "w").write("\n".join(r[1] for r in keep[: a.top]) + "\n")
    print(f"kept {min(len(keep), a.top)} of {len(rows)} (after filters: {len(keep)}) -> {a.out}")
    for r in keep[: a.top]:
        print(f"  {int(r[0]):>9,}  {r[2][:80]}")


def cmd_fetch(a):
    os.makedirs(a.out, exist_ok=True)
    ids = [l.strip() for l in open(a.ids) if l.strip()]
    for vid in ids:
        if os.path.exists(os.path.join(a.out, vid + ".info.json")) and not a.force:
            continue
        run(["yt-dlp", "--skip-download", "--write-info-json", "--write-comments",
             "--extractor-args", f"youtube:max_comments={a.max_comments},all,0,0;comment_sort={a.sort}",
             "-o", os.path.join(a.out, "%(id)s.%(ext)s"), f"https://www.youtube.com/watch?v={vid}"], a.dry_run)
    if not a.dry_run:
        got = len(glob.glob(os.path.join(a.out, "*.info.json")))
        print(f"{got} info.json files in {a.out}")


def infos(d):
    for p in sorted(glob.glob(os.path.join(d, "*.info.json"))):
        try:
            yield json.load(open(p, encoding="utf-8"))
        except ValueError:
            print("skip unreadable", p, file=sys.stderr)


def cmd_rows(a):
    rows = []
    for j in infos(a.dir):
        up = j.get("upload_date") or ""
        rows.append({"id": j["id"], "title": j.get("title"), "views": j.get("view_count"),
                     "upload": f"{up[:4]}-{up[4:6]}-{up[6:]}" if len(up) == 8 else up,
                     "channel": j.get("channel"), "subs": j.get("channel_follower_count"),
                     "comments": j.get("comment_count"), "comments_fetched": len(j.get("comments") or []),
                     "duration": j.get("duration"), "chapters": [c.get("title") for c in j.get("chapters") or []],
                     "url": f"https://www.youtube.com/watch?v={j['id']}"})
    rows.sort(key=lambda r: -(r["views"] or 0))
    json.dump(rows, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(rows)} rows -> {a.out}")


def cmd_tag(a):
    tax = {k: re.compile(v, re.I) for k, v in json.load(open(a.taxonomy, encoding="utf-8")).items()}
    per_video = collections.Counter(); per_comment = collections.Counter()
    fh = open(a.jsonl, "w", encoding="utf-8") if a.jsonl else None
    for j in infos(a.dir):
        seen = set()
        for c in j.get("comments") or []:
            if c.get("author_is_uploader"):
                continue
            tags = [k for k, rx in tax.items() if rx.search(c.get("text", ""))]
            for k in tags:
                per_comment[k] += 1; seen.add(k)
            if fh:
                fh.write(json.dumps({"id": f"{j['id']}:{c.get('id')}", "video": j["id"], "title": j.get("title"),
                                     "likes": c.get("like_count"), "text": c.get("text", ""), "keyword_tags": tags},
                                    ensure_ascii=False) + "\n")
        per_video.update(seen)
    print("| Pain (keyword) | Videos | Comments |\n|---|---:|---:|")
    for k, n in per_video.most_common():
        print(f"| {k} | {n} | {per_comment[k]} |")
    print("\nKeyword hits over-count (e.g. 'what theme is that?' is curiosity, not pain).")
    print("Read comments.jsonl and hand-count comments that clearly express a pain before publishing numbers.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("--queries", required=True); s.add_argument("--per-query", type=int, default=30); s.add_argument("--out", default="search.tsv")
    s = sub.add_parser("pick"); s.add_argument("tsv"); s.add_argument("--include"); s.add_argument("--exclude"); s.add_argument("--top", type=int, default=50); s.add_argument("--out", default="ids.txt")
    s = sub.add_parser("fetch"); s.add_argument("ids"); s.add_argument("--out", default="comments"); s.add_argument("--max-comments", type=int, default=100); s.add_argument("--sort", choices=["top", "new"], default="top"); s.add_argument("--force", action="store_true")
    s = sub.add_parser("rows"); s.add_argument("dir"); s.add_argument("--out", default="rows.json")
    s = sub.add_parser("tag"); s.add_argument("dir"); s.add_argument("--taxonomy", required=True); s.add_argument("--jsonl")
    a = ap.parse_args()
    {"search": cmd_search, "pick": cmd_pick, "fetch": cmd_fetch, "rows": cmd_rows, "tag": cmd_tag}[a.cmd](a)


if __name__ == "__main__":
    main()
