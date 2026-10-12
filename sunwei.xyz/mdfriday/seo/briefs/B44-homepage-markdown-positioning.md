---
title: "B44 · Homepage positioning: markdown to website"
brief_id: B44
target_keyword: "markdown to website"
url: "mdfriday.com/"
page_type: "Homepage"
month: "M07"
priority: "—"
status: planned
tags:
  - seo-brief
---

# B44 · Homepage positioning: markdown to website

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | markdown to website |
| URL | mdfriday.com/ |
| Page type | Homepage |
| Roadmap | M07 (Apr 2027) · — |
| Status | planned — Planned for M07 |

## Search intent

Shift the homepage focus from Obsidian to Markdown while keeping Obsidian as the first entry point.

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
