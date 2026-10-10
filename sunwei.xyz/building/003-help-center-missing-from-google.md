---
title: "Why Our Help Center Was Missing from Google"
date: 2026-10-09
lastmod: 2026-10-09
tags:
  - budding
description: "The help center's sitemap and canonical URLs were relative, so Google could not use them. The fix is in the source. The live site is not updated yet."
---

The help center looked finished. The pages were online. Search still had almost nothing to work with.

I publish [help.mdfriday.com](https://help.mdfriday.com) with the same tool our users use. On 9 October 2026 I opened the files a crawler actually reads. The sitemap listed pages as `/publish/custom-domain.html`, with no host. The canonical link and the social URL were the same kind of path. There was no `robots.txt`. The description tag was empty. The homepage title was the note title, 「首页」, not the name of the site.

A sitemap Google can fetch needs an absolute URL in each `<loc>`. A relative one does not count. That is a product bug, not a writing problem. Every site published with MDFriday had it, including this garden.

## What I had packed into one setting

The publisher already had `baseURL`. It is the path prefix: `/s/{siteId}/` on a share link, `/` on a custom domain, and a local path in preview. I had been tempted to drop the full public URL in there so the sitemap would look absolute.

That would have mixed two jobs. Links inside the page, the graph, and local preview all treat `baseURL` as a path. Putting `https://help.mdfriday.com/` in it would have broken those.

So the public origin is now a separate setting, `canonicalHost`. It is only the scheme and host, for example `https://help.mdfriday.com`. The address of a page is that host plus the path. In-page links stay as paths. Local preview still has no host.

## What the templates were doing wrong

A few template mistakes sat on top of that:

- The sitemap printed a last-modified date when the page did **not** have one, and skipped it when it did.
- A multilingual sitemap repeated the same language link once more, after the list.
- With no description in the note, the meta description was left blank instead of using a short plain-text summary.
- The home page used the note's title. On the old Chinese site that title was 「首页」.

`robots.txt` did not exist, so there was no pointer to the sitemap either.

## What is true today

The source for this is written. It is not what the live help center is serving.

The theme packages on the CDN are still the old templates. The plugin build people have installed does not yet include the new setting. I have not republished help.mdfriday.com, and I have not checked Search Console to see the sitemap read. Until that republish, the live pages can still show relative addresses.

I am not going to write a guide called "Obsidian SEO" until that check is done. A how-to that tells people to submit a sitemap, while our own sitemap is still relative, would be the same mistake twice. That guide, if it earns a page, belongs on [mdfriday.com](https://mdfriday.com), where the search queries are. This note is only the story of finding the bug.

When the live help center is republished, I will put the before-and-after here: the sitemap address, and whether Search Console says it was read.

## Related

- [[about|About Me]]
- [help.mdfriday.com](https://help.mdfriday.com)
- [MDFriday](https://mdfriday.com)
