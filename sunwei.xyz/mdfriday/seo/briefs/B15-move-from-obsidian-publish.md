---
title: "B15 · Move from Obsidian Publish to MDFriday"
brief_id: B15
target_keyword: "migrate from obsidian publish"
url: "mdfriday.com/move-from-obsidian-publish/"
page_type: "Guide"
month: "M03"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B15 · Move from Obsidian Publish to MDFriday

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | migrate from obsidian publish |
| URL | mdfriday.com/move-from-obsidian-publish/ |
| Page type | Guide |
| Roadmap | M03 (Dec 2026) · P1 |
| Status | planned — Planned for M03 |

## Search intent

Obsidian Publish users who have decided to move and want a safe step-by-step migration.

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
