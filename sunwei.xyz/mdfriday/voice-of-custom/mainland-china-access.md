---
title: Mainland China Access
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "GitHub Pages, Vercel and Cloudflare Pages either don't open in mainland China or are slow and unstable, while domestic hosting requires ICP filing. The strongest new signal from the web supplement."
---

# Mainland China Access

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

The free hosting Chinese users rely on most is either blocked in mainland China (vercel.app, some custom domains) or slow and unstable (GitHub Pages, Cloudflare Pages, especially in the evening), while domestic hosting requires an ICP filing. Unstable GitHub access also drags down Git-based publishing workflows. Note that opinions of Cloudflare on V2EX are **mixed**: some say it works and is reasonably fast, others measured it as clearly slower than domestic services. The conclusion: it's reachable, but speed and stability vary by region, carrier and time of day.

> [!info] Signal (approximate)
> ~16 web supplement sources (10 quoted, 6 corroborating); latest evidence 2026-09.
> **The strongest new signal in the web supplement**; relevance to MDFriday: **highest** (about 63% of existing customers use Chinese email domains).

## Voices

- 「就是国庆直接被墙干没了 临时搬到 cloudflare pages ，访问速度又过于感人」 — V2EX · 2023-10-02 · <https://www.v2ex.com/t/978574>
  - *Translation:* Over the National Day holiday it simply got wiped out by the firewall. I moved to Cloudflare Pages temporarily, and the access speed is, once again, painfully slow.
- 「我博客部署在 vercel ，白天还好，晚上经常打不开（浙江）」 — V2EX · 2025-02-21 · <https://www.v2ex.com/t/1113197>
  - *Translation:* My blog is deployed on Vercel. It's fine during the day, but at night it often won't open (Zhejiang).
- 「GitHub Pages 测出来是 100 ms ，Cloudflare Pages 是 180ms ，腾讯云 EdgeOne Pages 是 5 ms 。」 — V2EX · 2025-02-21 · <https://www.v2ex.com/t/1113197>
  - *Translation:* GitHub Pages measured 100 ms, Cloudflare Pages 180 ms, Tencent Cloud EdgeOne Pages 5 ms.
- 「用 GitHub pages 国内访问速度不行，百度也没啥收录。」 — V2EX · 2023-08-14 · <https://www.v2ex.com/t/965071>
  - *Translation:* With GitHub Pages, access speed inside China is poor, and Baidu barely indexes it either.
- 「国外一些免费的平台，如netlify、vercel、cloudflare page，在国内的访问速度都比较感人」 — Obsidian Chinese forum · 2022-09-26 · <https://forum-zh.obsidian.md/t/topic/10331>
  - *Translation:* Some free overseas platforms, like Netlify, Vercel and Cloudflare Pages, are all painfully slow to access from inside China.
- 「官方默认的网站部署网站部署服务是 Vercel，在国内网络环境下打不开，想正常使用还得绑定域名，又更麻烦了。」 — Obsidian Chinese forum · 2023-05-12 · <https://forum-zh.obsidian.md/t/topic/19256>
  - *Translation:* The official default site deployment service is Vercel, which won't open on networks inside China; to use it normally you also have to bind a domain, which is even more hassle.
- 「近期国内IP访问GitHub不稳定。」 — Obsidian Chinese forum · 2025-05-02 · <https://forum-zh.obsidian.md/t/topic/49911>
  - *Translation:* Recently, access to GitHub from IPs inside China has been unstable.

## Why it hurts

- **If the site won't open, nothing else matters.** For sites whose readers are mainly in China, reachability is the first priority.
- **The problem is intermittent and hard to reproduce.** It opens during the day but not at night, it's fast in one region and slow in another, so site owners struggle to diagnose or explain it.
- **ICP filing is another barrier.** Stability requires filing, and filing means a whole process around the domain, the provider and the footer notice (see [[chinese-community-voices|Chinese Community Voices]]).

## How people cope today

- Moving back and forth between GitHub Pages, Vercel, Cloudflare Pages and Netlify.
- Switching to domestic services such as Tencent Cloud EdgeOne Pages or Alibaba Cloud OSS / Tencent Cloud COS, while going through ICP filing.
- Binding a custom domain to Vercel to get around the vercel.app problem.

## MDFriday's response

- **Confirmed**: MDFriday builds locally, doesn't go through GitHub and doesn't need Vercel. The unstable-GitHub link is removed entirely. In the Chinese context, "no GitHub / Vercel needed" is worth even more than in English.
- **MDFriday sites are hosted on the Cloudflare CDN.** Given the mixed opinions above, actual access across regions and carriers in mainland China is **(unconfirmed)**. It needs real testing, and MDFriday must not promise "it opens in China too".
- Serving ICP-filed domains through a domestic CDN, exporting to domestic object storage: **(unconfirmed)**.

## Open questions

- Run an access test right away across several mainland regions and carriers (China Telecom / China Unicom / China Mobile), daytime and evening, and put the results in the FAQ.
- What do existing Chinese customers actually say about access speed? Ask them directly.
- If the results are poor, should MDFriday offer a domestic route or an export option? That would affect pricing and positioning in the Chinese market.

## Related

- [[chinese-community-voices|Chinese Community Voices]]
- [[chinese-filenames|Chinese Filenames]]
- [[payment-and-renewal|Payment & Renewal]]
- [[setup-and-deploy-barrier|Setup & Deploy Barrier]]
- [[custom-domains|Custom Domains]]
