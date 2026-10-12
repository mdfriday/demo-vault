---
title: "B13 · Quartz Alternative"
brief_id: B13
target_keyword: "quartz alternative"
url: "mdfriday.com/quartz-alternative/"
page_type: "Compare"
month: "M03"
priority: "P0"
status: planned
tags:
  - seo-brief
---

# B13 · Quartz Alternative

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | quartz alternative |
| URL | mdfriday.com/quartz-alternative/ |
| Page type | Compare |
| Roadmap | M03 (Dec 2026) · P0 |
| Status | planned — Planned for M03 |

## Search intent

Quartz users or evaluators who like the result but not the Git, Node and hosting setup.

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

40 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
