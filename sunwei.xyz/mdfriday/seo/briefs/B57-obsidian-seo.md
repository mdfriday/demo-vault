---
title: "B57 · SEO for Published Obsidian Notes"
brief_id: B57
target_keyword: "obsidian seo"
url: "mdfriday.com/obsidian-seo/"
page_type: "Guide"
month: "M05"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B57 · SEO for Published Obsidian Notes

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian seo |
| URL | mdfriday.com/obsidian-seo/ |
| Page type | Guide |
| Roadmap | M05 (Feb 2027) · P1 |
| Status | planned — Planned for M05 |

## Search intent

People whose published site doesn't show up in Google. Waits until the product's own SEO fixes are verified.

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

19 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
