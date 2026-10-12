---
title: Sitemap and canonical URL
weight: 56
tags: [reference, seo]
date: 2026-10-11
lastmod: 2026-10-11
description: How a MDFriday site builds its public address, sitemap, and canonical link. A custom domain needs one more publish after it is Active.
---

# Sitemap and canonical URL

Applies to plugin **v26.10.2** source. Update the plugin if your build is older, then publish again. This page does not promise that Google has indexed your site.

## The public address

In-page links stay as paths. The public address of a page is:

**host + path**

| How the site is hosted | Host | Path |
| --- | --- | --- |
| Share link | `https://share.mdfriday.com` | `/s/{site id}/…` |
| Custom domain, after you publish again | `https://your domain` | `/…` (the site root) |

The plugin writes that host when you publish. It does not put the host into the path setting. Local preview has no host, so a preview sitemap is not a public sitemap.

## What to do for a custom domain

1. Finish [[../publish/custom-domain|Custom domain]] until the status is **Active**
2. **Publish once more**
3. Open `https://your-domain/sitemap.xml`

Each `<loc>` should be an absolute URL on your domain, for example `https://notes.example.com/about.html`. A location that is only `/about.html` is not a sitemap a crawler can use. `robots.txt` should contain a `Sitemap:` line pointing at that file.

The canonical link and the social URL (`og:url`) use the same absolute address. The description tag uses the note's `description` field when you set one.

## What this is not

- There is no switch here to block or invite AI crawlers
- There is no per-page redirect list. Renaming a note changes its URL. See [[../publish/update-site|Update a published site]]
- Baidu indexing and speed inside mainland China are not covered. They have not been measured

## Related

- [[../publish/custom-domain|Custom domain]]
- [[../publish/update-site|Update a published site]]
- <https://mdfriday.com/products/obsidian-publish/>
