---
title: Claim Guest and upgrade
weight: 62
tags: [Guest, Free, Personal]
date: 2026-10-09
lastmod: 2026-10-09
description: Claim a Guest site before the next UTC 00:00 onto Free (same URL, 200 MB), or upgrade to Personal for a domain and 5 GB.
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
3. Storage becomes **200 MB**. You can publish as many sites as that storage allows. The site is not wiped on the 1st of the month, and it is not cleared at the next UTC 00:00. About 6 months without activity may archive it; sign in again to restore. About 30 days after archive, it may be deleted

Sidebar CTA example: **Sign up free**

## Upgrade to Personal

1. Upgrade on the account site (Creem checkout; cancel and invoices under Dashboard “Manage subscription & invoices”)
2. Unlocks: **5 GB** storage, **1 custom domain** (or **3** on the $60/year plan), publish history and rollback
3. Price: **$5/month**, **$50/year** (1 domain), or **$60/year** (3 domains)
4. Sidebar CTA: **Upgrade Personal · domain & more storage**

Protocol callback example: `event=upgrade&status=ok&plan=personal`

## Related

- [[../settings/credentials|mdf key]] (may be needed when switching devices / claiming)
- [[../publish/custom-domain|Custom domain]]
