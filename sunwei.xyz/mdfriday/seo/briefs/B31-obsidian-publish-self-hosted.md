---
title: "B31 · Obsidian Publish Self-Hosted"
brief_id: B31
target_keyword: "obsidian publish self hosted"
url: "mdfriday.com/obsidian-publish-self-hosted/"
page_type: "Guide"
month: "M05"
priority: "P2"
status: planned
tags:
  - seo-brief
---

# B31 · Obsidian Publish Self-Hosted

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | obsidian publish self hosted |
| URL | mdfriday.com/obsidian-publish-self-hosted/ |
| Page type | Guide |
| Roadmap | M05 (Feb 2027) · P2 |
| Status | planned — Planned for M05 |

## Search intent

Readers who want to host the published site themselves.

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
