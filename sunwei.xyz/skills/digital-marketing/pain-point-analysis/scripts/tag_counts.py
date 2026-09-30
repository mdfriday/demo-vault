#!/usr/bin/env python3
"""First-pass keyword tagging of a VOC corpus to seed manual pain-point tagging.

This is a triage aid, not the final count. Keyword hits over-count (a card
that mentions "theme" is not necessarily complaining about themes), so read
every hit and hand-tag before you publish numbers.

Input (pick one):
  --cards DIR      markdown cards with YAML frontmatter (date:, url:, title:)
  --jsonl FILE     one {"id", "text", "date"} object per line (e.g. comments)
Taxonomy: JSON {"tag": "regex", ...} (case-insensitive), see
references/taxonomy.example.json.

Output: per-tag counts (total and since --since-year) to stdout, and
optionally --csv with one row per item and its matched tags for review.

Example:
  python3 tag_counts.py --cards research/cards --taxonomy taxonomy.json \
      --since-year 2025 --csv review.csv
"""
import argparse, csv, json, os, re, collections


def load_cards(d):
    for root, _, files in os.walk(d):
        for f in sorted(files):
            if not f.endswith(".md") or f.lower() in ("readme.md", "index.md"):
                continue
            p = os.path.join(root, f)
            t = open(p, encoding="utf-8", errors="ignore").read()
            m = re.match(r"---\n(.*?)\n---\n", t, re.S)
            fm = m.group(1) if m else ""
            if not re.search(r"^url:", fm, re.M):
                continue  # not a card (README, notes, etc.)
            date = (re.search(r"^date:\s*(\S+)", fm, re.M) or [None, ""])[1]
            titles = " ".join(re.findall(r"^title(?:_en)?:\s*(.*)$", fm, re.M))
            yield os.path.relpath(p, d), titles + "\n" + t[m.end():], date  # tag body, not metadata keys


def load_jsonl(p):
    for line in open(p, encoding="utf-8"):
        if line.strip():
            o = json.loads(line)
            yield str(o.get("id")), o.get("text", ""), str(o.get("date", ""))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--cards"); g.add_argument("--jsonl")
    ap.add_argument("--taxonomy", required=True)
    ap.add_argument("--since-year", type=int)
    ap.add_argument("--csv", help="write per-item tags here for manual review")
    a = ap.parse_args()
    tax = {k: re.compile(v, re.I) for k, v in json.load(open(a.taxonomy, encoding="utf-8")).items()}
    items = list(load_cards(a.cards) if a.cards else load_jsonl(a.jsonl))
    total = collections.Counter(); recent = collections.Counter(); untagged = 0
    rows = []
    for iid, text, date in items:
        tags = [k for k, rx in tax.items() if rx.search(text)]
        untagged += not tags
        for k in tags:
            total[k] += 1
            if a.since_year and date[:4].isdigit() and int(date[:4]) >= a.since_year:
                recent[k] += 1
        rows.append((iid, date, ";".join(tags)))
    print(f"items {len(items)}  with >=1 tag {len(items) - untagged}  untagged {untagged}\n")
    hdr = "| Tag | Items |" + (f" Since {a.since_year} |" if a.since_year else "")
    print(hdr + "\n|---|---:|" + ("---:|" if a.since_year else ""))
    for k, n in total.most_common():
        print(f"| {k} | {n} |" + (f" {recent[k]} |" if a.since_year else ""))
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(["item", "date", "keyword_tags", "manual_tags", "background_only"])
            for r in rows:
                w.writerow(list(r) + ["", ""])
        print(f"\nreview sheet: {a.csv} (fill manual_tags; mark background_only for cards with no concrete pain)")


if __name__ == "__main__":
    main()
