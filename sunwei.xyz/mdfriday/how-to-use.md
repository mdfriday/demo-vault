---
title: How to use the MDFriday research system
tags:
  - mdfriday
  - voice-of-customer
  - seo
---

# How to use the MDFriday research system

← [[mdfriday/index|MDFriday]]

This section of the garden is one system with three parts. Everything in it comes from public posts and public plans.

| Part | What it is | Where |
|---|---|---|
| **VOC database** | One card per public post where someone talks about publishing notes: what they said (verbatim), what they need, how much it hurts, and what it means for MDFriday | [[voc-db/README\|VOC database]] · `voc-db/cards/` · [[voc.base]] |
| **Topic summaries** | 25 short essays, one per recurring theme (custom domains, selective publishing, rendering fidelity…), written from the cards | [[voice-of-custom/index\|Voice of the Customer]] |
| **SEO strategy and briefs** | How MDFriday plans to be found, and one note per planned page (target keyword, URL, status, search intent) | [[seo/index\|SEO strategy]] · `seo/briefs/` |

## How the parts link

```text
 card ──topic──────▶ topic summary      (why this keeps coming up)
  │
  └──seo_brief─────▶ SEO brief ──▶ SEO strategy   (which page answers it)
                         ▲
                         └── embedded table lists every card pointing here
```

- Every card has exactly one `topic` (a link to a summary) and at most one `seo_brief` (a link to a brief).
- Each brief note embeds a live table of the cards that link to it, so a page always shows the voices behind it.
- The [[seo/index|SEO strategy]] ends with all cards grouped by page.

## Reading the views in voc.base

Open [[voc.base]] and switch views at the top.

| View | Shows | Use it to |
|---|---|---|
| **Triage** | Cards with no `decision` yet | Sort new cards |
| **Reply today** | Last 30 days, `not-replied`, fit `supported` or `partial` | Pick threads worth answering now |
| **In conversation** | Cards where `engagement` isn't `none` | Keep conversations going |
| **Opportunities** | `decision: opportunity`, grouped by topic | See what we can act on, theme by theme |
| **Watch list** | `decision: watch` | Real needs we can't serve yet; review each quarter |
| **Pain map** | `intensity: pain`, grouped by topic | See where people hurt most |
| **By SEO page** | Cards with an `seo_brief`, grouped by page | Choose evidence and quotes for a page |
| **All** | Everything | Search and spot-check |

## Daily workflow

1. **Triage.** Open **Triage**. For each card set `fit` and `intensity`, then `decision` using the rules in [[voc-db/README#How to judge|How to judge]].
2. **Reply.** Open **Reply today**. Answer the person's actual question first; mention MDFriday only if it really fits. Then set `reply: replied`, paste `reply_url`, set `last_touch`.
3. **Log follow-ups.** When someone answers, set `engagement` (`they-replied` or `in-conversation`), update `last_touch`, and add a dated line under **Follow-up log**.
4. **Promote to an SEO brief.** If a voice is a good example for a page, set `seo_brief` to that brief, e.g. `"[[B06-share-obsidian-note]]"`. If no brief fits and the need keeps coming up, propose a new brief in the monthly review.
5. **Monthly.** Use **Pain map** and **By SEO page** to rank pages, go through **Watch list**, and update the topic summaries when a theme changes.

## Adding a new card

1. Create a note in `voc-db/cards/` from [[_template]].
2. Name it `YYYY-MM-DD-platform-slug.md` (post date, platform, short slug).
3. Check the `url` isn't already in the database: one card per post.
4. Paste the quote **verbatim** — only words that really appear in the post.
5. Fill in `need`, `pain`, `topic`, `platform`, `author`, `date`. Leave `decision` empty so it shows up in **Triage**.
6. `reply`: `not-replied` for forum, Reddit and HN posts from 2025 onwards; `not-appropriate` for older posts and blog articles.

## Fields in short

`fit` = how well MDFriday covers it today · `intensity` = pain / need / preference · `decision` = opportunity / watch / fyi · `reply` and `engagement` = our side and their side of the conversation · `seo_brief` = the page this voice supports. Full spec: [[voc-db/README|VOC database README]].

## A note on the first import

Most cards were imported on 2026-10-12 with a script and spot-checked. Their `topic`, `fit`, `intensity`, `decision` and `seo_brief` are first-pass values. Each one says so under **Our assessment**. Correct them as you work through the views.
