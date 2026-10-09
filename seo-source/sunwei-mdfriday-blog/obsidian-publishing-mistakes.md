---
title: "Obsidian Publishing Mistakes: 7 Ways Sites Break Later"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - publishing
  - checklist
description: "7 Obsidian publishing mistakes that break sites months later: renamed notes, missing images, storage surprises, leaky links, and a setup you can't maintain."
---

# Obsidian Publishing Mistakes: 7 Ways Sites Break Later

Most publishing problems don't show up on launch day. They show up three months later, when a link someone bookmarked returns a 404, an image is missing, or an update breaks a site you customised for hours.

I went through hundreds of forum threads, Reddit posts and YouTube comments from people publishing Obsidian notes. The same seven mistakes kept appearing. None of them are about a specific tool, so this list is useful whatever you use.

## Mistake 1: Publishing more of your vault than you meant to

It starts with "I'll just publish everything, it's mostly fine." Then a journal entry, a client name or a half-finished rant turns up in search results.

**Avoid it:** publish from one clearly bounded folder, and check links and embeds that point outside it. I wrote a full checklist in [[mdfriday/blog/publish-part-of-obsidian-vault|Publish Part of Your Obsidian Vault]].

## Mistake 2: Renaming notes after people have the link

In Obsidian, renaming is free: links update automatically. On the web, a renamed page usually means a new URL, and the old one breaks.

> “I’d like to be able to reorganize the content on my site without resulting in lots of 404 errors.” — [Obsidian forum, 2023](https://forum.obsidian.md/t/allow-for-custom-redirects/61766)

Tool upgrades can do it too. One Quartz upgrade broke previously published URLs that contained uppercase letters ([[mdfriday/voice-of-custom/stable-links-and-redirects|stable links]]).

**Avoid it:** settle on names before you share widely, and use short, lowercase, stable note names for anything important. When you must rename, update the links you control and accept that some old links will break. Don't count on redirects unless your tool clearly supports them.

## Mistake 3: Forgetting that attachments are content too

Text is tiny. Images, PDFs and audio are not. People discover storage limits the hard way, even on generous plans:

> “Obsidian Publish storage limits forces us to be mindful of image usage.” — [Obsidian forum, 2025](https://forum.obsidian.md/t/publish-compress-images-on-server/99986)

**Avoid it:** check the size of the folder you plan to publish before choosing a plan. Compress large images before they go into your vault. Host huge files such as long audio somewhere built for them, and link out ([[mdfriday/voice-of-custom/media-and-storage-limits|storage limits]]).

## Mistake 4: Assuming new images get published with the note

With some tools, attachments are published separately from the notes that use them:

> “if I add a photo to a published note, I need to remember to separately publish that new photo” — [Obsidian forum, 2024](https://forum.obsidian.md/t/publish-attached-files-with-note/79121)

**Avoid it:** after every update, open the changed pages on the live site and look for broken images. It takes a minute and catches the most embarrassing bug.

## Mistake 5: Testing with your easiest note

Everything renders a plain paragraph. The problems are in Dataview queries, Canvas, long equations, custom callouts and embeds.

**Avoid it:** build a "fidelity test" note with one of every element you use, and publish it with each tool you're considering. The steps are in [[mdfriday/blog/obsidian-notes-broken-after-publishing|Obsidian Notes Broken After Publishing?]].

## Mistake 6: Building on a setup you can't maintain

A heavily customised pipeline feels great on launch day. Then a dependency updates, a plugin goes quiet, or a theme repository disappears:

> “hours of customization at risk” — [Obsidian forum, 2026](https://forum.obsidian.md/t/mado-11-repository-is-gone/117600)

**Avoid it:** be honest about your appetite for maintenance ([[mdfriday/voice-of-custom/maintenance-burden|maintenance burden]]). If you don't enjoy debugging builds, choose a setup with fewer moving parts, even if it's less customisable.

## Mistake 7: Treating the host as your backup

Hosting services have outages, change their terms and sometimes shut down. And some free tiers are temporary by design. If your site lives only on a host, you're one policy change away from losing it.

**Avoid it:** keep your vault as the single source of truth, with its own backup, and make sure you can regenerate the site from it at any time. Read the retention rules of any free plan before you share links.

## Where MDFriday helps, and where it doesn't

I build MDFriday Publish, so here's an honest mapping against these seven:

- **Mistake 1 (publishing too much):** helps. Selective publish means you right-click only the note or folder you want public.
- **Mistake 6 (fragile setups):** helps. There's no Git, GitHub, terminal, tokens or pipeline to maintain. The build runs on your computer and the site is served from Cloudflare's CDN.
- **Mistake 7 (host as backup):** helps with the principle. Your vault stays on your machine and only the chosen notes are uploaded, so you can always publish again from your notes. But be clear on plans: **Guest content is cleared at the next UTC midnight, and Free content is cleared on the 1st of each month.** Only Personal (about \$5–6/month) is permanent.
- **Mistake 5 (easy-note testing):** it gives you a free, no-account way to run the test. AS mode renders pages to look like your Obsidian notes, but I don't claim Dataview, Canvas or Excalidraw support. Test them.
- **Mistake 3 (storage):** be careful. Personal includes 1 GB, less than some alternatives. Check your folder size.
- **Mistakes 2 and 4:** I'm not claiming anything special here. Follow the habits above.

## Try it on a small folder

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Right-click a small folder (say, five notes with images) and publish it in Guest mode. No account needed.
3. Walk through mistakes 1, 4 and 5 on the live site.

It's free to try, and your notes stay in your vault. Just remember the Guest site disappears at the next UTC midnight.

## Further reading

- [[mdfriday/blog/free-obsidian-publish-alternative|Free Obsidian Publish Alternative? What Free Really Costs]]
- [[mdfriday/blog/update-published-obsidian-notes|Update Published Obsidian Notes Without Copy-Paste]]
- [[mdfriday/blog/obsidian-seo-published-notes|Obsidian SEO: How to Get Your Published Notes Found]]
- Research notes: [[mdfriday/voice-of-custom/stable-links-and-redirects|Stable links]] · [[mdfriday/voice-of-custom/media-and-storage-limits|Media & storage limits]] · [[mdfriday/voice-of-custom/vendor-trust-and-reliability|Vendor trust]]
