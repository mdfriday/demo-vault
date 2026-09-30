---
title: Themes & Customization
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Users want a site that looks good and feels like their own, but in reality they have to write publish.css, edit TSX, and still can't remove the platform's branding."
---

# Themes & Customization

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Users want their website to look good and to feel like their own. The reality: writing `publish.css` / `publish.js`, merging several snippets, hunting for Publish-specific themes; in Quartz, changes to fonts, colors or the logo often refuse to take effect; Digital Garden's custom CSS only partly works. The editor theme and the website theme are two separate things, so "the editor and the website don't feel like the same product". There's also a branding complaint: the favicon can't be changed, "Powered by" can't be removed from the footer and titles, and social cards carry the platform's watermark.

> [!info] Signal (approximate)
> ~52 VOC cards (~30 since 2025) · ~11 YouTube comments · 1 web supplement source.
> Ranked **#6**: constant tinkering that hurts both looks and trust.

## Voices

- “without having to change publish.css ourselves” — Obsidian Forum · 2025-02-02 · <https://forum.obsidian.md/t/basic-customization-in-publish-settings-directly-for-published-site-with-preview/95956>
- “make my Reader view look exactly like the Publish view using CSS” — Obsidian Forum · 2025-08-31 · <https://forum.obsidian.md/t/consistent-theme-same-appearance-from-reader-to-publish/105019>
- “This tool is cool but the website has a lot of things I cannot customize or remove.” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=6s6DT1yN4dw>
- “now just need to work on making it not look awful” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=ITiiuBNVue0>
- “I’ve spent the last 45 minutes trying to remove the ‘powered by obsidian publish’ from the footer and the page titles.” — Obsidian Forum · 2023-06-02 · <https://forum.obsidian.md/t/help-removing-powered-by-from-footer-and-page-titles/60906>

## Why it hurts

- **A website is the storefront of a personal brand.** If it's ugly or "doesn't feel like me", users won't share the link.
- **Writing CSS is another technical barrier.** It's essentially the same as the [[setup-and-deploy-barrier|setup barrier]]: writers are forced to do front-end work.
- **Two looks, for the editor and the website, double the maintenance.** Users have already tuned their theme in Obsidian and don't want to do it again.

## How people cope today

- Asking for CSS snippets on the forum and piecing them together.
- Editing TSX and style files in Quartz, then hitting upstream conflicts when upgrading (see [[maintenance-burden|Maintenance Burden]]).
- Relying on community theme repositories, which can vanish without warning (the repository for Digital Garden's Mado 11 theme was deleted).

## MDFriday's response

- **AS mode**: the website matches Obsidian's reading view, so the look users tuned in Obsidian is the look of the website.
- **Multiple themes**: the same notes can switch between different themes (for example a professional style or a personal style), **without writing CSS**.
- Removing the platform watermark / "Powered by", custom favicon, custom footer: **(unconfirmed)**. A custom footer also matters for Chinese users who need to show an ICP filing number; see [[chinese-community-voices|Chinese Community Voices]].

## Open questions

- When switching themes, which settings do users most want to adjust: fonts, colors, logo, footer? Could these be a few simple switches instead of open CSS?
- Can advanced users inject custom CSS (unconfirmed)?
- Do the themes include a layout suited to blogging? See [[blogging-features|Blogging Features]].

## Related

- [[rendering-fidelity|Rendering Fidelity]]
- [[blogging-features|Blogging Features]]
- [[accessibility-and-languages|Accessibility & Languages]]
