---
title: "B08 · Obsidian Website Builder (product page)"
brief_id: B08
target_keyword: "obsidian website builder"
url: "mdfriday.com/products/obsidian-publish/"
page_type: "Product"
month: "M02"
priority: "P0"
status: planned
tags:
  - seo-brief
---

# B08 · Obsidian Website Builder (product page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian website builder |
| URL | mdfriday.com/products/obsidian-publish/ |
| Page type | Product |
| Roadmap | M02 (Nov 2026) · P0 |
| Status | planned — Planned for M02 |

## Search intent

Readers looking for a tool that turns Obsidian notes into a website.

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
