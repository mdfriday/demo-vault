---
title: "B01 · How to Publish Obsidian Notes"
brief_id: B01
target_keyword: "publish obsidian notes"
url: "mdfriday.com/publish-obsidian-notes/"
page_type: "Guide (pillar)"
month: "M01"
priority: "P0"
status: in-progress
tags:
  - seo-brief
---

# B01 · How to Publish Obsidian Notes

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | publish obsidian notes |
| URL | mdfriday.com/publish-obsidian-notes/ |
| Page type | Guide (pillar) |
| Roadmap | M01 (Oct 2026) · P0 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

Someone who has used Obsidian for a while wants their notes online but hasn't picked a tool. They want a map of the options, what each one needs, and which to choose.

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

21 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
