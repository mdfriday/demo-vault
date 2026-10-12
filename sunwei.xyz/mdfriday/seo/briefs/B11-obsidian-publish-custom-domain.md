---
title: "B11 · Obsidian Publish Custom Domain"
brief_id: B11
target_keyword: "obsidian publish custom domain"
url: "mdfriday.com/obsidian-publish-custom-domain/"
page_type: "Guide"
month: "M02"
priority: "P1"
status: planned
tags:
  - seo-brief
---

# B11 · Obsidian Publish Custom Domain

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian publish custom domain |
| URL | mdfriday.com/obsidian-publish-custom-domain/ |
| Page type | Guide |
| Roadmap | M02 (Nov 2026) · P1 |
| Status | planned — Planned for M02 |

## Search intent

People who want their published notes on their own domain, or who are stuck after configuring DNS.

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

26 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
