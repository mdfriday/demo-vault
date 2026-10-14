---
title: Retrieval as Light
description: A working note on why a small model needs a garden of passages, not a bigger prompt.
date: 2026-07-19
weight: 2
featured: true
cover: images/linked-paths.svg
tags:
  - evergreen
  - retrieval
  - models
---

A laptop model cannot hold the lab. It can hold a question, then fetch the passages that already live in the notes. I treat the vault the way the windowsill treats light: the plant does not store the sun, it stands where the sun arrives.

## A small score

Given a question \(q\) and a note \(d\), I rank with a dot product and stop when the next passage would not change the answer.

$$
s(q, d) = \frac{q \cdot d}{\|q\| \|d\|}
$$

The number is not the point. The point is that [[still-fuzzy]] can stay a seedling and still be retrieved when it is the right seedling. Completeness is not a precondition for being useful.

## What I link from here

- [[a-small-architecture]] — the diagram of the loop
- [[the-bench]] — every lab note, queried
- [[the-windowsill]] — the same idea, with leaves
- [[publish-while-it-grows]] — why this page shipped before the proof was tidy
