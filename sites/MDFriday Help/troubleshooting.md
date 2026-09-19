---
title: Troubleshooting checklist
weight: 90
tags: [troubleshooting]
date: 2026-09-19
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

- [ ] Site count: Guest 1 / Free 3 / Personal unlimited (plugin copy)
- [ ] Storage: 5 MB / 50 MB / 1 GB — overage blocks new publishes
- [ ] Wipe policy: Guest daily (UTC); Free on the 1st of each month — do not mistake this for a “lost data” bug

## F. Domain (Personal)

- [ ] Authenticated + published at least once
- [ ] DNS **short hostname** filled correctly
- [ ] Clicked verify / refresh status; HTTPS records complete

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
