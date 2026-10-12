---
title: "B03 · Publish an Obsidian Folder as a Website"
brief_id: B03
target_keyword: "publish obsidian folder"
url: "mdfriday.com/publish-obsidian-folder/"
page_type: "Guide"
month: "M01"
priority: "P0"
status: in-progress
tags:
  - seo-brief
---

# B03 · Publish an Obsidian Folder as a Website

← [[seo/index|SEO strategy]] · [[voc-db/README|VOC database]]

| | |
|---|---|
| Target keyword | publish obsidian folder |
| URL | mdfriday.com/publish-obsidian-folder/ |
| Page type | Guide |
| Roadmap | M01 (Oct 2026) · P0 |
| Status | in-progress — Going live in M01 (October 2026) |

## Search intent

The vault mixes journals and drafts with public notes. The reader wants to publish one folder and is afraid of uploading the whole vault.

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

37 cards pointed here as of 2026-10-12. The table above is live; open [[voc.base]] → **By SEO page** for all pages.
