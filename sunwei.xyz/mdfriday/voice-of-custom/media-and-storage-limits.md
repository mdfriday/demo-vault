---
title: Media & Storage Limits
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Users treat high-resolution images, PDFs and audio as site content, then hit storage caps, attachments that don't publish with the note, and image compression. Especially sensitive for MDFriday's quotas."
---

# Media & Storage Limits

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Users treat the high-resolution images, PDFs, audio and large files in their vault as part of the website's content, and then run into a string of problems: storage caps (Publish offers 4 GB and some already find it too little), attachments that don't publish with the note (add a new image and you have to remember to publish it separately), images compressed automatically, PDFs that won't upload, and in the end images moved to an external image host. Chinese users say outright that paying for more capacity would be fine.

> [!info] Signal (approximate)
> ~12 web supplement sources (7 quoted, 5 corroborating); latest evidence 2025-12.
> Relevance to MDFriday: **very high** (MDFriday's quotas are smaller than Publish's).

## Voices

- “Obsidian Publish storage limits forces us to be mindful of image usage.” — Obsidian Forum · 2025-04-25 · <https://forum.obsidian.md/t/publish-compress-images-on-server/99986>
- “these would fairly soon exceed 4gb” — Obsidian Forum · 2022-12-09 · <https://forum.obsidian.md/t/option-to-pay-for-additional-storage-in-obsidian-publish/49199>
- “My audio files I will need to add are already more than 4 GB” — Obsidian Forum · 2024-12-30 · <https://forum.obsidian.md/t/publish-linked-audio/93971>
- 「发布网站的容量建议支持扩容，付费扩容都是可以的」 — Obsidian Chinese forum · 2025-12-08 · <https://forum-zh.obsidian.md/t/topic/56559>
  - *Translation:* I'd suggest letting the published site's storage be expanded; paying for extra capacity would be totally fine.
- “if I add a photo to a published note, I need to remember to separately publish that new photo” — Obsidian Forum · 2024-03-23 · <https://forum.obsidian.md/t/publish-attached-files-with-note/79121>
- 「发布出去进入网站之后，显示the link destination does not exist.」 — Obsidian Chinese forum · 2023-12-14 · <https://forum-zh.obsidian.md/t/topic/27150>
  - *Translation:* After publishing and opening the site, it shows "the link destination does not exist."
- “I don't want it to automatically compress the image.” — GitHub Issues · 2023-10-04 · <https://github.com/oleeskild/obsidian-digital-garden/issues/464>

## Why it hurts

- **Images and attachments are the content.** In photography, design, course and podcast gardens, media files are far larger than the text.
- **Managing attachments by hand is error-prone.** Forget to publish one image and readers see a broken image or "link destination does not exist".
- **Storage anxiety discourages use.** Users start rationing images, and site quality drops.

## How people cope today

- Hosting images on an external image host or cloud storage, then facing the risk of that host failing (especially common among Chinese users; see [[chinese-community-voices|Chinese Community Voices]]).
- Compressing images by hand before putting them in the vault.
- Asking on the forum for paid extra storage.

## MDFriday's response

- **Current quotas**: Guest 5 MB, Free 50 MB, Personal 1 GB. **All three are smaller than Publish's 4 GB**, and users already complain that 4 GB isn't enough. This needs particular attention.
- Suggestion: before publishing, show "how much this upload is / how much quota is left"; on the pricing page, explain 1 GB as "roughly how many images and pages" **(unconfirmed)**.
- Automatic image compression / WebP conversion while keeping the original **(unconfirmed)**; attachments referenced by a note published automatically with it **(unconfirmed)**; paid extra storage **(unconfirmed)**.

## Open questions

- What does the distribution of existing users' site sizes look like? For how many people is 1 GB enough?
- Are referenced images and PDFs already bundled into the site automatically?
- What do users see when they exceed their quota? Is there a clear message and upgrade path?

## Related

- [[pricing-and-lock-in|Pricing & Lock-in]]
- [[export-beyond-the-web|Export Beyond the Web]]
- [[chinese-community-voices|Chinese Community Voices]]
- [[large-vault-builds|Large Vault Builds]]
