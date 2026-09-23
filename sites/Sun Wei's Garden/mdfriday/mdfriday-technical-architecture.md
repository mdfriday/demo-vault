---
title: MDFriday Technical Architecture
date: 2026-08-18
tags: [journey, mdfriday, tech]
---

# MDFriday Technical Architecture

This is a map, not a whitepaper. MDFriday's architecture exists to protect one feeling for the user: *my notes stayed mine; the site appeared*.

## Layers (mental model)

1. **Vault / Markdown source** — local files the user already trusts (often Obsidian).
2. **Publish selection** — which notes/folders are allowed to leave private mode.
3. **Foundry / build core** — the engine that understands Markdown structure and produces a static site. See [[Building Foundry]].
4. **Theme layer** — Hugo-compatible theme ecosystem so creators inherit design leverage instead of inventing CSS from zero.
5. **Deploy targets** — static hosting paths (Netlify, FTP, and similar). The point is output you can host, not a single mandatory cloud.

## Why Hugo literacy matters

I did not read Hugo source code for trivia. Hugo is a battle-tested grammar for content organization, taxonomies, and themes. [[Why I Read Hugo Source Code]] is the narrative of that investment; Foundry is where that literacy became product leverage.

## Design constraints

- **Local-first**: source of truth is on disk.
- **Selective by default**: publish is intentional.
- **Obsidian-friendly**: WikiLinks and note-centric navigation should not feel alien.
- **Boring where possible**: static files age better than clever servers you must babysit alone.

## How product surfaces map

[[MDFriday Publish]] is the human-facing workflow. Architecture exists to make that workflow reliable — preview, publish, unpublish, history — without forcing creators to memorize a toolchain.

## Related Assets

- [[How to Build a Product]]
- [[How to Use AI as a Builder]] — AI helps me move across these layers faster, not skip understanding them.

## Non-goals in the architecture

Foundry should not become a hosted editor, a sync service, or a social graph. Those problems are real; they are not *this* problem. Keeping the architecture skinny protects the publish promise and keeps a [[One Person Company]] able to maintain the core.
