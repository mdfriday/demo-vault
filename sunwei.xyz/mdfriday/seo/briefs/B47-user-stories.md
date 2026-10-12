---
title: "B47 · User stories series (5 posts)"
brief_id: B47
target_keyword: "(case studies)"
url: "mdfriday.com/blog/stories/<site>/"
page_type: "Story"
month: "M10–M12"
priority: "—"
status: planned
tags:
  - seo-brief
---

# B47 · User stories series (5 posts)

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | (case studies) |
| URL | mdfriday.com/blog/stories/<site>/ |
| Page type | Story |
| Roadmap | M10–M12 (Jul 2027 – Sep 2027) · — |
| Status | planned — Planned for M10 |

## Search intent

Readers who want proof from real users.

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
