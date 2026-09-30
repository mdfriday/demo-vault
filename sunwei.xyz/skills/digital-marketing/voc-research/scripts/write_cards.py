#!/usr/bin/env python3
"""Write voice-of-customer cards (one markdown file per post) from a JSON batch.

Input: a JSON array. Each object:
  url (required), theme (one of --themes), title, title_en (optional),
  date (YYYY-MM-DD, the post's date, not today), platform,
  says (what the user says: a verbatim excerpt or your paraphrase),
  says_type ("verbatim" | "paraphrase"), need, pain, implication,
  author (optional; only written with --keep-author, never publish it)

Cards go to OUT/<theme>/<date>-<slug>.md. A card is skipped when its URL
(normalized: reddit id, HN id, Discourse topic id, etc.) already exists in
OUT or in any --exclude file. Unknown themes are rejected, not guessed.

Example:
  python3 write_cards.py batch.json research/cards \
      --themes selective-publish,publish-fidelity,alternatives \
      --product "Acme" --exclude research/exclude_urls.txt
"""
import argparse, json, os, re, sys


def norm(u):
    u = u.strip().rstrip("/").lower()
    u = re.sub(r"^https?://(www\.|old\.|m\.)?", "", u)
    m = re.match(r"news\.ycombinator\.com/item\?id=(\d+)", u)
    if m:
        return "hn:" + m.group(1)
    u = re.sub(r"[?#].*$", "", u)
    m = re.match(r"reddit\.com/r/[^/]+/comments/([a-z0-9]+)", u)
    if m:
        return "reddit:" + m.group(1)
    m = re.match(r"([a-z0-9.-]+/t/)(?:[^/]*[^/\d][^/]*/)?(\d+)(?:/\d+)?$", u)
    return m.group(1) + m.group(2) if m else u


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:70] or "item"


def card(o, product, keep_author):
    fm = ["---", f"theme: {o['theme']}", f"title: {json.dumps(o.get('title',''), ensure_ascii=False)}"]
    if o.get("title_en"):
        fm.append(f"title_en: {json.dumps(o['title_en'], ensure_ascii=False)}")
    fm += [f"date: {o.get('date','')}", f"platform: {o.get('platform','')}", f"url: {o['url']}",
           f"says_type: {o.get('says_type','paraphrase')}"]
    if keep_author and o.get("author"):
        fm.append(f"author: {o['author']}  # internal only")
    fm.append("---")
    label = "What the user says (verbatim excerpt)" if o.get("says_type") == "verbatim" else "What the user says (paraphrase)"
    return "\n".join(fm) + f"""

# {o.get('title','')}

- **Platform:** {o.get('platform','')}
- **Date:** {o.get('date','')}
- **Link:** {o['url']}

## {label}

{o.get('says','')}

## Core need

{o.get('need','')}

## Pain

{o.get('pain','')}

## Implication for {product}

{o.get('implication','')}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("batch"); ap.add_argument("out")
    ap.add_argument("--themes", required=True, help="comma-separated theme folder names")
    ap.add_argument("--product", default="the product")
    ap.add_argument("--exclude", nargs="*", default=[], help="files with URLs to skip (one per line)")
    ap.add_argument("--keep-author", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    themes = set(t.strip() for t in a.themes.split(",") if t.strip())
    seen = set()
    for root, _, files in os.walk(a.out):
        for f in files:
            if f.endswith(".md"):
                for line in open(os.path.join(root, f), encoding="utf-8", errors="ignore"):
                    if line.startswith("url:"):
                        seen.add(norm(line.split(":", 1)[1]))
    for x in a.exclude:
        seen.update(norm(l) for l in open(x, encoding="utf-8") if l.strip())
    written = skipped = rejected = 0
    for o in json.load(open(a.batch, encoding="utf-8")):
        url = (o.get("url") or "").strip()
        if not url or o.get("theme") not in themes or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(o.get("date", ""))):
            rejected += 1
            print("REJECT (missing url/theme/date)", o.get("title") or url, file=sys.stderr)
            continue
        k = norm(url)
        if k in seen:
            skipped += 1
            continue
        seen.add(k)
        path = os.path.join(a.out, o["theme"], f"{o['date']}-{slug(o.get('title_en') or o.get('title') or url)}.md")
        if not a.dry_run:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(path, "w", encoding="utf-8").write(card(o, a.product, a.keep_author))
        written += 1
    print(f"written {written}  skipped-duplicate {skipped}  rejected {rejected}")


if __name__ == "__main__":
    main()
