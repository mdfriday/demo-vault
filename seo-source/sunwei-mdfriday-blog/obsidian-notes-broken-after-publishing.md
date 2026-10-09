---
title: "Obsidian Notes Broken After Publishing? What to Check First"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - rendering
  - troubleshooting
description: "Obsidian notes broken after publishing? Why Dataview, Canvas, math and callouts look different online, and a 15-minute fidelity test to run first."
---

# Obsidian Notes Broken After Publishing? What to Check First

It looks perfect in Obsidian. You publish, open the link, and half the page is wrong: a Dataview query shows up as raw code, the Canvas is missing, an equation runs off the edge of your phone screen.

> “I was initially dismayed that plugins generally don't render in Publish.” — [Reddit r/ObsidianMD, 2025](https://www.reddit.com/r/ObsidianMD/comments/1nh8730/obsidian_publish_my_journey_resources)

> “I rely on dataview too much for it not to be included in Quartz.” — [YouTube comment, ~2025](https://www.youtube.com/watch?v=6s6DT1yN4dw)

> “Just deployed but LateX code(equations) are not working on website.” — [YouTube comment, ~2022](https://www.youtube.com/watch?v=kg-9n_A4Tf0)

This was the fastest-growing complaint in my research ([[mdfriday/voice-of-custom/rendering-fidelity|rendering fidelity]]). The worst version is finding out *after* paying: one user subscribed to a publishing plan, discovered Canvas couldn't be published, and asked for a refund the same week.

So before you pick any tool, including mine, here's why it happens and how to test for it in about fifteen minutes.

## Why your notes break: they aren't really "just Markdown"

Obsidian is a Markdown editor, but over the years most of us have put a lot more than Markdown into our notes:

- **Queries** (Dataview, Bases) that are computed live inside the app
- **Canvases and drawings** (Canvas, Excalidraw) stored in their own formats
- **Math** (LaTeX), sometimes with custom preambles
- **Callouts**, including custom callout types from CSS snippets
- **Embeds**: other notes, PDFs, YouTube, iframes
- **Plugin styling**: coloured text, statblocks, infoboxes

To you, these *are* the content. To a publishing tool, many of them are instructions that only Obsidian, with your plugins installed, knows how to run. Obsidian Publish doesn't run community plugins. Quartz doesn't support Dataview. Digital Garden plugin users report Dataview images and links breaking. Every tool draws the line somewhere different, and the line is rarely on the feature page.

## The 15-minute fidelity test

Don't test your tool with your simplest note. Test it with your hardest.

**1. Build a test note (5 minutes).** Create `fidelity-test.md` containing one of each element you actually use:

- a callout, and a custom callout if you use them
- a short equation and a *long* one
- a footnote
- an embedded note and an embedded image
- a Dataview or Bases query, if you use them
- a Canvas or Excalidraw embed, if you use them
- a table, a task list and a code block
- any plugin-specific syntax your notes depend on

**2. Publish it with each tool you're considering (5 minutes).**

**3. Check it on two screens (5 minutes).** Look on desktop and on a phone. Long equations and wide tables often break only on mobile. Write down what renders, what degrades, and what disappears.

That list is your real feature comparison, specific to your notes, which beats any marketing table (mine included).

## If something you rely on doesn't render

You have a few workarounds, whatever tool you use:

- **Dataview or Bases:** for pages readers will see, paste a static snapshot of the result (a plain Markdown table) into a published note, and keep the live query in your private notes.
- **Canvas or Excalidraw:** export an image or SVG and embed that. You lose interactivity but keep the picture.
- **Long equations:** break them across lines, or check that your theme allows horizontal scrolling.
- **Custom styling:** accept that some purely visual plugins won't travel, or pick a theme that gets close.

It's extra work, so do the test *before* you commit your time or money.

## What I'm aiming for with MDFriday's AS mode

When I started MDFriday Publish, "what I see in Obsidian is what readers see" was the goal I cared most about. That's what **AS mode** is: it renders pages to look like your Obsidian notes, rather than forcing them into a generic blog template.

What that means for you:

- **Less double maintenance.** You don't keep one version for Obsidian and another for the web.
- **Proofreading happens where you write.** If it reads well in Obsidian, you're most of the way there.
- **Themes when you want them.** You can switch to one of several themes if you'd rather have a different look than your vault's.

And here's the honest part. I'm not going to claim support for Dataview, Bases, Canvas or Excalidraw in this post. If those are central to your notes, run the fidelity test above with MDFriday before anything else. That's exactly what the no-account Guest mode is for. I'd much rather you find a gap in five minutes for free than after paying.

## Run the test on MDFriday

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Right-click your `fidelity-test` note and publish it.
3. Check it on desktop and on your phone.

No account is needed for Guest. **Guest content is cleared at the next UTC midnight**, so the test cleans up after itself. The Free plan (3 sites, 50 MB) is also temporary and is cleared on the 1st of each month. Personal (about \$5–6/month, 1 GB) is the permanent option. Your notes stay in your vault either way. The only thing you risk is fifteen minutes.

## Further reading

- [[mdfriday/blog/obsidian-website-themes-without-css|Obsidian Website Themes: Look Good Without Writing CSS]]
- [[mdfriday/blog/is-obsidian-publish-worth-it|Is Obsidian Publish Worth It? An Honest Look]]
- [[mdfriday/blog/quartz-vs-obsidian-publish-vs-digital-garden|Quartz vs Obsidian Publish vs Digital Garden: Which Fits?]]
- Research notes: [[mdfriday/voice-of-custom/rendering-fidelity|Rendering fidelity]] · [[mdfriday/voice-of-custom/export-beyond-the-web|Export beyond the web]]
