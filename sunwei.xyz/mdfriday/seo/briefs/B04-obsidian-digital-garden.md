---
title: "B04 · Obsidian Digital Garden (solution page)"
brief_id: B04
target_keyword: "obsidian digital garden"
url: "mdfriday.com/solutions/digital-garden/"
page_type: "Solution"
month: "M01"
priority: "P0"
status: in-progress
tags:
  - seo-brief
---

# B04 · Obsidian Digital Garden (solution page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian digital garden |
| URL | mdfriday.com/solutions/digital-garden/ |
| Page type | Solution |
| Roadmap | M01 (Oct 2026) · P0 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

People who want their knowledge to become a browsable garden or wiki, and care about looks, backlinks and a graph.

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

37 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
