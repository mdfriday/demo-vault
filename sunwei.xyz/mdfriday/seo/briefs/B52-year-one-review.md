---
title: "B52 · MDFriday Year One review"
brief_id: B52
target_keyword: "(annual review)"
url: "mdfriday.com/blog/mdfriday-year-one/"
page_type: "Blog"
month: "M12"
priority: "—"
status: planned
tags:
  - seo-brief
---

# B52 · MDFriday Year One review

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (annual review) |
| URL | mdfriday.com/blog/mdfriday-year-one/ |
| Page type | Blog |
| Roadmap | M12 (Sep 2027) · — |
| Status | planned — Planned for M12 |

## Search intent

Readers following the build-in-public story.

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
