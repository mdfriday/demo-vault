---
title: Chinese Filenames
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "Many publishing tools' slugify step drops Chinese characters, causing broken links, duplicate permalinks and failed deploys; anchors for Chinese headings break too."
---

# Chinese Filenames

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

Many publishing tools' slugify step simply drops Chinese characters. The results: link addresses are wrong and published notes won't open; several Chinese notes in one folder get exactly the same permalink and the deploy fails outright; wikilinks or table-of-contents anchors pointing to Chinese headings don't jump. Even maintainers admit it's a recurring problem. For people who write in Chinese, this isn't an edge case; it affects every single note.

> [!info] Signal (approximate)
> ~6 web supplement sources; latest evidence 2025-07.
> Relevance to MDFriday: **high** (Chinese user base).

## Voices

- 「如果同一个文件夹下存在多个包含中文的笔记，则这些笔记的permal-link会是完全相同的，在vercel发布一步，会报错。」 — Obsidian Chinese forum · 2025-07-01 · <https://forum-zh.obsidian.md/t/topic/51795>
  - *Translation:* If one folder contains several notes with Chinese in their names, those notes all get exactly the same permal-link, and the Vercel publish step throws an error.
- 「如果你的文件夹名或文件名用了中文，你会发现在vercel会错报如下错误」 — Obsidian Chinese forum · 2024-09-27 · <https://forum-zh.obsidian.md/t/topic/40699>
  - *Translation:* If your folder or file names use Chinese, you'll find Vercel reports the following error
- 「只要笔记的路径或笔记本名里面有中文，就无法生成正确的链接地址，导致无法访问发布的笔记。」 — Obsidian Chinese forum · 2023-05-12 · <https://forum-zh.obsidian.md/t/topic/19256>
  - *Translation:* As soon as a note's path or notebook name contains Chinese, the correct link address can't be generated, so the published note can't be opened.
- “it is possible the chinese characters have broken it again (this is a recurring problem haha)” — GitHub Issues · 2024-03-04 · <https://github.com/KosmosisDire/obsidian-webpage-export/issues/389>
- 「不能有中文笔记名，netlify那边会报错。」 — Obsidian Chinese forum · 2022-10-20 · <https://forum-zh.obsidian.md/t/topic/10331>
  - *Translation:* You can't have Chinese note names; Netlify throws an error.
- 「使用digital garden发布功能中文章内标题无法使用双链功能，会导致部署错误」 — Obsidian Chinese forum · 2024-09-10 · <https://forum-zh.obsidian.md/t/topic/39921>
  - *Translation:* With the Digital Garden publish feature, headings inside Chinese articles can't be used with wikilinks; it causes deployment errors.

## Why it hurts

- **Tools only consider English by default.** Chinese users have to work around that default every time.
- **Renaming files is a compromise.** Changing Chinese note names to pinyin or English hurts readability and wikilinks inside the vault.
- **The error shows up at deploy time and is hard to diagnose.** Nothing in the error message says the Chinese filename is the problem.

## How people cope today

- Renaming files to English or pinyin and keeping Chinese only in the title.
- Turning off Digital Garden's Slugify option, or writing permalinks by hand.
- Giving up on a tool and switching to one that handles Chinese better.

## MDFriday's response

- The MDFriday team works in a Chinese-language context itself, so **it should make "Chinese filenames, Chinese headings and Chinese search work out of the box" a guarantee**.
- Current actual behavior: **(unconfirmed)**. Suggestion: first run a regression test with a Chinese vault (Chinese paths, duplicate names, Chinese heading anchors, Chinese full-text search), and once confirmed, put it in the Chinese-language marketing materials.

## Open questions

- In the URLs MDFriday generates, are Chinese filenames kept as Chinese, converted to pinyin, or handled by some other rule? Are the links readable when shared on WeChat?
- Do Chinese heading anchors and Chinese wikilinks (including aliases) all jump correctly?
- Does site search support Chinese word segmentation?

## Related

- [[mainland-china-access|Mainland China Access]]
- [[chinese-community-voices|Chinese Community Voices]]
- [[stable-links-and-redirects|Stable Links & Redirects]]
- [[knowledge-structure-on-the-web|Knowledge Structure on the Web]]
