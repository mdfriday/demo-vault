---
type: voc
id: "blog-runtimeterror-selective-quartz-2024"
date: 2024-09-29
platform: blog
url: "https://runtimeterror.dev/publish-silverbullet-notes-quartz/"
author: "runtimeterror"
title: "Publishing (Selected) SilverBullet Notes with Quartz and GitHub Actions"
quote: "Private SilverBullet/Git repo triggers public Quartz repo via repository_dispatch; ExplicitPublish + ignorePatterns for non-Markdown; warns Quartz docs that non-Markdown still emits publicly. Deploy via Tailscale/Caddy (later Bunny)."
need: "Keep a private notes repo while publishing only publish:true pages via Quartz."
pain: "ExplicitPublish filters Markdown only; non-md assets leak unless ignorePatterns; multi-repo Actions+PAT complexity."
topic: "[[selective-publish-and-privacy]]"
persona: developer
competitor:
  - "Quartz"
fit: partial
intensity: pain
decision: opportunity
reply: not-appropriate
engagement: none
reply_url:
last_touch:
seo_brief: "[[B03-publish-obsidian-folder]]"
source: "marketing/voice-of-customer/selective-publish/2024-09-29-blog-runtimeterror-selective-quartz-2024.md"
tags:
  - voc
---

# Publishing (Selected) SilverBullet Notes with Quartz and GitHub Actions

> Private SilverBullet/Git repo triggers public Quartz repo via repository_dispatch; ExplicitPublish + ignorePatterns for non-Markdown; warns Quartz docs that non-Markdown still emits publicly. Deploy via Tailscale/Caddy (later Bunny).

## Context

Blog post by runtimeterror on 2024-09-29. The quote is copied from the raw card's summary of the post; ellipses (…) mark cuts made when the card was written.

## Our assessment

- Fit: partial · Intensity: pain · Decision: opportunity
- MDFriday covers part of this; check the limits in the README before replying or citing it. Supports [[B03-publish-obsidian-folder|B03]].
- Auto-triaged during the 2026-10-12 migration. Review before replying or citing.

## Follow-up log

- (none yet)
