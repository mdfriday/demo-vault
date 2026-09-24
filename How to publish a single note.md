---
title: How to publish a single note
tags:
  - howto
  - publish
  - single-note
---

# How to publish a single note

## Goal

Turn **one** Markdown note in this demo vault into a shareable web link — without publishing the rest of the vault.

Use this vault as a **sandbox**. Experiment freely here so you do not risk notes in your real vault.

## Prerequisites

- Obsidian **desktop** (MDFriday Publish is desktop-only)
- **MDFriday Publish** enabled (this demo vault already lists it under Community plugins)
- Outbound internet
- Selection is a **file**, not a folder

## Recommended practice note

Open:

- [[Publish what you see in Obsidian ~ As-is]]

It is rich enough (images, callouts, tables, Mermaid, code) to show what As-is publish keeps.

## Steps

### 1. Open the note

Open the note in the editor, or select it in the file tree.

### 2. Open the publish panel

Pick any of these:

| Entry | What it does |
| --- | --- |
| **Right-click** the note → **Publish to MDFriday** | Opens the right panel and starts the publish-oriented flow |
| **Right-click** → **Open in MDFriday** | Opens the panel only (configure first, then click **Publish**) |
| Command palette → **Publish to MDFriday** | Same idea for the **currently open** Markdown file |
| Command palette → **Quick Share** | Opens the panel and prepares a local preview; you still click **Publish** to go live |

The **MDFriday Publish** sidebar appears on the right (tabs: **Publish** | **History**).

### 3. Confirm the target

In the panel, check **Target**:

- Badge shows **File**
- Path / name matches the note you meant

If you wanted a folder instead, stop and see [[How to publish a folder]].

### 4. Choose how to publish

For a single note you can pick:

| Mode | When to use |
| --- | --- |
| **As-is publish** (default) | Closest to Obsidian local preview (theme, many community plugin renders, CSS snippets — within what the local preview pipeline can staticize) |
| **Single-page theme** | A curated standalone page look; pick a Notes-family theme (often defaults toward `paper`) |

### 5. Optional — Advanced

Expand **Advanced** (hint: *Title, logo, password, custom domain*):

- **Title** — site title
- **Logo** — pick an image from the vault (path is relative to the vault root)
- **Access password** — visitors need a password to view
- **Custom domain** — unlocked on **Personal** only (Guest / Free show locked)

> [!note] Nav links
> Site `navLinks` default to empty in the plugin until an editor UI exists. You do not need to configure them for a single-note try.

### 6. Optional — local Preview

Click **Preview** in the sticky bottom bar to build and open a **local** preview (`http://127.0.0.1:…`). Preview never writes History and does not upload.

### 7. Publish

Click **Publish** (or **Publish again** if this path was published before).

**Guest (no account):** the first publish **automatically creates a guest key** for this device. There is **no Turnstile / browser human-check gate** in the current plugin — publishing is seamless. Guest allows **1 site**, **5 MB**, and content clears at the **next UTC 00:00** unless you claim Free.

On success the panel shows **Published** with a public URL — **Copy** or **Open**.

## Confirm success

- Result badge: **Published**
- URL opens in a browser and looks like the mode you chose
- Opening the same note again usually **remembers** mode / theme / password preference and updates the **same site**

## Tips for this demo vault

- Prefer practicing on notes **inside this vault only**
- Guest site limit is **1** — unpublish or claim Free if you hit the soft-gate
- Free plan (after sign-up / claim): **unlimited sites**, **50 MB permanent** storage
- Full docs: <https://help.mdfriday.com>

## Related

- [[How to publish a folder]]
- [[README]]
- Online: [Publish a note](https://help.mdfriday.com) · [Share a note solution](https://mdfriday.com/solutions/share-a-note/)

## Common failures

| Symptom | What to do |
| --- | --- |
| Wanted a multi-page Wiki | Right-click a **folder** — see [[How to publish a folder]] |
| As-is looks different from the vault | Some community syntax may not staticize; try a single-page theme or simplify the note |
| Guest site limit / soft-gate | Claim Free (keep the same URL) or unpublish the old Guest site |
| “Too many guest key requests” | Wait and retry — guest keys are rate-limited by network |
