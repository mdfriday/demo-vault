---
title: SEO, Discoverability & AI Crawlers
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "People who want to be found hit SPA crawling, sitemap, orphan-page and slow-loading problems; meanwhile two new demands have appeared: block AI crawlers, or make the site easier for LLMs to read."
---

# SEO, Discoverability & AI Crawlers

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

People who want to be found (bloggers, academic sites, community knowledge bases) run into a string of problems: Publish is a JavaScript single-page app, so crawlers and the Wayback Machine only see an empty shell, and if JS fails to load the page shows no text at all; a malformed sitemap stops Search Console from fetching it; duplicate canonicals, and pages flagged as orphans by SEO tools; no custom meta / OG / Schema. On performance: large sites take 5–10 seconds to load, up to 30 seconds on phones, with very low PageSpeed scores. Since 2024 there's a new dimension: some people want to **block** AI training crawlers (custom robots.txt, GPTBot, Google-Extended), others want their site to be **easier for LLMs to read** (llms.txt, Markdown versions), and the hosting platform offers neither.

> [!info] Signal (approximate)
> ~38 VOC cards (29 SEO ∪ 12 performance / reliability) · ~5 YouTube comments · ~6 web supplement sources (4 of them on AI crawlers / llms.txt).
> Ranked **#8**: a serious weakness for bloggers, academic and large sites; AI crawlers are a new 2025–2026 signal.

## Voices

- “so Google Search Console reports Could not fetch” — Obsidian Forum · 2026-08-01 · <https://forum.obsidian.md/t/publish-sites-auto-generated-sitemap-xml-is-missing-the-required-xmlns-http-www-sitemaps-org-schemas-sitemap-0-9-attribute/116766>
- “ahrefs audit says that all my pages are orphan pages” — Obsidian Forum · 2025-01-10 · <https://forum.obsidian.md/t/how-site-published-with-obsidian-reacts-to-ahrefs-audit/94625>
- “my publish site is impossible to find in a web search, why?” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=6h42ysmwJzM>
- “pages on mobile that take up to 30 seconds (!)” — Obsidian Forum · 2023-06-09 · <https://forum.obsidian.md/t/publish-performance-issues/61294>
- “if JavaScript fails to load for a visitor due to spotty signal or whatever, it will display no text” — Obsidian Forum · 2025-11-25 · <https://forum.obsidian.md/t/the-viability-of-using-obsidian-as-a-publication-platform/108341>
- “No known workaround exists other than blocking all web crawlers or putting everything behind a password.” — Obsidian Forum · 2024-01-10 · <https://forum.obsidian.md/t/disallow-llm-ai-ml-scraping-using-google-extended-on-obsidian-publish/74696>
- “Today websites are not just used to provide information to people, but they are also used to provide information to large language models.” — Obsidian Forum · 2024-09-02 · <https://forum.obsidian.md/t/provide-llm-friendly-content-by-adding-a-llms-txt-file-to-help-llms-use-an-obsidian-website/87818>
- “I see LLMs mostly as competition at best, thieves of my researched content at worst.” — Hacker News · 2025-05-08 · <https://news.ycombinator.com/item?id=43925341>

## Why it hurts

- **The point of publishing is to be seen.** For bloggers and knowledge creators, a site nobody can find is almost the same as not publishing.
- **Users can't change the SEO details.** The hosting platform controls the HTML structure, sitemap and meta; users can only post for help and wait.
- **In the AI era, control over content is a new anxiety.** Some worry their research will be "stolen" for training; others want to be cited by AI. Both need a switch that lets them decide.

## How people cope today

- Moving from Publish to purely static options like Hugo / Astro to gain SEO control.
- Patching Publish with publish.js.
- Blocking AI crawlers: according to forum feedback, on Publish there's no way other than blocking all crawlers or password-protecting the whole site.

## MDFriday's response

- **Local build → static website → Cloudflare CDN**: static HTML is naturally crawler-friendly, and CDN delivery helps speed.
- Specific support for sitemap, robots.txt, canonical and OG / custom meta: **(unconfirmed)**.
- A "block AI training crawlers" switch, generating llms.txt / Markdown versions: **(unconfirmed)**. Because the output is fully determined by the local build, switches like these would be cheap to build and could be a differentiator for 2025–2026.
- For Chinese users, whether sites get indexed by Baidu and how fast they open inside China: see [[mainland-china-access|Mainland China Access]].

## Open questions

- How do sites published with MDFriday (for example sunwei.xyz itself) actually perform in Search Console / PageSpeed? A public test could show it.
- Do more users want to block AI crawlers or welcome them? Ask directly on Reddit.
- Is a custom description / OG image per page offered (unconfirmed)?

## Related

- [[blogging-features|Blogging Features]]
- [[analytics-and-privacy-compliance|Analytics & Privacy Compliance]]
- [[large-vault-builds|Large Vault Builds]]
- [[stable-links-and-redirects|Stable Links & Redirects]]
- [[accessibility-and-languages|Accessibility & Languages]]
