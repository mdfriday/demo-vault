---
title: "B51 · Homepage positioning: publishing platform"
brief_id: B51
target_keyword: "markdown publishing platform"
url: "mdfriday.com/"
page_type: "Homepage"
month: "M12"
priority: "—"
status: planned
tags:
  - seo-brief
---

# B51 · Homepage positioning: publishing platform

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | markdown publishing platform |
| URL | mdfriday.com/ |
| Page type | Homepage |
| Roadmap | M12 (Sep 2027) · — |
| Status | planned — Planned for M12 |

## Search intent

Shift positioning to 'Publish what you know. Grow readers. Get paid.' once those features are in real use.

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
