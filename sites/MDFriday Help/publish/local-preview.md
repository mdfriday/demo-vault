---
title: Local preview
weight: 34
tags: [preview]
date: 2026-09-19
---

# Local preview

## Goal

View the build result in a local browser **without going live**.

## Prerequisites

- Desktop; publish target and mode / theme already chosen in the right panel

## Steps

1. Open the right-hand **Publish** tab
2. Click the secondary bottom button **“Preview”**
3. Wait for “Building… / Local preview · starting local server”
4. On success, open the local URL (like `http://127.0.0.1:port/`)
5. When done, you can **Stop preview**

<!-- MEDIA: screenshot — preview success result page -->
![Placeholder: local preview success](../images/placeholder-preview-success.png)

## Confirm success

- Badge is **Local preview** (not “Published”)
- Helper: **Preview is local only and does not write publish history**
- Guest Turnstile is **not** required; Guest can preview too

## Related

- [[quick-share|Quick share]] (opens the panel and prepares a preview)
- [[history|Publish history]] (only a real **Publish** enters history)

## Common failures

| Symptom | What to do |
| --- | --- |
| Blank preview | Check build errors; faithful depends on vault look/plugins — compare with themed mode |
| Port won’t open | Local firewall / antivirus; stop preview and retry |
| Thought it was live | Check whether the URL is localhost; public sharing needs **Publish** |
