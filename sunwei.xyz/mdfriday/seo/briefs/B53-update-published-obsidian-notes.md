---
title: "B53 · Update Published Obsidian Notes"
brief_id: B53
target_keyword: "update obsidian publish site"
url: "mdfriday.com/update-published-obsidian-notes/"
page_type: "Guide"
month: "M04"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B53 · Update Published Obsidian Notes

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | update obsidian publish site |
| URL | mdfriday.com/update-published-obsidian-notes/ |
| Page type | Guide |
| Roadmap | M04 (Jan 2027) · P1 |
| Status | planned — Planned for M04 |

## Search intent

Readers who already published, edited their notes, and want to know how the site follows, how fast, and whether links break.

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

22 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
