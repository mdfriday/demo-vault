---
title: Voice of the Customer
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
  - index
description: "MDFriday user research: 25 customer pain-point themes distilled from 567 VOC cards, 592 YouTube comments and 117 web pages."
---

# Voice of the Customer

← [[mdfriday/index|MDFriday]]

> Don't ask "What should I build next?"
> First ask "What are people already struggling with?"

This is MDFriday's User Research section. It doesn't record feedback from MDFriday users; it records **the real voices of users across the whole "Obsidian → website" market**: what they complain about, what they want, and how they make do today on forums, Reddit, Hacker News and in YouTube comment sections.

It serves the North Star question:

> Why do people choose MDFriday instead of their current workflow?

## What this research is

| Source | Scale (approximate) | Notes |
| --- | --- | --- |
| VOC cards | 567 | 7 theme folders; time span 2019-02 → 2026-09; by platform: Obsidian Forum 205, Reddit 194, Hacker News 87, Dev.to 36, personal blogs 31, Medium 12, other 2 |
| YouTube comments | 592 | From 35 videos about Obsidian publishing / digital gardens (selected from 50 popular videos) |
| Web supplement research | 117 archived pages | Obsidian English forum, Obsidian Chinese forum, V2EX, competitors' GitHub Issues, Hacker News, Juejin summaries, etc.; the original report verified 92 quotes and 76 unique URLs |
| Existing customer list | — | Only the distribution of email domains was counted (about 63% are Chinese email domains); **no personal information is quoted** |

**Method**

1. VOC cards were read one by one and multi-labeled by hand with 20 pain tags, then grouped into 15 main clusters; YouTube comments were read one by one, counting only comments that clearly express a pain.
2. The web supplement research looked specifically for new pains not covered by the first 15 clusters, producing 12 new clusters and 4 kinds of pain specific to the Chinese community; signal strength is counted as the number of distinct sources.
3. Here the two sets of results are merged, deduplicated and organized into **25 themes**, one article per theme.
4. Every quote is kept in its original language and was compared word for word against its source file / archived page with a script (153 quotes in this set, all passed). Quotes originally in Chinese are followed by an English translation. Quotes contain no usernames.
5. Dates: the original research was completed on 2026-09-26; this set of articles was compiled on 2026-09-28.

**How to read each article**: What users are saying (what users say + signal strength) → Voices (verbatim quotes) → Why it hurts (root causes) → How people cope today (current workarounds) → MDFriday's response (how MDFriday responds) → Open questions (what to validate next).

> [!warning] About "(unconfirmed)"
> MDFriday's confirmed capabilities are only: right-click publishing of a note or folder, local build, Cloudflare CDN, AS mode, multiple themes, selective publish, and the three plans Guest / Free / Personal. Any capability in these articles beyond that list is marked **(unconfirmed)** and does not mean it's supported.

## Ranked themes

### Tier 1 · Main clusters (VOC cards + YouTube comments)

Signal = number of VOC cards / number of YouTube comments (hand-labeled; read as ±10%).

| # | Theme | Signal | In one line |
| ---: | --- | --- | --- |
| 1 | [[setup-and-deploy-barrier\|Setup & Deploy Barrier]] | ~150 / ~46 | Free options all assume Git, CLI and CI; this is where most people give up |
| 2 | [[rendering-fidelity\|Rendering Fidelity]] | ~89 / ~24 | Plugins, Dataview, Bases, Canvas and math break once published; the fastest-growing pain |
| 3 | [[pricing-and-lock-in\|Pricing & Lock-in]] | ~67 / ~19 | Publish is too expensive, and people want their files in their own hands |
| 4 | [[knowledge-structure-on-the-web\|Knowledge Structure on the Web]] | ~59 / ~16 | Wikilinks, backlinks, graph, sidebar, search: the site should feel "like my vault" |
| 5 | [[selective-publish-and-privacy\|Selective Publish & Privacy]] | ~52 / ~17 | Publish only part, avoid mistakes, prevent leaks; often called "the only blocker" |
| 6 | [[themes-and-customization\|Themes & Customization]] | ~52 / ~11 | People want it beautiful and personal, but have to write CSS and can't remove watermarks |
| 7 | [[sync-and-update-workflow\|Sync & Update Workflow]] | ~37 / ~10 | Two content sources drift apart, and you can't publish from a phone |
| 8 | [[seo-discoverability-and-ai-crawlers\|SEO, Discoverability & AI Crawlers]] | ~38 / ~5 (+6 web sources) | Can't be found, loads slowly; AI crawlers should be blockable and welcomable |
| 9 | [[choosing-a-publishing-tool\|Choosing a Publishing Tool]] | ~36 / ~5 | Too many options and contradictory tutorials, so people never start |
| 10 | [[custom-domains\|Custom Domains]] | ~25 / ~8 | A 5-minute job becomes an hours-long DNS nightmare |
| 11 | [[blogging-features\|Blogging Features]] | ~23 / ~9 | No comments, weak RSS, no recent posts, no monetization |
| 12 | [[maintenance-burden\|Maintenance Burden]] | ~18 / ~10 | Abandoned plugins, deleted repos, upgrade conflicts; fear of wasted effort |
| 13 | [[access-control-and-collaboration\|Access Control & Collaboration]] | ~20 / ~6 (+7 web sources) | Page-level passwords, members-only areas, team permissions; rare but high willingness to pay |
| 14 | [[export-beyond-the-web\|Export Beyond the Web]] | ~22 / 0 | PDF, EPUB, offline HTML; clearly growing over the past year |
| 15 | [[single-note-sharing\|Single-note Sharing]] | ~11 / ~9 | People just want to share one note, and the link mustn't expire |

### Tier 2 · New pains from the web supplement

Signal = number of distinct sources. **This number can't be compared directly with the card counts in Tier 1**, but several of these are highly relevant to MDFriday.

| # | Theme | Signal | Relevance to MDFriday | In one line |
| ---: | --- | --- | --- | --- |
| 16 | [[mainland-china-access\|Mainland China Access]] | ~16 | 🔴 Highest | GitHub Pages / Vercel / Cloudflare don't open or are unstable in mainland China |
| 17 | [[chinese-community-voices\|Chinese Community Voices]] | ~17 (4 sub-types, partly overlapping other themes) | 🔴 High | Cross-posting, image hosts, ICP filing numbers, Feishu sharing |
| 18 | [[media-and-storage-limits\|Media & Storage Limits]] | ~12 | 🔴 Very high | Users find 4 GB too little, while MDFriday Personal is 1 GB |
| 19 | [[analytics-and-privacy-compliance\|Analytics & Privacy Compliance]] | ~7 | 🟠 Medium | No wish to be forced onto Google; EU site owners must handle cookie compliance |
| 20 | [[vendor-trust-and-reliability\|Vendor Trust & Reliability]] | ~6 | 🔴 High | No status page, fear the vendor vanishes; Guest / Free get cleared |
| 21 | [[chinese-filenames\|Chinese Filenames]] | ~6 | 🔴 High | Chinese paths cause broken links and failed deploys |
| 22 | [[large-vault-builds\|Large Vault Builds]] | ~5 | 🟠 Medium | With thousands of notes, builds slow down exponentially or fail |
| 23 | [[stable-links-and-redirects\|Stable Links & Redirects]] | ~5 | 🟠 Medium | Tidying notes creates a pile of 404s |
| 24 | [[payment-and-renewal\|Payment & Renewal]] | ~4 | 🟠 Medium | Can't find a WeChat renewal option, don't want to save a card |
| 25 | [[accessibility-and-languages\|Accessibility & Languages]] | ~3 (+ VOC ~7 / YouTube ~3) | 🟡 Low to medium | Keyboard navigation, alt, lang; English-only interface |

## Top 5 takeaways

1. **Lead with "no Git, GitHub or terminal needed: right-click to publish".** This is the largest group of pains (about 150 cards + 46 comments), and the most direct answer from MDFriday's confirmed capabilities. Guest mode needs no sign-up, which brings the cost of "let me see the result first" close to zero. See [[setup-and-deploy-barrier|Setup & Deploy Barrier]].
2. **Answer fidelity with AS mode, backed by an honest support matrix.** Fidelity is the fastest-growing pain, and the story of "subscribed, then found Canvas can't be published, asked for a refund" shows that stating the support scope clearly matters more than the feature itself. Dataview / Bases / Canvas are all (unconfirmed) for now. See [[rendering-fidelity|Rendering Fidelity]].
3. **Turn the privacy boundary into a verifiable promise.** Selective publish + local build are confirmed; next, confirm that the graph, site search, dead links and attachments don't leak unpublished content, then say so publicly. See [[selective-publish-and-privacy|Selective Publish & Privacy]].
4. **Pair "cheaper than Publish" with storage and clearing rules.** Users find 4 GB too little, while Personal is 1 GB; Guest / Free get cleared, which runs straight into anxieties about expiring links and vanishing vendors. Show the quota before publishing, explain the trial tiers clearly, and stress that source notes always stay local. See [[pricing-and-lock-in|Pricing & Lock-in]], [[media-and-storage-limits|Media & Storage Limits]], [[vendor-trust-and-reliability|Vendor Trust & Reliability]].
5. **Chinese users are a different map.** About 63% of existing customers use Chinese email domains, yet the top 15 clusters come almost entirely from English communities. The biggest pains in the Chinese community are mainland access, Chinese filenames and payment/renewal. Most urgent: test how Cloudflare actually performs inside mainland China, run a Chinese-vault regression test, and confirm the payment methods. See [[mainland-china-access|Mainland China Access]], [[chinese-filenames|Chinese Filenames]], [[chinese-community-voices|Chinese Community Voices]].

## Known gaps

- **The Chinese-community data is thin.** Only the Obsidian Chinese forum (35 topics), V2EX (11 topics) and 4 Juejin summaries; there is no data from Zhihu (login required), Xiaohongshu or Bilibili, and Sspai had no quotable pains. The conclusions lean toward technical Chinese users.
- **Reddit coverage is limited.** The VOC cards include 194 Reddit posts, but during the web supplement the Reddit API timed out a lot and only 2 posts were retrieved, so recent Reddit discussion may be missing. Product Hunt, Dev.to and Medium weren't searched in the supplement.
- **Counts are approximate.** The VOC cards were multi-labeled by hand by one person; read them as ±10%. Tier 2 signals are source counts and can't be compared directly with card counts.
- **Some card quotes may be excerpts.** Cards are summaries written at collection time; only the original English post excerpts in the cards are quoted here, never the card author's Chinese paraphrase. YouTube comment years are estimated from "N years ago" and are only approximate.
- **This is the voice of the market, not of MDFriday users.** MDFriday's own users haven't been systematically interviewed yet. People who post on forums also skew toward the few who have problems and speak up.
- **Many MDFriday capabilities are still (unconfirmed).** Until they're confirmed, the suggestions in these articles are only hypotheses.

## Next steps

- Turn the Open questions in each article into questions for user conversations (Tuesday Conversations).
- Validate three things from the Top 5 first: a mainland access test, a Chinese-vault regression test, and the support matrix.
- Run another round of research on the Chinese community and Reddit.

---

Related: [[mdfriday/index|MDFriday]] · [[vision|MDFriday Vision]] · [[03.operating-system|SunWei Operating System]] · [[mdfriday/blog/index|MDFriday Blog]]
