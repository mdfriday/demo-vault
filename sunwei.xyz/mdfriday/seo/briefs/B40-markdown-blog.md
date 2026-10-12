---
title: "B40 · Markdown Blog (solution page)"
brief_id: B40
target_keyword: "markdown blog"
url: "mdfriday.com/solutions/markdown-blog/"
page_type: "Solution"
month: "M08"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B40 · Markdown Blog (solution page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | markdown blog |
| URL | mdfriday.com/solutions/markdown-blog/ |
| Page type | Solution |
| Roadmap | M08 (May 2027) · P1 |
| Status | planned — Planned for M08 |

## Search intent

Readers who want a blog from Markdown or Obsidian notes.

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

52 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
