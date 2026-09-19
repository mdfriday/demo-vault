---
title: 安装与首次发布
weight: 10
tags: [入门, 安装, Guest]
date: 2026-09-19
---

# 安装与首次发布

## 目标

在 Obsidian 桌面端装好 **MDFriday Publish**，用 **Guest（无需账号）** 路径发布一篇笔记，拿到可分享的公开链接。

## 前置条件

- Obsidian 桌面端（插件为 **desktop-only**；最低应用版本见 `manifest.json` 的 `minAppVersion`，当前为 **1.8.7**）
- 能访问外网（首次 Guest 发布可能需在浏览器完成人机验证）
- 一篇 Markdown 笔记，或一个准备公开的文件夹

## 步骤

### 1. 安装插件

1. 打开 **设置 → 社区插件**，关闭安全模式（若尚未关闭）
2. 浏览 / 搜索 **MDFriday Publish**（id：`mdfriday-publish`）
3. 安装并**启用**

也可从官网入口跳转：<https://obsidian.md/plugins?search=mdfriday-publish>

<!-- MEDIA: screenshot — 社区插件搜索 MDFriday Publish -->
![占位：安装插件](images/placeholder-install-plugin.png)

### 2. 打开右侧发布面板

任选一种方式：

- **右键**笔记或文件夹 → **「在 MDFriday 中打开」**（只打开配置面板，不立刻发布）
- **右键** → **「发布到 MDFriday」**（打开面板并走发布流程）
- 命令面板：**「快速分享」** 或 **「发布到 MDFriday」**

右侧会出现 **MDFriday** 边栏（发布 | 历史）。

<!-- MEDIA: screenshot — 右键菜单「发布到 MDFriday」 -->
![占位：发布菜单](images/placeholder-publish-menu.png)

### 3. 首次 Guest 发布（无需账号）

1. 确认发布对象是当前笔记 / 文件夹
2. 单篇默认多为 **原样发布**；文件夹固定为 **Wiki 发布**（详见 [[publish/modes|发布模式]]）
3. 可选：点 **预览**，先在本机浏览器看效果（[[publish/local-preview|本地预览]]）
4. 点 **发布**。若是 Guest 且尚未验证，按钮可能显示 **「验证并发布」**
5. 按提示前往 **mdfriday.com** 完成 Turnstile 人机验证，再回到 Obsidian 继续
6. 成功后复制公开 URL 分享

<!-- MEDIA: video — 一键发布演示 -->
![占位：发布演示视频](videos/placeholder-publish-demo.md)

> [!info] Credential 会自动签发
> 首次发布会自动创建 **mdf key**（Guest 或后续用户凭证）。设置页可查看 / 复制，用于账号认领或换设备。详见 [[settings/credentials|Credential（mdf key）]]。

## 结果确认

- 面板出现 **「发布成功」**，有可打开 / 复制的 URL（生产环境分享域一般为 `https://share.mdfriday.com/...`）
- 项目状态变为 **已发布**
- Guest：内容会在**下一个 UTC 00:00** 清空（认领 Free 可保留同一 URL）— 见 [[plans/guest-free-personal|Guest / Free / Personal]]

## 相关链接

- [[publish/publish-note|发布一篇笔记]]
- [[publish/publish-folder|发布文件夹]]
- [[plans/claim-and-upgrade|认领 Guest 与升级]]
- [[troubleshooting|排查清单]]

## 常见失败

| 现象 | 可能原因 | 去看 |
| --- | --- | --- |
| 移动端找不到插件能力 | 桌面端专用 | [[faq\|FAQ · 桌面端]] |
| 卡在「验证并发布」 | 未完成 Turnstile 或未回到 Obsidian | [[troubleshooting\|排查]] |
| 发布失败 · 站点上限 | Guest 仅 **1** 个站点（以插件文案为准） | [[plans/guest-free-personal\|计划]] |
| 预览空白 / 构建失败 | 附件路径、主题、端口占用等 | [[faq\|FAQ]] · [[troubleshooting\|排查]] |
