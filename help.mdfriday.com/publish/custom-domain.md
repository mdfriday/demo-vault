---
title: Custom domain in MDFriday
weight: 38
tags: [domain, Personal]
date: 2026-09-19
lastmod: 2026-10-11
description: Bind a Personal site to your own hostname. Copy the DNS table from the panel, wait until Active, then publish once more.
---

# Custom domain in MDFriday

Applies to plugin **v26.10.2**.

## Goal

Serve a site you already published at your own hostname, with HTTPS. Example: `www.example.com`.

Use a **name in front of the root**, such as `www` or `notes`. The panel asks for that on purpose. A bare root (`example.com`) often cannot use the CNAME this wizard shows.

## Prerequisites

- **Personal**. Guest and Free show **Upgrade to use**
- You are signed in. Otherwise the panel says **Verify first**
- This project has **published successfully once**. Otherwise it says **Publish to bind**
- You can edit DNS for that hostname
- Quota: **1** domain on the $5/month plan and the $50/year plan. **3** on the $60/year plan. If you later drop to a smaller quota, the earliest domains stay and the extra ones show **Paused: renew to restore**
- HTTPS is issued for you. You do not buy a certificate

MDFriday does not file an ICP record and does not offer a mainland-China route.

## Steps

1. Publish tab → **Advanced** → **Custom domain**
2. **Step 1.** Enter the hostname (`www.example.com`) → **Next**
3. **Step 2.** Open your DNS host and add **every row** in the table. Copy Host and Value. Do not invent them
   - One row is a **CNAME**. The panel marks it **Points visitors to MDFriday**
   - One row is a **TXT** whose name starts with `_mdfriday-verify`. The panel marks it **Proves you own this domain**. Copy the Host cell; for `www.example.com` that short name is not just `_mdfriday-verify`
   - Host is the **short name**. If the panel already knows `example.com`, pasting the full name again creates `www.example.com.example.com`
   - Paste a full hostname only when that DNS form says it wants the complete name
4. Wait a few minutes. Click **I've added them — verify**
5. **Step 3.** Add the HTTPS rows the panel shows (**Enables secure HTTPS**). If you previously put a TXT on that same host, **delete the TXT and keep only this CNAME**
6. Click **Refresh status**, or **Keep checking (about 6 min)**, until the pill says **Active**. An empty HTTPS table means Cloudflare has not returned the challenge yet. Refresh. That wait is normal
7. **Publish once more.** The panel says to do this when the domain is done. This publish serves the site at the domain root and records your domain as the public host. Skip it and the domain can still be empty or on the old path
8. Open `https://www.example.com/`. Do not judge success from the share link alone

<!-- MEDIA: screenshot — domain wizard DNS table, then Active, then the site on the custom domain -->

## Confirm success

- Status is **Active**
- The hostname opens over HTTPS and shows this site
- The old share link **301-redirects** to the same path on your domain. That is expected. The site was not deleted
- `https://your-domain/sitemap.xml` lists absolute URLs on your domain. See [[../reference/seo|Sitemap and canonical URL]]

## If your DNS is Cloudflare

Create the records as **DNS only** (grey cloud). An orange-cloud proxy, or SSL set to **Flexible**, commonly loops or breaks the certificate. The certificate is issued on MDFriday's side. Your DNS only has to answer the rows in the table.

## Unbind

**Unbind** returns this project to the share link. The certificate is kept so you can bind the hostname to another project later. If the panel says the domain is bound to another site, unbind it there first.

## Related

- [[../plans/guest-free-personal|Plan comparison]]
- [[../plans/claim-and-upgrade|Upgrade to Personal]]
- [[update-site|Update a published site]]
- Pricing: <https://mdfriday.com/pricing/>

## Common failures

| What the panel says | What to do |
| --- | --- |
| **Verify first** | Sign in, then publish once |
| **Publish to bind** | Publish this project once on the share link |
| **Upgrade to use** | The account is not Personal |
| **Misconfigured** | Compare Host and Value with the table. Check the short-name mistake. Click **Refresh status** |
| **Paused: renew to restore** | The plan no longer includes this extra domain. Renew or remove it |
| Bound to another project | Unbind it on that project first |
| HTTPS table stays empty | Wait, then **Refresh status**. Do not add a guessed record |
| Redirect loop on Cloudflare | Set the record to DNS only. Do not use Flexible SSL |
| Domain opens but the site is missing or the sitemap has no host | Status was not **Active** yet, or you did not **publish once more** after it was |
