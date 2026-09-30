#!/usr/bin/env python3
"""Check candidate titles against search-friendly title rules.

For each title: character count, whether it fits the range (default 50-60),
whether the keyword appears at the very start (or within --lead chars), and
what a results page would show when it truncates at --cut characters.

Example:
  python3 title_check.py --keyword "publish obsidian notes" \
      "Publish Obsidian Notes Without GitHub (No Terminal Needed)" \
      "How to Publish Obsidian Notes Without GitHub or Git"
  python3 title_check.py --keyword "obsidian seo" --file titles.txt
"""
import argparse, sys


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("titles", nargs="*")
    ap.add_argument("--file", help="one title per line")
    ap.add_argument("--keyword", required=True)
    ap.add_argument("--min", type=int, default=50)
    ap.add_argument("--max", type=int, default=60)
    ap.add_argument("--lead", type=int, default=0, help="keyword may start within this many chars (0 = must be first)")
    ap.add_argument("--cut", type=int, default=60, help="truncation point for the preview")
    a = ap.parse_args()
    titles = list(a.titles) + ([l.strip() for l in open(a.file, encoding="utf-8") if l.strip()] if a.file else [])
    if not titles:
        ap.error("give titles or --file")
    kw = a.keyword.lower()
    bad = 0
    print("len\tfit\tkw-first\ttitle\tpreview")
    for t in titles:
        pos = t.lower().find(kw)
        first = pos != -1 and pos <= a.lead
        fit = a.min <= len(t) <= a.max
        bad += not (fit and first)
        prev = t if len(t) <= a.cut else t[: a.cut - 1].rstrip() + "…"
        print(len(t), "ok" if fit else "NO", "ok" if first else "NO", t, prev, sep="\t")
    sys.exit(1 if bad == len(titles) else 0)


if __name__ == "__main__":
    main()
