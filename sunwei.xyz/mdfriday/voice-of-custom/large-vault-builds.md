---
title: Large Vault Builds
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Past a thousand notes, SSG build times grow non-linearly: one edit means a full rebuild, and some builds fail outright with out-of-memory errors."
---

# Large Vault Builds

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Once a vault reaches a thousand-plus notes, self-hosted SSG build times grow non-linearly: one edit means a full rebuild, components such as Explorer make build time rise exponentially, around 1,700 notes can hit a call-stack overflow, and Digital Garden runs out of memory on Vercel. Hosted options have similar problems: with a large vault, just opening Publish's publish dialog takes 30+ seconds. Users with academic wikis and large digital gardens care about this most.

> [!info] Signal (approximate)
> ~5 web supplement sources (latest 2025-07) + several VOC cards about slow publishing of large vaults.
> Relevance to MDFriday: **medium** (local build performance needs real testing).

## Voices

- “Slow / Exponential Build Time Caused by Component.Explorer” — GitHub Issues · 2024-09-15 · <https://github.com/jackyzha0/quartz/issues/1411>
- “all 2319 need to be emitted which takes 60 seconds” — GitHub Issues · 2023-12-17 · <https://github.com/jackyzha0/quartz/issues/633>
- “It seems to happen only with a very large number of Markdown files. My vault currently has 1708 notes.” — GitHub Issues · 2025-07-27 · <https://github.com/jackyzha0/quartz/issues/2064>
- “Out of Memory - Vercel Deploy Failing” — GitHub Issues · 2025-03-27 · <https://github.com/oleeskild/obsidian-digital-garden/issues/675>
- 「支持全局图谱，但1K+笔记就很卡」 — Obsidian Chinese forum · 2022-07-14 · <https://forum-zh.obsidian.md/t/topic/8852>
  - *Translation:* Supports a global graph, but it gets really laggy once you have 1K+ notes.
- “I need to wait >30 seconds every time I want to publish” — Obsidian Forum · 2022-12-28 · <https://forum.obsidian.md/t/reduce-publish-friction-30-second-to-open-the-modal-on-large-vault/50860>

## Why it hurts

- **The most dedicated writers hit the wall first.** The more notes you have, the slower the tool: it punishes the most loyal users.
- **Slowness changes behavior.** If each publish takes ages, users batch changes and hold off, and the site gradually drifts away from the vault (see [[sync-and-update-workflow|Sync & Update Workflow]]).
- **When a build fails, ordinary users have nowhere to start.** Stack overflows and OOM errors mean nothing to a writer.

## How people cope today

- Filing bugs in GitHub Issues and waiting for fixes, or turning off certain components themselves.
- Publishing only a small part of the vault.
- Switching to a faster SSG, or putting up with Publish's wait.

## MDFriday's response

- MDFriday also uses a **local build**, so build and upload times for 1k / 3k / 5k notes, and whether incremental publishing is supported, need **real testing before any claims (unconfirmed)**.
- **Selective publish** itself helps somewhat: publish only the folders that need to be public.
- If testing goes well, MDFriday could publish a "time to publish 5,000 notes" benchmark that answers the Quartz issues directly.

## Open questions

- What are MDFriday's current build time and memory use on large vaults?
- Is incremental publishing (rebuilding only changed pages) already supported (unconfirmed)?
- How do the graph and search index perform in the browser on large sites? See [[seo-discoverability-and-ai-crawlers|SEO, Discoverability & AI Crawlers]].

## Related

- [[sync-and-update-workflow|Sync & Update Workflow]]
- [[seo-discoverability-and-ai-crawlers|SEO, Discoverability & AI Crawlers]]
- [[knowledge-structure-on-the-web|Knowledge Structure on the Web]]
- [[media-and-storage-limits|Media & Storage Limits]]
