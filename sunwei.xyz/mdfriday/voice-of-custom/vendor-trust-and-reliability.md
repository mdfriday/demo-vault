---
title: Vendor Trust & Reliability
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "When a hosted service fails, users can't tell whether the problem is theirs or the platform's; Chinese users who have seen image hosts vanish and hosting shut down are wary of keeping content on someone else's platform."
---

# Vendor Trust & Reliability

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

When a hosted service fails, users have no idea whether they misconfigured something or the platform is down, because there's no status page; intermittent outages make people doubt whether the platform is reliable. Chinese users' experience is more concrete: image hosts that "ran off" and free static hosts shut down one after another because of content censorship, so people are generally uneasy about keeping their content on someone else's platform. This differs from [[maintenance-burden|abandoned open-source tools]]: it's about whether the **hosted service itself** works and survives.

> [!info] Signal (approximate)
> ~6 web supplement sources; latest evidence 2026-03.
> Relevance to MDFriday: **high** (MDFriday is a small vendor, and Guest / Free are cleared periodically).

## Voices

- “I tried to find information about whether or not it was down, or if I had done something wrong – but I couldn’t find such a thing.” — Obsidian Forum · 2024-08-24 · <https://forum.obsidian.md/t/status-webpage-indicating-server-issues-and-uptime/87354>
- “the intermittent outages seem like either a sign that Obsidian Publish’s hosting servers are on fire” — Obsidian Forum · 2022-11-04 · <https://forum.obsidian.md/t/obsidian-publish-site-connection-is-not-private-warning/46975>
- 「用别家图床多少会担心跑路的问题」 — Obsidian Chinese forum · 2026-03-29 · <https://forum-zh.obsidian.md/t/topic/60004>
  - *Translation:* Using someone else's image host, you always worry a bit that it will just run off one day.
- 「用别人的就跟租房一样」 — Obsidian Chinese forum · 2023-03-17 · <https://forum-zh.obsidian.md/t/topic/16887>
  - *Translation:* Using someone else's is just like renting a place.
- 「早两年其实有很多静态托管服务的，后来慢慢都因为内容审查关闭了。」 — V2EX · 2024-02-23 · <https://www.v2ex.com/t/1017853>
  - *Translation:* A couple of years ago there were actually lots of static hosting services; later they gradually all shut down because of content censorship.

## Why it hurts

- **Trust is the precondition for a hosted service.** Users put years of knowledge on it, and what they fear most is that one day it won't open, or the platform will disappear.
- **Uncertainty during an outage is worse than the outage itself.** If you don't know whose problem it is, you don't know whether to wait or to fix.
- **Small vendors naturally have one more thing to prove.** A big platform's survival is assumed; a small vendor's has to be argued for.

## How people cope today

- Choosing big platforms, or self-hosting (see the ownership demand in [[pricing-and-lock-in|Pricing & Lock-in]]).
- Keeping a full local copy, ready to move at any time.
- Chinese users tend to set up their own object storage or choose services from large domestic providers.

## MDFriday's response

- **Source notes always stay local**, and the website can be regenerated at any time with a right-click. That's the built-in reassurance of a local build, and it's worth spelling out in the copy.
- **The clearing rules must be explained clearly**: Guest is cleared at the next UTC midnight, Free on the 1st of each month, and Personal is kept permanently. If the two trial tiers aren't explained, they'll collide head-on with the fear that the vendor will vanish or content will be lost.
- A public status page **(unconfirmed)**; exporting static files for self-hosting, as a promise that "even if we're gone, your site is still there" **(unconfirmed)**.

## Open questions

- On the publish-success page and in emails, can users clearly see whether and when their site will be cleared?
- When Cloudflare has a regional outage, how does MDFriday tell users?
- Could a public, steady maintenance rhythm (changelog, releases) increase trust?

## Related

- [[maintenance-burden|Maintenance Burden]]
- [[pricing-and-lock-in|Pricing & Lock-in]]
- [[single-note-sharing|Single-note Sharing]]
- [[chinese-community-voices|Chinese Community Voices]]
