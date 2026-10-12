---
title: "B34 · MDFriday on Product Hunt"
brief_id: B34
target_keyword: "(launch)"
url: "mdfriday.com/blog/mdfriday-on-product-hunt/"
page_type: "Blog (launch)"
month: "M06"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B34 · MDFriday on Product Hunt

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (launch) |
| URL | mdfriday.com/blog/mdfriday-on-product-hunt/ |
| Page type | Blog (launch) |
| Roadmap | M06 (Mar 2027) · P1 |
| Status | planned — Planned for M06 |

## Search intent

Visitors arriving from the Product Hunt launch.

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
