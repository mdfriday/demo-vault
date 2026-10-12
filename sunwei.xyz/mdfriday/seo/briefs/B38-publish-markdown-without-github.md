---
title: "B38 · Publish Markdown Without GitHub"
brief_id: B38
target_keyword: "publish markdown without github"
url: "(TBD)"
page_type: "Guide"
month: "M07"
priority: "P2"
status: planned
tags:
  - seo-brief
---

# B38 · Publish Markdown Without GitHub

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | publish markdown without github |
| URL | (TBD) |
| Page type | Guide |
| Roadmap | M07 (Apr 2027) · P2 |
| Status | planned — Planned for M07 |

## Search intent

Same need as B02, for readers who don't use Obsidian.

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
