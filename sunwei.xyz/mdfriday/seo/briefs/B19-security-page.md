---
title: "B19 · Security page"
brief_id: B19
target_keyword: "(trust page)"
url: "mdfriday.com/security/"
page_type: "Trust"
month: "M01"
priority: "P0"
status: in-progress
tags:
  - seo-brief
---

# B19 · Security page

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (trust page) |
| URL | mdfriday.com/security/ |
| Page type | Trust |
| Roadmap | M01 (Oct 2026) · P0 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

Readers checking what is encrypted, what stays public, and where their data goes.

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
