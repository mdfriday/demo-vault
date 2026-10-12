---
title: "B28 · Obsidian Knowledge Base (solution page)"
brief_id: B28
target_keyword: "obsidian knowledge base"
url: "mdfriday.com/solutions/knowledge-base/"
page_type: "Solution"
month: "M05"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B28 · Obsidian Knowledge Base (solution page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian knowledge base |
| URL | mdfriday.com/solutions/knowledge-base/ |
| Page type | Solution |
| Roadmap | M05 (Feb 2027) · P1 |
| Status | planned — Planned for M05 |

## Search intent

People who want a public knowledge base from their notes.

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
