#!/usr/bin/env python3
"""Build the discovery report from a template + an evidence list, verifying as it goes.

Evidence (JSON list), one entry per quote:
  {"cluster": "N1", "url": "https://...", "quote": "verbatim text",
   "platform": "Obsidian Forum", "date": "2025-04-25"}
Every url must be archived in --registry (archive_page.py) and every quote
must appear verbatim in that archived page. With --known, a url that is
already in the existing research is rejected (the point is NEW evidence),
unless its cluster is listed in --allow-known (e.g. "S2" for a section that
adds fresh evidence to existing clusters).

Template placeholders:
  {{Q:N1}}          bullet list of all quotes for cluster N1
  {{E:S2:0}}        the text of the i-th quote of a cluster, inline (for prose)
  {{N:N1}}          number of distinct source URLs for cluster N1
  {{X:url | url}}   corroborating sources (archived, not quoted): "title <url>; ..."

Example:
  python3 build_report.py --template report_template.md --evidence evidence.json \
      --registry pages/registry.json --known known_urls.txt --out REPORT.md
"""
import argparse, html, json, os, re, sys, unicodedata

sys.dont_write_bytecode = True  # keep the skill folder free of __pycache__
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dedupe_urls import norm as url_key  # same normalization as the dedupe step


def ws(s):  # display form: keep the original characters, only tidy whitespace
    return re.sub(r"\s+", " ", s or "").strip()


def n(s):  # comparison form
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", html.unescape(s or ""))).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--template", required=True); ap.add_argument("--evidence", required=True)
    ap.add_argument("--registry", required=True); ap.add_argument("--known")
    ap.add_argument("--allow-known", default="", help="comma list of clusters allowed to cite known URLs")
    ap.add_argument("--out", default="REPORT.md")
    ap.add_argument("--sep", default="; ", help="separator between corroborating sources (e.g. '；' for Chinese)")
    a = ap.parse_args()
    E = json.load(open(a.evidence, encoding="utf-8"))
    reg = json.load(open(a.registry, encoding="utf-8")); base = os.path.dirname(os.path.abspath(a.registry))
    known = set(url_key(l) for l in open(a.known, encoding="utf-8") if l.strip()) if a.known else set()
    allow = set(x for x in a.allow_known.split(",") if x)
    bad = []
    for e in E:
        if e["url"] not in reg:
            bad.append(("NOTSAVED", e["cluster"], e["url"])); continue
        if n(e["quote"]) not in n(open(os.path.join(base, reg[e["url"]]["file"]), encoding="utf-8").read()):
            bad.append(("MISS", e["cluster"], e["url"], e["quote"][:60]))
        if url_key(e["url"]) in known and e["cluster"] not in allow:
            bad.append(("KNOWN", e["cluster"], e["url"]))

    def Q(c):
        return "\n".join(f"  - 「{ws(e['quote'])}」 — {e['platform']} · {e['date']} · {e['url']}" for e in E if e["cluster"] == c)

    def X(m):
        urls = [u.strip() for u in m.group(1).split("|")]
        for u in urls:
            if u not in reg:
                bad.append(("X-NOTSAVED", u))
            elif url_key(u) in known:
                bad.append(("X-KNOWN", u))
        return a.sep.join(f"{(reg.get(u) or {}).get('title') or u} <{u}>" for u in urls)

    T = open(a.template, encoding="utf-8").read()
    T = re.sub(r"\{\{Q:(\w+)\}\}", lambda m: Q(m.group(1)), T)
    T = re.sub(r"\{\{E:(\w+):(\d+)\}\}", lambda m: ws([e["quote"] for e in E if e["cluster"] == m.group(1)][int(m.group(2))]), T)
    T = re.sub(r"\{\{N:(\w+)\}\}", lambda m: str(len({e["url"] for e in E if e["cluster"] == m.group(1)})), T)
    T = re.sub(r"\{\{X:([^}]+)\}\}", X, T)
    if "{{" in T:
        bad.append(("LEFTOVER-PLACEHOLDER",))
    if bad:
        for b in bad:
            print(*b, sep="\t")
        print(f"FAILED: {len(bad)} problems, report not written"); sys.exit(1)
    open(a.out, "w", encoding="utf-8").write(T)
    print(f"ok: {len(E)} quotes from {len({e['url'] for e in E})} URLs verified -> {a.out}")


if __name__ == "__main__":
    main()
