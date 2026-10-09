---
title: "Publish Part of Your Obsidian Vault, Keep the Rest Private"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - privacy
  - selective-publish
description: "How to publish part of your Obsidian vault and keep private notes private: folder boundaries, a pre-publish checklist, and the leaks people miss."
---

# Publish Part of Your Obsidian Vault, Keep the Rest Private

Most of us keep one vault for everything. Journals sit next to project notes, client details next to the essay you'd love to share. So the question isn't really "how do I publish my vault?" It's "how do I publish *this part* without the rest leaking out?"

> “there are a lot of private content like diaries, drafts and incomplete notes that I don't want to publish” — [Reddit r/ObsidianMD, 2025](https://www.reddit.com/r/ObsidianMD/comments/1mznj8r/how_to_publish_only_part_of_my_vault)

> “the idea that it would be there for the whole internet to see and I can do nothing about it, puts me off.” — [YouTube comment, ~2022](https://www.youtube.com/watch?v=1pf6aj3Uwuk)

That fear is rational. Once a private note is indexed by a search engine, you can't really take it back. In my research, this worry came up less often than setup problems, but it was often described as *the* thing stopping someone from publishing at all ([[mdfriday/voice-of-custom/selective-publish-and-privacy|selective publish and privacy]]).

Here's a practical approach that works with any tool.

## The three layers of the problem

1. **Choosing** what goes public: by folder, by tag, or by a `publish: true` property.
2. **Preventing mistakes**, like a template that stamps a publish flag on every new note, or an "add linked notes" button that pulls in hundreds of pages.
3. **Leaks after publishing**, which happen where you aren't looking: graph views, search indexes, broken links that reveal private titles, and attachments.

Most guides only cover layer 1. The scary stories are all about layers 2 and 3.

## Layer 1: Pick one clear boundary

You have three common ways to choose what's public:

- **A public folder.** Everything in `public/` (or `garden/`) is published, and nothing else. It's easy to reason about and easy to audit.
- **A property flag** like `publish: true` on each note. It's flexible, but easy to get wrong at scale. One person wished they could add the flag “to hundreds of my notes with a click”.
- **Tags.** Workable, but tags are easy to add by accident.

My recommendation for most people is the folder. It's the one boundary you can check with a single glance at your file explorer.

## Layer 2: A pre-publish checklist

Before your first publish, and before any big one, run through this:

1. **Links out of the boundary.** Search public notes for wikilinks to notes outside it. Depending on the tool, these can show as plain text, a broken link or the private note's title.
2. **Embeds.** `![[private note]]` doesn't just link, it pulls the content in. Check every embed in your public notes.
3. **Attachments.** Images and PDFs can contain more than you think: screenshots of inboxes, client names in file names, location data in photos.
4. **Templates.** Make sure your templates don't add a publish flag or a public tag by default.
5. **Frontmatter.** Properties like `client:` or `status: confidential` may be shown on the page by some themes.
6. **File names.** Titles alone can say a lot.

## Layer 3: Test like a stranger

After publishing, open the site in a private browser window and behave like a curious visitor:

- search for a private word you know exists in your vault
- click every link on your index page
- look at the graph or navigation, if your tool has them
- try the URL of a note you *didn't* publish

Users of hosted tools have reported surprises here, including:

> “When a note is marked as hidden client side, it is still searchable in the search bar on obsidian publish.” — [Obsidian forum, 2024](https://forum.obsidian.md/t/hidden-notes-accessible-through-search-in-publish/78634)

That's not a reason to avoid publishing. It's a reason to spend ten minutes testing with any tool, including mine.

## How I approached this in MDFriday

Privacy was one of the first things I designed around, because it's the reason so many people never publish at all.

- **Selective publish.** You right-click the note or folder you want to share, and only that is published. So your journal and client notes don't even enter the process.
- **The build runs locally.** The site is generated on your computer, your vault stays on your machine, and only the chosen notes are uploaded. So your full vault never gets synced to a server just to publish three notes.
- **No Git repository.** So there's no public repo with your vault's history in it, which is a leak path people forget with GitHub-based setups.
- **AS mode.** Pages render to look like your Obsidian notes. So proofreading in Obsidian really is proofreading the page.

What I won't claim: I haven't published a formal guarantee about exactly how every link to an unpublished note is displayed, or how every attachment is handled. So please run the Layer 3 test on your first MDFriday site too. If you find something that surprises you, that's exactly the kind of feedback I want.

## Start with a single safe note

The lowest-risk way to try selective publishing is with something that's already public in spirit, like a reading list or a how-to.

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Right-click that one note and publish it.
3. Run the "test like a stranger" steps above.

Guest mode needs no account. **Guest content is cleared at the next UTC midnight**, which here is a feature: your test disappears on its own. The Free plan (3 sites, 50 MB) is also temporary and is cleared on the 1st of each month. Personal (about \$5–6/month, 1 GB) is for sites you want to keep permanently.

## Further reading

- [[mdfriday/blog/obsidian-digital-garden-without-git|Obsidian Digital Garden: How to Grow One Without Git]]
- [[mdfriday/blog/share-a-single-obsidian-note|Share a Single Obsidian Note as a Web Page]]
- [[mdfriday/blog/obsidian-publishing-mistakes|Obsidian Publishing Mistakes: 7 Ways Sites Break Later]]
- Research notes: [[mdfriday/voice-of-custom/selective-publish-and-privacy|Selective publish & privacy]] · [[mdfriday/voice-of-custom/access-control-and-collaboration|Access control & collaboration]]
