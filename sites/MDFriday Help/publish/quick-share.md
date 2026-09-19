---
title: Quick share
weight: 35
tags: [commands, share]
date: 2026-09-19
---

# Quick share

## Goal

Open the publish flow for the current note from the command palette as fast as possible, generate a local preview, then one-click publish after you confirm.

## Prerequisites

- **Desktop only** (mobile shows “Quick share is only available on desktop”)
- Current view is a Markdown note

## Steps

1. Open the note you want to share
2. Command palette → **“Quick share”** (`quick-share`)
3. Wait for “Preparing quick share…” → “Ready! Click Publish to share your note”
4. Confirm in the right panel, then click **Publish**

> [!tip] Difference from the “Publish to MDFriday” command
> - **Quick share**: focuses on opening the panel and preparing a preview
> - **Publish to MDFriday** (`quick-publish`): runs the publish-oriented flow for the current file  
> Both require desktop + an open Markdown file.

## Confirm success

- Right panel shows the current note; a preview result is usually ready to open
- Public sharing still means the public URL after **Published successfully**

## Related

- [[local-preview|Local preview]]
- [[publish-note|Publish a note]]

## Common failures

| Symptom | What to do |
| --- | --- |
| “Please open a Markdown file first” | Focus an md tab first |
| Quick share failed | Read the Notice error; retry via “Open in MDFriday” and preview manually |
