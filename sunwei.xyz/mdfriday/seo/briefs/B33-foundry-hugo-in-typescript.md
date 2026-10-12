---
title: "B33 · Foundry: Hugo Reimplemented in TypeScript"
brief_id: B33
target_keyword: "(developer audience)"
url: "mdfriday.com/blog/foundry-hugo-in-typescript/"
page_type: "Blog (technical)"
month: "M06"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B33 · Foundry: Hugo Reimplemented in TypeScript

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (developer audience) |
| URL | mdfriday.com/blog/foundry-hugo-in-typescript/ |
| Page type | Blog (technical) |
| Roadmap | M06 (Mar 2027) · P1 |
| Status | planned — Planned for M06 |

## Search intent

Developers curious about the engine behind MDFriday.

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
