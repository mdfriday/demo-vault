---
title: "B48 · State of Obsidian Publishing 2027"
brief_id: B48
target_keyword: "(original research)"
url: "mdfriday.com/state-of-obsidian-publishing-2027/"
page_type: "Report"
month: "M11"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B48 · State of Obsidian Publishing 2027

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (original research) |
| URL | mdfriday.com/state-of-obsidian-publishing-2027/ |
| Page type | Report |
| Roadmap | M11 (Aug 2027) · P1 |
| Status | planned — Planned for M11 |

## Search intent

Readers and writers looking for data on how people publish Obsidian notes.

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
