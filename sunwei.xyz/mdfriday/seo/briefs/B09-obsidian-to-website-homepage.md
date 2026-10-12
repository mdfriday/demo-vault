---
title: "B09 · Obsidian to Website (homepage)"
brief_id: B09
target_keyword: "obsidian to website"
url: "mdfriday.com/"
page_type: "Homepage"
month: "M02"
priority: "P0"
status: planned
tags:
  - seo-brief
---

# B09 · Obsidian to Website (homepage)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian to website |
| URL | mdfriday.com/ |
| Page type | Homepage |
| Roadmap | M02 (Nov 2026) · P0 |
| Status | planned — Planned for M02 |

## Search intent

First-time visitors who want to know in seconds what MDFriday does and how to start.

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
