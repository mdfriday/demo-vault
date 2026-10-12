---
title: "B21 · Friday Plugin End of Support (announcement)"
brief_id: B21
target_keyword: "(announcement)"
url: "mdfriday.com/blog/friday-plugin-end-of-support/"
page_type: "Blog"
month: "M04"
priority: "P0"
status: planned
tags:
  - seo-brief
---

# B21 · Friday Plugin End of Support (announcement)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (announcement) |
| URL | mdfriday.com/blog/friday-plugin-end-of-support/ |
| Page type | Blog |
| Roadmap | M04 (Jan 2027) · P0 |
| Status | planned — Planned for M04 |

## Search intent

Users of the older Friday plugin who need dates, impact and the migration path.

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
