---
title: Setup & Deploy Barrier
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Almost every free way to publish Obsidian notes assumes you know Git, the command line and CI. It's the largest and most emotional group of pains in the research."
---

# Setup & Deploy Barrier

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

What users want is simple: turn the notes they've written in Obsidian into a web address other people can open. But the free alternatives (Quartz, the Digital Garden plugin, Hugo / Jekyll / Astro / MkDocs) almost all assume you know GitHub, Node / npx and GitHub Actions, and can configure Netlify / Vercel / Cloudflare Pages. The sticking points are highly concentrated: `npx quartz sync` errors, failed Actions builds, GitHub Pages 404s or blank pages, stuck Netlify / Vercel sign-up verification, Windows / WSL environment problems, submodule errors. The comment sections of YouTube tutorials are basically a collection of failed deploys. There are usually only two endings: give up after a long struggle, or pay for Obsidian Publish.

> [!info] Signal (approximate)
> ~150 VOC cards (26% of 567, ~73 of them since 2025) · ~46 YouTube comments · 2 web supplement sources.
> Ranked **#1**: the largest and most emotional pain, and it leads directly to giving up.

## Voices

- “it's been so painful to get to that result, I think I'll just drop it now” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=6s6DT1yN4dw>
- “Still too technical for non-coders. Have to study before I can apply this.” — YouTube comment · ~2023 · <https://www.youtube.com/watch?v=ITiiuBNVue0>
- “Ah too complicated. I paid.” — YouTube comment · ~2023 · <https://www.youtube.com/watch?v=PZ7r3Agdk8M>
- “the worst part almost 90% of these alternatives require GitHub” — Reddit r/ObsidianMD · 2023-08-06 · <https://www.reddit.com/r/ObsidianMD/comments/15jxx07/obsidian_publish_localhost>
- “I got stuck at the very beginning with Netlify sign up identity verification” — YouTube comment · ~2025 · <https://www.youtube.com/watch?v=7f8e5IiUkeo>
- “followed everything... always get 404 error very sad.” — YouTube comment · ~2025 · <https://www.youtube.com/watch?v=6s6DT1yN4dw>
- “There are static site generators, which unfortunately are mostly designed for computer people” — Obsidian Forum · 2025-11-25 · <https://forum.obsidian.md/t/the-viability-of-using-obsidian-as-a-publication-platform/108341>
- 「对非技术用户堪称灾难（曾因输错命令删过整个仓库）」 — Obsidian Chinese forum · 2025-02-24 · <https://forum-zh.obsidian.md/t/topic/46945>
  - *Translation:* For non-technical users it's nothing short of a disaster (I once deleted an entire repository by typing the wrong command).

## Why it hurts

- **The job to be done is "publish", not "learn a front-end engineering stack".** Git, CI and DNS are developer workflows; for writers they're pure overhead.
- **Every step is a point of failure.** Tokens, repository permissions, build scripts, hosting accounts: if any step fails, the error message is unreadable and there's nobody to ask.
- **Both options disappoint.** Users are forced to choose between spending money (Obsidian Publish) and spending time (DIY). This pain often appears alongside [[pricing-and-lock-in|Pricing & Lock-in]].
- **Non-technical users suffer most.** They're drawn in by the idea of a digital garden and then get stuck on the tools.

## How people cope today

- Following YouTube tutorials step by step, asking in the comments when something breaks, then waiting.
- Giving up on DIY and buying Obsidian Publish instead ("I paid.").
- Switching back and forth between Quartz, the Digital Garden plugin and Hugo; see [[choosing-a-publishing-tool|Choosing a Publishing Tool]].
- Competitors are already going after this position: Flowershow promotes one-click plugin publishing with no Git and no command line, and new tools such as Verdant also stress "no terminal".

## MDFriday's response

- **This is what MDFriday should lead with.** Right-click a note or a folder in Obsidian, build a static website locally, and publish it to the Cloudflare CDN. The whole GitHub, Git, terminal, Actions and hosting-account chain isn't needed.
- **Guest lets you try without signing up**: 1 site, 5 MB, cleared at the next UTC midnight. Good for "let me see what it looks like first", but it must be clear that it's a trial tier (see [[vendor-trust-and-reliability|Vendor Trust & Reliability]]).
- In demos, you can simply delete the long "GitHub → Token → Deploy → Domain" section of a Quartz / Digital Garden tutorial and keep only "right-click → publish → open the URL".

## Open questions

- How long does it take a real new user to go from installing the plugin to getting their first URL? Where do they get stuck? This maps directly to the success metric "First publish completed".
- When the plugin hits an error, is the message plain enough for non-technical users to fix it themselves?
- Do non-technical users understand the difference between Guest / Free / Personal, and that Guest gets cleared?
- In the Chinese context, "no GitHub / Vercel needed" is worth even more; see [[mainland-china-access|Mainland China Access]].

## Related

- [[choosing-a-publishing-tool|Choosing a Publishing Tool]]
- [[pricing-and-lock-in|Pricing & Lock-in]]
- [[maintenance-burden|Maintenance Burden]]
- [[custom-domains|Custom Domains]]
- [[chinese-community-voices|Chinese Community Voices]]
