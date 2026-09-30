---
title: 'Worked example: MDFriday VOC library (7 themes)'
---

# Worked example: MDFriday VOC library (7 themes)

Context: MDFriday Publish turns Obsidian notes into websites. The lens was the whole "Obsidian → website" market, not MDFriday's own users. 567 cards were collected (target 1,000, paused), spanning 2019-02 to 2026-09.

| Theme folder | Cards | Meaning |
|---|---:|---|
| `personal-site/` | 112 | Personal site, wiki, knowledge network, digital garden |
| `export-pipelines/` | 94 | Export, multi-output, publishing friction |
| `alternatives/` | 84 | Tool choice and alternatives |
| `publish-fidelity/` | 83 | Output fidelity (styles, PDF, plugin rendering, SEO) |
| `competitor-signals/` | 74 | Competitor launches and market signals |
| `vault-to-web/` | 71 | Vault or notes → website structure and visualization |
| `selective-publish/` | 49 | Selective publishing and sync |

Platform mix: Obsidian Forum 205, Reddit 194, Hacker News 87, Dev.to 36, personal blogs 31, Medium 12, other 2.

## Lessons from this library

- Themes were about customer jobs; pains cut across them. Ranking pains later needed a separate tag layer (see `pain-point-analysis`), so do not over-invest in the perfect theme split.
- `competitor-signals/` kept launch posts out of the pain counts. 56 cards turned out to be background only (garden philosophy essays, launch posts) and were excluded from pain counts.
- Some cards mixed verbatim excerpts and the collector's paraphrase in the same field. That forced a caveat in every downstream report. Record `says_type` from the start.
- An `exclude_urls.txt` (451 URLs) plus URL normalization prevented re-adding the same thread from old.reddit/new.reddit or forum slug variants.
- Batches were written per source and window (`voc-batch-forum-w3.json`, `voc-batch-reddit-older.json`, ...), which made failures and coverage easy to audit.

## Designing themes for another product (suggested; not a measured rule)

1. Write the market lens in one line ("people trying to get X done").
2. Skim a few dozen posts and group them by the job the person was doing.
3. Keep 5–8 themes, each with a one-line meaning, plus one bucket for competitor and market signals.
