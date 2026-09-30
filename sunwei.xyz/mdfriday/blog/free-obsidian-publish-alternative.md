---
title: "Free Obsidian Publish Alternative? What Free Really Costs"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - obsidian-publish
  - pricing
description: "Looking for a free Obsidian Publish alternative? Here's what free really costs in setup, upkeep and permanence, and when a few dollars a month is smarter."
---

# Free Obsidian Publish Alternative? What Free Really Costs

"Free Obsidian Publish alternative" shows up constantly in forum threads and YouTube titles, and I understand why. A personal garden with a few hundred visitors a month doesn't earn anything, so a subscription is hard to justify.

> “The full annual price is \$192. I think that’s quite expensive.” — [Medium, 2022](https://medium.com/effie-write-mindmap-note/why-im-no-longer-using-obsidian-publish-5234f35f089e)

(Prices have changed since then. Publish is roughly \$8–10 per site per month today, depending on billing.)

But "free" is rarely free. It moves the cost somewhere else. Here's where it goes, so you can pick the kind of cost you're happy to pay. And yes, I sell a paid plan, so I'll be upfront about mine too.

## Cost 1: Setup time

Every popular free option (Quartz, the Digital Garden plugin, Hugo, Jekyll) is free in dollars and paid in hours. You create a GitHub repository, install Node, configure a host and debug the first failed build. Tutorials that look like 20 minutes regularly turn into an evening, or into giving up:

> “it's been so painful to get to that result, I think I'll just drop it now” — [YouTube comment, ~2024](https://www.youtube.com/watch?v=6s6DT1yN4dw)

If you enjoy that kind of tinkering, this cost is close to zero, maybe even fun. If you don't, it's the most expensive part of "free". I wrote about skipping it in [[mdfriday/blog/publish-obsidian-notes-without-github|Publish Obsidian Notes Without GitHub]].

## Cost 2: Maintenance, forever

This is the cost nobody puts in the tutorial. Free tools are maintained by volunteers, and life happens:

> “I noticed that obsidian-hugo is now archived and read only.” — [YouTube comment, ~2024](https://www.youtube.com/watch?v=ITiiuBNVue0)

In the threads I studied ([[mdfriday/voice-of-custom/maintenance-burden|maintenance burden]]), people describe plugins going quiet, theme repositories disappearing, tutorials going stale within months, and upgrades causing merge conflicts. None of this is a criticism of open source. Those projects are generous gifts. It's just that a website is a long-term asset, and a free pipeline means you are its long-term maintainer.

## Cost 3: Permanence and trust

Free hosting tiers change their rules. Services shut down. And some "free" plans are free because they're temporary.

This applies to MDFriday too, so let me say it clearly:

- **Guest** (no account): 1 site, 5 MB. **Content is cleared at the next UTC midnight.** It exists so you can see your notes online in a couple of minutes.
- **Free** (with an account): 3 sites, 50 MB. **Content is cleared on the 1st of each month.** Good for experiments, not for a site you'll link from your CV.
- **Personal:** about \$5–6 a month, 1 GB, and your site is **kept permanently**.

I'd rather you know that now than discover a missing site next month. Trust is harder for a small vendor to earn ([[mdfriday/voice-of-custom/vendor-trust-and-reliability|vendor trust]]), and hiding the fine print is the fastest way to lose it.

## Cost 4: Lock-in, the hidden one

Some people choose free tools less for the price and more for ownership:

> “i’d love to generate files locally so i can upload where i want” — [Obsidian forum, 2025](https://forum.obsidian.md/t/option-for-publish-to-create-files-locally-or-another-destination/98842)

Whatever you choose, ask one question: if this service disappeared tomorrow, what would I still have? With any tool that reads your vault directly, the honest answer should be "all my notes, untouched". Be wary of anything that asks you to move your writing into its own editor or database.

## So when is paying smarter than free?

A rough rule of thumb:

- **Go free (Quartz, Hugo, Digital Garden)** if you're comfortable with Git, enjoy customising, and see the site as a hobby project in itself.
- **Pay for Obsidian Publish** if you want the official product, need the 4 GB of storage, and value a big, established vendor.
- **Pay a little for something in between** if you want no Git and no maintenance, but Publish's price or model doesn't fit.

That third group is who I built MDFriday Publish for.

## What MDFriday costs you, in money and time

**Money:** nothing to try. Personal is about \$5–6 a month. That's cheaper than Publish, but let's be fair: it's 1 GB against Publish's 4 GB. If your site is mostly photos or audio, check your vault size first ([[mdfriday/voice-of-custom/media-and-storage-limits|storage limits]]).

**Time:** close to none at setup. You install a plugin, right-click a note or folder, and publish. No GitHub, no Git, no terminal and no tokens.

**Maintenance:** there's no repo or pipeline for you to keep alive. The build runs on your computer and the site is served from Cloudflare's CDN.

**Ownership:** your vault stays on your machine, and only the notes you choose are uploaded. Your writing stays as ordinary notes in your Obsidian vault. The site is built from them, not the other way round.

**What you give up:** plugin-heavy features. I don't claim support for Dataview, Canvas or Excalidraw, so test those notes first. And you're trusting a small, founder-run product. I'd rather earn that than ask for it.

## Try it for free (and know exactly what free means)

Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>

Right-click one note and publish it in Guest mode. No account, no card. Remember that it's cleared at the next UTC midnight, so do it when you have five minutes to actually look at the result. If you like it, the Free plan gives you room to experiment (cleared monthly). When you want it to stay up, Personal keeps it permanently.

## Further reading

- [[mdfriday/blog/is-obsidian-publish-worth-it|Is Obsidian Publish Worth It? An Honest Look]]
- [[mdfriday/blog/obsidian-publish-alternatives|Obsidian Publish Alternatives: 6 Honest Options Compared]]
- [[mdfriday/blog/obsidian-publishing-mistakes|Obsidian Publishing Mistakes: 7 Ways Sites Break Later]]
- Research notes: [[mdfriday/voice-of-custom/pricing-and-lock-in|Pricing & lock-in]] · [[mdfriday/voice-of-custom/maintenance-burden|Maintenance burden]] · [[mdfriday/voice-of-custom/vendor-trust-and-reliability|Vendor trust]]
