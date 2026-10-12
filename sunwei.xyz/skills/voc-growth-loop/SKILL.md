---
name: VOC growth loop
description: >-
  Use for the daily run that finds new public user voices about publishing notes
  (Obsidian etc.), adds them as cards to the MDFriday VOC database, links them
  to topics and SEO briefs, and the weekly/monthly check that proves the loop
  with real SEO data.
---
# VOC growth loop

Goal: grow the public VOC database organically every day, and prove with real search data that pages built from these voices bring the traffic we want.

System (in the vault `demo-vault/sunwei.xyz/mdfriday/`):
- `voc-db/cards/` one card per public voice; spec in `voc-db/README.md` (source of truth, read it every run); template `voc-db/_template.md`; views `voc-db/voc.base`.
- `voice-of-custom/` 25 topic summaries; each card's `topic` links to exactly one.
- `seo/index.md` strategy + page list; `seo/briefs/Bxx-*.md` one note per planned page; card `seo_brief` links to one.
- `how-to-use.md` usage guide. Everything public, English (quotes stay in original language).

## Daily run
1. Search the last 1-3 days on Reddit (r/ObsidianMD, r/selfhosted, r/PKMS, r/Blogging), Obsidian forum, HN, GitHub issues of Quartz / Digital Garden / Obsidian Publish alternatives. Queries come from the target keywords in `seo/briefs` plus topic names (publish obsidian, share note, without github, custom domain, digital garden, obsidian publish alternative, password, etc.).
2. Keep only real users with a publishing / sharing / personal-site need. Skip vendor promos, our own posts, spam.
3. De-dupe by `url` against existing cards. Same person same thread = add to that card's Follow-up log.
4. Create a card from the template, named `YYYY-MM-DD-platform-slug.md`. Rules:
   - `quote` verbatim, copied from the post. Never paraphrase or invent. No usable text = use the title and say so in Context.
   - `fit` only from confirmed product facts listed in the README; unsure = `not-supported` + "to verify".
   - Set `intensity`, then `decision` by README rules (opportunity = supported/partial and pain/need; watch = real need we can't serve; fyi = preference/off-direction). If genuinely unsure leave `decision` empty so it lands in Triage.
   - `topic` = best of the 25 summaries; if none fits for 3+ cards, propose a new topic to the user instead of forcing.
   - `seo_brief` = brief whose target keyword/intent the voice proves; empty if none. If several voices point to a page that has no brief, propose a new brief.
   - `reply: not-replied`, `engagement: none` for 2025+ posts; `not-appropriate` for older posts and blogs.
5. Reply candidates (fresh, not-replied, supported/partial): draft a helpful reply for the user to review. Never post or send yourself. After the user replies, update `reply`, `reply_url`, `last_touch`.
6. Revisit `In conversation` cards: check threads for new responses, update `engagement`, `last_touch`, Follow-up log.
7. Also fix a few auto-triaged cards each day (marked "Auto-triaged"): check quote, topic, fit, decision; remove the marker when reviewed.
8. Report to the user: new cards (count by topic/decision), top 3 opportunities with links, reply drafts, proposed new topics/briefs, cards fixed.

## Weekly / monthly proof with SEO data
1. For each brief page that is live, pull Google Search Console (impressions, clicks, queries, position) and GA4 `install_click` by page/UTM campaign. No data connected = say so, do not invent numbers.
2. Record in the brief note a dated metrics line, and compare: card count + intensity for the brief vs impressions/clicks/install_click.
3. Check that real search queries match the words users use in quotes; add new query wording as candidate keywords.
4. Feed the monthly report (`arch/seo/reports/monthly/`): which VOC-backed pages gained traffic, which got none, and the method lesson (section 11 Method notes).
5. Respect the no-data rule: do not change titles or main keywords of live pages before the 8-week review.

## Guardrails
- Public pages: no internal staff names, IDs, prices in briefs, or unconfirmed product claims.
- Fact priority: founder confirmation > backend source > help center > old drafts.
- Never post replies, DMs, or emails without the user's explicit send.
