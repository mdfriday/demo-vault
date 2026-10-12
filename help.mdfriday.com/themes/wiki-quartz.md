---
title: Wiki themes in MDFriday
weight: 53
tags: [themes, Wiki]
date: 2026-09-19
lastmod: 2026-10-11
description: Folder publish offers Quartz, Creator, Flint, and Jasper. All four search, including Chinese. The layout is what differs.
---

# Wiki themes in MDFriday

Applies to plugin **v26.10.2**.

A folder always uses Wiki mode. The picker lists four themes. The default is **Quartz**. Book, notebook, and other wiki-tagged packs are hidden on purpose.

All four support wikilinks, callouts, Mermaid, math, dark mode, site search, and a graph. Search accepts Chinese as well as English. Where the graph sits depends on the layout, so confirm it in Live demo.

| Theme | Best for | How the site is organized |
| --- | --- | --- |
| **Quartz** | A knowledge base that should feel like a vault | Sidebar explorer, graph, backlinks, table of contents. This is the default |
| **Jasper** | A help center | Home page of collection cards. An article has a graph and a table of contents |
| **Flint** | Product documentation | Top bar, left navigation, table of contents, and a control to copy the page |
| **Creator** | A digital garden of cards | Home is a hero plus cards. Top-level folders become sections. See below |

Quartz's graph, search, and backlinks come from the Quartz project. MDFriday packages that path so you preview and publish from Obsidian without Node, Git, or a CI job.

## Creator's homepage

Creator reads structure you already have in the folder:

| In the folder | On the home page |
| --- | --- |
| Root `index.md` | Hero. The title and description become the hero text. The body is the introduction |
| `featured: true` on a note | A featured card |
| A top-level folder | A section, plus a garden menu when the site has folders |
| Folder `index.md` | That section's title, description, and intro. Optional `icon:`. Optional `layout: stream` or `layout: grid` |
| Daily notes, or files named `YYYY-MM-DD` | A time stream |
| `#seedling`, `#budding`, `#evergreen` | Growth stage. The most mature tag wins. No tag means seedling |

You do not need a config file for those. `cover` on a note is the card image.

## What a wiki theme will not do

- Run Dataview or Bases. Those queries run only in **Faithful** mode, and Faithful is single-note only
- Publish Canvas or Excalidraw
- Offer RSS or comments
- Let you delete the **Built with MDFriday** footer

## Related

- [[../publish/publish-folder|Publish a folder]]
- [[../reference/supported-syntax|Supported syntax]]
- <https://mdfriday.com/solutions/digital-garden/>
