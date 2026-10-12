---
title: "B59 · Case study: How We Run MDFriday's Help Center on MDFriday"
brief_id: B59
target_keyword: "(case study)"
url: "mdfriday.com/blog/stories/help-center/"
page_type: "Story"
month: "M02"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B59 · Case study: How We Run MDFriday's Help Center on MDFriday

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (case study) |
| URL | mdfriday.com/blog/stories/help-center/ |
| Page type | Story |
| Roadmap | M02 (Nov 2026) · P1 |
| Status | planned — Planned for M02 |

## Search intent

Readers evaluating MDFriday for docs — the help center is our own site, and it says so.

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
