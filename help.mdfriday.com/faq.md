---
title: FAQ
weight: 80
tags: [FAQ]
date: 2026-09-19
lastmod: 2026-10-09
description: Short answers on desktop-only install, a publish that fails after preview, Guest sites clearing at the next UTC 00:00, and saving a ZIP.
---

# FAQ

## Install and platform

### Why can’t I use it on phone / iPad?

The plugin sets `isDesktopOnly: true`. Local build and preview need a desktop environment.

### I can’t find it in Community Plugins?

Confirm Restricted Mode is off and you can reach the community plugin list; search **MDFriday Publish** or id `mdfriday-publish`. Or open <https://obsidian.md/plugins?search=mdfriday-publish>.

## Publish and build

### Build failed — what now?

1. Read the Obsidian Notice / panel error text  
2. Try [[publish/local-preview|Local preview]] first to tell build vs upload apart  
3. Simplify attachments and fix broken images  
4. Switch **faithful ↔ themed** and compare  
5. Still stuck → [[troubleshooting|Troubleshooting]] or Discord

### Preview works but publish fails?

Common causes: storage quota, Guest verification incomplete, upload interrupted. Match the red panel error (localized in the UI). Sites are not counted; Guest, Free, and Personal are limited by storage only.

### Attachments / images missing?

Confirm images are inside the selected note or folder scope; avoid relying on absolute OS paths alone. Faithful and themed modes collect assets differently — preview both once.

### Do Chinese paths work?

Usually yes. For rare encoding issues, shorten the path, avoid odd symbols, and verify links in preview.

### Do I need a License to publish?

**No.** Guest publish works without an account. Personal adds a custom domain, **5 GB** storage, and publish history (the last 10 releases). Free is **200 MB** and is kept while you stay active — it is not a paid plan, and it is not wiped the next day.

## Plans and wipe policy

### Guest site gone the next day?

Guest is cleared at the **next UTC 00:00**. [[plans/claim-and-upgrade|Claim Free]] to keep the same URL. After you claim, the site follows Free retention: it stays while you stay active, and about 6 months without activity may archive it.

## Themes and fidelity

### Faithful publish doesn’t match my vault exactly?

Expected: only render that can be staticized ships. Runtime query features like Dataview usually do not survive into a static site.

### Why can’t folders use faithful?

Multi-page + wikilink/graph needs a Wiki engine; the UI disables faithful and explains why.

## Taking a copy of the site

### How do I download the built site?

Preview locally, then click **Export**. That saves a ZIP of the static site. See [[publish/export|Export a ZIP]]. Publishing itself still goes to MDFriday hosting. There is no Netlify or FTP publish path.

### How do I set up Sync?

Out of scope for this plugin’s help. See Sync: <https://mdfriday.com/products/obsidian-sync/>.

## Related

- [[troubleshooting|Troubleshooting]]
- Discord: <https://discord.gg/t7FHJ6qNzT>
