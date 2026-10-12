---
title: "B25 · Obsidian Publish Themes"
brief_id: B25
target_keyword: "obsidian publish themes"
url: "mdfriday.com/themes/"
page_type: "Themes"
month: "M04"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B25 · Obsidian Publish Themes

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian publish themes |
| URL | mdfriday.com/themes/ |
| Page type | Themes |
| Roadmap | M04 (Jan 2027) · P1 |
| Status | planned — Planned for M04 |

## Search intent

Readers choosing how their published site should look.

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

28 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
