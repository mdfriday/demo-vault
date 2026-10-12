---
title: "B17 · Obsidian Website Examples (showcase)"
brief_id: B17
target_keyword: "obsidian website examples"
url: "mdfriday.com/showcase/"
page_type: "Showcase"
month: "M01–M12"
priority: "P1"
status: in-progress
tags:
  - seo-brief
---

# B17 · Obsidian Website Examples (showcase)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian website examples |
| URL | mdfriday.com/showcase/ |
| Page type | Showcase |
| Roadmap | M01–M12 (Oct 2026 – Sep 2027) · P1 |
| Status | in-progress — Empty state in M01, first version in M03, updated through M12 |

## Search intent

Readers who want to see real sites before choosing a tool.

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
