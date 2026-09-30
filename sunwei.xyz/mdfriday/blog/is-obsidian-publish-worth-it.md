---
title: "Is Obsidian Publish Worth It? An Honest Look at the Price"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - obsidian-publish
  - pricing
description: "Is Obsidian Publish worth it? A fair look at what you get, where users say it falls short, and a checklist to decide before you pay for a year."
---

# Is Obsidian Publish Worth It? An Honest Look at the Price

It feels odd for someone who builds a competing tool to write this post. But "is Obsidian Publish worth it?" is a question that comes up again and again, and they deserve a straight answer instead of a sales page. For a lot of people, the answer is yes. For some, it's clearly no. Here's how to tell which group you're in.

## What you actually get

Let's start with the case for Publish, because it's a good one:

- **It's official.** It's made by the Obsidian team and designed around Obsidian's own features. You're not relying on a volunteer's side project.
- **No technical setup.** No Git, no GitHub, no terminal, no hosting account. You pick notes and click publish.
- **Garden features built in.** A graph view, site search and navigation come out of the box.
- **Room for media.** 4 GB of storage per site.
- **You fund Obsidian.** Some users pay for exactly this reason. One commenter who gave up on a free setup wrote: “Ah too complicated. I paid.”

If your notes are mostly plain Markdown and the price doesn't sting, you can stop reading here. It's a solid product.

## Where users say it falls short

From the forum threads, Reddit posts and YouTube comments I went through ([[mdfriday/voice-of-custom/pricing-and-lock-in|pricing and lock-in]]), five complaints come up again and again.

**1. The price adds up.** Publish is roughly \$8–10 per site per month depending on billing, charged separately from Sync. For a personal site that earns nothing, many people can't justify it.

> “People don’t like being nickled-and-dimed.” — [Obsidian forum, 2025](https://forum.obsidian.md/t/your-pricing-model-needs-work/96575)

**2. Community plugins don't render.** If Dataview, Canvas or other plugins shape your notes, those parts won't look the same online. The painful version is finding out after you've paid:

> “I subscribed… Canvas can't be published… Can I be refunded” — [Obsidian forum, 2026](https://forum.obsidian.md/t/just-subscribed-to-publish-plan-canvas-cant-be-published-can-i-be-refunded-5-after-subscribing/110890)

**3. Custom domains can be fiddly.** Connecting your own domain goes through Cloudflare or a reverse proxy, and misconfiguration causes redirect loops and errors ([[mdfriday/voice-of-custom/custom-domains|custom domains]]).

> “This turned a 5 minute job into an hours long nightmare.” — [Obsidian forum, 2024](https://forum.obsidian.md/t/cannot-get-obsidian-publish-to-work-with-a-custom-domain/75546)

**4. Access control is all or nothing.** A password protects the whole site, which rules out a public landing page with a private section ([[mdfriday/voice-of-custom/access-control-and-collaboration|access control]]). Collaborators have also asked for finer-grained permissions.

**5. Privacy edges.** Users have reported links in comments appearing in the public graph and hidden notes showing up in site search. If you share a vault with private material, test carefully.

None of these are dealbreakers for everyone. They're the reasons some people start searching for alternatives.

## A checklist before you pay for a year

Answer these honestly:

1. **Is my content mostly core Markdown** (text, images, wikilinks, callouts)? Yes points toward Publish.
2. **Do I rely on community plugins** for key pages? If so, test those pages before subscribing, with any tool.
3. **Will I publish more than one site?** Per-site pricing multiplies.
4. **Do I need my own domain on day one?** Budget an hour for DNS, or ask the community for help first.
5. **Do I need private sections or per-person access?** Publish's model is whole-site.
6. **Would I rather pay money than spend time?** If yes, Publish, or another paid tool, beats a free DIY setup.
7. **Am I comfortable with my notes on Obsidian's servers?** Some people aren't. One user put it simply: “I don't want my files to be on the Obsidian servers”.

If you answered mostly in Publish's favour, subscribe with a clear conscience. If not, keep reading.

## When it isn't worth it, what then?

If price or model is the problem but you still don't want Git, you have a few routes, which I compare in [[mdfriday/blog/obsidian-publish-alternatives|Obsidian Publish Alternatives: 6 Honest Options Compared]]. Here's the one I built, described the way I'd want a competitor described.

**MDFriday Publish** is an Obsidian plugin. You right-click a note or folder and publish it.

- **Lower monthly cost.** Personal is about \$5–6 a month. So a small personal site costs less to keep online.
- **Your vault stays with you.** The build runs on your computer, and only the notes you choose are uploaded. So there's no copy of your whole vault on anyone's server.
- **No Git, GitHub, terminal or tokens.** So setup is the same "click publish" feeling as Publish.
- **AS mode.** Pages render to look like your Obsidian notes, so what you proofread is what readers see.
- **Several switchable themes.** So you can change the look without touching CSS.
- **Served from Cloudflare's CDN.** So you don't need a hosting account.

**Where it's weaker, honestly:** Personal includes 1 GB, a quarter of Publish's 4 GB. It's a small, founder-run product rather than the official one. And I'm not claiming support for Dataview, Canvas or Excalidraw. Test those notes first. I'm also not going to promise custom domains or password-protected pages in this post. If either is a must-have, check the current plan details before you decide.

## Try before you commit to anything

Whichever way you lean, test with your own notes before paying for a year.

For MDFriday: open **Settings → Community plugins** in Obsidian, search for **MDFriday Publish**, and install it (<https://obsidian.md/plugins?search=mdfriday-publish>). Right-click your most complex note and publish it. Guest mode needs no account. **Guest content is cleared at the next UTC midnight, and the Free plan (3 sites, 50 MB) is cleared on the 1st of each month**, so treat both as a test drive. Personal is the plan that keeps your site permanently.

If it turns out Publish is the better fit, you've lost nothing, and you'll subscribe knowing exactly what you're paying for.

## Further reading

- [[mdfriday/blog/free-obsidian-publish-alternative|Free Obsidian Publish Alternative? What Free Really Costs]]
- [[mdfriday/blog/quartz-vs-obsidian-publish-vs-digital-garden|Quartz vs Obsidian Publish vs Digital Garden: Which Fits?]]
- [[mdfriday/blog/obsidian-notes-broken-after-publishing|Obsidian Notes Broken After Publishing? What to Check First]]
- Research notes: [[mdfriday/voice-of-custom/pricing-and-lock-in|Pricing & lock-in]] · [[mdfriday/voice-of-custom/custom-domains|Custom domains]] · [[mdfriday/voice-of-custom/access-control-and-collaboration|Access control & collaboration]]
