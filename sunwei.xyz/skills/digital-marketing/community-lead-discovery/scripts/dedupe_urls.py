#!/usr/bin/env python3
"""Normalize URLs and dedupe new finds against everything already collected.

Normalization makes the same thread compare equal across mirrors and slugs:
  reddit.com/r/x/comments/<id>/...   -> reddit:<id>   (www./old./m. ignored)
  news.ycombinator.com/item?id=<n>   -> hn:<n>
  forum.example.com/t/<slug>/<id>    -> forum.example.com/t/<id>  (Discourse)
  v2ex.com/t/<id>                    -> v2ex:<id>
  youtube.com/watch?v=<id>, youtu.be/<id> -> yt:<id>
  everything else: lowercase, strip scheme, www., query, fragment, trailing /

Commands:
  normalize URL...                     print the key for each URL
  collect PATH...                      print every URL found in files under PATH
                                       (frontmatter `url:` lines and inline links)
  check --known FILE [FILE...] CANDIDATES
                                       print NEW/DUP for each candidate URL
                                       (CANDIDATES: text file, one URL per line,
                                       or '-' for stdin); also flags duplicates
                                       inside the candidate list itself.

Examples:
  python3 dedupe_urls.py collect research/cards > known_urls.txt
  python3 dedupe_urls.py check --known known_urls.txt exclude_urls.txt new_urls.txt
"""
import argparse, os, re, sys

URL_RE = re.compile(r"https?://[^\s<>)\]\"'`|]+")


def norm(u):
    m = re.search(r"(?:youtube\.com/watch\?(?:.*&)?v=|youtu\.be/|youtube\.com/shorts/)([\w-]{11})", u)
    if m:  # video ids are case-sensitive
        return "yt:" + m.group(1)
    u = u.strip().rstrip(".,;").rstrip("/").lower()
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^(www\.|old\.|m\.|new\.)", "", u)
    m = re.match(r"news\.ycombinator\.com/item\?id=(\d+)", u)
    if m:
        return "hn:" + m.group(1)
    u = re.sub(r"[?#].*$", "", u)
    m = re.match(r"reddit\.com/r/[^/]+/comments/([a-z0-9]+)", u)
    if m:
        return "reddit:" + m.group(1)
    m = re.match(r"v2ex\.com/t/(\d+)", u)
    if m:
        return "v2ex:" + m.group(1)
    m = re.match(r"([a-z0-9.-]+/t/)(?:[^/]*[^/\d][^/]*/)?(\d+)(?:/\d+)?$", u)  # Discourse topic
    if m:
        return m.group(1) + m.group(2)
    return u.rstrip("/")


def urls_in(path):
    for root, _, files in os.walk(path) if os.path.isdir(path) else [("", [], [path])]:
        for f in files:
            p = os.path.join(root, f)
            if f.startswith(".") or not f.endswith((".md", ".txt", ".json", ".csv", ".tsv")):
                continue
            for line in open(p, encoding="utf-8", errors="ignore"):
                for u in URL_RE.findall(line):
                    yield u


def read_list(p):
    fh = sys.stdin if p == "-" else open(p, encoding="utf-8", errors="ignore")
    return [l.strip() for l in fh if l.strip().startswith("http")]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("normalize"); s.add_argument("urls", nargs="+")
    s = sub.add_parser("collect"); s.add_argument("paths", nargs="+")
    s = sub.add_parser("check"); s.add_argument("--known", nargs="+", required=True); s.add_argument("candidates")
    a = ap.parse_args()
    if a.cmd == "normalize":
        for u in a.urls:
            print(norm(u), u, sep="\t")
    elif a.cmd == "collect":
        seen = set()
        for p in a.paths:
            for u in urls_in(p):
                k = norm(u)
                if k not in seen:
                    seen.add(k); print(u)
    else:
        known = set()
        for k in a.known:
            known.update(norm(u) for u in read_list(k))
        new = dup = 0
        batch = set()
        for u in read_list(a.candidates):
            k = norm(u)
            if k in known or k in batch:
                dup += 1; print("DUP", u, sep="\t")
            else:
                new += 1; batch.add(k); print("NEW", u, sep="\t")
        print(f"# new {new}  dup {dup}  known {len(known)}", file=sys.stderr)


if __name__ == "__main__":
    main()
