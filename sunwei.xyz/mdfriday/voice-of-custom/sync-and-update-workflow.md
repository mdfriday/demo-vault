---
title: Sync & Update Workflow
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Publishing isn't a one-off. After editing, people want to republish quickly, without maintaining two copies of their content or writing copy scripts, and they want to update from their phone too."
---

# Sync & Update Workflow

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Publishing isn't a one-off. Users want to republish quickly after editing, update from several devices and from their phone, and not start from scratch every week. The reality: many people write their own rsync / Python / shell scripts to copy between the vault and the SSG repository, and over time the two drift out of sync; posting to platforms like Substack means copy-paste, broken formatting and re-uploading images one by one; Git-based plugins conflict with sync tools; Quartz or Git publishing can't run on a phone; with a large vault, opening Publish's publish dialog takes 30+ seconds.

> [!info] Signal (approximate)
> ~37 VOC cards · ~10 YouTube comments (pushing from mobile, multiple devices, automatic deploys, whether edits sync automatically).
> Ranked **#7**: long-term friction after publishing.

## Voices

- “they usually got updated on my hugo blog and drifted out of sync” — Personal blog · 2026-08-16 · <https://hypersubject.net/posts/fourth-migration-of-the-year/>
- “watch the formatting break, re-upload every image by hand, fix the footnotes” — Reddit r/ObsidianMD · 2026-08-27 · <https://www.reddit.com/r/ObsidianMD/comments/1vzqtgt/i_got_tired_of_copypasting_obsidian_notes_into/>
- “I'd like to be able to push changes from my mobile phone.” — YouTube comment · ~2026 · <https://www.youtube.com/watch?v=dSm8aLPdVz0>
- “Is it easy to sync and scan for chnages, or do i have to re-do everything from scratch every week ?” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=ITiiuBNVue0>
- “I was wondering if there is a way to sync you files with your android” — Reddit r/ObsidianMD · 2026-05-28 · <https://www.reddit.com/r/ObsidianMD/comments/1tpnm2u/obsidian_quartz_on_android>

## Why it hurts

- **Two content sources are bound to drift.** As long as the website's content is copied out of the vault, there will always be "changed it here, forgot it there".
- **Repetitive work drains the enthusiasm for writing.** Every publish means copying, fixing formatting and uploading images again; the process eats the joy of writing.
- **Writing happens anywhere.** Ideas often come on the phone, but publishing only happens back at the computer.

## How people cope today

- Writing their own sync scripts, or pushing on a schedule with a Git plugin.
- Putting the vault directly inside the SSG repository, bending the vault's structure to fit the website's.
- Copy-pasting by hand into newsletter / blog platforms. Chinese users posting to WeChat Official Accounts or Xiaohongshu face the same kind of pain; see [[chinese-community-voices|Chinese Community Voices]].

## MDFriday's response

- **Right-click to republish**: there's only one copy of the content, the notes in your vault, and no second repository to keep in sync.
- **Local build + Cloudflare CDN**: after editing, rebuild locally and upload.
- Publishing from mobile (unconfirmed; the currently known form is an Obsidian desktop plugin); automatic / incremental updates (unconfirmed).

## Open questions

- How often do users republish? Repeat publishing is one of the success metrics, so the friction of this action is worth watching.
- How long does one republish take on a large vault? See [[large-vault-builds|Large Vault Builds]].
- How strong is the mobile need? Is it "publish from the phone", or is "edit on the phone, publish automatically back at the computer" enough?

## Related

- [[large-vault-builds|Large Vault Builds]]
- [[export-beyond-the-web|Export Beyond the Web]]
- [[chinese-community-voices|Chinese Community Voices]]
- [[setup-and-deploy-barrier|Setup & Deploy Barrier]]
