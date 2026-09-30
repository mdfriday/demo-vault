---
title: Analytics & Privacy Compliance
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "After publishing, people want to know whether anyone is reading, without being forced onto Google; EU site owners also carry compliance responsibility for cookies and tracking embeds (GDPR)."
---

# Analytics & Privacy Compliance

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

After publishing, users want to know whether anyone is reading. But Publish only integrates with Google Analytics: privacy-minded users want options like Matomo or Cloudflare Web Analytics, and Chinese users need Baidu Tongji / 51.la. The other side is compliance: EU site owners are legally responsible for how visitors are tracked, yet the hosting platform offers no cookie banner and no "load on click" option for YouTube / Twitter embeds, so users have to write their own scripts.

> [!info] Signal (approximate)
> ~7 web supplement sources (4 on analytics, 3 on GDPR / cookies); latest evidence 2026-09.
> Relevance to MDFriday: **medium**, a low-cost differentiator; GDPR mainly matters to EU users.

## Voices

- “But I really don’t like being forced to use a Google service to get such a basic feature working.” — Obsidian Forum · 2026-09-17 · <https://forum.obsidian.md/t/google-analytics-tracking-alternative-for-publish/118339>
- “Is this still not available (besides invasive Google Analytics, naturally)?” — Obsidian Forum · 2024-07-04 · <https://forum.obsidian.md/t/publish-site-visit-count/10576>
- “want to see if the analytics work with Cloudflare” — Reddit r/ObsidianMD · 2025-07-08 · <https://www.reddit.com/r/ObsidianMD/comments/1luyoy2/>
- 「增加统计代码，需要自己去51.la或百度统计等申请」 — Obsidian Chinese forum · 2024-04-20 · <https://forum-zh.obsidian.md/t/topic/33406>
  - *Translation:* To add analytics code, you have to sign up yourself with 51.la, Baidu Tongji or similar.
- “So I guess I would have to add some kind of pop up asking for permission? If so, how can I do that in Publish?” — Obsidian Forum · 2024-08-17 · <https://forum.obsidian.md/t/google-analytics-gdpr-pop-up/87012>
- “This should be something that non-technical people would be able to set up.” — Obsidian Forum · 2024-08-17 · <https://forum.obsidian.md/t/cookie-banner-management-in-obsidian-publish/87018>
- “it puts publish users at risk of getting sued” — Obsidian Forum · 2024-12-03 · <https://forum.obsidian.md/t/publish-embed-privacy-aka-two-click-eu-gdpr/92682>

## Why it hurts

- **Without feedback, it's hard to keep writing.** Visitor data is the most basic feedback loop for a knowledge creator.
- **Being forced to use tracking tools goes against why many people start a digital garden.**
- **Compliance responsibility lands on non-technical users.** They don't understand cookie law but carry the risk of being sued.

## How people cope today

- Injecting analytics scripts and cookie banners themselves with publish.js.
- Opening issues / PRs on Quartz asking for Matomo, Cloudflare Web Analytics, PostHog and others (the web supplement only looked at titles and didn't quote them one by one).
- Not installing analytics at all.

## MDFriday's response

- Sites are hosted on the **Cloudflare CDN**, so in principle basic cookie-free analytics is possible, but whether built-in analytics (for example Cloudflare Web Analytics) is offered is **(unconfirmed)**.
- Allowing custom head scripts, making it easy to add Baidu Tongji, 51.la or Umami: **(unconfirmed)**.
- If analytics were cookie-free, MDFriday could say "no cookie banner needed"; "load on click" for embeds: **(unconfirmed)**.

## Open questions

- What share of early users are in the EU? That decides the priority of GDPR-related features.
- Do users want a simple "is anyone reading" number, or a full analytics tool?
- Should analytics be planned together with [[blogging-features|Blogging Features]]?

## Related

- [[seo-discoverability-and-ai-crawlers|SEO, Discoverability & AI Crawlers]]
- [[blogging-features|Blogging Features]]
- [[mainland-china-access|Mainland China Access]]
