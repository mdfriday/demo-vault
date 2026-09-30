#!/usr/bin/env python3
"""Count headline patterns across high-performing titles, weighted by views.

Input: CSV (columns include title and views), JSON list of objects, or TSV.
Output: a markdown table  Pattern | Titles | Total views | Median views,
sorted by total views. Use it to build the "pattern stats" section of a
swipe file. Views are a snapshot; record the date you collected them.

Default patterns are generic (number, how-to, question/exclaim, first person,
free, without, vs, mistakes, easiest/fastest, alternative). Add topic
patterns with --pattern "label=regex" (case-insensitive), repeatable.

Examples:
  python3 title_patterns.py top50.csv
  python3 title_patterns.py analysis_rows.json --pattern "digital garden=digital garden" \
      --pattern "Quartz=\\bquartz\\b" --title-key title --views-key views
"""
import argparse, csv, json, re, statistics

DEFAULT = [
    ("starts with / contains a number", r"^\d|\b\d+\b"),
    ("how to", r"\bhow (to|i)\b"),
    ("question or exclamation mark", r"[?!]"),
    ("first person (I / my)", r"\b(i|my|i'm|i've)\b"),
    ("free", r"\bfree\b"),
    ("without / no [objection]", r"\bwithout\b|\bno (git|code|github|terminal|css)\b"),
    ("vs / compared", r"\bvs\.?\b|\bversus\b|compare"),
    ("mistakes / what I wish I knew", r"mistake|wish i knew|don.t do"),
    ("easiest / fastest / easy", r"\beas(y|iest)\b|\bfastest\b|\bquick(ly)?\b"),
    ("alternative(s)", r"alternative"),
]


def load(path, tk, vk):
    if path.endswith(".json"):
        rows = json.load(open(path, encoding="utf-8"))
    else:
        dialect = "excel-tab" if path.endswith(".tsv") else "excel"
        rows = list(csv.DictReader(open(path, encoding="utf-8"), dialect=dialect))
    out = []
    for r in rows:
        try:
            out.append((str(r[tk]), int(float(str(r[vk]).replace(",", "") or 0))))
        except (KeyError, ValueError):
            continue
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("--title-key", default="title")
    ap.add_argument("--views-key", default="views")
    ap.add_argument("--pattern", action="append", default=[], help='"label=regex", repeatable')
    ap.add_argument("--no-defaults", action="store_true")
    a = ap.parse_args()
    rows = load(a.input, a.title_key, a.views_key)
    pats = ([] if a.no_defaults else DEFAULT) + [tuple(p.split("=", 1)) for p in a.pattern]
    res = []
    for label, rx in pats:
        v = [views for t, views in rows if re.search(rx, t, re.I)]
        if v:
            res.append((label, len(v), sum(v), int(statistics.median(v))))
    res.sort(key=lambda x: -x[2])
    print(f"{len(rows)} titles, {sum(v for _, v in rows):,} total views\n")
    print("| Pattern in title | Titles | Total views | Median views |\n|---|---:|---:|---:|")
    for label, n, tot, med in res:
        print(f"| {label} | {n} | {tot:,} | {med:,} |")


if __name__ == "__main__":
    main()
