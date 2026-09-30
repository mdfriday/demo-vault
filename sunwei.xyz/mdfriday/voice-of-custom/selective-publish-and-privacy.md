---
title: Selective Publish & Privacy
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "One vault holds diaries, drafts and notes meant to be public. How to publish only part of it, how to avoid publishing by mistake, and whether anything leaks afterwards is often called the only blocker."
---

# Selective Publish & Privacy

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Most people keep "everything in one vault": diaries, drafts, client material and notes they want to make public, all mixed together. The pain has three layers: ① **how to publish only part of it** (by folder, by tag, by `publish: true`); ② **how to avoid publishing by mistake** (a publish flag in a template overrides a folder exclusion; one "add linked notes" click pulls in hundreds of notes); ③ **leaks after publishing**: unpublished notes appear in the public graph, links inside comments get picked up by the graph, notes marked hidden still show up in site search, dead links expose the titles of private notes, and attachments aren't controlled. Some people also need **paragraph-level** hiding, for example a D&D game master who doesn't want players to see spoilers.

> [!info] Signal (approximate)
> ~52 VOC cards · ~17 YouTube comments · 1 web supplement source.
> Ranked **#5**: medium frequency, but often called "the only blocker".

## Voices

- “there are a lot of private content like diaries, drafts and incomplete notes that I don't want to publish” — Reddit r/ObsidianMD · 2025-08-25 · <https://www.reddit.com/r/ObsidianMD/comments/1mznj8r/how_to_publish_only_part_of_my_vault>
- “the interactive graph in Obsidian Publish still detects and displays links found inside these comments.” — Obsidian Forum · 2026-05-31 · <https://forum.obsidian.md/t/exclude-links-in-comments-from-obsidian-publish-graph-view/114833>
- “in all situations I would want to share some but not all of my notes” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=ITiiuBNVue0>
- “the idea that it would be there for the whole internet to see and I can do nothing about it, puts me off.” — YouTube comment · ~2022 · <https://www.youtube.com/watch?v=1pf6aj3Uwuk>
- “too difficult to make a separation between public and personal information” — Obsidian Forum · 2021-07-29 · <https://forum.obsidian.md/t/cancel-publish-how/21705>
- “When a note is marked as hidden client side, it is still searchable in the search bar on obsidian publish.” — Obsidian Forum · 2024-03-15 · <https://forum.obsidian.md/t/hidden-notes-accessible-through-search-in-publish/78634>
- “I wish there was some plugin or a way to add publish tag to hundreds of my notes with a click” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=eULVrTjT11w>
- “Choosing what content to publish (or not) is hard” — Personal blog · 2023-11-23 · <https://untested.sonnet.io/notes/abusing-and-reviewing-obsidian-publish/>

## Why it hurts

- **One mistaken publish can't be undone.** Once a diary or client file is indexed by a search engine, it's hard to take back. That fear makes some people not publish at all.
- **Users don't want to reorganize their vault just to publish.** They want to keep one vault rather than split it into a "public vault" and a "private vault".
- **Leaks often happen where users can't see them**: the graph, the search index, dead links, attachments. Users can pick the right notes and still leak.

## How people cope today

- Splitting into two vaults, or creating a dedicated "public" folder and copying notes by hand.
- Adding a publish flag to frontmatter note by note (some wish they could "add it to hundreds of notes with one click").
- Using metadata-driven options such as Quartz's ExplicitPublish or Enveloppe, which still don't control attachments and the graph.

## MDFriday's response

- **Selective publish**: only the notes or folders you select are published; everything else stays local.
- **Local build**: the website is generated locally and only the generated site is uploaded, never the vault itself.
- Whether the graph, site search or dead links expose titles of unpublished notes, and whether attachments leak: **(unconfirmed)**. If "no" can be confirmed, it's worth stating as a public promise.
- Paragraph-level hiding (unconfirmed; the showcase draft listed it as roadmap).

## Open questions

- If a published note links to an unpublished note, what does the website show: the link text, the title, or nothing?
- Do users prefer choosing "by folder" or "by tag / frontmatter"?
- Could there be a pre-publish preview listing which files will become public?

## Related

- [[access-control-and-collaboration|Access Control & Collaboration]]
- [[knowledge-structure-on-the-web|Knowledge Structure on the Web]]
- [[single-note-sharing|Single-note Sharing]]
- [[media-and-storage-limits|Media & Storage Limits]]
