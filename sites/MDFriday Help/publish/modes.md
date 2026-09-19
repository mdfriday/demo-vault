---
title: Publish modes
weight: 33
tags: [concepts, modes]
date: 2026-09-19
---

# Publish modes

## Goal

Understand when **Faithful publish / Single-page theme / Wiki publish** appear in the panel, and what the defaults are.

## Rules (matches source)

| Selection | Available modes | Default (right-click publish) |
| --- | --- | --- |
| **Note** | `faithful` · `themed` (single-page theme) | **Faithful**, no theme, no password |
| **Folder** | `themed` only (UI calls it Wiki publish) | **Wiki**, default theme slug **`quartz`**, no password |

> [!info] Copy reference (from zh-CN UI)
> - Faithful publish: keep the local preview feel (theme, community plugin rendering, CSS snippets)
> - Single-page theme: curated single-page themes, optionally with Live demo
> - Wiki: Quartz / Obsidian Publish–style digital garden · graph · multi-page
> - Folders cannot be faithful: multi-page structure needs the Wiki engine for wikilinks and graph

## How to choose (practical)

| Scenario | Recommendation |
| --- | --- |
| Share something that should “look like the vault” | Note → **Faithful** |
| Want a more standalone / branded page | Note → **Single-page theme** |
| A cluster of interlinked notes | **Folder → Wiki** |

## Related

- [[publish-note|Publish a note]]
- [[publish-folder|Publish a folder]]
- [[../themes/_index|Themes]]
