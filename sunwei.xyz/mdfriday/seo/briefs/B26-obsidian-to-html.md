---
title: "B26 · Obsidian to HTML"
brief_id: B26
target_keyword: "obsidian to html"
url: "mdfriday.com/obsidian-to-html/"
page_type: "Guide"
month: "M04"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B26 · Obsidian to HTML

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian to html |
| URL | mdfriday.com/obsidian-to-html/ |
| Page type | Guide |
| Roadmap | M04 (Jan 2027) · P1 |
| Status | planned — Planned for M04 |

## Search intent

Readers who want plain HTML files from their notes to host anywhere.

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

4 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
