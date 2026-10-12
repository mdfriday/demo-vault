---
title: "B05 · Share Obsidian Notes (solution page)"
brief_id: B05
target_keyword: "share obsidian notes"
url: "mdfriday.com/solutions/share-a-note/"
page_type: "Solution"
month: "M01"
priority: "P0"
status: in-progress
tags:
  - seo-brief
---

# B05 · Share Obsidian Notes (solution page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | share obsidian notes |
| URL | mdfriday.com/solutions/share-a-note/ |
| Page type | Solution |
| Roadmap | M01 (Oct 2026) · P0 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

Readers who want to share notes by link, including with a password. The page states accurately what password protection covers.

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

18 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
