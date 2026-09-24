---
title: How to publish a folder
tags:
  - howto
  - publish
  - folder
  - wiki
  - digital-garden
---

# How to publish a folder

## Goal

Select **one folder** and publish it as a **Wiki / digital garden** (multi-page site with wikilinks / graph — Quartz-family themes).

Use this demo vault as a **sandbox**. Curate a public subset here instead of pointing the plugin at a private folder in your real vault.

## Prerequisites

- Obsidian **desktop** + **MDFriday Publish** enabled
- Folder contains publishable Markdown
- Understand: **folders cannot use As-is publish** — they always go through the Wiki engine

## Recommended practice folder

Use the folder already in this vault:

- `Digital Garden/` (start from [[Digital Garden/index|Digital Garden · Home]])

It has linked notes under AI / Business / Productivity — a good small garden for a first Wiki publish.

## Steps

### 1. Select the folder

In the file tree, click the **folder** (not a single note inside it).

> [!warning] Scope = only that folder
> Only Markdown (and assets) **inside the selected folder** ship. Keep private notes outside it, or do not select a parent that contains them. Whole-vault one-click upload is not the default product model.

### 2. Open the publish panel

| Entry | What it does |
| --- | --- |
| **Right-click the folder** → **Publish to MDFriday** | Opens the right panel and runs the publish-oriented flow for that folder |
| **Right-click** → **Open in MDFriday** | Opens the panel so you can pick a Wiki skin / Advanced options first |

(Command palette **Quick Share** / **Publish to MDFriday** target the **current note**, not a folder — use the file-tree right-click for folders.)

### 3. Confirm the target

In the panel:

- Badge shows **Folder**
- **Publish mode** is fixed to **Wiki publish** (As-is is unavailable for folders by design)
- Path matches the folder you meant

### 4. Pick a Wiki skin

In **Wiki skins**, choose a Quartz-family theme (defaults toward `quartz`).

Optional: open a theme’s **Live demo** to compare looks before publishing.

### 5. Optional — Advanced

Expand **Advanced**:

- **Title** / **Logo** — branding for the site
- **Access password** — gate the whole site
- **Custom domain** — **Personal** only

> [!note] Nav links
> `navLinks` default to **empty** in the plugin until an Advanced editor exists. Theme-seeded nav is not applied for new projects. Multi-page navigation still comes from folder structure + `[[wikilinks]]` / the Wiki theme.

### 6. Optional — local Preview

Click **Preview** to build a local multi-page preview before uploading.

### 7. Publish

Click **Publish site** (first time) or **Publish again**.

**Guest:** first publish **auto-creates a guest key** — **no Turnstile UI** in the current plugin. Guest = **1 site**, **5 MB**, clears next **UTC 00:00** unless you claim Free (**unlimited sites**, **50 MB permanent**).

Copy the public URL when the result shows **Published**.

## Confirm success

- Browser can open multiple pages and follow `[[wikilinks]]` that stay **inside** the selected folder
- The project binds to that **folder path**; republishing the same folder updates the same site
- Graph / search depend on the Quartz theme you picked

## Tips for this demo vault

- Practice on **`Digital Garden/`** here — leave your real vault alone until you are comfortable
- If wikilinks look broken, check that link targets live **inside** the published folder
- Guest allows only one site — unpublish or claim Free when experimenting with both a note and a folder

## Related

- [[How to publish a single note]]
- [[README]]
- Online: [Publish a folder](https://help.mdfriday.com) · [Digital garden solution](https://mdfriday.com/solutions/digital-garden/)

## Common failures

| Symptom | What to do |
| --- | --- |
| As-is / Faithful unavailable | By design — multi-page needs the Wiki engine |
| Links broken / empty graph | Keep linked notes inside the selected folder |
| Accidental private notes online | Unpublish; next time select a narrower folder |
| Guest site limit | Claim Free or unpublish the previous Guest site |
