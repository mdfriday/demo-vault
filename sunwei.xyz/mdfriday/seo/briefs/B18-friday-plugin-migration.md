---
title: "B18 · Friday Plugin Migration Guide"
brief_id: B18
target_keyword: "(existing users)"
url: "help center + /blog/friday-plugin-migration/"
page_type: "Trust"
month: "M01"
priority: "P0"
status: in-progress
tags:
  - seo-brief
---

# B18 · Friday Plugin Migration Guide

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (existing users) |
| URL | help center + /blog/friday-plugin-migration/ |
| Page type | Trust |
| Roadmap | M01 (Oct 2026) · P0 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

Users of the older Friday plugin who need to move to the new Sync and Publish plugins.

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
