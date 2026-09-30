---
title: Knowledge Structure on the Web
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Digital gardeners want more than pages; they want the site to feel like their vault: wikilinks, backlinks, a graph, sidebar navigation, search and clean URLs."
---

# Knowledge Structure on the Web

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Digital gardeners want more than a pile of pages; they want the site to feel "like my vault": wikilinks that don't break, backlinks and a graph, sidebar navigation that matches the folders, a table of contents (TOC), full-text search, and clean URLs (no vault name, home page at `/`). Ordinary static site generators treat wikilinks as broken syntax; Obsidian Publish's graph can't be tuned and doesn't show on phones, and its search can't filter by path; in a single shared note, every internal link breaks.

> [!info] Signal (approximate)
> ~59 VOC cards · ~16 YouTube comments (6 on sidebar / file-tree navigation, 4 on the graph, 1 on search, 1 on links in a single note, etc.).
> Ranked **#4**: the core expectation of digital gardeners.

## Voices

- “takes a folder of Markdown files with wiki links and generates HTML files” — Hacker News · 2021-11-06 · <https://news.ycombinator.com/item?id=29126212>
- “is there a way to get something similar to the left-sidebar file navigation that we see in Obsidian Publish?” — YouTube comment · ~2022 · <https://www.youtube.com/watch?v=ITiiuBNVue0>
- “How do you control the structure of the navigation pane ?” — YouTube comment · ~2025 · <https://www.youtube.com/watch?v=7f8e5IiUkeo>
- “Is there a way that links in my original Note can work on the shared version of the Note I send someone?” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=j7eDF7DHut0>
- “Looks like the obsidian publish doesn’t support path search?” — Reddit r/ObsidianMD · 2026-07-04 · <https://www.reddit.com/r/ObsidianMD/comments/1umzykq/best_way_to_search_in_obsidian_publish_site>
- “Is there any chance to publish/embed the graph view?” — YouTube comment · ~2025 · <https://www.youtube.com/watch?v=-5RO4Xsw9Ec>

## Why it hurts

- **The links are the knowledge.** For PKM users, the relationships between notes are worth more than any single note. Break the relationships and the site is just a pile of isolated articles.
- **Navigation decides whether readers explore.** A digital garden is read by wandering, not by reading a blog in time order. Without a sidebar and a graph, readers read one page and leave.
- **After migrating, it "doesn't feel like my vault".** Many SSGs treat wikilinks and folder trees as second-class citizens, so users either rewrite every link or accept an unfamiliar website.

## How people cope today

- Using Quartz, because its graph, backlinks and callouts are closest to Publish, while putting up with the [[setup-and-deploy-barrier|setup barrier]].
- Adding plugins or scripts to Hugo / MkDocs to convert wikilinks.
- Living with Publish's graph and search limitations.

## MDFriday's response

- **Select a folder, right-click, publish it as a website**: the shortest path from "a folder" to "a Wiki / digital garden".
- **AS mode** renders notes the way Obsidian does.
- Whether every wikilink inside the folder becomes a site link, backlinks, graph, full-text search, controllable sidebar order, custom slugs: **all (unconfirmed)**. Suggestion: confirm them one by one and add them to a support matrix.

## Open questions

- When publishing a folder, what happens to wikilinks that point to (unpublished) notes outside it? This ties directly to the [[selective-publish-and-privacy|privacy boundary]].
- Which do readers use most: the sidebar, search or the graph? Interviews can settle the priority.
- Do anchors for Chinese headings and Chinese search work? See [[chinese-filenames|Chinese Filenames]].

## Related

- [[selective-publish-and-privacy|Selective Publish & Privacy]]
- [[stable-links-and-redirects|Stable Links & Redirects]]
- [[rendering-fidelity|Rendering Fidelity]]
- [[large-vault-builds|Large Vault Builds]]
