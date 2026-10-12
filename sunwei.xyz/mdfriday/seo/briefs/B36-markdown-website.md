---
title: "B36 · Markdown Website (category page)"
brief_id: B36
target_keyword: "markdown website"
url: "mdfriday.com/solutions/markdown-website/"
page_type: "Solution"
month: "M07"
priority: "P0"
status: planned
tags:
  - seo-brief
---

# B36 · Markdown Website (category page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | markdown website |
| URL | mdfriday.com/solutions/markdown-website/ |
| Page type | Solution |
| Roadmap | M07 (Apr 2027) · P0 |
| Status | planned — Planned for M07 |

## Search intent

People with a Markdown folder who want a website, with or without Obsidian.

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
