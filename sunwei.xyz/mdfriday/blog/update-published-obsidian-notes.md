---
title: "Update Published Obsidian Notes Without Copy-Paste"
date: 2026-09-28
tags:
  - blog
  - obsidian
  - workflow
  - publishing
description: "Update published Obsidian notes without copy-paste or scripts: why two copies always drift, 4 common workflows compared, and a one-source way to republish."
---

# Update Published Obsidian Notes Without Copy-Paste

Publishing once is the easy part. The real test is week six, when you've fixed a typo, rewritten a section and added three notes, and your website still shows the old version.

> “they usually got updated on my hugo blog and drifted out of sync” — [personal blog, 2026](https://hypersubject.net/posts/fourth-migration-of-the-year/)

> “watch the formatting break, re-upload every image by hand, fix the footnotes” — [Reddit r/ObsidianMD, 2026](https://www.reddit.com/r/ObsidianMD/comments/1vzqtgt/i_got_tired_of_copypasting_obsidian_notes_into/)

> “Is it easy to sync and scan for chnages, or do i have to re-do everything from scratch every week ?” — [YouTube comment, ~2024](https://www.youtube.com/watch?v=ITiiuBNVue0)

The first quote comes from a blogger describing their *fourth* migration of the year. Update friction is how a publishing setup slowly dies ([[mdfriday/voice-of-custom/sync-and-update-workflow|sync and update workflow]]).

## The root problem: two copies always drift

If your website's content is a *copy* of your vault, the two will drift apart. It doesn't matter how disciplined you are. You'll edit the vault and forget the site, or hot-fix the site and forget the vault.

So the most important rule for a sustainable workflow is simple: **your vault should be the only source.** The website should be *generated* from it, never edited separately.

Let's look at common workflows through that lens.

## 4 common update workflows, compared

### 1. Copy notes into a site repo with a script

A script (rsync, Python, shell) copies notes from your vault into a Hugo, Quartz or Astro repo, then you commit and push.

- **Pros:** full control, works with any static site generator.
- **Cons:** it's still a copy. Scripts break, you forget to run them, and edits made in the repo don't flow back.

### 2. Put your vault inside the site repo

You make the vault itself the Git repo, often with a Git plugin that pushes on a timer.

- **Pros:** one source of truth.
- **Cons:** your vault structure has to suit the website, Git plugins can conflict with sync tools, and anything in the vault is one mistake away from being committed.

### 3. Copy and paste into a blogging platform

You paste into Substack, Medium, Ghost or WordPress.

- **Pros:** you get the platform's audience features.
- **Cons:** formatting breaks, images need re-uploading, footnotes need fixing, and every future edit means doing it again.

### 4. Publish directly from the vault

Tools like Obsidian Publish and MDFriday publish straight from your notes.

- **Pros:** one source, no copying, and you update from where you write.
- **Cons:** you work within the tool's features and plans.

## Habits that keep any setup healthy

Whatever you choose, these small habits help:

1. **Batch your updates.** Edit freely during the week, then publish once. It's calmer than publishing every tiny change.
2. **Keep a "recently updated" note.** List what changed. Readers like it, and it reminds you to publish.
3. **Don't edit the website directly**, even for a typo. Fix it in the vault and republish.
4. **Publish less, not more.** The smaller the published area, the faster and safer every update is. It also helps a lot with large vaults, where building everything can get slow.
5. **Avoid renaming published notes casually.** Renames can break links people have saved (more in [[mdfriday/blog/obsidian-publishing-mistakes|Obsidian Publishing Mistakes]]).

## Signs your update workflow is about to break

Watch for these early warnings, whatever tool you use:

- You've stopped fixing small typos on the site because it's "too much hassle".
- You keep a mental list of notes that are "different online".
- Publishing needs a checklist you have to look up every time.
- You haven't published in a month, even though you've been writing.

If two of these sound familiar, the problem isn't your discipline. Your workflow has too many steps.

## How updates work with MDFriday

I built MDFriday Publish around workflow 4, because workflows 1 and 2 are developer workflows, and writers shouldn't need them.

- **Right-click to publish again.** After editing, you right-click the same note or folder and publish. So there's no copying, no script and no commit.
- **The vault is the only source.** The site is built from your notes on your computer, and only the chosen notes are uploaded. So there's no second copy to drift.
- **Selective publish.** You only publish the folder that needs to be public. So each rebuild covers what matters, not your whole vault.
- **No Git, no pipeline.** So there's nothing to break between you and your readers except a right-click.
- **Cloudflare CDN.** So you don't manage any hosting when you update.

What I'm not promising here: phone publishing, or automatic publishing whenever you save. Plan to republish from Obsidian on your computer. If you have a very large vault, publish the folders you need rather than everything, and time it yourself before relying on it.

## Try the update loop

The best test of a publishing tool isn't the first publish. It's the second.

1. Install **MDFriday Publish** from Obsidian's Community plugins: <https://obsidian.md/plugins?search=mdfriday-publish>
2. Right-click a folder and publish it.
3. Edit two notes, add a new one, and publish again. See how it feels.

Guest mode needs no account. **Guest content is cleared at the next UTC midnight**, which is plenty of time to test an update loop. The Free plan (3 sites, 50 MB) is also temporary and is cleared on the 1st of each month. Personal (about \$5–6/month, 1 GB) keeps your site permanently.

## Further reading

- [[mdfriday/blog/obsidian-blog-from-notes|Obsidian Blog: Start One From Your Notes Without a CMS]]
- [[mdfriday/blog/obsidian-digital-garden-without-git|Obsidian Digital Garden: How to Grow One Without Git]]
- [[mdfriday/blog/obsidian-publishing-mistakes|Obsidian Publishing Mistakes: 7 Ways Sites Break Later]]
- Research notes: [[mdfriday/voice-of-custom/sync-and-update-workflow|Sync & update workflow]] · [[mdfriday/voice-of-custom/large-vault-builds|Large vault builds]]
