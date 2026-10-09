---
title: Export a ZIP
weight: 35
tags: [export, preview]
date: 2026-10-09
lastmod: 2026-10-09
description: After a local preview, save the built static site as a ZIP. Available on every plan. The ZIP does not include hosting features.
---

# Export a ZIP

## Goal

Save the site you just previewed as a ZIP of static files, so you can open it offline or put it on another static host.

## Prerequisites

- Obsidian desktop
- A successful **local preview** of this project. *Export* is not on the panel until the preview result is showing

## Steps

1. Open the right-hand **Publish** tab and click **Preview**
2. Wait until the result says **Local preview**
3. Click **Export** under that result
4. In the save dialog (**Save site archive**), choose where to put the ZIP. The suggested name is the project name plus `.zip`
5. After it finishes, Obsidian shows the path it wrote

<!-- MEDIA: screenshot — Export under a local preview result -->
![Placeholder: export after preview](../images/placeholder-export.png)

## Confirm success

- The notice says the site was exported, and the ZIP is at the path you chose
- Preview stays local. Export does **not** publish the site and does **not** write publish history
- Any plan can export, including Guest. A Guest site on MDFriday still clears at the next UTC 00:00. The ZIP on your computer is a separate copy and is not cleared

## What is in the ZIP

The ZIP is the built static site (HTML, CSS, images). It is not your vault, and it is not a Markdown source backup.

Hosting features are not in the file. A custom domain and the subscribe form need MDFriday hosting. Opening the ZIP elsewhere will not turn those on.

## Related

- [[local-preview|Local preview]]
- [[unpublish|Unpublish]] (takes a live MDFriday site offline; it does not delete a ZIP you already saved)
- <https://mdfriday.com/pricing/>

## Common failures

| Symptom | What to do |
| --- | --- |
| No **Export** button | Preview first. Export only appears on a local-preview result |
| “Please generate a preview first” | The preview server is gone. Click **Preview** again, then **Export** |
| Wanted the live site taken down | Export only copies files to your computer. Use [[unpublish\|Unpublish]] for a site that is already public |
