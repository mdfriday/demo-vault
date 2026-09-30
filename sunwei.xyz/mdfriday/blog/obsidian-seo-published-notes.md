---
title: "Obsidian SEO: How to Get Your Published Notes Found"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - seo
  - publishing
description: "Obsidian SEO for published notes: why some note sites are invisible to search, 7 fixes you control in any tool, and simple tests to check what Google sees."
---

# Obsidian SEO: How to Get Your Published Notes Found

You publish your notes, share the link with a few friends, and wait for the world to find you. Weeks later, you search for your own note's exact title and it's nowhere.

> “my publish site is impossible to find in a web search, why?” — [YouTube comment, ~2024](https://www.youtube.com/watch?v=6h42ysmwJzM)

For bloggers, researchers and anyone building a knowledge site, a site nobody can find is barely published at all. In my research, search visibility and speed were a recurring headache ([[mdfriday/voice-of-custom/seo-discoverability-and-ai-crawlers|SEO and discoverability]]). The good news: much of SEO is in your notes, not your tool.

## Why some note sites are hard to find

There are three technical reasons, and then there are content reasons.

**1. Pages that need JavaScript to show text.** Some hosted note sites are single-page apps: the HTML is a shell, and JavaScript fills in the content. Search engines have gotten better at running JavaScript, but it's still a weaker position, and readers suffer too:

> “if JavaScript fails to load for a visitor due to spotty signal or whatever, it will display no text” — [Obsidian forum, 2025](https://forum.obsidian.md/t/the-viability-of-using-obsidian-as-a-publication-platform/108341)

**2. Slow pages.** Large sites can load slowly, especially on phones:

> “pages on mobile that take up to 30 seconds (!)” — [Obsidian forum, 2023](https://forum.obsidian.md/t/publish-performance-issues/61294)

**3. Technical details you can't control.** Sitemaps, canonical tags and page metadata are decided by the tool. Users have reported sitemap errors in Search Console and SEO audits flagging all their pages as orphans.

## 7 SEO fixes you control, in any tool

**1. Title every note like a search result.** Put the phrase people would type at the start, and keep it around 50–60 characters so it isn't cut off. "Sourdough Starter: A 7-Day Schedule" beats "Bread thoughts (v3)".

**2. One topic per note.** Atomic notes are great for SEO, because each page clearly answers one question.

**3. Write a first paragraph that answers the question.** Search engines and readers both judge the page by its opening. Say what the note covers in plain words.

**4. Add a description in your frontmatter.** Many tools use a `description` property for the snippet under your title in search results. Check whether yours does.

**5. Link like a garden.** Internal links help search engines discover pages and understand what matters. Hub notes that link to your best notes are especially valuable. Pages with no links pointing to them are easy to miss.

**6. Keep images light.** Compress images before adding them to your vault. It's the single easiest speed win.

**7. Tell Google you exist.** Add your site to Google Search Console, check which pages are indexed, and be patient. New sites take weeks, not days.

## Two tests that show what search engines see

- **The "view source" test.** Open a published page, right-click, and choose *View Page Source*. Can you find your note's text in the HTML? If yes, crawlers can too. If you only see scripts, the content depends on JavaScript.
- **The phone test.** Open your site on your phone on mobile data, not Wi-Fi. If it feels slow to you, it probably feels slow to search engines too.

Run both on any tool you're considering.

## A new question: do you want AI crawlers or not?

Since 2024, people have been asking something new, and they split into two camps. Some want AI to read their sites:

> “Today websites are not just used to provide information to people, but they are also used to provide information to large language models.” — [Obsidian forum, 2024](https://forum.obsidian.md/t/provide-llm-friendly-content-by-adding-a-llms-txt-file-to-help-llms-use-an-obsidian-website/87818)

Others very much don't:

> “I see LLMs mostly as competition at best, thieves of my researched content at worst.” — [Hacker News, 2025](https://news.ycombinator.com/item?id=43925341)

Whichever camp you're in, find out what control your publishing tool gives you *before* you publish research you care about.

## How MDFriday fits in

Here's what I can say with confidence about MDFriday Publish, and what I can't.

**What it does:**

- **Builds a static website on your computer.** You right-click a note or folder, and the site is generated locally from your notes. So you end up with ordinary web pages. Run the "view source" test on your own site to confirm your text is there.
- **Serves it from Cloudflare's CDN.** So your pages are delivered from a global network, and you don't have to configure hosting.
- **Publishes only what you choose.** So your published site stays focused on the notes you actually want found, not every scrap in your vault.
- **AS mode and switchable themes.** So your pages look like your notes, or like a site, without any CSS.

**What I'm not claiming here:** control over sitemaps, per-page metadata, social preview images, `robots.txt` or AI-crawler settings. If any of those matter for your site, check the current plugin before relying on it. I'd rather you verify than find out after publishing.

## Check your own notes' SEO for free

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Retitle one note using fix #1, write a strong first paragraph, then right-click and publish it.
3. Run the "view source" and phone tests.

Guest mode needs no account. **Guest content is cleared at the next UTC midnight**, so it's for testing, not for getting indexed. The Free plan (3 sites, 50 MB) is also temporary and is cleared on the 1st of each month. For a site you want search engines to find and keep finding, you'll want a permanent plan: Personal is about \$5–6/month for 1 GB.

## Further reading

- [[mdfriday/blog/obsidian-blog-from-notes|Obsidian Blog: Start One From Your Notes Without a CMS]]
- [[mdfriday/blog/obsidian-publishing-mistakes|Obsidian Publishing Mistakes: 7 Ways Sites Break Later]]
- [[mdfriday/blog/obsidian-digital-garden-without-git|Obsidian Digital Garden: How to Grow One Without Git]]
- Research notes: [[mdfriday/voice-of-custom/seo-discoverability-and-ai-crawlers|SEO, discoverability & AI crawlers]] · [[mdfriday/voice-of-custom/analytics-and-privacy-compliance|Analytics & privacy compliance]]
