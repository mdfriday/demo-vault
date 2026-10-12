---
title: "B58 · Case study: Publishing a 255-Note Obsidian Garden with MDFriday"
brief_id: B58
target_keyword: "(case study)"
url: "mdfriday.com/blog/stories/sunwei-xyz/"
page_type: "Story"
month: "M03"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B58 · Case study: Publishing a 255-Note Obsidian Garden with MDFriday

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (case study) |
| URL | mdfriday.com/blog/stories/sunwei-xyz/ |
| Page type | Story |
| Roadmap | M03 (Dec 2026) · P1 |
| Status | planned — Planned for M03 |

## Search intent

Readers who want a real, honest example — this is the founder's own site, and it says so.

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
