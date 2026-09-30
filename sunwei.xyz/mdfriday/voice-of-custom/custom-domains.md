---
title: Custom Domains
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "A custom domain should take 5 minutes, but it often turns into hours of DNS, proxy and SSL nightmares."
---

# Custom Domains

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Custom domains on Obsidian Publish depend on a Cloudflare proxy or a self-hosted reverse proxy. Users run into redirect loops, Error 1014, the vault name showing up in URLs behind an Nginx or Netlify proxy, CNAMEs on the root domain, and more. Students even assume they have to buy a paid Cloudflare plan. Some people cancel outright because they can't get the domain working. The most common YouTube questions are more basic: is a domain included in the service? How do I connect it? How long does DNS take to propagate?

> [!info] Signal (approximate)
> ~25 VOC cards · ~8 YouTube comments.
> Ranked **#10**: "a 5-minute job turned into an hours-long nightmare".

## Voices

- “This turned a 5 minute job into an hours long nightmare.” — Obsidian Forum · 2024-01-23 · <https://forum.obsidian.md/t/cannot-get-obsidian-publish-to-work-with-a-custom-domain/75546>
- “which is way beyond my student budget” — Obsidian Forum · 2021-01-21 · <https://forum.obsidian.md/t/alternatives-to-cloudfare-for-custom-domain-publish/11766>
- “I can't figure out how to "connect" it to Obsidian Publish.” — YouTube comment · ~2025 · <https://www.youtube.com/watch?v=7f8e5IiUkeo>
- “Is the customdomain name included in the service ?” — YouTube comment · ~2025 · <https://www.youtube.com/watch?v=1pf6aj3Uwuk>

## Why it hurts

- **Your own domain = your own brand and ownership.** Publishing on a subdomain always makes the site feel "borrowed".
- **DNS and SSL are the hardest layer to understand.** When something goes wrong there's hardly ever a readable message, and it's hard to tell whether the registrar, the CDN or the platform is at fault.
- **If it doesn't work, people cancel.** This step leads directly to churn.

## How people cope today

- Working through Cloudflare configuration threads on the forum step by step; pick the wrong SSL mode (Full / Flexible) and you get a redirect loop.
- Running their own Nginx reverse proxy, or giving up on a custom domain.
- Chinese users also have to think about ICP filing; see [[chinese-community-voices|Chinese Community Voices]].

## MDFriday's response

- Whether custom domains are supported, how many Personal includes, and whether SSL is issued automatically: **(unconfirmed)** (an earlier showcase draft said "Personal includes up to 3 custom domains"; check against the current product before saying it publicly).
- If it can be "enter the domain → add one DNS record as prompted → automatic SSL", that would be a very strong point in comparisons with Publish.

## Open questions

- What exactly is the custom-domain capability of the current Personal plan?
- Can ICP-filed domains use a domestic route? See [[mainland-china-access|Mainland China Access]].
- When setup fails, could there be a self-check page (has DNS propagated, has the certificate been issued)?

## Related

- [[setup-and-deploy-barrier|Setup & Deploy Barrier]]
- [[mainland-china-access|Mainland China Access]]
- [[stable-links-and-redirects|Stable Links & Redirects]]
