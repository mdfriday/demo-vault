---
title: Export Beyond the Web
date: 2026-09-28
tags:
  - voice-of-customer
  - user-research
  - mdfriday
description: "The web isn't the only output. Users also want PDF, EPUB, single-file HTML and offline browsing, and complain that exports lose formatting and images."
---

# Export Beyond the Web

← [[mdfriday/voice-of-custom/index|Voice of the Customer]]

## What users are saying

The web isn't the only output. Users want to export notes as PDF (résumés, TTRPG modules, class materials, printable cards), EPUB (book manuscripts), a single HTML file, or an offline static site. Common complaints: exports lose indentation, math and diagrams; PDF export fails under an RTL interface; PDFs embedded in a Publish site only show the first page on phones. Wayde's own `requirements.md` records a similar need: after publishing a Wiki, PDFs should be easy to read and download on mobile.

> [!info] Signal (approximate)
> ~22 VOC cards (~19 since 2025, concentrated in the past year) · 0 YouTube comments.
> Ranked **#14**: clearly growing over the past year.

## Voices

- “I cant copy the text with source mode on I cant export as PDF I downloaded a program to export as HTML Everything strips my indents.” — Reddit r/ObsidianMD · 2026-09-08 · <https://www.reddit.com/r/ObsidianMD/comments/1wacd8z/cant_export_my_tab_indents_no_matter_what_i_try/>
- “I made some diagrams to go along with my notes, but when I export to pdf to send to my friends, the diagrams doesn't appear.” — Reddit r/ObsidianMD · 2026-09-03 · <https://www.reddit.com/r/ObsidianMD/comments/1w68t9y/exporting_md_files_with_tikzjax/>
- “export my notes as a6 notecards to later print.” — Reddit r/ObsidianMD · 2026-08-30 · <https://www.reddit.com/r/ObsidianMD/comments/1w2uysm/include_yaml_frontmatter_properties_in_pandoc_pdf/>
- “My aim is to make my vault into a static website to browse offline across different PCs.” — Reddit r/ObsidianMD · 2026-07-02 · <https://www.reddit.com/r/ObsidianMD/comments/1ulbpfj/how_to_set_up_quartz_strictly_for_offline_pc>

## Why it hurts

- **Readers and situations vary.** Some people need to print, some need to read offline, some need to send notes to friends who don't use Obsidian.
- **Every new output format restarts the fidelity problem.** It has the same root as [[rendering-fidelity|Rendering Fidelity]].
- **Users don't want to be stuck in one format.** According to a VOC card summary, one Reddit user described the feeling as knowledge being "trapped in the vault", with the web as the only way out.

## How people cope today

- Obsidian's built-in PDF export, the Pandoc plugin and the Webpage HTML Export plugin, each with its own formatting problems.
- Installing third-party converters and then fixing formatting by hand.
- Generating a static site with Quartz for offline browsing, which leads straight back to the [[setup-and-deploy-barrier|setup barrier]].

## MDFriday's response

- The clearly confirmed capability today is **web publishing**: right-click → local build → Cloudflare CDN.
- PDF / EPUB / offline HTML export: **(unconfirmed)**.
- A small first step: in a published Wiki, PDF attachments that are readable and downloadable on mobile (unconfirmed), which matches the need in `requirements.md`.

## Open questions

- Are the users who need export the same people who publish websites, or an adjacent market?
- Can the static site produced by the local build be delivered directly as an offline version (unconfirmed)?
- Has the reading experience of PDF attachments on phones been tested?

## Related

- [[rendering-fidelity|Rendering Fidelity]]
- [[media-and-storage-limits|Media & Storage Limits]]
- [[single-note-sharing|Single-note Sharing]]
- [[sync-and-update-workflow|Sync & Update Workflow]]
