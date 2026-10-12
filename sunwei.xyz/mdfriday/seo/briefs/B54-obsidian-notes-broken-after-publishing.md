---
title: "B54 · Obsidian Notes Broken After Publishing? What to Check First"
brief_id: B54
target_keyword: "obsidian notes broken after publishing"
url: "mdfriday.com/obsidian-notes-broken-after-publishing/"
page_type: "Guide"
month: "M05"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B54 · Obsidian Notes Broken After Publishing? What to Check First

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian notes broken after publishing |
| URL | mdfriday.com/obsidian-notes-broken-after-publishing/ |
| Page type | Guide |
| Roadmap | M05 (Feb 2027) · P1 |
| Status | planned — Planned for M05 |

## Search intent

Plugin output, math, Canvas or embeds look wrong after publishing. The second-biggest pain in our VOC research.

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

60 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
