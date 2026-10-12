---
title: "B10 · Pricing page"
brief_id: B10
target_keyword: "mdfriday pricing"
url: "mdfriday.com/pricing/"
page_type: "Pricing"
month: "M02"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B10 · Pricing page

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | mdfriday pricing |
| URL | mdfriday.com/pricing/ |
| Page type | Pricing |
| Roadmap | M02 (Nov 2026) · P1 |
| Status | planned — Planned for M02 |

## Search intent

Readers comparing plans who want to know what a realistic setup costs per year.

## Voice of the customer

Cards that link here (through `seo_brief`):

```base
filters:
  and:
    - type == "voc"
    - file.hasLink(this.file)
views:
  - type: table
    name: VOC cards for this page
    order:
      - file.name
      - title
      - decision
      - reply
      - date
    sort:
      - property: date
        direction: DESC
```

0 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
