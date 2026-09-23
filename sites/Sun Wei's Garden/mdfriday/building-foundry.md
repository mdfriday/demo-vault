---
title: Building Foundry
date: 2026-06-28
tags: [journey, mdfriday, tech]
---

# Building Foundry

**Foundry** is the name I use for the build core behind MDFriday — the part that turns selected Markdown into a static site with enough theme compatibility to inherit real design leverage.

This note is the narrative sibling of [[Why I Read Hugo Source Code]]. Reading was input. Foundry is the output that users never have to romanticize.

## Why a named core matters

If everything is "the plugin," you cannot reason about tradeoffs. Naming Foundry helped me separate:

- UX people touch (publish flows, selection, preview) → [[MDFriday Publish]]
- Engine responsibilities (content model, rendering pipeline, theme expectations) → Foundry
- Business packaging → plans, positioning, [[First 10 Paying Customers]]

## Design goals

1. Respect local Markdown as source of truth.
2. Make selective publish a first-class concept, not a patch.
3. Stay compatible enough with Hugo-theme ideas that creators are not trapped in a one-off skin.
4. Fail in understandable ways — builders need errors they can act on.

## What "building" looked like in practice

Lots of small ships. Dogfooding on my own garden. Using AI to accelerate boilerplate and exploration while I kept responsibility for architecture. Refusing features that would make Foundry a CMS in disguise — see [[Why Focus on Publish]].

## Hard parts

Edge cases in real vaults: messy links, incomplete front matter, folders that mean something to a human and nothing to a build. Obsidian culture and static-site culture are cousins, not twins. Foundry lives in the translation layer.

## Where it sits now

Foundry is not "done." It is stable enough to carry product promises, and flexible enough to keep learning from users. Architecture overview: [[MDFriday Technical Architecture]]. Status: [[Latest Status]].

## Takeaway for other builders

If your product wraps a powerful ecosystem, invest in a real core. Themes and UI are visible; the foundry is what keeps the visible parts from lying.
