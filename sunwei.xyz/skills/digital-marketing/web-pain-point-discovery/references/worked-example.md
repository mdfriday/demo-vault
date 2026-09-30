---
title: 'Worked example: MDFriday web supplement (2026-09-26)'
---

# Worked example: MDFriday web supplement (2026-09-26)

**Scope.** Supplement to a 15-cluster summary. 117 pages archived. Result: 12 new clusters + 1 weak signal, 4 Chinese-community pains, a short new-evidence section. 92 quotes from 76 distinct URLs, 92/92 verified. URLs deduped against ~5,200 normalized URLs from the existing research.

## New clusters (excerpt)

| # | New cluster | Signal | Latest | Relevance |
|---:|---|---:|---|---|
| N1 | Attachment / media storage limits and large files | 12 | 2025-12 | Very high (product quota is smaller than the official one) |
| N2 | Large-vault builds slow or failing | 5 | 2025-07 | Medium (local build performance must be measured) |
| N3 | Analytics without being forced onto Google | 4 | 2026-09 | Medium (cheap differentiator) |
| N7 | Reliability and trust in a small vendor | 6 | 2026-03 | High (free tiers are cleared periodically) |
| N8 | Mainland China access (GitHub Pages / Vercel / Cloudflare) | 16 | 2026-09 | Highest (~63% of customers have Chinese email domains) |
| N12 | Chinese file names and titles break links or deploys | 6 | 2025-07 | High |

## One cluster, as built

**N1 Attachment / media storage limits.** People treat high-res images, PDFs and audio in the vault as site content, then hit a size cap (4 GB on the official product), attachments that don't publish with the note, or forced compression.

- Signal: 12 sources (7 quoted, 5 corroborating archived threads).
- Quotes (verbatim, original language):
  - 「these would fairly soon exceed 4gb」 — Obsidian Forum · 2022-12-09
  - 「if I add a photo to a published note, I need to remember to separately publish that new photo」 — Obsidian Forum · 2024-03-23
  - 「发布网站的容量建议支持扩容，付费扩容都是可以的」 — Obsidian Chinese forum · 2025-12-08
    - *Translation:* I'd suggest letting the published site's storage be expanded; paying for extra capacity would be totally fine.
- Response: the product's quotas (5 MB / 50 MB / 1 GB by tier) are smaller than the 4 GB users already call insufficient. Suggested: show upload size vs remaining quota before publishing; explain 1 GB as "about how many images/pages"; image compression, bundling attachments and paid expansion all marked **to be confirmed**.

## Chinese community section

Source honesty: the Chinese Obsidian forum (35 topics) and V2EX (11 topics) worked; Juejin gave summaries only; Sspai gave nothing quotable; Zhihu needed login; Xiaohongshu and Bilibili were not tried. So conclusions lean technical and under-represent non-technical Chinese users.

Qualitative finding (no counts): after the shared "setup" and "price" pains, Chinese users rank network reachability (N8), Chinese paths/titles (N12) and payment/renewal (N9) highest. Plus four community-specific pains: C1 cross-posting to domestic platforms (WeChat official accounts, Xiaohongshu, Zhihu), C2 image-host dependence and dead image links, C3 ICP filing display requirements, C4 Feishu-style cloud docs used instead of "publishing".

## Priority impact (excerpt)

| Priority | Pain | Why | Must confirm first |
|---|---|---|---|
| P0 | N8 mainland access | Strongest new signal; most customers are Chinese-speaking; hosting reputation mixed | Measured access from several regions and carriers |
| P0 | N1 storage limits | Quota comparison invites complaints | Compression, attachment bundling, expansion pricing |
| P1 | N12 Chinese paths/titles | Cheap to guarantee, strongly felt | Regression test on a Chinese vault |

Message impact: "No Git needed" becomes, for Chinese audiences, "No GitHub/Vercel needed, and it opens in China" (second half only after measurement); add "Chinese file names, titles and search work out of the box".
