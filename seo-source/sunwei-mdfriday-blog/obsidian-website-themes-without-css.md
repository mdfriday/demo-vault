---
title: "Obsidian Website Themes: Look Good Without Writing CSS"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - themes
  - design
description: "Obsidian website themes without CSS: why published notes often look off, 6 content fixes that help in any tool, and how to switch site themes in a click."
---

# Obsidian Website Themes: Look Good Without Writing CSS

You finally got your notes online. Then you look at the site and think: this doesn't look like *me*. You spent months getting your Obsidian theme just right, and the website looks like a stranger's.

> “now just need to work on making it not look awful” — [YouTube comment, ~2024](https://www.youtube.com/watch?v=ITiiuBNVue0)

> “make my Reader view look exactly like the Publish view using CSS” — [Obsidian forum, 2025](https://forum.obsidian.md/t/consistent-theme-same-appearance-from-reader-to-publish/105019)

> “without having to change publish.css ourselves” — [Obsidian forum, 2025](https://forum.obsidian.md/t/basic-customization-in-publish-settings-directly-for-published-site-with-preview/95956)

That last quote is the heart of it. Writers want a site that looks good. They don't want a second job as a front-end developer. When I sampled the comments on 30 popular publishing videos, complaints about looks and themes showed up under 29 of them ([[mdfriday/voice-of-custom/themes-and-customization|themes and customization]]).

## Why published notes often look "off"

There are three reasons, and none of them are your fault:

1. **Your editor theme and your website theme are two separate things.** In most tools, the theme you use in Obsidian doesn't carry over to the site, so you style everything twice.
2. **Customising means code.** Obsidian Publish uses `publish.css` and `publish.js`. Quartz means editing styles and TSX components, which can conflict with upstream updates. Custom CSS in the Digital Garden plugin reportedly only partly applies.
3. **Defaults are designed for everyone**, which means they fit no one in particular.

If you enjoy CSS, all three are solvable, and Quartz in particular gives you enormous control. If you don't, here's how to get most of the way there anyway.

## 6 content fixes that help in any tool

Good-looking sites are mostly good *content structure*. These work with every theme and every tool:

1. **Give every page one H1, then use H2s.** Clear headings make any theme look intentional.
2. **Keep paragraphs short.** Three or four lines on a phone screen is plenty. Dense text looks worse online than in your editor.
3. **Write a real home page.** A short intro, three "start here" links, and what the site is about. First impressions come from the index page, not the theme.
4. **Be consistent with images.** Similar widths, and no giant screenshots mixed with thumbnails. Compress big images before adding them.
5. **Use callouts sparingly.** One or two per page draw the eye. Ten turn into noise.
6. **Name notes like titles.** "Why I Garden" reads better in a navigation list than "2023-04-why-garden-v2".

## Pick a look for what your readers do

Before comparing colours, think about how people will read your site:

- **Readers who skim** (a blog, a newsletter archive) need big titles, dates and a clean list of posts.
- **Readers who wander** (a digital garden, a wiki) need visible links, hub pages and easy ways back home.
- **Readers who look things up** (docs, a course, a reference) need clear headings and a table of contents.

The "right" theme is the one that fits that behaviour, not the one with the prettiest screenshot.

## Three ways to get a site that looks like you

**Option A: Learn just enough CSS.** Grab a community snippet, tweak colours and fonts, and accept some maintenance when your tool updates. This is best if you like tinkering.

**Option B: Use a tool with good-looking defaults and live with them.** Quartz's default garden look is lovely. Many people are happy with it untouched.

**Option C: Let the site look like your vault, or switch themes with a click.** This is the approach I took with MDFriday Publish.

## How MDFriday handles themes

I built MDFriday Publish for people who'd rather write than style. There are two ideas:

- **AS mode renders pages to look like your Obsidian notes.** So the look you already tuned in Obsidian is the look your readers get, and you don't have to recreate it in CSS.
- **Multiple themes you can switch between.** So the same notes can be presented in a different style when you want a more "website" feel, without editing any code. Try one, don't like it, and switch.

Put together, you can publish a folder, look at it in one theme, and switch to another in minutes. That's a very different afternoon from debugging a stylesheet.

A few things I'm deliberately not claiming here: I'm not promising specific branding controls (favicons, footers and the like) in this post. If those matter to you, check the current plugin before relying on them. And like any tool, notes that depend on plugin-specific styling may not carry over exactly. See [[mdfriday/blog/obsidian-notes-broken-after-publishing|Obsidian Notes Broken After Publishing?]] for how to test that.

## Try two themes on the same folder

The quickest way to judge is to see your own notes in more than one look:

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Right-click a folder and publish it.
3. Switch the theme and publish again. Compare both on your phone.

Guest mode needs no account. **Guest content is cleared at the next UTC midnight, and the Free plan (3 sites, 50 MB) is cleared on the 1st of each month**, so use them to experiment. Personal (about \$5–6/month, 1 GB) keeps your site permanently. Your vault stays on your machine the whole time.

## Further reading

- [[mdfriday/blog/obsidian-digital-garden-without-git|Obsidian Digital Garden: How to Grow One Without Git]]
- [[mdfriday/blog/obsidian-blog-from-notes|Obsidian Blog: Start One From Your Notes Without a CMS]]
- [[mdfriday/blog/obsidian-notes-broken-after-publishing|Obsidian Notes Broken After Publishing? What to Check First]]
- Research notes: [[mdfriday/voice-of-custom/themes-and-customization|Themes & customization]] · [[mdfriday/voice-of-custom/rendering-fidelity|Rendering fidelity]]
