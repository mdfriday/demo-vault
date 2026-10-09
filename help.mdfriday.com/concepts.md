---
title: How it differs from Obsidian Publish / Quartz
weight: 20
tags: [concepts, comparison]
date: 2026-09-19
lastmod: 2026-10-09
description: How MDFriday Publish differs from Obsidian Publish and self-hosted Quartz: a local build, no account required, and what you still run yourself.
---

# How it differs from Obsidian Publish / Quartz

> [!quote] For people choosing a stack
> Below are **facts the current MDFriday Publish plugin can deliver**, not marketing roadmap items treated as shipped features.

## One-liners

| Option | One-liner |
| --- | --- |
| **MDFriday Publish** | Pick a note/folder in Obsidian → build locally → one-click upload to the MDFriday CDN; Guest works without an account |
| **Obsidian Publish** | Official hosted reader; subscription-style vault / site publishing |
| **Self-hosted Quartz** | Free and powerful; you bring Node / a repo / CLI or CI |

## Comparison (honest)

Sources: product comparison table on the website + plugin behavior (Cloudflare publish, faithful / themed / Wiki fork).

| Dimension | MDFriday Publish | Obsidian Publish | Self-hosted Quartz / Hugo |
| --- | --- | --- | --- |
| Publish scope | **Single note or folder** (you choose what ships) | Vault / site–oriented workflows | Project directory; you draw the boundary |
| Where it builds | **Local** build; upload is static output | Mostly hosted-side | Local or CI |
| Source Markdown uploaded as an editable copy? | Product stance: **source notes stay on device**; cloud hosts build output | Hosting-first | Usually lives in a Git repo |
| Local preview | ✓ In-plugin local server | — | ✓ (you start it) |
| No-account trial | ✓ **Guest** | Usually needs an Obsidian account and subscription | “Account trial” does not apply |
| Look and feel | **Faithful publish** (close to in-vault reading) or **Notes / Quartz themes** | Official reader look | Theme ecosystem you maintain |
| Wiki capability | Folder → Quartz-family Wiki themes (graph, backlinks, etc.) | Official feature set | Upstream Quartz you operate yourself |
| Custom domain | **Personal**: **$5/month** or **$50/year** includes 1 domain; **$60/year** includes 3. Automatic HTTPS | Supported on the official stack | DIY |
| History / rollback | **Personal** | Limited / product-specific | Git DIY |
| Ops burden | Done inside the plugin; no DIY CLI | Low (official hosting) | High (toolchain + config) |

## Two publish behaviors (product fork)

The plugin forks by selection type (see `publish-config` and UI copy):

1. **Single note**
   - **Faithful publish**: default recommendation; keep the local preview feel (theme, community plugin rendering, CSS snippets)
   - **Single-page theme (themed)**: pick a Notes-family theme (default slug: `paper`)
2. **Folder**
   - **Wiki only (themed)**: faithful is not available; a Wiki engine is required for multi-page, wikilinks, and graph (default slug: `quartz`)

See [[publish/modes|Publish modes]] and [[mdfriday/help/themes/index|Themes]].

## Difference from older “Friday” help

Older **Friday Help** mixed **Sync + Publish** and described Netlify, FTP, and bulk Hugo exports. Those publish paths are not in MDFriday Publish.

Current **MDFriday Publish**:

- Publish goes to MDFriday hosting. A share link is the default; Personal can add a custom domain
- Guest → share link is the trial path. Guest content clears at the next **UTC 00:00**
- To keep a copy of the built files, preview locally and [[publish/export|export a ZIP]]. That ZIP is static files only
- For Sync, use the separate Sync product — do not look for whole-vault sync inside this plugin

## Related

- [[get-started|Install and first publish]]
- <https://mdfriday.com/products/obsidian-publish/>
- <https://mdfriday.com/solutions/share-a-note/>
- <https://mdfriday.com/solutions/digital-garden/>
