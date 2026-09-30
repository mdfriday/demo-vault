---
title: Maintenance Burden
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "The hidden cost of free options is maintenance: abandoned plugins, deleted repos, major rewrites and upstream merge conflicts. Users fear their time investment will be wasted."
---

# Maintenance Burden

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

The hidden cost of free options is maintenance. Plugins stop being updated (someone posted asking whether the Digital Garden plugin is dead), dependency repos get archived (obsidian-hugo) or deleted (the Mado 11 theme), Quartz gets rewritten for a major version, pulling upstream updates brings merge conflicts, tutorials go stale within months, and a submodule quietly breaks and the deploy fails. What users fear most: a site they spent dozens of hours customizing suddenly stops working one day.

> [!info] Signal (approximate)
> ~18 VOC cards · ~10 YouTube comments.
> Ranked **#12**: a trust problem, the fear of wasted effort.

## Voices

- “hours of customization at risk” — Obsidian Forum · 2026-08-22 · <https://forum.obsidian.md/t/mado-11-repository-is-gone/117600>
- “Git merge conflicts every time updates are fetched upstream” — Personal blog · 2026-09-10 · <https://burgeonlab.com/notes/2026/0910-0021/>
- “Looks like the sekund plugin is no longer being updated.” — YouTube comment · ~2023 · <https://www.youtube.com/watch?v=J0LUf8_K_oo>
- “seems to me like this method is not working anymore.” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=eULVrTjT11w>
- “I noticed that obsidian-hugo is now archived and read only.” — YouTube comment · ~2024 · <https://www.youtube.com/watch?v=ITiiuBNVue0>
- “I feel like this plugin deserves more time and "love"?” — Reddit r/ObsidianMD · 2024-12-31 · <https://www.reddit.com/r/ObsidianMD/comments/1hqd5uf/is_obsidian_digital_garden_plugin_dead_are_there>

## Why it hurts

- **A website is a long-term asset, but tools are short-lived.** Users want to write for ten years; a tool may be replaced in one or two.
- **Maintenance cost is unpredictable.** Nobody knows what the next upgrade will break, so people stop upgrading and fall further and further behind.
- **Open-source projects depend on a few maintainers.** When the maintainers run out of time, users have no fallback.

## How people cope today

- Pinning versions and never upgrading, dealing with problems when they come.
- Migrating to another tool (one blogger migrated four times in a year).
- Eventually paying for a hosted service in exchange for "someone else maintains it for me".

## MDFriday's response

- **Hosted service + local build**: users don't maintain templates, dependencies or deploy scripts; MDFriday takes care of plugin upgrades.
- **Source notes are always plain Obsidian Markdown**: even if you switch tools someday, the content itself isn't locked in.
- Evidence of ongoing maintenance (number of releases, downloads) could be shown publicly, but the specific numbers need checking first (unconfirmed).
- Note: MDFriday is itself a small vendor, and users are just as sensitive to "will it be abandoned?"; see [[vendor-trust-and-reliability|Vendor Trust & Reliability]].

## Open questions

- When the plugin is upgraded, could published sites change their look / URLs because of theme or rendering changes? See [[stable-links-and-redirects|Stable Links & Redirects]].
- Could a public changelog and release cadence become a trust signal?

## Related

- [[vendor-trust-and-reliability|Vendor Trust & Reliability]]
- [[setup-and-deploy-barrier|Setup & Deploy Barrier]]
- [[choosing-a-publishing-tool|Choosing a Publishing Tool]]
- [[stable-links-and-redirects|Stable Links & Redirects]]
