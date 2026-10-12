---
title: "B35 · Chinese localization (6 pages)"
brief_id: B35
target_keyword: "(Chinese core pages)"
url: "mdfriday.com/zh/…"
page_type: "Localization"
month: "M06"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B35 · Chinese localization (6 pages)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (Chinese core pages) |
| URL | mdfriday.com/zh/… |
| Page type | Localization |
| Roadmap | M06 (Mar 2027) · P1 |
| Status | planned — Planned for M06 |

## Search intent

Chinese-speaking Obsidian users who need the core pages in their language — localized, not translated line by line.

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

1 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
