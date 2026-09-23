---
title: Why I Read Hugo Source Code
date: 2026-05-20
tags: [journey, mdfriday, tech]
---

# Why I Read Hugo Source Code

I did not open Hugo's source because I wanted to become a Hugo core contributor. I opened it because **MDFriday** needed a deeper kind of honesty: if I was going to help knowledge creators publish with a Hugo-theme ecosystem, I needed to understand the grammar under the themes — not only the docs happy path.

## The practical itch

Themes are leverage. They are also a trap if you treat them as magic skins. When something breaks — menus, taxonomies, partials, content organization — "try another theme" is not a strategy. Reading source is how you learn which behaviors are intentional, which are conventions, and which are sharp edges you must design around in a product.

## What I was looking for

- How content is discovered and rendered
- How themes compose layouts and partials
- Where assumptions about folders and front matter quietly rule everything
- Which parts are stable enough to build a product on

That reading later fed [[Building Foundry]] and the map in [[MDFriday Technical Architecture]].

## What surprised me

Hugo is opinionated in a useful way. It rewards structure. Knowledge creators in Obsidian are also opinionated — just differently (WikiLinks, evergreen notes, daily fragments). The product problem is translation with respect, not forced conversion of someone's vault into a textbook Hugo blog.

## How this changed MDFriday

I stopped thinking "wrap Hugo somehow" as a vague slogan and started thinking in seams: selection → build → theme → deploy. Foundry became the place where those seams could be owned without pretending users must memorize Hugo's entire mental model.

## Advice if you are building nearby

Read upstream systems when your product stands on them. Use AI to navigate faster — [[How to Use AI as a Builder]] — but do not outsource understanding. The customers who stretch your product will eventually hit the same seams you avoided learning.

## Related

- [[Building Foundry]]
- [[MDFriday Publish]]
- [[Why Focus on Publish]]
