---
title: "B45 · Obsidian Newsletter (solution page)"
brief_id: B45
target_keyword: "obsidian newsletter"
url: "mdfriday.com/solutions/newsletter/"
page_type: "Solution"
month: "M10"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B45 · Obsidian Newsletter (solution page)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian newsletter |
| URL | mdfriday.com/solutions/newsletter/ |
| Page type | Solution |
| Roadmap | M10 (Jul 2027) · P1 |
| Status | planned — Planned for M10 |

## Search intent

Writers who want readers to subscribe to their site. Waits for email sending.

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
