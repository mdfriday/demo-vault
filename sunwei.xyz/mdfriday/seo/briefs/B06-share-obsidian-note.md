---
title: "B06 · Share a Single Obsidian Note as a Web Page"
brief_id: B06
target_keyword: "share obsidian note"
url: "mdfriday.com/share-obsidian-note/"
page_type: "Guide"
month: "M01"
priority: "P1"
status: in-progress
tags:
  - seo-brief
---

# B06 · Share a Single Obsidian Note as a Web Page

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | share obsidian note |
| URL | mdfriday.com/share-obsidian-note/ |
| Page type | Guide |
| Roadmap | M01 (Oct 2026) · P1 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

Someone wants to send one note to a classmate or colleague without building a site.

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

7 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
