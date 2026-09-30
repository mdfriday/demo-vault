---
title: Claim Guest and upgrade
weight: 62
tags: [Guest, Free, Personal]
date: 2026-09-19
---

# Claim Guest and upgrade

## Guest first-time human check

1. Sidebar primary button becomes **Verify and publish**
2. Follow instructions to **mdfriday.com** (Guest Challenge) and complete Turnstile
3. Return to Obsidian to continue publishing  
Deep-link protocol: `obsidian://mdfriday-publish?event=…` (verify / claim / upgrade callbacks)

## Claim Free

When a soft-gate appears or you upgrade yourself:

1. Open <https://mdfriday.com/account/> and sign up for free
2. Follow the product flow to **claim** the current Guest site and **keep the same URL**
3. Get higher storage and up to 3 sites (plugin copy); wipe policy becomes the 1st of each month

Sidebar CTA example: **Sign up free · expand to 3 sites**

## Upgrade to Personal

1. Upgrade on the account site (Creem checkout; cancel/invoices under Dashboard “Manage subscription & invoices”)
2. Unlocks: permanent retention, 1 GB, up to 3 custom domains, history rollback
3. Sidebar CTA: **Upgrade Personal · unlimited sites**

Protocol callback example: `event=upgrade&status=ok&plan=personal`

## Related

- [[../settings/credentials|mdf key]] (may be needed when switching devices / claiming)
- [[../publish/custom-domain|Custom domain]]
