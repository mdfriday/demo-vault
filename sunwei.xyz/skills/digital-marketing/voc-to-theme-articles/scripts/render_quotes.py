#!/usr/bin/env python3
"""Render article templates, replacing {{Q:id}} lines with verified quotes.

You write each article in SRC with placeholder lines like `{{Q:setup-03}}`
where a quote should go. Quotes live in one JSON quote bank:

  {"setup-03": {"quote": "...", "source": "<URL or file path>",
                "url": "https://...", "platform": "Reddit r/Foo", "date": "2026-04-09"}}

`source` is where the verbatim text is checked (a URL in --registry, or a
file under --base; yt-dlp *.info.json files are searched per comment).
`url` is what readers see (defaults to source when it is a URL).

Each placeholder becomes:
  - “quote” — Platform · date · <url>        (「quote」 when it contains CJK)
`$` is escaped as `\\$` (for sites that render LaTeX). `{{NQUOTES}}` in
index.md becomes the total number of quotes used. The run FAILS (writes
nothing) if any quote does not verify or any placeholder is unknown.
It also reports quotes used in more than one article and unused quotes.

Example:
  python3 render_quotes.py --src drafts --out articles --quotes quotes.json \
      --registry pages/registry.json --base research
"""
import argparse, collections, glob, html, json, os, re, sys, unicodedata


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", html.unescape(s or ""))).strip()


def texts(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    if path.endswith(".info.json"):
        return [norm(c.get("text", "")) for c in json.loads(raw).get("comments") or []]
    return [norm(raw)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--quotes", required=True); ap.add_argument("--registry"); ap.add_argument("--base", default=".")
    ap.add_argument("--no-escape-dollar", action="store_true")
    a = ap.parse_args()
    Q = json.load(open(a.quotes, encoding="utf-8"))
    reg, regdir = {}, "."
    if a.registry:
        reg = json.load(open(a.registry, encoding="utf-8")); regdir = os.path.dirname(os.path.abspath(a.registry))
    cache, failures = {}, []

    def verified(qid):
        q = Q[qid]; src = q["source"]
        p = os.path.join(regdir, reg[src]["file"]) if src in reg else os.path.join(a.base, src)
        if not os.path.isfile(p):
            return False
        cache.setdefault(p, texts(p))
        return any(norm(q["quote"]) in t for t in cache[p])

    def fmt(qid):
        q = Q[qid]
        t = q["quote"] if a.no_escape_dollar else q["quote"].replace("$", "\\$")
        t = f"「{t}」" if re.search("[\u4e00-\u9fff]", t) else f"“{t}”"
        url = q.get("url") or (q["source"] if q["source"].startswith("http") else "")
        parts = [q.get("platform", "")] + ([q["date"]] if q.get("date") else []) + ([f"<{url}>"] if url else [])
        return f"- {t} — " + " · ".join(p for p in parts if p)

    used = collections.defaultdict(list); rendered = {}
    files = sorted(glob.glob(os.path.join(a.src, "*.md")), key=lambda p: p.endswith("/index.md"))
    for f in files:
        name = os.path.basename(f); lines = []
        for line in open(f, encoding="utf-8").read().split("\n"):
            m = re.fullmatch(r"\{\{Q:([\w.-]+)\}\}", line.strip())
            if not m:
                lines.append(line); continue
            qid = m.group(1)
            if qid not in Q:
                failures.append(("UNKNOWN", name, qid)); continue
            if not verified(qid):
                failures.append(("UNVERIFIED", name, qid, Q[qid]["quote"][:60])); continue
            used[qid].append(name); lines.append(fmt(qid))
        rendered[name] = "\n".join(lines)
    if "index.md" in rendered:
        rendered["index.md"] = rendered["index.md"].replace("{{NQUOTES}}", str(sum(len(v) for v in used.values())))
    for name, t in rendered.items():
        if "{{" in t:
            failures.append(("LEFTOVER-PLACEHOLDER", name))
    if failures:
        for x in failures:
            print(*x, sep="\t")
        print(f"FAILED: {len(failures)} problems, nothing written"); sys.exit(1)
    os.makedirs(a.out, exist_ok=True)
    for name, t in rendered.items():
        open(os.path.join(a.out, name), "w", encoding="utf-8").write(t)
    dups = {k: v for k, v in used.items() if len(v) > 1}
    print(f"articles {len(rendered)}  quotes used {sum(len(v) for v in used.values())}  unique {len(used)}")
    if dups:
        print("used in more than one article:", json.dumps(dups, ensure_ascii=False))
    unused = [k for k in Q if k not in used]
    if unused:
        print("unused quotes:", ", ".join(unused))


if __name__ == "__main__":
    main()
