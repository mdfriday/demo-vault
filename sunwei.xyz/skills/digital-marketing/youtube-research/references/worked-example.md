---
title: 'Worked example: MDFriday YouTube study (2026-09-20)'
---

# Worked example: MDFriday YouTube study (2026-09-20)

**Setup.** 18 query groups × ~30 results → relevance filter (removed crystal/animation results, pure Hugo intros and AI site-builder noise) → sorted by views → Top 50. Metadata via yt-dlp. Comments: top comments from the 30 most relevant videos (35 videos in total ended up with comments).

**Queries.** share obsidian notes · quartz digital garden · publish obsidian notes · obsidian wiki publish · obsidian website · obsidian quartz · obsidian publish free · obsidian publish alternative · obsidian publish · obsidian netlify · obsidian knowledge base website · obsidian hugo publish · obsidian github pages · obsidian digital garden · obsidian blog · how to publish obsidian · free alternative to obsidian publish · digital garden plugin obsidian

## Market structure

1. **Traffic layer (philosophy / lifestyle):** "digital garden to end doomscrolling" style videos, up to ~823K views, but they don't drive plugin installs.
2. **Conversion layer (publishing tutorials):** Quartz, Digital Garden plugin, official Publish, single-note sharing; ~15K–66K views; comment pains overlap the product's strongly.

Strategy: "Acquire with layer 1, convert with layer 2. Our videos stand in layer 2 but borrow layer 1 language in titles."

## Comment pains (per-video keyword tags, directional)

| Pain | Videos | Product mapping |
|---|---:|---|
| Theme / appearance tinkering | 29 | Theme library + local preview |
| Sync / auto-update hassle | 16 | Right-click republish |
| GitHub / Git barrier | 14 | No Git |
| Wants a free alternative | 14 | Guest / Free tiers, cheaper than official |
| Wants to share only some notes | 13 | Single note / folder publish |
| Setup too complex | 10 | Publish in seconds |
| Deploy failures (Netlify / Vercel / 404) | 10 | Hosting built in |

Later, reading every comment by hand showed "themes 29" was mostly curiosity ("What theme is that?"): only 11 comments expressed a theme pain. Keep both numbers and label them.

Quote example: ([How to publish your notes for free with Quartz](https://www.youtube.com/watch?v=6s6DT1yN4dw)) "followed everything... always get 404 error very sad."

## P0 topics (conversion)

| Topic | Why | Structure to model |
|---|---|---|
| How to Publish a Single Obsidian Note in 30 Seconds | Single-note sharing is an unmet need; share-plugin videos proved demand | Pain → install → right-click → link |
| Obsidian Publish vs Digital Garden vs Quartz vs MDFriday | Comparison queries carry the strongest intent | Comparison table → scenario picks → CTA |
| Publish Obsidian Notes Without GitHub / Vercel | Biggest friction in comments | Show the complex path failing → one-click path |

## Reusable structure (one of three)

**Free-alternative tutorial:** hook ("don't want to pay \$10–20/month") → introduce the tool → long steps (GitHub → token → deploy → domain) → success demo and customization.
**Product rewrite:** delete step 3 entirely and replace it with "right-click Publish → copy link"; spend the saved time on selective publishing and theme preview.

**One-line decision:** don't compete on "how to use Obsidian"; compete on "how to publish your knowledge without GitHub", with single-note sharing as the smallest conversion path.

## Title pattern stats from the same Top 50

| Pattern in title | Videos | Total views | Median views |
|---|---:|---:|---:|
| "digital garden" | 19 | 1,238,589 | 16,098 |
| first person "I / my" | 13 | 1,134,400 | 7,455 |
| "free" | 8 | 209,934 | 17,042 |
| "Quartz" | 3 | 130,680 | 59,271 |

(Reproduced with `scripts/title_patterns.py` on the saved rows.)
