---
title: Publish a note
weight: 31
tags: [publish, single-note]
date: 2026-09-19
---

# Publish a note

## Goal

Turn **this one** Markdown note into a public (or password-protected) web link without exposing other notes in the vault.

## Prerequisites

- MDFriday Publish enabled (desktop)
- Selection is a **file**, not a folder

## Steps

1. Locate the note in the file list or editor
2. **Right-click** → **Publish to MDFriday** (or **Open in MDFriday** first, then publish)
3. In the right panel, confirm **Publish target** is that file (badge “File”)
4. Choose how to publish:
   - **Faithful publish** (default recommendation): close to Obsidian’s local preview
   - **Single-page theme**: pick from Notes-family themes (defaults toward `paper`)
5. (Optional) Set an [[password|access password]] under Advanced
6. (Optional) [[local-preview|Preview]]
7. Click **Publish** / **Verify and publish**, then **Copy** the URL

<!-- MEDIA: screenshot — single-note mode switch: faithful / single-page theme -->
![Placeholder: note modes](../images/placeholder-note-modes.png)

## Confirm success

- Result page shows **Published** + public URL
- Opening the same path again **remembers** mode / theme / password toggle
- Republishing usually updates the **same site** (mdf key / Guest credential persists)

## Related

- [[modes|Publish modes]]
- [[../themes/notes-themes|Notes themes]]
- Website solution: <https://mdfriday.com/solutions/share-a-note/>

## Common failures

| Symptom | What to do |
| --- | --- |
| Wanted a folder but stayed in single-note UI | Right-click the folder; see [[publish-folder\|Publish a folder]] |
| Faithful look differs from the vault | Community plugins / custom syntax may not all staticize; try a single-page theme or simplify the note |
| Guest site limit reached | Claim Free or unpublish an old site; see [[../plans/guest-free-personal\|Plans]] |
