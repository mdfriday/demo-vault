---
title: Rendering Fidelity
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Fine in Obsidian, broken once published: plugins, Dataview, Bases, Canvas and math are the most frequent casualties."
---

# Rendering Fidelity

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

"It looks fine in Obsidian, and breaks as soon as it's published." The most frequent casualties, in order: Dataview / Bases tables and cards, Canvas, Excalidraw, LaTeX math (including preambles, inline math in headings, and long formulas cut off on phones), callouts and custom callouts, footnotes, iframe / YouTube / PDF embeds, Properties, plugin-based coloring, and all kinds of statblocks and infoboxes. Obsidian Publish doesn't run community plugins, Quartz doesn't support Dataview, and the Digital Garden plugin breaks Dataview images and links. One user subscribed to Publish, only then discovered that Canvas can't be published, and immediately asked for a refund.

> [!info] Signal (approximate)
> ~89 VOC cards (~51 since 2025, clearly growing) · ~24 YouTube comments (8 Dataview / Bases, 4 Canvas, 4 images / attachments, 3 math) · 2 web supplement sources.
> Ranked **#2**: the fastest-growing pain, and one that leads directly to refunds or giving up.

## Voices

- “I was initially dismayed that plugins generally don't render in Publish.” — Reddit r/ObsidianMD · 2025-09-15 · <https://www.reddit.com/r/ObsidianMD/comments/1nh8730/obsidian_publish_my_journey_resources>
- “I subscribed… Canvas can't be published… Can I be refunded” — Obsidian Forum · 2026-02-06 · <https://forum.obsidian.md/t/just-subscribed-to-publish-plan-canvas-cant-be-published-can-i-be-refunded-5-after-subscribing/110890>
- “I rely on dataview too much for it not to be included in Quartz.” — YouTube comment · ~2025 · <https://www.youtube.com/watch?v=6s6DT1yN4dw>
- “I would pay to be able to publish a canvas using Obsius or any other way.” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=-5RO4Xsw9Ec>
- “Just deployed but LateX code(equations) are not working on website.” — YouTube comment · ~2022 · <https://www.youtube.com/watch?v=kg-9n_A4Tf0>
- 「目前发布功能还不支持官方的数据库」 — Obsidian Chinese forum · 2025-12-08 · <https://forum-zh.obsidian.md/t/topic/56559>
  - *Translation:* The publish feature doesn't support the official database yet.
- 「一些很长的数学公式在发布网站的移动端，会直接被隐藏掉」 — Obsidian Chinese forum · 2026-01-26 · <https://forum-zh.obsidian.md/t/topic/58215>
  - *Translation:* Some very long math formulas simply get hidden on the mobile version of the published site.

## Why it hurts

- **Users' notes aren't plain Markdown.** Over the years people have put more and more structure into plugins: Dataview queries, Bases databases, Canvas boards. To them, that is the content.
- **The "what you see is what you get" expectation breaks.** The editor shows one thing and the website another, so users rewrite by hand or substitute screenshots, and maintain two versions.
- **Finding out after paying hurts most.** The refund request shows that an unclear support scope damages trust more than a missing feature.

## How people cope today

- Manually turning Dataview results into static tables, or pasting in screenshots.
- Pre-processing with plugins like Enveloppe or Digital Garden, which often brings new errors.
- Living with Publish not running plugins, or simply not publishing that content.
- Competitor positioning: Kiln positions itself as "if it works in Obsidian, it should work on the website" (paraphrased); Flowershow already advertises Canvas and Bases support.

## MDFriday's response

- **AS mode**: renders faithfully the way Obsidian does, with the goal that the website looks the way the note looks in Obsidian.
- **Whether Dataview / Bases / Canvas / Excalidraw are supported: (unconfirmed)**; how long formulas behave on phones: (unconfirmed).
- Suggestion: publish an honest "supported / not supported" matrix. That is itself a trust selling point, and it keeps the "only found out after subscribing" story from repeating with MDFriday.
- Guest mode needs no sign-up, which lets users check rendering with their own real notes before paying.

## Open questions

- AS mode's current coverage of callouts, LaTeX, Mermaid, footnotes, embeds and Properties needs a list that can be published.
- Of Dataview / Bases / Canvas, which do users need first? Ask directly in conversations.
- If plugin rendering isn't possible, could there be a fallback that turns results into static output at build time?

## Related

- [[themes-and-customization|Themes & Customization]]
- [[knowledge-structure-on-the-web|Knowledge Structure on the Web]]
- [[export-beyond-the-web|Export Beyond the Web]]
- [[setup-and-deploy-barrier|Setup & Deploy Barrier]]
