---
name: course-to-knowledge-articles
title: Course to Knowledge Articles
description: Turns course material (lecture notes, transcripts, slides) into a set of mastery-level knowledge articles, one idea per article, each covering what it is, why it matters, how to use it, how to verify it worked, how to keep optimizing, common mistakes and a checklist, plus a learning-order index with coverage notes. Use when studying a course or book and wanting reusable, linkable notes for a digital garden or second brain, when asked to "turn this course into knowledge points", or before distilling knowledge into skills.
---

# Course to Knowledge Articles

Convert a course into a small library of articles you can apply, check and improve, not a summary you reread once.

## When to use

- You have lecture notes or transcripts and want durable, linked notes.
- You want a knowledge layer that later becomes skills (Knowledge → Skills).
- Not for product research (use the VOC skills) or for publishing marketing posts.

## Goal

Each important idea from the course becomes one article that a reader (or an agent) can act on and verify, with clear separation between what the course says and what is general practice.

## Inputs

- Course files (one per lecture is ideal), course title and instructor.
- Reader context: who you are and what you are working on now (used for "why this matters for me" and illustrative examples).
- Target folder and the site's frontmatter conventions.

## Steps

1. **Inventory lectures.** List every lecture with its number and whether it has content. Empty or missing lectures are recorded, not guessed.
2. **Split into ideas.** One article per idea, not per lecture. A dense lecture may become several articles (e.g. one "headlines" lecture became Magnetic Headlines, Search-Friendly Titles and Headline Variations & Swipe Files). A thin lecture may be folded into a related article; say so in the index.
3. **Write each article** with the template in [references/article-template.md](references/article-template.md): What it is · Why it matters · How to use it (Inputs, Output, numbered steps) · How to verify it worked (signals, how to measure, good vs bad) · How to keep optimizing · Common mistakes · Checklist (about six items) · Related · Source.
4. **Keep the course's own words attributed.** Quote short phrases with quotation marks; paraphrase the rest.
5. **Add one illustration** from the reader's context in a callout (`> [!example] Illustration: ...`), labelled "illustrative only; claims must match the real product".
6. **Mark general practice.** Anything not from the course (metrics tables, verification methods, filled-in topics for empty lectures) is labelled in the Source section.
7. **Link the set.** Related sections use wikilinks between articles; the Checklist and How-to steps link to sibling articles where a step depends on another idea.
8. **Write the index** ([references/index-template.md](references/index-template.md)): about the course, why it matters now, articles in learning order grouped by course section, a suggested short path, and coverage notes (lectures captured, empty, missing, folded).
9. **Lint:** `python3 scripts/lint_article.py out/*.md --vault <vault-root> --vault-prefix <target-folder>` to check frontmatter and that every wikilink resolves.

## Output

`<folder>/index.md` plus one kebab-case `.md` per idea, frontmatter `title`, `date`, `tags`, `description`.

## Checklist

- [ ] Every captured lecture is used or explicitly folded; empty lectures noted
- [ ] One idea per article; titles say the idea plainly
- [ ] Every article has all nine sections and a ~6-item checklist
- [ ] Course claims vs general practice are distinguishable in each Source section
- [ ] Illustrations are labelled illustrative and make no unconfirmed product claims
- [ ] All wikilinks resolve; index lists every article

## Guardrails

- Don't pad empty lectures with invented "course content"; fill with general practice only if useful and label it.
- Don't copy long passages from paid courses; summarize and attribute.
- Examples about your own product are illustrations, not results. Never present them as data.

## References

- [references/article-template.md](references/article-template.md): article skeleton with section guidance.
- [references/index-template.md](references/index-template.md): index skeleton with coverage notes.
- [references/worked-example.md](references/worked-example.md): excerpt of the AIDA article and the lecture-to-article map from the reference run.
- `scripts/lint_article.py` (`--help`).
