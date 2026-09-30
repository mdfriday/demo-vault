---
title: VOC card template
---

# VOC card template

## Batch JSON (input to `scripts/write_cards.py`)

```json
[
  {
    "url": "https://forum.example.com/t/some-topic/9285",
    "theme": "selective-publish",
    "title": "Single vault for public and private notes: needs an ignore list",
    "title_en": "Ignore/Whitelist/Blacklist for Publish",
    "date": "2020-11-30",
    "platform": "Obsidian Forum",
    "says": "Single vault for private and public notes; risk of inadvertently publishing notes never meant to be public; wants ignore/whitelist/blacklist.",
    "says_type": "paraphrase",
    "need": "Reliably exclude private notes inside the same vault.",
    "pain": "Mixing public and private notes makes accidental publishing likely; no folder- or rule-level guard.",
    "implication": "Safe by default: exclusion rules plus a pre-publish 'this will be public' list build trust."
  }
]
```

Field rules:

| Field | Rule |
|---|---|
| `url` | Canonical thread URL. Required. Dedupe key. |
| `date` | Date of the post, `YYYY-MM-DD`. Not the collection date. |
| `theme` | One of the configured theme folders. Unknown themes are rejected. |
| `title` | Short, specific, in the library's working language. `title_en` optional for bilingual libraries. |
| `says` | Verbatim excerpt (copy exactly) or a faithful paraphrase. |
| `says_type` | `verbatim` or `paraphrase`. Later skills quote only `verbatim` text as a quote. |
| `need` | The job the person is trying to get done, one sentence. |
| `pain` | What blocks them, one or two sentences. |
| `implication` | What this means for the product. Leave empty rather than guess. |

## Rendered card

```markdown
---
theme: selective-publish
title: "Single vault for public and private notes: needs an ignore list"
title_en: "Ignore/Whitelist/Blacklist for Publish"
date: 2020-11-30
platform: Obsidian Forum
url: https://forum.example.com/t/some-topic/9285
says_type: paraphrase
---

# Single vault for public and private notes: needs an ignore list

- **Platform:** Obsidian Forum
- **Date:** 2020-11-30
- **Link:** https://forum.example.com/t/some-topic/9285

## What the user says (paraphrase)
...
## Core need
...
## Pain
...
## Implication for <Product>
...
```

## Library README skeleton

```markdown
# Voice of the Customer · <Product> customer needs library

**N** cards (target M; collection paused/ongoing). One folder per theme; every card links to the original post.

| Theme folder | Cards | Meaning |
|---|---:|---|
| `theme-a/` | 83 | ... |

## All cards (newest first)
1. `2026-09-12` [Share by folder](theme-a/2026-09-12-share-by-folder.md) — Reddit r/Example

## Card fields
Metadata (date / platform / URL), what the user says, core need, pain, implication.
```
