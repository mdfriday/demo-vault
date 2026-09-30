#!/usr/bin/env python3
"""Pre-publish lint for digital-garden markdown articles.

Checks (each can be tuned or disabled with flags):
  * frontmatter keys present, in order (--keys title,date,tags,description)
  * title length (--title-range 50,60) and description length (--desc-range 140,160)
  * kebab-case filename
  * every [[wikilink]] resolves to exactly one note in --vault
    (path-qualified 'folder/note' or a unique basename)
  * quote count per article (--min-quotes/--max-quotes; index.md is skipped)
  * no @handles or u/usernames in prose (privacy)
  * no unescaped $ in prose when the site renders LaTeX (--math)
  * forbidden blocks that the site cannot render (--forbid mermaid,dataview,base,canvas)

Exit code 1 if any ERROR was printed; WARN lines do not fail the run.

Example:
  python3 lint_article.py posts/*.md --vault ~/vault --title-range 50,60 \
      --desc-range 140,160 --min-quotes 2 --max-quotes 6 --math
"""
import argparse, os, re, sys

QLINE = re.compile(r"“[^”]+”|「[^」]+」")


def vault_notes(root):
    notes = []
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        for f in files:
            if f.endswith(".md"):
                notes.append(os.path.relpath(os.path.join(d, f), root)[:-3].replace(os.sep, "/"))
    return notes


def resolve(target, notes, extra):
    t = target.split("#")[0].strip()
    cands = [n for n in notes + extra if n == t or n.endswith("/" + t)]
    return len(set(cands)) == 1, cands


def rng(s):
    a, b = s.split(",")
    return int(a), int(b)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--vault", help="vault root used to resolve wikilinks")
    ap.add_argument("--vault-prefix", default="", help="where these files will live inside the vault, e.g. mdfriday/blog (lets new files resolve before they are copied in)")
    ap.add_argument("--keys", default="title,date,tags,description")
    ap.add_argument("--title-range", type=rng)
    ap.add_argument("--desc-range", type=rng)
    ap.add_argument("--min-quotes", type=int)
    ap.add_argument("--max-quotes", type=int)
    ap.add_argument("--math", action="store_true", help="flag unescaped $ (site renders LaTeX)")
    ap.add_argument("--forbid", default="mermaid,dataview,base", help="comma list of fenced block languages to forbid")
    a = ap.parse_args()
    notes = vault_notes(a.vault) if a.vault else None
    extra = []
    for f in a.files:
        if a.vault and os.path.abspath(f).startswith(os.path.abspath(a.vault) + os.sep):
            continue  # already inside the vault, so vault_notes() lists it
        extra.append((a.vault_prefix.rstrip("/") + "/" if a.vault_prefix else "") + os.path.basename(f)[:-3])
    errors = 0

    def out(level, f, msg):
        nonlocal errors
        errors += level == "ERROR"
        print(level, os.path.basename(f), msg, sep="\t")

    for f in a.files:
        t = open(f, encoding="utf-8").read()
        name = os.path.basename(f)
        m = re.match(r"---\n(.*?)\n---\n", t, re.S)
        if not m:
            out("ERROR", f, "no YAML frontmatter"); continue
        fm = m.group(1)
        keys = [l.split(":")[0] for l in fm.splitlines() if re.match(r"^[A-Za-z_]", l)]
        want = [k for k in a.keys.split(",") if k]
        if [k for k in keys if k in want] != want:
            out("ERROR", f, f"frontmatter keys {keys}, want {want}")
        val = lambda k: (re.search(rf"^{k}:\s*(.*)$", fm, re.M) or [None, ""])[1].strip().strip('"').strip("'")
        if a.title_range and name != "index.md":
            n = len(val("title"))
            if not a.title_range[0] <= n <= a.title_range[1]:
                out("WARN", f, f"title length {n} outside {a.title_range}")
        if a.desc_range:
            n = len(val("description"))
            if not a.desc_range[0] <= n <= a.desc_range[1]:
                out("WARN", f, f"description length {n} outside {a.desc_range}")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*\.md|SKILL\.md", name):
            out("WARN", f, "filename is not kebab-case")
        body = t[m.end():]
        nocode = re.sub(r"```.*?```", "", body, flags=re.S)
        nocode = re.sub(r"`[^`\n]*`", "", nocode)
        if notes is not None:
            for l in re.findall(r"\[\[([^\]]+?)\]\]", nocode):
                tgt = l.replace("\\|", "|").split("|")[0]
                ok, c = resolve(tgt, notes, extra)
                if not ok:
                    out("ERROR", f, f"wikilink [[{tgt}]] -> {len(set(c))} matches")
        nq = sum(len(QLINE.findall(l)) for l in nocode.splitlines() if l.startswith(("- “", "- 「", "> “", "> 「")))
        if name != "index.md":
            if a.min_quotes is not None and nq < a.min_quotes:
                out("ERROR", f, f"only {nq} sourced quotes (min {a.min_quotes})")
            if a.max_quotes is not None and nq > a.max_quotes:
                out("WARN", f, f"{nq} sourced quotes (max {a.max_quotes})")
        for i, line in enumerate(nocode.splitlines(), 1):
            if re.search(r"(?<![\w.])@[A-Za-z0-9_]{2,}|(?<![\w/])u/[A-Za-z0-9_-]{3,}", line):
                out("WARN", f, f"possible username/handle: {line.strip()[:80]}")
            if a.math and re.search(r"(?<!\\)\$", line):
                out("ERROR", f, f"unescaped $ (renders as math): {line.strip()[:80]}")
        for lang in [x for x in a.forbid.split(",") if x]:
            if re.search(rf"```{lang}\b", body):
                out("ERROR", f, f"forbidden ```{lang} block")
    print(f"checked {len(a.files)} files, {errors} errors")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
