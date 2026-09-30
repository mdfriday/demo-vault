#!/usr/bin/env python3
"""Search archived pages for candidate quotes, with context.

Reads the registry written by archive_page.py and prints up to --hits
matches per page with --width characters of context on each side. Copy the
exact wording you want from here into your evidence list, then run
verify_quotes.py.

Example:
  python3 grep_archive.py "4 ?gb|storage limit|容量" --registry pages/registry.json --width 160
"""
import argparse, json, os, re


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pattern", help="case-insensitive regex")
    ap.add_argument("--registry", default="pages/registry.json")
    ap.add_argument("--width", type=int, default=200)
    ap.add_argument("--hits", type=int, default=4)
    ap.add_argument("--only", default="", help="only pages whose URL contains this")
    a = ap.parse_args()
    reg = json.load(open(a.registry, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(a.registry))
    rx = re.compile(a.pattern, re.I)
    for url, v in reg.items():
        if a.only and a.only not in url:
            continue
        t = open(os.path.join(base, v["file"]), encoding="utf-8").read()
        hits = [m.start() for m in rx.finditer(t)]
        if not hits:
            continue
        print("=====", url, (v.get("date") or "")[:10], v.get("title") or "")
        last = -10**9
        for h in hits[: a.hits]:
            if h - last < a.width:
                continue
            last = h
            print("  ..." + t[max(0, h - a.width): h + a.width].replace("\n", " ") + "...")


if __name__ == "__main__":
    main()
