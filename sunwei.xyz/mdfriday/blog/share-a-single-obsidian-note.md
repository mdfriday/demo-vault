---
title: "Share a Single Obsidian Note as a Web Page (the Easy Way)"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - sharing
  - how-to
description: "How to share a single Obsidian note as a web page: 5 options compared, when links expire, and a right-click way to publish one note without a whole site."
---

# Share a Single Obsidian Note as a Web Page (the Easy Way)

Not everyone wants a website. Often you just want to send one note to one person: meeting notes to a client, a recipe to a friend, a guide to a new teammate. And suddenly you're reading about static site generators.

> “Sometimes I just want to share one note with someone.” — [Reddit r/ObsidianMD, 2026](https://www.reddit.com/r/ObsidianMD/comments/1sgom74/is-there-a-good-way-to-share-a-single-obsidian-note-without-publishing-your-whol)

> “I don’t always want to expose my whole vault or set up a publish flow just for one note.” — [Reddit r/ObsidianMD, 2026](https://www.reddit.com/r/ObsidianMD/comments/1sgom74/is-there-a-good-way-to-share-a-single-obsidian-note-without-publishing-your-whol)

Sharing one note is often the very first moment someone needs to turn a note into a web page ([[mdfriday/voice-of-custom/single-note-sharing|single-note sharing]]). Here are your options, what each is good at, and the one detail that trips people up: how long the link lives.

## What "good" looks like for a shared note

From what people ask for, a good single-note share should:

1. **Look like the note.** Formatting, callouts and images intact.
2. **Take seconds, not a setup session.**
3. **Not expose anything else** in your vault.
4. **Stay up as long as you need it.** Links that quietly expire are a real problem:

> “Problem is with expiration date for the links. That is something I cannot accept!” — [YouTube comment, ~2026](https://www.youtube.com/watch?v=4t3J8m7Z_jE)

Keep point 4 in mind as you read, because it applies to my own tool's free tiers too.

## Option 1: Export to PDF

Obsidian has built-in PDF export. It works offline and the recipient needs nothing.

**Good for:** documents people will print or archive.
**Downsides:** it's a snapshot that goes stale as soon as you edit, formatting can shift (users report lost indents and missing diagrams), and it's awkward to read on a phone.

## Option 2: Copy and paste into a doc or email

This is quick for short notes.

**Downsides:** wikilinks, callouts and embeds break, images need re-uploading, and now you have two copies to keep in sync.

## Option 3: A dedicated single-note sharing plugin

This category exists for exactly this job. **Share Note** is popular because it keeps a note's full theme and content and offers optional encryption. **JotBird** focuses on zero-friction publishing without signing up. **Obsius** is another simple option that YouTube tutorials often recommend.

**Good for:** frequent, lightweight sharing.
**Check:** how long links last, what happens to internal links, and whether the look matches your notes.

## Option 4: Obsidian Publish

You can publish one note on a Publish site.

**Good for:** people who already pay for Publish.
**Downsides:** it's a whole-site subscription, which is a lot for sharing the occasional note. One commenter asked whether it was worth going that route just to share a note, and said it “Seems way too complicated”.

## Option 5: Right-click publish with MDFriday

This is the option I built, so here's the honest version.

With MDFriday Publish, you right-click a single note in Obsidian and publish it as a web page.

- **One right-click, no setup.** No Git, no GitHub, no terminal, no tokens. So sharing a note takes about as long as writing the message you'll paste the link into.
- **AS mode.** The page renders to look like your Obsidian note. So the recipient sees what you see, not a stripped-down copy.
- **Selective by design.** Only that note is published, and the build runs on your computer. So nothing else in your vault is uploaded.
- **Switchable themes.** So a client-facing note can look more polished than your personal theme, if you like.
- **Served from Cloudflare's CDN.** So there's no hosting for you to set up, and the page is delivered from a global network.

## Which option should you pick?

- **The recipient will print or file it:** export to PDF.
- **It's three paragraphs and a one-off:** copy and paste is fine.
- **You share notes every day and want encryption:** try a dedicated plugin like Share Note.
- **You already pay for Obsidian Publish:** use it.
- **You want a page that looks like your note, from a right-click, and might later grow into a small site:** try MDFriday.

## The part about links expiring (please read)

This is where I have to be very clear, because it's exactly the complaint above:

- **Guest** (no account): 1 site, 5 MB. **The content is cleared at the next UTC midnight.** Great for "look at this today". Not for anything that needs to last.
- **Free** (with an account): 3 sites, 50 MB. **The content is cleared on the 1st of each month.** Fine for short-lived shares.
- **Personal:** about \$5–6 a month, 1 GB, and **permanent**. If the link is going into a proposal, a course or your CV, this is the plan you want.

I'd rather you choose the right plan up front than send a link that stops working.

One more honest note: if your shared note links to other notes, test how those links behave before sending, as you should with any single-note tool.

## Share one note in the next five minutes

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Right-click the note you want to share and choose **Publish to MDFriday**.
3. Open the link on your phone, then send it.

Guest mode needs no account and costs nothing. Just remember it's cleared at the next UTC midnight. Your vault stays on your machine either way.

## Further reading

- [[mdfriday/blog/publish-part-of-obsidian-vault|Publish Part of Your Obsidian Vault, Keep the Rest Private]]
- [[mdfriday/blog/publish-obsidian-notes-without-github|Publish Obsidian Notes Without GitHub]]
- [[mdfriday/blog/obsidian-publish-alternatives|Obsidian Publish Alternatives: 6 Honest Options Compared]]
- Research notes: [[mdfriday/voice-of-custom/single-note-sharing|Single-note sharing]] · [[mdfriday/voice-of-custom/vendor-trust-and-reliability|Vendor trust]] · [[mdfriday/voice-of-custom/export-beyond-the-web|Export beyond the web]]
