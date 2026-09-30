---
title: 'Worked example: MDFriday pain point report (excerpts)'
---

# Worked example: MDFriday pain point report (excerpts)

Corpus: 567 VOC cards (2019-02 → 2026-09; Obsidian Forum 205, Reddit 194, HN 87, Dev.to 36, blogs 31, Medium 12) and 592 YouTube comments from 35 videos. 56 cards background-only, 511 with at least one of 20 tags. Quote verification: VOC 55/55, YouTube 45/45.

## Ranked clusters (top 8 of 15)

| # | Cluster | VOC cards | Since 2025 | YouTube comments | Intensity |
|---:|---|---:|---:|---:|---|
| 1 | Setup and deploy barrier (Git / CLI / CI / hosting config) | 150 | 73 | 46 | Most frequent; directly causes abandonment |
| 2 | Rendering fidelity lost (plugins / Dataview / Bases / Canvas / math) | 89 | 51 | 24 | Frequent, growing; causes refunds and abandonment |
| 3 | Price, subscription and lock-in (ownership / self-host) | 67 | 26 | 19 | Long-standing; main migration motive |
| 4 | Knowledge structure lost on the web (wikilinks / nav / graph / search) | 59 | 24 | 16 | Core expectation of digital gardeners |
| 5 | Selective publishing and privacy boundary | 52 | 24 | 17 | Medium frequency, often "the only blocker" |
| 6 | Themes and customization cost | 52 | 30 | 11 | Constant tinkering; hurts trust |
| 7 | Sync, update, mobile and glue workflows | 37 | 22 | 10 | Long-term friction after publishing |
| 8 | SEO, discoverability and performance | 38 | 22 | 5 | Hard blocker for bloggers, academics, large sites |

## One cluster, as written

**2.1 Setup and deploy barrier.** The largest and most emotional cluster. Free alternatives assume GitHub, Node/npx and Actions, plus Netlify/Vercel/Cloudflare Pages. People get stuck on `npx quartz sync` errors, failed Actions builds, GitHub Pages 404s, sign-up verification and Windows paths. Some give up after two weeks; some pay for the official product instead.

- Evidence: 150 cards (26% of 567; 73 since 2025); 46 YouTube comments.
- Quotes:
  - "it's been so painful to get to that result, I think I'll just drop it now" — `youtube-research-2026-09/comments/6s6DT1yN4dw.info.json` · https://www.youtube.com/watch?v=6s6DT1yN4dw
  - "Ah too complicated. I paid." — `youtube-research-2026-09/comments/PZ7r3Agdk8M.info.json` · https://www.youtube.com/watch?v=PZ7r3Agdk8M
  - "the worst part almost 90% of these alternatives require GitHub" (card) — `voice-of-customer/competitor-signals/2023-08-06-reddit-obsidianmd-15jxx07.md`
- Competitors: Quartz (most), Digital Garden plugin + Vercel/Netlify, Hugo/Jekyll/Astro/MkDocs. Flowershow already claims "No Git required. No command line."
- Opportunity: right-click publish, local build, CDN hosting (confirmed). "This is the point to lead with."

## Top messages (first two of five)

1. **"Publish without Git, GitHub or a terminal: right-click in Obsidian."** Cluster 1 (150 cards + 46 comments). Hooks: "too technical for non-coders", "I think I'll just drop it now". Demo: delete the whole "GitHub → token → deploy → domain" section from a typical tutorial.
2. **"Publish only the notes or folders you choose; the rest of the vault stays local."** Clusters 5 and 3. Pre-condition: confirm graph, dead links and attachments cannot leak unpublished content before making it a promise.

## Product gaps (excerpt)

| Priority | Gap | Evidence | Note |
|---|---|---|---|
| P0 | Dynamic content fidelity (Dataview / Bases / Canvas / Excalidraw / math) | VOC 89, YouTube 24 | Fastest-growing; at least publish a support matrix |
| P0 | Privacy guarantees after publishing (graph, dead links, attachments) | Several concrete leak reports | Section-level hiding is roadmap in drafts |
| P1 | Access control (page / user passwords, public landing + private area) | VOC 20, YouTube 6 | Clearest willingness to pay |

Data gap called out: existing customers are mostly Chinese-speaking (aggregate email-domain share ~63%), but almost all pain evidence came from English communities. This triggered the `web-pain-point-discovery` run.
