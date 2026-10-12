---
title: "B49 · What Is a Digital Garden"
brief_id: B49
target_keyword: "what is a digital garden"
url: "(TBD)"
page_type: "Guide"
month: "M11"
priority: "P3"
status: planned
tags:
  - seo-brief
---

# B49 · What Is a Digital Garden

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | what is a digital garden |
| URL | (TBD) |
| Page type | Guide |
| Roadmap | M11 (Aug 2027) · P3 |
| Status | planned — Planned for M11 |

## Search intent

Top-of-funnel readers learning the concept.

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
