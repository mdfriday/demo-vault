---
title: "B41 · Hugo Alternative"
brief_id: B41
target_keyword: "hugo alternative"
url: "(TBD)"
page_type: "Compare"
month: "M08"
priority: "P2"
status: planned
tags:
  - seo-brief
---

# B41 · Hugo Alternative

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | hugo alternative |
| URL | (TBD) |
| Page type | Compare |
| Roadmap | M08 (May 2027) · P2 |
| Status | planned — Planned for M08 |

## Search intent

Hugo users or evaluators who want to avoid the command line.

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
