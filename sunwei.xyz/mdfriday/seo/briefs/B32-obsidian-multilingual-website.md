---
title: "B32 · Obsidian Multilingual Website"
brief_id: B32
target_keyword: "obsidian multilingual website"
url: "mdfriday.com/obsidian-multilingual-website/"
page_type: "Guide"
month: "M06"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B32 · Obsidian Multilingual Website

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian multilingual website |
| URL | mdfriday.com/obsidian-multilingual-website/ |
| Page type | Guide |
| Roadmap | M06 (Mar 2027) · P1 |
| Status | planned — Planned for M06 |

## Search intent

Readers who want a bilingual or multilingual site from their notes. Waits until the product supports it in the plugin.

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

6 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
