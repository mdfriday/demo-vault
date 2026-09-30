---
title: Install and first publish
weight: 10
tags: [getting-started, install, Guest]
date: 2026-09-19
---

# Install and first publish

## Goal

Install **MDFriday Publish** in Obsidian desktop and publish a note via the **Guest (no account)** path to get a shareable public link.

## Prerequisites

- Obsidian desktop (the plugin is **desktop-only**; see `minAppVersion` in `manifest.json`, currently **1.8.7**)
- Outbound internet (first Guest publish may require a browser human check)
- One Markdown note, or a folder you are ready to make public

## Steps

### 1. Install the plugin

1. Open **Settings → Community plugins** and turn off Restricted Mode if needed
2. Browse / search **MDFriday Publish** (id: `mdfriday-publish`)
3. Install and **enable** it

You can also jump from: <https://obsidian.md/plugins?search=mdfriday-publish>

<!-- MEDIA: screenshot — Community Plugins search for MDFriday Publish -->
![Placeholder: install plugin](images/placeholder-install-plugin.png)

### 2. Open the right-hand publish panel

Pick any of these:

- **Right-click** a note or folder → **“Open in MDFriday”** (opens the config panel only; does not publish yet)
- **Right-click** → **“Publish to MDFriday”** (opens the panel and starts the publish flow)
- Command palette: **“Quick share”** or **“Publish to MDFriday”**

The **MDFriday** sidebar appears on the right (Publish | History).

<!-- MEDIA: screenshot — right-click menu “Publish to MDFriday” -->
![Placeholder: publish menu](images/placeholder-publish-menu.png)

### 3. First Guest publish (no account)

1. Confirm the publish target is the current note / folder
2. A single note usually defaults to **faithful publish**; a folder is always **Wiki publish** (see [[publish/modes|Publish modes]])
3. Optional: click **Preview** to check the result in a local browser first ([[publish/local-preview|Local preview]])
4. Click **Publish**. For Guest users who have not verified yet, the button may say **“Verify and publish”**
5. Follow the prompt to **mdfriday.com**, complete the Turnstile human check, then return to Obsidian
6. On success, copy the public URL and share it

<!-- MEDIA: video — one-click publish demo -->
![Placeholder: publish demo video](videos/placeholder-publish-demo.md)

> [!info] Credential is issued automatically
> The first publish automatically creates an **mdf key** (Guest or later user credential). You can view / copy it in Settings for account claim or device switches. See [[settings/credentials|Credential (mdf key)]].

## Confirm success

- The panel shows **“Published successfully”** with an openable / copyable URL (production share hosts are typically `https://share.mdfriday.com/...`)
- Project status becomes **Published**
- Guest: content is cleared at the **next UTC 00:00** (claim Free to keep the same URL) — see [[plans/guest-free-personal|Guest / Free / Personal]]

## Related

- [[publish/publish-note|Publish a note]]
- [[publish/publish-folder|Publish a folder]]
- [[plans/claim-and-upgrade|Claim Guest and upgrade]]
- [[troubleshooting|Troubleshooting]]

## Common failures

| Symptom | Likely cause | See |
| --- | --- | --- |
| No plugin capability on mobile | Desktop only | [[faq\|FAQ · desktop]] |
| Stuck on “Verify and publish” | Turnstile not finished or you did not return to Obsidian | [[troubleshooting\|Troubleshooting]] |
| Publish failed · site limit | Guest allows **1** site (plugin copy wins) | [[plans/guest-free-personal\|Plans]] |
| Blank preview / build failed | Attachment paths, theme, port in use, etc. | [[faq\|FAQ]] · [[troubleshooting\|Troubleshooting]] |
