---
type: voc
id: "obsidian-forum-119366"
date: 2026-10-12
platform: obsidian-forum
url: "https://forum.obsidian.md/t/links-work-in-obsidian-but-404-after-i-publish-case-thing/119366"
author: "xexu"
title: "Links work in Obsidian but 404 after publishing because of filename casing"
quote: "[[setup]] opens Setup.md fine inside Obsidian. I publish the vault, click the same link, 404. Every time it’s the casing. Windows doesn’t care, Obsidian doesn’t care, then Linux hosting cares a lot."
need: "Catch or fix wikilinks whose casing differs from the file name before the published site goes live."
pain: "Links that work inside Obsidian break with 404s on case-sensitive Linux hosting, and manual checking still misses some."
topic: "[[stable-links-and-redirects]]"
persona: unknown
competitor: []
fit: not-supported
intensity: pain
decision:
reply: not-replied
engagement: none
reply_url:
last_touch:
seo_brief: "[[B54-obsidian-notes-broken-after-publishing]]"
source:
tags:
  - voc
---

# Links work in Obsidian but 404 after publishing because of filename casing

> [[setup]] opens Setup.md fine inside Obsidian. I publish the vault, click the same link, 404. Every time it’s the casing. Windows doesn’t care, Obsidian doesn’t care, then Linux hosting cares a lot.

## Context

Obsidian Forum post by xexu on 2026-10-12 (22:14 Asia/Shanghai). Also writes: "This keeps biting me and I want to know if it’s just me." and "Right now I just eyeball my links before deploying and I still miss some. There has to be a better way to catch these. What do you all do?" The post does not name the publishing tool; it mentions publishing the vault to Linux hosting. Found by the VOC growth loop run of 2026-10-13 00:04; no raw card.

## Our assessment

- Fit: not-supported (to verify) · Intensity: pain · Decision: left for triage
- To verify: whether MDFriday resolves wikilinks case-insensitively when building, so `[[setup]]` reaches `Setup.md`. This is not in the confirmed product facts, so do not claim it until checked.
- Strong evidence for [[B54-obsidian-notes-broken-after-publishing|B54]]: the exact "works in Obsidian, 404 after publish" wording.

## Follow-up log

- 2026-10-14 00:00 Asia/Shanghai: 1 reply in-window (not from OP). u/CawlinTeffid (2026-10-13 23:22 Asia/Shanghai): hasn't seen casing listed as a limitation on the help site; suggests emailing support@obsidian.md if nobody answers. OP hasn't replied; still unresolved.
- 2026-10-14: Third reply from u/dawni (2026-10-14 03:23 Asia/Shanghai): Linux filesystems are case sensitive; suggests picking links from Obsidian's suggester, using display text (`[[Setup.md|setup]]`), a case-insensitive (casefold) host option, lowercase filenames, or lowercase redirects. OP (xexu) has not replied; still unresolved. Thread now 3 posts.
- 2026-10-14 16:00 Asia/Shanghai: Fourth reply from u/CawlinTeffid (2026-10-14 15:46 Asia/Shanghai): apologizes for thinking it was Obsidian Publish; clarifies Obsidian internal links are case-insensitive but URL path segments are case-sensitive regardless of hosting OS; most sites use all-lowercase URLs; suggests server/.htaccess redirect to a canonical capitalization. OP (xexu) still has not replied; still unresolved. Thread now 4 posts.
