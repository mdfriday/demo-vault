---
title: "B00 · Guides and Compare hub pages"
brief_id: B00
target_keyword: "(none — navigation page)"
url: "mdfriday.com/guides/ and /compare/"
page_type: "Hub"
month: "M01"
priority: "P0"
status: in-progress
tags:
  - seo-brief
---

# B00 · Guides and Compare hub pages

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (none — navigation page) |
| URL | mdfriday.com/guides/ and /compare/ |
| Page type | Hub |
| Roadmap | M01 (Oct 2026) · P0 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

Give every guide and comparison page a parent page grouped by topic cluster, so readers and search engines can browse them.

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
