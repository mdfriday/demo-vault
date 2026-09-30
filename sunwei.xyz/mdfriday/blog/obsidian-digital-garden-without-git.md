---
title: "Obsidian Digital Garden: How to Grow One Without Git"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - digital-garden
  - how-to
description: "Build an Obsidian digital garden without Git: pick a folder, add hub notes, link with care, and publish with a right-click. A practical, tool-agnostic guide."
---

# Obsidian Digital Garden: How to Grow One Without Git

A blog is a timeline: you write a post, and it sinks under the next one. A digital garden is a map: notes link to each other and keep changing as your thinking grows. That idea is why the most-watched videos about Obsidian publishing aren't tutorials at all. They're about gardening your ideas in public.

Then you try to plant one, and the first instruction is "fork this repository".

Here's what people who want a garden actually ask for:

> “takes a folder of Markdown files with wiki links and generates HTML files” — [Hacker News, 2021](https://news.ycombinator.com/item?id=29126212)

> “is there a way to get something similar to the left-sidebar file navigation that we see in Obsidian Publish?” — [YouTube comment, ~2022](https://www.youtube.com/watch?v=ITiiuBNVue0)

> “How do you control the structure of the navigation pane ?” — [YouTube comment, ~2025](https://www.youtube.com/watch?v=7f8e5IiUkeo)

A folder of linked notes in, a site that feels like your vault out. That's the whole wish ([[mdfriday/voice-of-custom/knowledge-structure-on-the-web|knowledge structure on the web]]). This guide gets you most of the way with any tool, then shows the no-Git route I use.

## Step 1: Give your garden its own folder

Don't try to publish your whole vault. Create one folder, say `garden/`, and treat it as the boundary between public and private. Everything inside may be read by strangers. Everything outside stays yours.

This one decision solves most privacy worries before they start. It also works with every publishing tool, from Obsidian Publish to Quartz to MDFriday. (For more on this, see [[mdfriday/blog/publish-part-of-obsidian-vault|Publish Part of Your Obsidian Vault]].)

## Step 2: Plant a few hub notes

Readers need a way in. Before worrying about graph views or sidebars, write three to five **hub notes** (some people call them maps of content):

- an `index` note that says who you are and where to start
- one hub per big topic, listing and briefly describing the notes under it
- optionally a "now" or "recently tended" note

Hub notes are the most reliable navigation there is. They work in every tool and every theme, on mobile and on slow connections. Features like graph views are lovely extras, but a well-written hub note does more for a first-time reader.

## Step 3: Link generously, but inside the fence

Links are what make a garden a garden. Link freely between notes inside `garden/`.

Be careful with links that point *outside* the folder. Different tools handle them differently. Some show plain text, some show a broken link, and some can reveal the title of a private note. Before you publish, search your garden folder for links to notes outside it and decide on each one: move the target in, or remove the link.

## Step 4: Label how finished each note is

Gardens are allowed to be messy, as long as you're honest about it. Add a simple status at the top of each note:

- 🌱 **Seedling**: rough idea, likely to change
- 🌿 **Budding**: taking shape
- 🌳 **Evergreen**: stable, worth citing

This takes the perfectionism out of publishing. You can share half-formed thoughts without pretending they're essays.

## Step 5: Choose how you'll publish it

Here are your realistic options:

- **Quartz.** Free, open source, and arguably the prettiest garden out there, with a graph view, backlinks and callouts that feel close to Obsidian. It requires Node, Git and GitHub. If you're comfortable with those, it's a great choice.
- **The Digital Garden plugin.** Free, and you start inside Obsidian, but you connect GitHub and Vercel or Netlify once.
- **Obsidian Publish.** Official, no Git, and graph and search built in. It's paid per site.
- **MDFriday Publish.** No Git, and you right-click the folder.

If you're weighing the first three, [[mdfriday/blog/quartz-vs-obsidian-publish-vs-digital-garden|Quartz vs Obsidian Publish vs Digital Garden]] goes deeper.

## The no-Git way: right-click the folder

This is the route I built MDFriday Publish for, and the one I use myself. This site, sunwei.xyz, is published from an Obsidian folder with MDFriday.

- **Right-click your `garden/` folder and publish.** So your garden goes online without a repository, a token or a terminal.
- **Selective publish.** Only that folder goes public. So your journal, drafts and client notes stay where they are.
- **The build runs on your computer.** Your vault stays on your machine, and only the chosen notes are uploaded. So there's no copy of your vault sitting in a Git repo.
- **AS mode.** Pages render to look like your Obsidian notes. So the garden your readers wander through looks like the one you tend.
- **Several switchable themes.** So you can try a different look for your garden without writing CSS.
- **Cloudflare CDN.** So pages are served from a global network without you configuring hosting.

To be straight with you: every tool treats links, navigation and plugin output a little differently, and I'd rather you check than take my word for it. Publish your garden folder, click through your hub notes and a dozen links, and open it on your phone. If your garden depends on Dataview or Canvas, test those notes specifically.

## Tending: the part that makes it a garden

A garden isn't a launch. It's a habit. After you edit notes in Obsidian, right-click and publish again, and the site is rebuilt from the same notes. There's no second copy to keep in sync. (More on update workflows in [[mdfriday/blog/update-published-obsidian-notes|Update Published Obsidian Notes Without Copy-Paste]].)

## Plant your first seedling today

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Create a `garden/` folder with one hub note and two linked notes.
3. Right-click the folder and publish.

Guest mode needs no account. **Guest is for trying things out: 1 site, 5 MB, cleared at the next UTC midnight.** The Free plan (3 sites, 50 MB) is also temporary and is cleared on the 1st of each month. When your garden is ready to stay, Personal (about \$5–6/month, 1 GB) keeps it permanently. Trying it costs nothing, and your vault stays on your machine.

## Further reading

- [[mdfriday/blog/publish-obsidian-notes-without-github|Publish Obsidian Notes Without GitHub]]
- [[mdfriday/blog/publish-part-of-obsidian-vault|Publish Part of Your Obsidian Vault, Keep the Rest Private]]
- [[mdfriday/blog/obsidian-website-themes-without-css|Obsidian Website Themes: Look Good Without Writing CSS]]
- Research notes: [[mdfriday/voice-of-custom/knowledge-structure-on-the-web|Knowledge structure on the web]] · [[mdfriday/voice-of-custom/setup-and-deploy-barrier|Setup & deploy barrier]]
