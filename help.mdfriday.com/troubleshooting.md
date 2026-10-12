---
title: Troubleshooting checklist
weight: 90
tags: [troubleshooting]
date: 2026-09-19
lastmod: 2026-10-11
description: A checklist when MDFriday publish fails: desktop setup, preview, Guest verification, storage, and the custom-domain status lines.
---

# Troubleshooting checklist

Work top to bottom; most issues surface in the first few steps.

## A. Environment

- [ ] Obsidian **desktop**, plugin enabled
- [ ] Version ≥ `minAppVersion` (current manifest: **1.8.7**)
- [ ] You can open <https://mdfriday.com> and the share host (production is often `share.mdfriday.com`)

## B. Entry and target

- [ ] You right-clicked the **intended** note or folder
- [ ] Panel “Publish target” path is correct (missing path → file deleted/moved)
- [ ] Do not hard-switch file vs folder types inside the same project (older copy asks you to clear and reselect)

## C. Preview

- [ ] Click **Preview** to see whether build fails or only upload fails
- [ ] Does localhost open? If not → port / permissions
- [ ] Blank page → switch mode (faithful/themed), remove suspicious plugin syntax, check images

## D. Guest verification

- [ ] Stuck on **Verify and publish**?
- [ ] Did you finish Turnstile in the browser and **return to Obsidian**?
- [ ] Is the protocol callback blocked (`obsidian://mdfriday-publish?...`)?

## E. Quotas

- [ ] Sites are not counted. Guest, Free, and Personal are limited by storage only
- [ ] Storage: Guest **5 MB** (enough to try one note) / Free **200 MB** / Personal **5 GB** — over quota blocks new publishes; live sites stay up
- [ ] Retention: Guest clears at the next UTC 00:00. Free is not wiped on the 1st of the month. A Free site that disappears after about 6 months of inactivity was archived, not lost — sign in to restore it. About 30 days after archive, it may be deleted

## F. Domain (Personal)

Match the panel text. Details are on [[publish/custom-domain|Custom domain]].

- [ ] **Verify first** — sign in
- [ ] **Publish to bind** — this project has one successful publish
- [ ] **Upgrade to use** — the account is Personal
- [ ] Host is the short name from the table, not `www.example.com.example.com`
- [ ] The ownership TXT is the Host cell from the table (it starts with `_mdfriday-verify`). Later, the HTTPS row replaces any TXT on that same host
- [ ] Cloudflare DNS is grey-cloud, not Flexible SSL
- [ ] **Misconfigured** — refresh after DNS has had a few minutes
- [ ] Status **Active**, then you published **once more**
- [ ] **Paused: renew to restore** — the plan no longer includes this extra domain

## G. Credentials

- [ ] Settings already has an mdf key; after switching machines you may need to reclaim/import (follow the account site)

## Still stuck

1. Copy the full panel error text  
2. Note: note vs folder, mode, plan tier, whether preview succeeded  
3. Discord: <https://discord.gg/t7FHJ6qNzT>  
4. Or the website contact entry (footer email / about page)

## Related

- [[faq|FAQ]]
- [[plans/guest-free-personal|Plans]]
- [[publish/right-panel|Right panel]]
