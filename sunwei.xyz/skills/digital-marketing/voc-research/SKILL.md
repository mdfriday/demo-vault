---
date: 2026-10-02
name: voc-research
title: VOC Research
description: Collects voice-of-customer (VOC) evidence from public communities (Reddit, Discourse forums, Hacker News, Dev.to, Medium, personal blogs) into one markdown card per post, filed under a small set of themes and deduplicated by normalized URL. Use when starting customer research for a product or market, building or extending a VOC library, "listening" before building, or when asked to find what people complain about, ask for, or compare. Produces the raw corpus that pain-point-analysis, voc-to-theme-articles and voc-to-blog-post consume.
---

# VOC Research

Build a searchable library of real customer voices: one card per public post, each with a link, what the person said, their need, their pain and what it means for the product.

## When to use

- Before positioning, copy or roadmap work: "what are people already struggling with?"
- To extend an existing VOC library with a new batch or a new time window.
- Not for scoring fresh leads to reply to today (use `community-lead-discovery`), and not for finding pains missing from an existing summary (use `web-pain-point-discovery`).

## Goal

A corpus big enough to rank pains honestly (hundreds of cards, several platforms, several years), where every card can be traced back to its source.

## Inputs

- Product name and one-paragraph description of the job it does.
- Market lens: the problem space, not the product (e.g. "publishing notes as a website", not "our plugin").
- Communities to search (subreddits, forums, HN, Dev.to/Medium tags, blogs) and search phrases in customer language.
- Themes: 5–8 folders that split the problem space (draft them after reading ~30 posts). See [references/themes-example.md](references/themes-example.md).
- Existing URL lists to skip (previous cards, exclusions).

## Steps

1. **Draft themes.** Skim 20–30 posts, then define 5–8 themes with one-line meanings. Keep them about customer jobs, not product features.
2. **Search by source and window.** Work one source at a time (e.g. forum, Reddit, HN) and one time window at a time (recent first, then older). Use the endpoints and query patterns in [references/source-playbook.md](references/source-playbook.md). Record which sources failed or rate-limited.
3. **Dedupe before writing.** Collect known URLs and check new finds:
   `python3 scripts/dedupe_urls.py collect cards/ > known.txt`
   `python3 scripts/dedupe_urls.py check --known known.txt exclude_urls.txt new_urls.txt`
4. **Write a batch JSON** (schema in [references/card-template.md](references/card-template.md)). For each post: the post's own date, platform, URL, a title, what the user says, core need, pain, implication. Mark `says_type` as `verbatim` only if the text is copied exactly; otherwise `paraphrase`.
5. **Write cards:** `python3 scripts/write_cards.py batch.json cards/ --themes a,b,c --product "<Product>" --exclude exclude_urls.txt`. The script skips duplicates and rejects unknown themes or missing dates.
6. **Update the library README:** theme table with counts, and a date-descending list of all cards (date, title, platform, relative link).
7. **Stop at a target or at diminishing returns** (new batches mostly DUP), and say so in the README ("collection paused at N of target M").

## Output

- `cards/<theme>/<YYYY-MM-DD>-<slug>.md`, one per post.
- `README.md`: total count, theme table, date-sorted index, card field list.
- `exclude_urls.txt` and batch JSON files kept for audit.

## Checklist

- [ ] Every card has a working URL, the post's own date, platform and theme
- [ ] No duplicate threads (normalized URL check passes)
- [ ] `says_type` is honest: paraphrases are not presented as quotes
- [ ] Several platforms and years represented; failures noted
- [ ] Background-only posts (no concrete pain) still allowed but recognizable
- [ ] README counts match the files on disk

## Guardrails

- Never invent posts, URLs, dates or quotes. If a source fails, record the failure instead of filling the gap.
- Keep usernames and emails out of anything public. Cards are research notes; strip `author` before publishing (the script omits it unless `--keep-author`).
- Collect the market's voice, not only your own users. Tag competitor launches and your own posts so they are not counted as customer pain later.
- Read-only: never post, vote or DM while researching.

## References

- [references/card-template.md](references/card-template.md): card format, batch JSON schema, filled example.
- [references/themes-example.md](references/themes-example.md): the 7-theme MDFriday library as a worked example.
- [references/source-playbook.md](references/source-playbook.md): sources, endpoints, query patterns, rate-limit notes.
- `scripts/write_cards.py`: batch JSON to cards with URL dedupe (`--help`).
- `scripts/dedupe_urls.py`: normalize, collect and check URLs (`--help`).
