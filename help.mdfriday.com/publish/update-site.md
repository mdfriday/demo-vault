---
title: Update a published site
weight: 34
tags: [publish, update]
date: 2026-10-11
lastmod: 2026-10-11
description: Edit the note in your vault, then publish the same target again. There is no second copy to sync, and mobile cannot publish.
---

# Update a published site

Applies to plugin **v26.10.2**.

## Goal

Replace the live site with the notes as they are now. The notes in the vault are the only copy. There is no Git repository to keep in step with the website.

## Prerequisites

- The same note or folder you published before
- Obsidian desktop. The plugin does not publish from a phone or iPad

## Steps

1. Edit the note in Obsidian. Do not keep a second Markdown copy just for the website
2. Right-click that **same** note or folder → **Publish to MDFriday**
3. Confirm the publish target path is the one already bound to this project
4. Optional: **Preview**. A preview does not update the public site and does not create a history entry
5. Click **Publish**
6. Open the same public URL. Personal keeps the last **10** publishes and can roll back. See [[history|Publish history and rollback]]

Unchanged files are reused from the previous snapshot. One file can be at most **25 MB**. One publish can include at most **20,000** files.

## URLs when you rename or move

The public path is the vault path:

| In the vault | On the site |
| --- | --- |
| `notes/Hello.md` | `…/notes/Hello.html` |
| `garden/index.md` | `…/garden/` |
| A file whose name contains Chinese | Those characters stay in the URL |

After a rename, the old URL stops working. MDFriday does not write redirects for renamed notes. The only automatic redirects are: a share link sending visitors to your custom domain once that domain is active, and a slash added to a folder URL.

If a link you already sent must keep working, do not rename the file. Put the new title in the note's `title` field instead of changing the file name.

## Related

- [[publish-note|Publish a note]]
- [[publish-folder|Publish a folder]]
- [[../reference/seo|Sitemap and canonical URL]]
- <https://mdfriday.com/solutions/digital-garden/>

## Common failures

| Symptom | What to do |
| --- | --- |
| A new site appeared instead of an update | You published a different note or folder. Open the original target and publish that |
| Old URL is a 404 after you tidy the vault | Expected. There is no rename redirect. Publish the new path and update the links you control |
| Wanted it to publish from the phone | Not available. Edit on the phone if you use Sync, then publish from the desktop |
