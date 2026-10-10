---
date: 2026-10-02
name: headline-swipe-file
title: Headline Swipe File
description: Builds an evidence-based headline swipe file from high-performing titles (e.g. top YouTube videos by views, community post titles, search queries), ranks title patterns with view counts, and generates keyword-first, 50–60 character title variations logged with the chosen pick and its pattern. Use when writing titles for blog posts, videos or landing pages, when asked for "magnetic headlines", "SEO titles", "title ideas" or a "swipe file", or before a batch of content so every title is grounded in proven patterns and real search language.
---

# Headline Swipe File

Ground titles in what already earns attention for this topic, then write many variations and pick the one that is keyword-first, the right length, and honest.

## When to use

- Before writing a batch of posts or videos on one topic.
- When a draft has a weak or generic title.
- Not for body copy (use `voc-to-blog-post`) or for finding the demand itself (use the research skills).

## Goal

A swipe file with evidence (titles, views, dates, search queries, customer phrases), a ranked list of patterns, and a title log where each post has variations and one justified pick.

## Inputs

- High-performing titles with an engagement number and date (e.g. YouTube `analysis_rows.json` from `youtube-research`, as CSV, JSON or TSV).
- The search queries you used or know people type.
- Community post titles (e.g. VOC cards) and customer phrases from research.
- The list of planned posts with one target keyword each.
- Confirmed product facts (for honesty checks on words like "free").

## Steps

1. **Collect evidence (section A).** Top titles with views and year. Keep the collection date; views are a snapshot.
2. **Count patterns.** `python3 scripts/title_patterns.py rows.json --pattern "digital garden=digital garden" --pattern "Quartz=\bquartz\b"` gives a table with pattern | titles | total views | median views. Add topic patterns as needed.
3. **Record search language (section B).** List the queries people type, plus keyword counts across community titles (e.g. "publish" in 277 of 567 titles).
4. **Rank patterns (section C).** For the top ~10 patterns, give each one its best examples with numbers and a line on why it works. Separate the *traffic layer* (big views, weak intent) from the *conversion layer* (moderate views, comments full of the pain you solve).
5. **Build a keyword bank (D) and customer phrases (E)** in the customer's words. Point to where the exact quotes are verified.
6. **Write variations per post.** 10–25 when practising; at least 3 per post in production. Use patterns from [references/pattern-catalog.md](references/pattern-catalog.md). Adapt the structure, never copy a title.
7. **Check mechanically.** `python3 scripts/title_check.py --keyword "<target keyword>" "<title 1>" "<title 2>"` shows length (50–60), keyword position, and the truncation preview.
8. **Pick and log.** Mark the pick with ✅ and label its pattern, e.g. `✅ Publish Obsidian Notes Without GitHub (No Terminal Needed) [how-to + without]`. Log the format in [references/swipe-file-template.md](references/swipe-file-template.md).
9. **Honesty pass.** Every promise in the title must be delivered by the body and true for the product ("free" only if a real free path exists, with its limits stated in the post).

## Output

- `swipe-file.md` (sections A–F, internal working file).
- `title-log.md`: per post, the keyword, the variations, and the ✅ pick with its [pattern].

## Checklist

- [ ] Evidence has numbers and a collection date; no invented view counts
- [ ] Pattern table reproducible from the input file
- [ ] Each chosen title starts with (or leads with) the target keyword
- [ ] Each chosen title is 50–60 characters, or has a logged reason for the exception
- [ ] One clear pattern per title; the promise is delivered by the body
- [ ] No title reuses a competitor's title verbatim

## Guardrails

- Numbers in titles ("7 mistakes", "6 options") must match the body.
- Avoid fake urgency, clickbait and superlatives you can't back up ("best", "fastest") unless the body shows a fair comparison.
- Swipe files are internal; don't publish them with competitor titles as your content.

## References

- [references/pattern-catalog.md](references/pattern-catalog.md): course patterns and evidence-ranked patterns with examples.
- [references/swipe-file-template.md](references/swipe-file-template.md): swipe file sections A–F and the title log format.
- [references/worked-example.md](references/worked-example.md): MDFriday swipe file stats and title log excerpt.
- `scripts/title_patterns.py`, `scripts/title_check.py` (`--help` on each).
