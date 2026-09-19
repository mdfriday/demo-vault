---
title: FAQ
weight: 80
tags: [FAQ]
date: 2026-09-19
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

Common causes: quotas (sites/storage), Guest verification incomplete, upload interrupted. Match the red panel error: site limit / storage full, etc. (localized in the UI).

### Attachments / images missing?

Confirm images are inside the selected note or folder scope; avoid relying on absolute OS paths alone. Faithful and themed modes collect assets differently — preview both once.

### Do Chinese paths work?

Usually yes. For rare encoding issues, shorten the path, avoid odd symbols, and verify links in preview.

### Do I need a License to publish?

**No.** Guest Cloudflare publish is a no-account path; LicenseState can skip init in Cloudflare guest mode. Paid value is mainly Personal features: domain / permanent retention / history.

## Plans and wipe policy

### Guest site gone the next day?

Guest is wiped at the **next UTC 00:00**. [[plans/claim-and-upgrade|Claim Free]] to keep the URL, or upgrade to Personal for permanent retention.

### Site says “unlimited sites” on the website, but the plugin says Guest only gets 1?

Trust the **plugin errors and plan cards** (see [[plans/_index|Plans]]). If marketing copy lags, the UI of the plugin version you installed wins.

## Themes and fidelity

### Faithful publish doesn’t match my vault exactly?

Expected: only render that can be staticized ships. Runtime query features like Dataview usually do not survive into a static site.

### Why can’t folders use faithful?

Multi-page + wikilink/graph needs a Wiki engine; the UI disables faithful and explains why.

## Legacy features

### Are Netlify / FTP / “export static package” still supported?

Current publish type is **Cloudflare**. The README lists Netlify/FTP as legacy. This help does not teach them as the main flow. If an old Foundry project still has leftover config, treat it as advanced/legacy — only if the panel still exposes those entries (the new Publish panel centers on CF share links).

### How do I set up Sync?

Out of scope for this plugin’s help. See Sync: <https://mdfriday.com/products/obsidian-sync/>.

## Related

- [[troubleshooting|Troubleshooting]]
- Discord: <https://discord.gg/t7FHJ6qNzT>
