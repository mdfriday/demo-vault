---
title: "B50 · Obsidian Course Notes Website"
brief_id: B50
target_keyword: "obsidian for students publish notes"
url: "(TBD)"
page_type: "Guide (seasonal)"
month: "M11"
priority: "P2"
status: planned
tags:
  - seo-brief
---

# B50 · Obsidian Course Notes Website

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian for students publish notes |
| URL | (TBD) |
| Page type | Guide (seasonal) |
| Roadmap | M11 (Aug 2027) · P2 |
| Status | planned — Planned for M11 |

## Search intent

Students who want to share class notes before the new term.

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
