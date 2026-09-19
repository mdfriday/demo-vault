---
title: Custom domain
weight: 38
tags: [domain, Personal]
date: 2026-09-19
---

# Custom domain

## Goal

Bind a published site to your own domain (e.g. `www.example.com`) with HTTPS.

## Prerequisites

- **Personal** plan (Guest / Free are locked in the UI)
- Account authenticated, and the project has **published successfully at least once**
- You can edit DNS for that domain
- Personal quota: **up to 3** custom domains (product copy)

## Steps (panel wizard)

1. Publish tab → **Advanced** → **Custom domain**
2. **Step 1**: enter the hostname (e.g. `www.example.com`) → Next
3. **Step 2**: add the records shown in the table in your DNS console  
   - Host record uses the **short name** (do not re-append the apex, or you get `…example.com.example.com`)
   - After DNS propagates, click **“I’ve added the records — start verification”**
4. **Step 3**: add the HTTPS-related records as prompted; use **Refresh status** / **Keep checking**
5. Once binding is active, **publish once more** so the domain serves the site

<!-- MEDIA: screenshot — domain DNS table -->
![Placeholder: custom domain wizard](../images/placeholder-custom-domain.png)

## Confirm success

- Status pill: **Active**
- Browser opens your domain with HTTPS

## Unbind

Use **Unbind**: the site falls back to the share link; certificates may be kept so you can rebind to another project later. If the domain is already bound elsewhere, unbind it there first.

## Related

- [[../plans/guest-free-personal|Plan comparison]]
- [[../plans/claim-and-upgrade|Upgrade to Personal]]
- Pricing: <https://mdfriday.com/pricing/>

## Common failures

| Status copy | Meaning |
| --- | --- |
| Authenticate first | Finish account-side authentication |
| Available after publish | Publish successfully once first |
| Available after upgrade | Not on Personal yet |
| Waiting / misconfigured | Check DNS host records and verify TXT/CNAME; click refresh status |
