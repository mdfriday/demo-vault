---
title: Pricing & Lock-in
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Many users call Obsidian Publish too expensive; the other half of the demand is ownership: generate files locally and host them anywhere."
---

# Pricing & Lock-in

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Many users call the official Obsidian Publish (roughly \$8–10 per site per month, often quoted as \$16–20 per month in earlier years) "too expensive, not worth it", and students are especially price-sensitive. The more specific complaint is stacked charges: Sync and Publish are billed separately, and every collaborator pays too. The other half of the demand is **ownership**: people don't want their files on someone else's server; they want to generate files locally and push them to S3, WebDAV, Synology or their own server; they worry about platform lock-in and their data staying behind after they cancel. This is the main reason people look for alternatives, and it often appears alongside the [[setup-and-deploy-barrier|setup barrier]]: either spend money or spend time.

> [!info] Signal (approximate)
> ~67 VOC cards (46 on price ∪ 26 on lock-in / ownership) · ~19 YouTube comments (10 on price, 9 on self-hosting / local hosting) · 2 web supplement sources.
> Ranked **#3**: long-standing, and the main motivation for migrating.

## Voices

- “The full annual price is \$192. I think that’s quite expensive.” — Medium · 2022-10-09 · <https://medium.com/effie-write-mindmap-note/why-im-no-longer-using-obsidian-publish-5234f35f089e>
- “16\$/ monthly for this features is way too much.” — YouTube comment · ~2021 · <https://www.youtube.com/watch?v=1pf6aj3Uwuk>
- “I’m not sure I’ll use it enough to pay \$20/mo” — YouTube comment · ~2023 · <https://www.youtube.com/watch?v=ITiiuBNVue0>
- “People don’t like being nickled-and-dimed.” — Obsidian Forum · 2025-02-12 · <https://forum.obsidian.md/t/your-pricing-model-needs-work/96575>
- “i’d love to generate files locally so i can upload where i want” — Obsidian Forum · 2025-03-27 · <https://forum.obsidian.md/t/option-for-publish-to-create-files-locally-or-another-destination/98842>
- “Would be cool if it can push to your own s3 or WebDAV receiver” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=-5RO4Xsw9Ec>
- “I don't want my files to be on the Obsidian servers” — Reddit r/ObsidianMD · 2026-06-29 · <https://www.reddit.com/r/ObsidianMD/comments/1uitj6j/publish_single_obsidian_notes_to_your_site>
- 「官方的publish有点小贵，digital garden之类的同步插件配置非常麻烦」 — Obsidian Chinese forum · 2025-09-12 · <https://forum-zh.obsidian.md/t/topic/53870>
  - *Translation:* The official Publish is a bit pricey, and sync plugins like Digital Garden are a real pain to configure.

## Why it hurts

- **The value doesn't feel right.** Many sites are personal gardens with little traffic and no income, so a monthly fee is hard to justify.
- **A subscription is a long-term commitment.** Some say outright they aren't sure they'll use it enough, and monthly billing amplifies that hesitation.
- **Ownership anxiety.** Notes are assets built up over years; users want "the files are in my hands, and I decide where they go".

## How people cope today

- Switching to "free alternatives" such as Quartz or Digital Garden, then running into the [[setup-and-deploy-barrier|setup barrier]] and the [[maintenance-burden|maintenance burden]].
- Looking for one-time-purchase tools (a one-time price is one of Verdant's selling points).
- Writing their own scripts to export HTML and push it to their own server.

## MDFriday's response

- **Pricing**: Personal about \$5–6/month, 1 GB, kept permanently; Free 3 sites, 50 MB; Guest no sign-up, 1 site, 5 MB.
- **Local build**: source notes always stay on your own computer; only the generated website is uploaded.
- **Risk to flag**: Free is cleared on the 1st of each month and Guest at the next UTC midnight, which can easily trigger "I'm afraid of losing my content" anxiety. The copy must make clear that these two are trial tiers and that Personal is the permanent one (see [[vendor-trust-and-reliability|Vendor Trust & Reliability]]).
- **Be careful comparing storage**: users already complain that Publish's 4 GB isn't enough, while Personal is 1 GB; see [[media-and-storage-limits|Media & Storage Limits]].
- Exporting static files and pushing them to your own S3 / server (unconfirmed); paid extra storage (unconfirmed).

## Open questions

- Should "cheaper than Publish" be reframed as "pay for what you need, no stacked subscriptions", so users don't just compare 1 GB with 4 GB?
- How many users really need "self-hosted export", versus just the reassurance that the platform won't disappear?
- Is a student / education discount worth offering?

## Related

- [[setup-and-deploy-barrier|Setup & Deploy Barrier]]
- [[media-and-storage-limits|Media & Storage Limits]]
- [[vendor-trust-and-reliability|Vendor Trust & Reliability]]
- [[payment-and-renewal|Payment & Renewal]]
- [[access-control-and-collaboration|Access Control & Collaboration]]
