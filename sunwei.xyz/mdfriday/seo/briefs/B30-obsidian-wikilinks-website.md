---
title: "B30 · Obsidian Wikilinks on a Website"
brief_id: B30
target_keyword: "obsidian wikilinks website"
url: "mdfriday.com/obsidian-wikilinks-website/"
page_type: "Guide"
month: "M05"
priority: "P2"
status: planned
tags:
  - seo-brief
---

# B30 · Obsidian Wikilinks on a Website

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian wikilinks website |
| URL | mdfriday.com/obsidian-wikilinks-website/ |
| Page type | Guide |
| Roadmap | M05 (Feb 2027) · P2 |
| Status | planned — Planned for M05 |

## Search intent

Readers who want wikilinks, backlinks and a graph to keep working on the published site.

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

18 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
