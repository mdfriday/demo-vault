---
title: Voice of the Customer database (VOC DB)
tags:
  - voice-of-customer
  - mdfriday
---

# Voice of the Customer database (VOC DB)

← [[voice-of-custom/index|Voice of the Customer]] · [[seo/index|SEO strategy]] · [[how-to-use|How to use this system]]

One voice = one card (a note in `cards/`). Open [[voc.base]] in Obsidian Bases to browse. The goal is to see at a glance what the market is saying, which posts we have replied to, who is talking with us, what is an opportunity, what to watch, and what is just good to know.

Everything comes from public posts. Quotes stay verbatim in the original language; every other field is in English.

## Sources

- Raw cards: `marketing/voice-of-customer/<theme>/*.md`
- Topic summaries (25): `sunwei.xyz/mdfriday/voice-of-custom/*.md`. Each card's `topic` links to one of them.
- SEO pages: `sunwei.xyz/mdfriday/seo/briefs/*.md`. Each card's `seo_brief` links to the page it can support. See [[seo/index|SEO strategy]].

## Field spec

| Field | Meaning | Allowed values / format |
|---|---|---|
| `type` | Fixed | `voc` |
| `id` | Unique ID, reused from the raw card | text |
| `date` | Date of the original post | `YYYY-MM-DD` |
| `platform` | Where it was posted | `reddit` / `obsidian-forum` / `hn` / `blog` / `github` / `youtube` / `other` |
| `url` | Link to the original post | URL (used for de-duplication) |
| `author` | Author of the original post | text |
| `title` | One-line summary | text |
| `quote` | What they said | Verbatim, original language. **Only sentences that really appear in the post or raw card. No rewording, no invention.** |
| `need` | Core need | one sentence |
| `pain` | Pain | one sentence |
| `topic` | Main topic, exactly one | Link to one of the 25 summaries, e.g. `"[[selective-publish-and-privacy]]"` |
| `persona` | Who they are | `student` / `researcher` / `developer` / `writer` / `knowledge-worker` / `team` / `unknown` |
| `competitor` | Tools mentioned | list, may be empty |
| `fit` | How well MDFriday covers it today | `supported` / `partial` / `not-supported` / `wont-do` |
| `intensity` | How much it hurts | `pain` / `need` / `preference` |
| `decision` | What it means for us | `opportunity` / `watch` / `fyi` (empty on a new card = needs triage) |
| `reply` | Have we replied? | `not-replied` / `replied` / `not-appropriate` |
| `engagement` | Did they respond? | `none` / `they-replied` / `in-conversation` |
| `reply_url` | Link to our reply | URL, may be empty |
| `last_touch` | Date of the latest interaction | `YYYY-MM-DD`, may be empty |
| `seo_brief` | SEO page this voice supports | May be empty. A link to a brief note, e.g. `"[[B06-share-obsidian-note]]"`. The full list is in [[seo/index#Page list\|SEO strategy → Page list]]. |
| `source` | Path to the raw card | relative to the workspace |
| `tags` | Fixed | `[voc]` |

Body has three sections: **Context**, **Our assessment**, **Follow-up log**.

## How to judge

**fit (based on confirmed product facts only)**
- `supported`: publish a single note or a folder from a right-click; no account or token for the first publish; local build and preview; themes (including a Quartz-style wiki with graph, search and backlinks); password protection on every plan, supported by all themes; vault sync across devices with MDFriday Sync; custom domains on Personal; ZIP export; roll back to the last 10 releases; subscribe form.
- `not-supported`: Canvas, Excalidraw, Dataview inside folder publishing, redirects, RSS, comments, payments, multi-user collaboration.
- Old Friday plugin: support ends on 2027-01-20. Its users move to MDFriday Sync (sync) and MDFriday Publish (publish); from that date, China-market users get custom support (including deployment and hosting help), and old sync and publish users can contact us for one free year of the matching new service. For old-plugin voices, set `fit` against the new service, not the old plugin.
- If unsure, use `not-supported` and note "to verify" in **Our assessment**.

**intensity**
- `pain`: they are stuck, about to give up, or willing to pay to fix it.
- `need`: they want it but can get by without it.
- `preference`: nice to have.

**decision**
- `opportunity`: `fit` is `supported`/`partial` and `intensity` is `pain`/`need`. We can act on it now (reply, or use it on an SEO page).
- `watch`: a real need we can't serve yet (e.g. Canvas, payments, collaboration). Review it every quarter.
- `fyi`: a preference, or outside our direction.

**reply**
- Posts before 2025-01-01 and blog articles → `not-appropriate`.
- Everything else starts as `not-replied`; after a real reply, set `replied` and fill in `reply_url`.

## Workflow

1. New lead → create a card from [[_template]], leave `decision` empty; it shows up in **Triage**.
2. Triage: fill in `fit` and `intensity`, then set `decision` by the rules above. Set `seo_brief` if a page in the [[seo/index|SEO strategy]] can use it.
3. **Reply today**: cards from the last 30 days, `not-replied`, `supported`/`partial`. After replying, update `reply`, `reply_url`, `last_touch`.
4. They respond → update `engagement` and `last_touch`, and add a dated line to **Follow-up log**.
5. Monthly review: use **Pain map** and **By SEO page** to prioritize SEO pages; go through **Watch list**.

## Naming and de-duplication

- File name: `YYYY-MM-DD-platform-slug.md`, e.g. `2026-04-09-reddit-share-single-note.md`.
- De-duplication: one card per `url`. Follow-up replies from the same person in the same thread go into **Follow-up log**, not a new card.

## Migration note

The first 10 cards were triaged by hand. The remaining cards were imported on 2026-10-12 by script (topic, fit, intensity, decision and seo_brief chosen by keyword rules, then spot-checked) and say so in **Our assessment**. Fix values as you review them.

## Views (voc.base)

Triage / Reply today / In conversation / Opportunities (grouped by topic) / Watch list / Pain map (grouped by topic) / By SEO page / All.
