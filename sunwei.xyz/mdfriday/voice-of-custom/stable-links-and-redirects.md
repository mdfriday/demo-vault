---
title: Stable Links & Redirects
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Rename a note or move it to another folder, and links you've already shared turn into 404s; users need redirects and permalinks that survive renames."
---

# Stable Links & Redirects

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Digital gardens keep growing and being reorganized. But rename a note or move it to another folder while tidying up, and every link already shared turns into a 404. Users need a redirect table and permalinks that don't change on rename; tool upgrades also mustn't silently change URL rules (for example Quartz v5 lowercased all URLs, and old links 404'd en masse). Chinese users also report that after renaming they have to delete and republish; it doesn't overwrite automatically.

> [!info] Signal (approximate)
> ~5 web supplement sources (4 quoted, 1 corroborating); latest evidence 2026-06.
> Relevance to MDFriday: **medium**. The more users write and restructure, the more certain they are to hit it.

## Voices

- “I’d like to be able to reorganize the content on my site without resulting in lots of 404 errors.” — Obsidian Forum · 2023-06-18 · <https://forum.obsidian.md/t/allow-for-custom-redirects/61766>
- “If you change that or the note’s title, then the link goes to a 404.” — Obsidian Forum · 2023-12-28 · <https://forum.obsidian.md/t/obsidian-publish-note-permalink-options/73787>
- 「需要先删除，然后再发布新的，不能检测到我改名字，然后自动覆盖吗？」 — Obsidian Chinese forum · 2022-05-08 · <https://forum-zh.obsidian.md/t/topic/7321>
  - *Translation:* I have to delete it first and then publish the new one. Can't it detect that I renamed it and overwrite it automatically?
- “upgrading to v5 breaks all previously published URLs that contained uppercase letters, resulting in widespread 404 errors.” — GitHub Issues · 2026-06-05 · <https://github.com/jackyzha0/quartz/issues/2432>

## Why it hurts

- **A shared link is a promise to readers.** External references, search engine indexes and social media shares all depend on it.
- **Reorganizing is the nature of a garden.** If renaming costs a pile of 404s, users stop tidying and the vault slowly gets messy.
- **Accumulated SEO gets wiped out.** 404s make already-indexed pages drop out of search results.

## How people cope today

- Not renaming, or settling names before publishing.
- Writing permalinks / slugs by hand in frontmatter.
- Checking URL changes by hand when upgrading tools, or not upgrading at all (see [[maintenance-burden|Maintenance Burden]]).

## MDFriday's response

- Redirects and permanent links are not among the currently confirmed capabilities.
- Suggestions: generate permanent links from a slug or alias in frontmatter; automatically create 301 redirects when a rename is detected at publish time; keep existing URL rules unchanged across plugin upgrades (**all unconfirmed**).
- After renaming and republishing, whether old pages are cleaned up or left behind: **(unconfirmed)**; this also relates to the [[selective-publish-and-privacy|privacy boundary]].

## Open questions

- What rule does MDFriday currently use to generate URLs: filename, path or frontmatter?
- Are URLs generated from Chinese filenames stable and readable? See [[chinese-filenames|Chinese Filenames]].

## Related

- [[knowledge-structure-on-the-web|Knowledge Structure on the Web]]
- [[seo-discoverability-and-ai-crawlers|SEO, Discoverability & AI Crawlers]]
- [[chinese-filenames|Chinese Filenames]]
- [[maintenance-burden|Maintenance Burden]]
