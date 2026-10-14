---
title: A Small Architecture
description: "The loop I actually run: question, notes, answer, then a new note."
date: 2026-08-02
weight: 3
tags:
  - budding
  - retrieval
---

This is the system on one page. It is still budding because the write-back step is sloppy. I often forget to plant the answer as its own note.

```mermaid
flowchart LR
  Q[Question] --> R[Retrieve notes]
  R --> A[Draft an answer]
  A --> N[Plant a new note]
  N --> R
```

[[retrieval-as-light]] is the scoring note. [[the-bench]] is what the retrieve step can see today. When a passage is only a [[still-fuzzy|seedling]], the diagram does not care. The tag tells a reader how much to trust it. The link still works.
