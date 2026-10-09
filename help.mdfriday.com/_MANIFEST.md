---
title: MDFriday Help · Manifest
date: 2026-09-19
lastmod: 2026-10-09
description: Internal inventory of help pages and the screenshot placeholders still to replace. Not a user guide.
---

# MDFriday Help — page inventory and MEDIA TODO

Generated: 2026-09-19 (Asia/Shanghai)  
Aligned plugin: `mdfriday-publish` **v26.10.2** (mirrored at `/workspace/mdfriday-src/obsidian-publish`; on Mac use `…/obsidian-publish/manifest.json`)

## File tree

```
MDFriday Help/
├── _MANIFEST.md          ← this file
├── index.md
├── get-started.md
├── concepts.md
├── faq.md
├── troubleshooting.md
├── images/               ← empty (only .gitkeep)
├── videos/
│   └── placeholder-publish-demo.md
├── publish/
│   ├── index.md
│   ├── publish-note.md
│   ├── publish-folder.md
│   ├── modes.md
│   ├── local-preview.md
│   ├── export.md
│   ├── quick-share.md
│   ├── right-panel.md
│   ├── password.md
│   ├── custom-domain.md
│   ├── history.md
│   └── unpublish.md
├── themes/
│   ├── index.md
│   ├── choose-theme.md
│   ├── notes-themes.md
│   └── wiki-quartz.md
├── plans/
│   ├── index.md
│   ├── guest-free-personal.md
│   └── claim-and-upgrade.md
├── migrate/
│   └── from-friday.md
└── settings/
    ├── index.md
    └── credentials.md
```

## MEDIA placeholders (Wayde to replace with real shots / recordings)

| Placeholder | Suggested capture | Used on |
| --- | --- | --- |
| `images/placeholder-help-home.png` | Help vault home / navigation | index |
| `images/placeholder-install-plugin.png` | Community plugin search install | get-started |
| `images/placeholder-publish-menu.png` | Right-click “Publish to MDFriday” | get-started |
| `images/placeholder-note-modes.png` | Note: faithful / single-page theme switch | publish-note |
| `images/placeholder-wiki-publish.png` | Folder Wiki skin list | publish-folder |
| `images/placeholder-preview-success.png` | Local preview success result | local-preview |
| `images/placeholder-export.png` | Export under a local preview result | export |
| `images/placeholder-right-panel.png` | Full right panel | right-panel |
| `images/placeholder-password.png` | Advanced · access password | password |
| `images/placeholder-custom-domain.png` | Domain wizard DNS table | custom-domain |
| `images/placeholder-history.png` | Personal history list | history |
| `images/placeholder-theme-picker.png` | Theme list + Live demo | choose-theme |
| `videos/placeholder-publish-demo.md` | One-click publish demo (replace with mp4 etc.) | get-started |

## Feature inventory (used while writing)

Sources: `manifest.json`, `README.md`, `src/main.ts`, `setting.ts`, `types/publish*.ts`, `utils/theme.ts`, `cloudflare-env.ts`, `i18n/locales/zh-cn.ts`, `svelte/publish/PublishPanel.svelte`, `ux/DESIGN.md`; website `/products/obsidian-publish/`, `/solutions/*`, `/pricing/`.

- Commands: `quick-share` (Quick share), `quick-publish` (Publish to MDFriday)
- Menu: Open in MDFriday, Publish to MDFriday
- Modes: note faithful/themed; folder themed-only (Wiki); defaults paper / quartz
- Publish: Cloudflare V2; Guest without account; Turnstile; mdf key
- Preview: local webserver; does not enter history
- Plans: Guest/Free/Personal. Sites are not counted. Storage is 5 MB / 200 MB / 5 GB. Guest clears at the next UTC 00:00. Free stays while active (about 6 months inactive may archive)
- Domain / history rollback: Personal
- Settings: Credentials only
- **Not written as main paths**: Sync. Netlify / FTP are not a publish path. A ZIP of the built site is [[publish/export]] after local preview

## Known gaps / ambiguities

1. **Site count**: No plan counts sites. Guest, Free, and Personal are limited by storage (5 MB / 200 MB / 5 GB). Guest’s 5 MB is meant for trying one note.
2. **Friday Help reference tree**: this environment could not read Mac `Friday Help`; help.mdfriday.com fetch failed; structure rebuilt from the brief + current plugin IA; Sync chapters not copied.
3. **Website source repo**: GitHub clone needed credentials and failed; used live pages via WebFetch instead.
4. **Export**: after a successful local preview, **Export** saves a ZIP of the static site (`publish/export.md`). It is not a Markdown backup and does not include hosting features.
5. **Personal price**: $5/month (1 domain), $50/year (1 domain), $60/year (3 domains). Checkout page wins if they ever diverge.
