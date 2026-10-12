---
title: "B20 · Changelog"
brief_id: B20
target_keyword: "(trust page)"
url: "mdfriday.com/changelog/"
page_type: "Trust"
month: "M01"
priority: "P0"
status: in-progress
tags:
  - seo-brief
---

# B20 · Changelog

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (trust page) |
| URL | mdfriday.com/changelog/ |
| Page type | Trust |
| Roadmap | M01 (Oct 2026) · P0 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

Readers checking whether the product is actively maintained.

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
