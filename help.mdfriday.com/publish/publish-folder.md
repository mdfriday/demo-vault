---
title: Publish a folder (Wiki)
weight: 32
tags: [publish, Wiki, folder]
date: 2026-09-19
---

# Publish a folder (Wiki)

## Goal

Select **one folder** in the vault and publish it as a Wiki / digital garden with wikilinks / graph (Quartz-family themes).

## Prerequisites

- Desktop plugin enabled
- Folder contains publishable Markdown (curate a public subset first to avoid shipping private notes)
- Understand: **folders cannot use faithful publish**; they always go through the Wiki engine

## Steps

1. In the file tree, **right-click the folder** → **Publish to MDFriday**
2. Panel badge is “Folder”; publish mode is fixed to **Wiki publish**
3. Pick a theme in the **Wiki skin** list (defaults toward `quartz`; only Quartz-family themes are shown)
4. (Optional) Open the theme **Live demo** to compare looks
5. (Optional) [[password|Access password]], [[local-preview|Local preview]]
6. **Publish**, then copy the URL

<!-- MEDIA: screenshot — folder Wiki skin picker -->
![Placeholder: Wiki publish](../images/placeholder-wiki-publish.png)

> [!warning] Scope = the folder you selected
> Only content inside that folder ships. Whole-vault one-click upload is not the default product model. Keep private notes outside the folder, or do not select a parent that contains them.

## Confirm success

- Browser can navigate multiple pages and follow `[[wikilinks]]` (exact capability depends on the Quartz theme)
- The project binds to that **folder path**; after rename the plugin tries to migrate pathConfigs (if it fails, see troubleshooting)

## Related

- [[../themes/wiki-quartz|Wiki / Quartz themes]]
- <https://mdfriday.com/solutions/digital-garden/>
- [[modes|Publish modes]]

## Common failures

| Symptom | What to do |
| --- | --- |
| Faithful is unavailable | By design: multi-page needs the Wiki engine |
| Links broken / empty graph | Check notes are inside the selected folder; wikilink targets must be in scope too |
| Odd Chinese-path behavior | See [[../faq\|FAQ · Chinese paths]] |
