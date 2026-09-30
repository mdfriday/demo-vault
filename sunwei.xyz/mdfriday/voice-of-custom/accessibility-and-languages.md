---
title: Accessibility & Languages
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Published sites can't be navigated by keyboard, lack alt text and lang attributes, and render math poorly for screen readers; the interface is English-only and there's no good way to publish multilingual content."
---

# Accessibility & Languages

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

This page merges three small signals. **Accessibility**: published sites can't be navigated by keyboard, focus outlines are removed, image alt text and the `lang` attribute are missing, and math isn't screen-reader friendly, which blocks users in education and the public sector. **Interface language**: fixed text on the site (for example "On this page") is English-only, which looks odd on non-English sites, and RTL languages have problems too. **Multilingual content**: some people want one page to exist in several languages while still counting as a single page.

> [!info] Signal (approximate)
> Accessibility: ~3 web supplement sources · Interface language / RTL: ~7 VOC cards, ~3 YouTube comments · Several language versions of one page: 1 source (weak signal).
> Relevance to MDFriday: **low to medium**, mainly affecting education / public sector and non-English sites.

## Voices

- “There are lots of a11y issues with websites powered by Obsidian Publish.” — Obsidian Forum · 2021-10-26 · <https://forum.obsidian.md/t/publish-accessibility-issues-keyboard-navigation/26193>
- “Obsidian Publish sites typically get amber rated scores for accessibility in Lighthouse due to missing image alt text and a lack of a language attribute.” — Obsidian Forum · 2022-07-01 · <https://forum.obsidian.md/t/publish-accessibility-issues-keyboard-navigation/26193>
- “So I’m a little concerned that math notation won’t be accessible to him.” — Obsidian Forum · 2024-08-23 · <https://forum.obsidian.md/t/is-obsidian-publish-esp-math-rendering-accessible-for-visually-impaired-folks/87318>
- “Actually, this is the only thing the W3 validator complains about” — Obsidian Forum · 2021-07-25 · <https://forum.obsidian.md/t/language-tag-to-html-tag-while-publishing/21488>
- “it is crazy that Obsidian publish is “english only”” — Obsidian Forum · 2023-03-15 · <https://forum.obsidian.md/t/hide-replace-text-labels-like-on-this-page-on-published-sites/56387>
- “I still have to solve a multilanguage option I want to offer to my readers” — YouTube comment · ~2025 · <https://www.youtube.com/watch?v=7f8e5IiUkeo>
- “I would like to make at least some of my pages in Obsidian exist in multiple languages, but still be considered a single page” — Obsidian Forum · 2021-08-05 · <https://forum.obsidian.md/t/pages-in-multiple-languages/22063>

## Why it hurts

- **Accessibility is a hard requirement for some users.** Schools, public institutions and content for visually impaired readers can't use a tool that doesn't meet the standard.
- **The `lang` attribute affects both screen readers and SEO.** If a Chinese site is marked as English, screen readers mispronounce it and search engines may misjudge it.
- **Fixed English text makes non-English sites look unprofessional.**

## How people cope today

- Patching alt text, `lang` and focus styles themselves with publish.js / CSS.
- Replacing the site's English labels with a script.
- Splitting multilingual content into two sets of pages or two sites.

## MDFriday's response

- There are no dedicated accessibility or multilingual features among the currently confirmed capabilities.
- Suggestions: run a Lighthouse / axe accessibility check on the default themes; let each site set `lang` (`zh-CN` for Chinese sites); localize fixed theme text; output math in a screen-reader-friendly format (**all unconfirmed**).
- For MDFriday's Chinese user base, "interface text in Chinese and a correct `lang`" is a low-cost, highly visible detail.

## Open questions

- What Lighthouse accessibility score do MDFriday's current themes get?
- Does fixed theme text already support Chinese (unconfirmed)?
- How should a bilingual Chinese/English site be organized (for example, something sunwei.xyz may need in future)?

## Related

- [[themes-and-customization|Themes & Customization]]
- [[seo-discoverability-and-ai-crawlers|SEO, Discoverability & AI Crawlers]]
- [[chinese-filenames|Chinese Filenames]]
- [[rendering-fidelity|Rendering Fidelity]]
