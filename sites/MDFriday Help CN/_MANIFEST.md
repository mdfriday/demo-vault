---
title: MDFriday Help · Manifest
date: 2026-09-19
---

# MDFriday Help — 页面清单与 MEDIA 待填

生成时间：2026-09-19（Asia/Shanghai）  
对齐插件：`mdfriday-publish` **v26.9.4**（`/workspace/mdfriday-src/obsidian-publish` 镜像；Mac 上请以 `…/obsidian-publish/manifest.json` 为准）

## 文件树

```
MDFriday Help/
├── _MANIFEST.md          ← 本文件
├── index.md
├── get-started.md
├── concepts.md
├── faq.md
├── troubleshooting.md
├── images/               ← 空目录（仅 .gitkeep）
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

## MEDIA 占位（需 Wayde 实拍/实录替换）

| 占位 | 建议拍摄内容 | 引用页 |
| --- | --- | --- |
| `images/placeholder-help-home.png` | 帮助库首页 / 导航 | index |
| `images/placeholder-install-plugin.png` | 社区插件搜索安装 | get-started |
| `images/placeholder-publish-menu.png` | 右键「发布到 MDFriday」 | get-started |
| `images/placeholder-note-modes.png` | 单篇：原样 / 单页主题切换 | publish-note |
| `images/placeholder-wiki-publish.png` | 文件夹 Wiki 皮肤列表 | publish-folder |
| `images/placeholder-preview-success.png` | 本地预览成功结果 | local-preview |
| `images/placeholder-right-panel.png` | 右侧面板全貌 | right-panel |
| `images/placeholder-password.png` | 高级选项 · 访问密码 | password |
| `images/placeholder-custom-domain.png` | 域名向导 DNS 表 | custom-domain |
| `images/placeholder-history.png` | Personal 历史列表 | history |
| `images/placeholder-theme-picker.png` | 主题列表 + Live demo | choose-theme |
| `videos/placeholder-publish-demo.md` | 一键发布演示（换成 mp4 等） | get-started |

## 功能清单（写作所用）

来源：`manifest.json`、`README.md`、`src/main.ts`、`setting.ts`、`types/publish*.ts`、`utils/theme.ts`、`cloudflare-env.ts`、`i18n/locales/zh-cn.ts`、`svelte/publish/PublishPanel.svelte`、`ux/DESIGN.md`；官网 `/products/obsidian-publish/`、`/solutions/*`、`/pricing/`。

- 命令：`quick-share`（快速分享）、`quick-publish`（发布到 MDFriday）
- 菜单：在 MDFriday 中打开、发布到 MDFriday
- 模式：note faithful/themed；folder themed-only（Wiki）；默认 paper / quartz
- 发布：Cloudflare V2；Guest 无账号；Turnstile；mdf key
- 预览：本地 webserver；不进历史
- 计划：Guest/Free/Personal（配额见 plans 页；插件 vs 官网站点数量文案冲突已标注）
- 域名 / 历史回滚：Personal
- 设置：Credentials only
- **未作为主路径写**：Sync、Netlify/FTP、旧版大批量 Hugo 导出

## 已知缺口 / 歧义

1. **站点数量**：插件 UI 与官网定价「unlimited sites」不一致 → 文档已声明以插件为准。
2. **Friday Help 参考树**：本环境无法读取 Mac 上 `Friday Help`，help.mdfriday.com 拉取失败；结构按任务书 + 当前插件 IA 重建，未抄 Sync 章。
3. **website 源码仓**：GitHub clone 需凭据失败；改用已上线页面 WebFetch。
4. **导出静态包 / 站点路径 UI**：新 Publish 面板未见用户向「导出」「站点路径」主按钮；sitePath/baseURL 多为 CF 内部。未编造导出教程。
5. **Personal 月价**：$5 年付折算 vs $6 月付 — 来自官网 pricing，结账页为准。
