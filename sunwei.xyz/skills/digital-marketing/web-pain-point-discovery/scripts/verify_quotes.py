#!/usr/bin/env python3
"""Verify that every quote appears verbatim in its archived source.

A quote passes only if its normalized text is a substring of the normalized
source text. Normalization = HTML-entity decode, Unicode NFKC, collapse all
whitespace. Nothing else is forgiven by default (no fuzzy matching).

Sources are resolved in this order:
  1. --registry JSON mapping URL -> {"file": path} (paths relative to the
     registry file), as written by archive_page.py;
  2. a file path (relative to --base);
  3. otherwise the quote is reported NOTSAVED (you must archive it first).

yt-dlp ``*.info.json`` files are searched comment by comment (comments[].text).

Modes:
  --quotes FILE     JSON list of {"quote", "source"} (or TSV: source<TAB>quote)
  --markdown FILES  extract “…” / 「…」 quotes from finished articles. A quote
                    with a URL on the same line is checked against that URL's
                    archived page (via --registry). If the URL is not archived,
                    or there is no URL, it must appear in --corpus (any file
                    under that folder, e.g. your verified research notes);
                    otherwise it is reported NOTSAVED / UNSOURCED.

Exit code 0 when everything verifies, 1 otherwise.

Examples:
  python3 verify_quotes.py --quotes quotes.json --registry pages/registry.json
  python3 verify_quotes.py --markdown posts/*.md --registry pages/registry.json --corpus research/
"""
import argparse, glob, html, json, os, re, sys, unicodedata

FOLD = str.maketrans({"\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"', "\u2026": "..."})


def norm(s, fold=False):
    s = unicodedata.normalize("NFKC", html.unescape(s or ""))
    if fold:
        s = s.translate(FOLD)
    return re.sub(r"\s+", " ", s).strip()


def texts_of(path, section=None):
    """Return a list of candidate texts for one source file."""
    raw = open(path, encoding="utf-8", errors="replace").read()
    if path.endswith(".info.json"):
        try:
            return [c.get("text", "") for c in json.loads(raw).get("comments") or []]
        except ValueError:
            return [raw]
    if section:
        m = re.search(re.escape(section) + r"\n(.*?)(\n#{1,6} |\Z)", raw, re.S)
        return [m.group(1)] if m else [""]
    return [raw]


class Resolver:
    def __init__(self, registry=None, base=".", section=None, fold=False):
        self.reg, self.regdir = {}, "."
        if registry:
            self.reg = json.load(open(registry, encoding="utf-8"))
            self.regdir = os.path.dirname(os.path.abspath(registry))
        self.base, self.section, self.fold = base, section, fold
        self.cache = {}

    def path_for(self, source):
        if source in self.reg:
            f = self.reg[source]["file"] if isinstance(self.reg[source], dict) else self.reg[source]
            return f if os.path.isabs(f) else os.path.join(self.regdir, f)
        p = source if os.path.isabs(source) else os.path.join(self.base, source)
        return p if os.path.isfile(p) else None

    def check(self, quote, source):
        p = self.path_for(source)
        if not p or not os.path.isfile(p):
            return "NOTSAVED"
        if p not in self.cache:
            self.cache[p] = [norm(t, self.fold) for t in texts_of(p, self.section)]
        q = norm(quote, self.fold)
        return "OK" if q and any(q in t for t in self.cache[p]) else "MISS"


def load_quotes(path):
    if path.endswith(".json"):
        data = json.load(open(path, encoding="utf-8"))
        if isinstance(data, dict):  # {"id": {...}}
            data = [dict(v, id=k) for k, v in data.items()]
        return [(d.get("id", i), d["quote"], d["source"]) for i, d in enumerate(data)]
    out = []
    for i, line in enumerate(open(path, encoding="utf-8")):
        if line.strip() and not line.startswith("#"):
            src, q = line.rstrip("\n").split("\t", 1)
            out.append((i + 1, q, src))
    return out


QRE = re.compile(r"“([^”]+)”|「([^」]+)」")
URE = re.compile(r"<(https?://[^>\s]+)>|\]\((https?://[^)\s]+)\)")


def corpus_texts(folder, fold):
    out = []
    for p in glob.glob(os.path.join(folder, "**", "*"), recursive=True):
        if os.path.isfile(p) and p.endswith((".md", ".txt", ".json", ".html")):
            out.extend(norm(t, fold) for t in texts_of(p))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--quotes", help="JSON list of {quote, source} or TSV source<TAB>quote")
    g.add_argument("--markdown", nargs="+", help="finished markdown files to scan for quotes")
    ap.add_argument("--registry", help="registry.json mapping URL -> {file}")
    ap.add_argument("--base", default=".", help="base folder for relative source paths")
    ap.add_argument("--corpus", help="markdown mode: folder that unsourced quotes must appear in")
    ap.add_argument("--section", help="only search under this heading in markdown sources, e.g. '## What the user says'")
    ap.add_argument("--fold-punct", action="store_true", help="also treat curly and straight quotes/apostrophes and … as equal")
    a = ap.parse_args()
    r = Resolver(a.registry, a.base, a.section, a.fold_punct)
    ok, bad, warn = 0, [], []
    if a.quotes:
        items = load_quotes(a.quotes)
        for qid, q, src in items:
            st = r.check(q, src)
            ok += st == "OK"
            if st != "OK":
                bad.append((st, qid, src, q))
        total = len(items)
    else:
        corpus = corpus_texts(a.corpus, a.fold_punct) if a.corpus else None
        total = 0
        for f in a.markdown:
            for n, line in enumerate(open(f, encoding="utf-8"), 1):
                urls = [x or y for x, y in URE.findall(line)]
                for m in QRE.finditer(line):
                    q = m.group(1) or m.group(2)
                    total += 1
                    st = "UNSOURCED"
                    for u in urls:  # archived page for the cited URL wins
                        st = r.check(q, u)
                        if st == "OK":
                            break
                    if st != "OK" and corpus is not None and st in ("UNSOURCED", "NOTSAVED"):
                        st = "OK" if any(norm(q, a.fold_punct) in t for t in corpus) else "MISS"
                    ok += st == "OK"
                    if st != "OK":
                        (warn if st == "UNSOURCED" else bad).append((st, f"{f}:{n}", urls[0] if urls else "-", q))
    print(f"verified {ok} / {total}")
    for row in bad + warn:
        print(*row, sep="\t")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
