---
title: MDFriday Help · Manifest
date: 2026-09-19
---

# MDFriday Help — page inventory and MEDIA TODO

Generated: 2026-09-19 (Asia/Shanghai)  
Aligned plugin: `mdfriday-publish` **v26.8.25** (mirrored at `/workspace/mdfriday-src/obsidian-publish`; on Mac use `…/obsidian-publish/manifest.json`)

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
│   ├── _index.md
│   ├── publish-note.md
│   ├── publish-folder.md
│   ├── modes.md
│   ├── local-preview.md
│   ├── quick-share.md
│   ├── right-panel.md
│   ├── password.md
│   ├── custom-domain.md
│   ├── history.md
│   └── unpublish.md
├── themes/
│   ├── _index.md
│   ├── choose-theme.md
│   ├── notes-themes.md
│   └── wiki-quartz.md
├── plans/
│   ├── _index.md
│   ├── guest-free-personal.md
│   └── claim-and-upgrade.md
└── settings/
    ├── _index.md
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
- Plans: Guest/Free/Personal (quotas on plans pages; plugin vs website site-count copy conflict noted)
- Domain / history rollback: Personal
- Settings: Credentials only
- **Not written as main paths**: Sync, Netlify/FTP, legacy bulk Hugo export

## Known gaps / ambiguities

1. **Site count**: plugin UI vs website pricing “unlimited sites” disagree → docs state plugin wins.
2. **Friday Help reference tree**: this environment could not read Mac `Friday Help`; help.mdfriday.com fetch failed; structure rebuilt from the brief + current plugin IA; Sync chapters not copied.
3. **Website source repo**: GitHub clone needed credentials and failed; used live pages via WebFetch instead.
4. **Export static package / site-path UI**: new Publish panel has no user-facing primary “Export” / “Site path” buttons; sitePath/baseURL are mostly CF-internal. No invented export tutorial.
5. **Personal monthly price**: $5 annualized vs $6 monthly — from website pricing; checkout page wins.
