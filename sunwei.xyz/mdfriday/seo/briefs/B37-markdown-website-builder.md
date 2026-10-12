---
title: "B37 · Markdown Website Builder (Studio product page)"
brief_id: B37
target_keyword: "markdown website builder"
url: "mdfriday.com/products/studio/"
page_type: "Product"
month: "M07"
priority: "P0"
status: planned
tags:
  - seo-brief
---

# B37 · Markdown Website Builder (Studio product page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | markdown website builder |
| URL | mdfriday.com/products/studio/ |
| Page type | Product |
| Roadmap | M07 (Apr 2027) · P0 |
| Status | planned — Planned for M07 |

## Search intent

Readers looking for a browser-based Markdown website builder. Waits for Studio's public beta.

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
