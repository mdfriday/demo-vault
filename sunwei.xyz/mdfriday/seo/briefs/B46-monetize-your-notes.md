---
title: "B46 · Monetize Your Notes"
brief_id: B46
target_keyword: "monetize obsidian notes"
url: "(TBD)"
page_type: "Guide"
month: "M11"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B46 · Monetize Your Notes

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | monetize obsidian notes |
| URL | (TBD) |
| Page type | Guide |
| Roadmap | M11 (Aug 2027) · P1 |
| Status | planned — Planned for M11 |

## Search intent

Creators who want to earn from their notes. Waits for payments.

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

1 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
