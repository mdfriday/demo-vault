---
title: Chinese Community Voices
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Chinese users rank their pains differently from English communities: besides network access, Chinese paths and payment/renewal, there's cross-posting, image hosting, ICP filing numbers and Feishu sharing."
---

# Chinese Community Voices

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Judging from the Chinese posts collected this round (a qualitative judgment, not a count), **Chinese users rank their pains quite differently from English communities**. Besides the shared [[setup-and-deploy-barrier|setup barrier]] and [[pricing-and-lock-in|pricing]], the top pains are [[mainland-china-access|network reachability]], [[chinese-filenames|Chinese path / title compatibility]] and [[payment-and-renewal|payment and renewal]]. There are also 4 pains specific to the Chinese community:

1. **Cross-posting to domestic platforms**: for Chinese writers, "publishing" often doesn't mean building a website; it means posting to WeChat Official Accounts, Xiaohongshu, Zhihu or Juejin. Copy-paste breaks the formatting, loses images, and Obsidian syntax such as block references doesn't carry over. Several plugins have already appeared in the community just to solve this.
2. **Dependence on image hosts and broken image links**: people routinely use PicGo plus an image host (GitHub / jsDelivr / SM.MS and so on). Then the host shuts down or the CDN gets blocked, and images in notes and websites break in bulk.
3. **ICP filing and the filing number in the footer**: stable access inside mainland China requires an ICP filing, and once filed, the footer must show the filing number, but the hosting platform's footer can't be edited.
4. **Using Feishu and other domestic cloud docs instead of "share / publish"**: because the official Publish is expensive, Digital Garden is fiddly to configure and the domestic network is unstable, one developer syncs Obsidian notes into Feishu cloud docs for sharing and says it already has thousands of users; enterprise users also want company accounts to control who can view.

> [!info] Signal (approximate)
> Cross-posting ~6 sources · image hosting ~4 · ICP filing ~4 · Feishu / cloud-doc sharing ~3 (some sources overlap with [[mainland-china-access|Mainland China Access]] and other articles).
> Almost all sources are from the Obsidian Chinese forum and V2EX, so **they say little about non-technical Chinese users**.
> Also, about 63% of the existing customer list uses Chinese email domains (only the domain distribution was counted; no personal information is involved), while the 15 main clusters above come almost entirely from English communities. That in itself is a data gap.

## Voices

- 「搞个网站还没有个傻瓜版吗？」 — Obsidian Chinese forum · 2025-02-25 · <https://forum-zh.obsidian.md/t/topic/46945>
  - *Translation:* Is there still no foolproof way to make a website?
- 「一篇文章写了两小时。发出去，又是两小时。」 — Obsidian Chinese forum · 2026-07-30 · <https://forum-zh.obsidian.md/t/topic/62798>
  - *Translation:* Two hours to write an article. Another two hours to publish it.
- 「目前通过obsidian编写的文章想直接转到微信公众号这类平台发现比较麻烦」 — Obsidian Chinese forum · 2022-01-30 · <https://forum-zh.obsidian.md/t/topic/4148>
  - *Translation:* Right now, moving articles written in Obsidian straight onto platforms like WeChat Official Accounts turns out to be quite a hassle.
- 「我的文章使用了块引用，无法直接复制完整的 md」 — Obsidian Chinese forum · 2023-04-17 · <https://forum-zh.obsidian.md/t/topic/18354>
  - *Translation:* My articles use block references, so I can't directly copy the complete md.
- 「去SM.MS原网站，一看，哦豁，SM.MS没了」 — Obsidian Chinese forum · 2026-03-28 · <https://forum-zh.obsidian.md/t/topic/60004>
  - *Translation:* I went to the original SM.MS site, took a look, and, whoops, SM.MS is gone.
- 「图床的域名或者自定义域名未开启科学网络情况无法访问」 — Obsidian Chinese forum · 2025-06-15 · <https://forum-zh.obsidian.md/t/topic/51358>
  - *Translation:* Without a VPN ("scientific internet"), the image host's domain or a custom domain can't be reached.
- 「希望将发布的网站展示在 www 域名上，但是被要求必须展示备案号。」 — Obsidian Chinese forum · 2024-01-17 · <https://forum-zh.obsidian.md/t/topic/28980>
  - *Translation:* I want to show the published site on a www domain, but I'm required to display the ICP filing number.
- 「我想将网页发布，但是需要看的人登录微软公司账户密码才可以查看。」 — Obsidian Chinese forum · 2025-02-09 · <https://forum-zh.obsidian.md/t/topic/46179>
  - *Translation:* I want to publish a web page, but viewers should have to sign in with their Microsoft company account and password to see it.

> [!note] About the sources
> The second quote comes from a post in which a plugin author introduces their own plugin, so it describes a pain the author observed.

## Why it hurts

- **The Chinese content ecosystem is platform-centered.** Readers are on WeChat Official Accounts, Xiaohongshu and Zhihu, not on personal websites. A website can hardly be the only outlet.
- **The infrastructure is unstable.** Image hosts, CDNs and overseas hosting can stop working at any time, so users are forced to worry about whether their pages even open.
- **Compliance is a real cost.** ICP filing, the footer notice and real-name registration are all things English communities never have to think about.

## How people cope today

- WeChat Official Account formatting plugins (NoteToMP, Obs2Publisher, copy-to-mp and others).
- PicGo plus assorted image hosts, then bulk-replacing links when one fails.
- Feishu / cloud-doc sharing (for example Obshare): fast inside China, with mature permission management.
- Injecting the ICP filing number into the footer with JS.

## MDFriday's response

- **Local build, no GitHub / Vercel needed** (confirmed), which is worth even more in the Chinese context.
- **AS mode + multiple themes + a real website**: compared with "sync to Feishu", MDFriday's difference is fidelity, themes, a complete website and SEO.
- **Local images are published together with the site**, so in principle MDFriday could claim "no image host needed", but how attachments are bundled and how well sites load inside mainland China are both **(unconfirmed)** (see [[media-and-storage-limits|Media & Storage Limits]]).
- Custom footer / ICP filing number (**unconfirmed**; very low cost, very specific need); export in WeChat Official Account format **(unconfirmed)**; company-account login **(unconfirmed)**.
- Chinese-language marketing can make this clear: the website is your master copy, and on WeChat Official Accounts or Xiaohongshu you post a link or republish it.

## Open questions

- In the next research round, add Zhihu, Xiaohongshu, Bilibili comments and Sspai to see whether non-technical Chinese users rank their pains the same way.
- Interview a few existing Chinese customers directly: what do you publish with MDFriday? Where are your readers? How fast does it load inside China?
- Is "website + WeChat Official Account" the real workflow in the Chinese market?

## Related

- [[mainland-china-access|Mainland China Access]]
- [[chinese-filenames|Chinese Filenames]]
- [[payment-and-renewal|Payment & Renewal]]
- [[single-note-sharing|Single-note Sharing]]
- [[media-and-storage-limits|Media & Storage Limits]]
- [[sync-and-update-workflow|Sync & Update Workflow]]
