---
title: "B42 · Markdown Mermaid Website"
brief_id: B42
target_keyword: "markdown mermaid website"
url: "(TBD)"
page_type: "Guide"
month: "M09"
priority: "P2"
status: planned
tags:
  - seo-brief
---

# B42 · Markdown Mermaid Website

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | markdown mermaid website |
| URL | (TBD) |
| Page type | Guide |
| Roadmap | M09 (Jun 2027) · P2 |
| Status | planned — Planned for M09 |

## Search intent

Readers who need Mermaid diagrams to render on a published site.

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
