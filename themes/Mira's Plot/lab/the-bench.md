---
title: The Bench
description: A base over the lab folder. The table updates when a note is added, not when I edit this page.
date: 2026-09-04
weight: 4
tags:
  - budding
  - meta
---

I stopped keeping a hand-written index of the lab. This block reads the folder.

```base
filters:
  and:
    - file.inFolder("lab")
views:
  - type: table
    name: Lab notes
    order:
      - title
      - description
    sort:
      - property: weight
        direction: ASC
```

New notes show up after the next publish. Drafts and unlisted pages stay out. That is the same rule as the rest of the garden: if it is planted, it can be found.
