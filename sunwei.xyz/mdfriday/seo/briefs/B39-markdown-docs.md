---
title: "B39 · Markdown Docs (solution page)"
brief_id: B39
target_keyword: "markdown docs"
url: "mdfriday.com/solutions/markdown-docs/"
page_type: "Solution"
month: "M08"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B39 · Markdown Docs (solution page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | markdown docs |
| URL | mdfriday.com/solutions/markdown-docs/ |
| Page type | Solution |
| Roadmap | M08 (May 2027) · P1 |
| Status | planned — Planned for M08 |

## Search intent

Teams or individuals who want a documentation site from Markdown.

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
