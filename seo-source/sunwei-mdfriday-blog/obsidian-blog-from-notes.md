---
title: "Obsidian Blog: Start One From Your Notes Without a CMS"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - blogging
  - how-to
description: "Start an Obsidian blog from the notes you already write, without a CMS: a simple folder setup, what blog features to plan for, and a right-click way to publish."
---

# Obsidian Blog: Start One From Your Notes Without a CMS

You already write every day in Obsidian. A blog should just be a few of those notes, made public. Instead, most advice sends you off to set up a CMS, pick a static site generator, or copy-paste into a platform that mangles your formatting.

And the tool hunt can swallow the writing itself:

> “I found I spent too much time worrying about the tool the theme etc and and up with overwhelm and lack of focus” — [Reddit r/ObsidianMD, 2025](https://www.reddit.com/r/ObsidianMD/comments/1pf5ht9/blogging_with_obsidian_publish)

This post is a simple, tool-agnostic setup for blogging from your vault. It's honest about the blog features you'll need to plan for, and it shows how I publish mine. (These posts are written as ordinary notes in my Obsidian vault, and sunwei.xyz is published from an Obsidian folder with MDFriday.)

## Blog or digital garden? Decide first

They look similar but read differently:

- **A blog is a timeline.** Posts have dates, readers expect new ones, and older posts sink.
- **A digital garden is a map.** Notes link to each other and keep evolving.

Plenty of people do both: a dated `blog/` folder for posts, inside a larger linked garden. If the garden is what excites you, read [[mdfriday/blog/obsidian-digital-garden-without-git|Obsidian Digital Garden: How to Grow One Without Git]]. For a blog, read on.

## A 10-minute blog setup in your vault

**1. Create a `blog/` folder.** Everything in it is public. Nothing outside it is.

**2. Use the same frontmatter on every post:**

```yaml
---
title: "Your Post Title: Keyword First, Promise Second"
date: 2026-09-28
tags: [topic]
description: "One or two sentences, around 150 characters, saying what the reader gets."
---
```

**3. Make a template** with that frontmatter so every post starts right.

**4. Write an index note** (`blog/index`) that lists your posts, newest first, with one line each. Yes, by hand. It takes ten seconds per post, it works with every tool, and it doubles as your editorial overview.

**5. Add an About note.** Who you are, what you write about, and how to reach you.

That's a blog. Everything else is presentation.

## The blog features to plan for (and how people cope)

This is where people using notes-first tools get stuck ([[mdfriday/voice-of-custom/blogging-features|blogging features]]).

**Comments.** For some, it's the one missing piece:

> “The only thing stopping me from using Publish as my personal site is the absence of a comment section” — [Obsidian forum, 2021](https://forum.obsidian.md/t/comment-section-on-obsidian-publish/11252)

Workarounds: end each post with an invitation to reply by email, or link to a discussion thread on Reddit, Mastodon or wherever your readers are. Some bloggers prefer this anyway, because it keeps conversations thoughtful.

**Subscriptions.** Readers need a way to follow you. Tools differ a lot in feed support. The simplest tool-agnostic option is a link to a newsletter signup on a service you already trust.

**A "latest posts" list.** Your hand-kept index note does this job.

**Monetisation.** People do ask:

> “Can you monetize your published notes?” — [YouTube comment, ~2024](https://www.youtube.com/watch?v=eULVrTjT11w)

For now, most notes-based bloggers link out to a product, a paid newsletter or a tip jar rather than relying on the publishing tool.

If comments, memberships and newsletters are the heart of your plan, a full platform like Ghost or WordPress is honestly the better fit. You'll pay for it in copy-paste or integration work. If writing is the heart of your plan, a notes-first setup keeps you writing.

## Your publishing options

- **Ghost or WordPress:** the most complete blog features. Publishing from Obsidian means a plugin or copy-paste, and formatting and images often need fixing.
- **Hugo, Astro or Jekyll:** full control and every feature you're willing to build. Requires Git and some developer comfort.
- **Obsidian Publish:** simple and official. Users have described its RSS feed as “nearly unusable for readers” and missed comments, so check it meets your needs.
- **MDFriday Publish:** right-click your `blog/` folder. More below.

## How I publish a blog with MDFriday

- **Right-click the `blog/` folder and publish.** So a new post goes live without leaving Obsidian. No Git, GitHub, terminal or tokens.
- **Selective publish.** Only `blog/` goes public. So drafts, journals and everything else stay private.
- **The build runs on your computer.** Your vault stays on your machine, and only the chosen notes are uploaded. So your notes remain the single source. Fix a typo in Obsidian and publish again, with no second copy to update.
- **AS mode and multiple themes.** Posts can look like your Obsidian notes, or you can switch to a theme that feels more like a blog, without CSS.
- **Cloudflare CDN.** So there's no hosting to set up.

To be clear, I'm not claiming built-in comments, feeds, newsletters or payments in MDFriday. Use the workarounds above. The trade I'm offering is simpler: the shortest path from "I wrote something" to "it's online".

## Publish your first post today

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Create `blog/` with an index note and one post.
3. Right-click the folder and publish.

Guest mode needs no account. **Guest content is cleared at the next UTC midnight, and the Free plan (3 sites, 50 MB) is cleared on the 1st of each month**, so use them to try things out. When you're ready for a blog that stays up, Personal (about \$5–6/month, 1 GB) keeps it permanently.

## Further reading

- [[mdfriday/blog/update-published-obsidian-notes|Update Published Obsidian Notes Without Copy-Paste]]
- [[mdfriday/blog/obsidian-seo-published-notes|Obsidian SEO: How to Get Your Published Notes Found]]
- [[mdfriday/blog/obsidian-website-themes-without-css|Obsidian Website Themes: Look Good Without Writing CSS]]
- Research notes: [[mdfriday/voice-of-custom/blogging-features|Blogging features]] · [[mdfriday/voice-of-custom/sync-and-update-workflow|Sync & update workflow]]
