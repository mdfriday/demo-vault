---
title: Reply guidelines (drafts for the owner to post)
---

# Reply guidelines (drafts for the owner to post)

## Preconditions

- Thread is open, on-topic, not locked or removed, and the brand has **not** already been mentioned by anyone.
- The sub or forum allows tool recommendations (check the rules).
- You can answer the question usefully without the product.

## Structure

1. **Validate the specific pain** in one line, using their words.
2. **Give 2–3 practical lanes** (including free and competitor options) with the trade-off of each.
3. **Soft mention with founder disclosure:** first person ("that's the lane I've been building with <Product>" or "Disclosure: I build <Product>"), one sentence on the fitting confirmed capabilities, and one honest limit ("Fair warning — it doesn't replace …").
4. **Close with a question** that helps them decide (their constraint, device or hosting).

Length: usually 100–250 words. No links unless the sub allows them; never more than one product link.

## Example (reference run, a draft for a "publish without git" thread, lightly shortened)

> You're hitting a real split: LiveSync solves *sync*; most "self-hosted publish" stacks quietly assume *git as the CMS*. Those are different jobs, so the conflict pain makes sense.
>
> Practical lanes that skip git:
> 1) **Synced folder → static site.** Keep LiveSync as the source of truth. On a machine that has the vault folder, run a local Markdown→HTML build and deploy the *output* (Netlify drop / FTP / Cloudflare Pages upload / nginx). …
> 2) **Change-driven publish (what you sketched).** A CouchDB listener / filesystem watcher that rebuilds on note change is a solid DIY path. …
> 3) **Share-a-note tools.** Good for one page / temporary share. Usually weaker if you want a multi-note site that tracks ongoing edits.
>
> If the goal is "select notes/folders → local preview → static site → host anywhere" without adopting git workflows, that's the lane I've been building with **MDFriday Publish** (Obsidian plugin, desktop): local build, selective note/folder publish, themes, then Cloudflare / export. Fair warning — it doesn't replace LiveSync, and it's not a CouchDB→web listener. …
>
> Curious: do you want continuous auto-publish on every CouchDB change, or "I hit publish when a batch is ready"?

Why it works: the pain is named precisely, the lanes include the DIY path the OP proposed, the product is the last lane with first-person founder framing ("the lane I've been building"), the limits are stated, and it ends with a question that moves the OP forward.

## Never

- Post, vote, DM or create accounts for the owner.
- Reply twice in a thread, or reply where the brand already appeared (listen only).
- Claim unconfirmed features, invent user numbers, or disparage alternatives.
- Suggest bypassing employer IT policies or platform rules.
