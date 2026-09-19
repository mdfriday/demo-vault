---
title: 常见问题
weight: 80
tags: [FAQ]
date: 2026-09-19
---

# 常见问题

## 安装与平台

### 为什么手机 / iPad 上不能用？

插件 `isDesktopOnly: true`。本地构建与预览依赖桌面环境。

### 社区插件里搜不到？

确认已关闭安全模式、能访问社区插件列表；关键词用 **MDFriday Publish** 或 id `mdfriday-publish`。也可打开 <https://obsidian.md/plugins?search=mdfriday-publish>。

## 发布与构建

### 构建失败怎么办？

1. 看 Obsidian Notice / 面板错误原文  
2. 先 [[publish/local-preview|本地预览]] 定位是构建问题还是上传问题  
3. 简化附件、检查断链图片  
4. 换 **原样 ↔ 主题** 对比  
5. 仍失败 → [[troubleshooting|排查清单]] 或 Discord

### 预览成功但发布失败？

常见：配额（站点/存储）、Guest 未完成验证、网络上传中断。对照面板红色错误：站点上限 / 存储已满等文案已本地化。

### 附件 / 图片不显示？

确认图片在所选笔记或文件夹范围内；避免仅靠绝对系统路径。原样模式与主题模式的资源收集路径不同，可两边各预览一次。

### 中文路径可以吗？

一般可用；若遇极端编码问题，尝试缩短路径、避免特殊符号，并在预览中验证链接。

### 必须买 License 才能发吗？

**不必。** Guest Cloudflare 发布是无账号路径；LicenseState 在 Cloudflare guest 模式下可跳过初始化。付费能力主要是 Personal 的域名 / 永久保留 / 历史等。

## 计划与清空

### Guest 站点第二天没了？

Guest 在**下一个 UTC 00:00**清空。请 [[plans/claim-and-upgrade|认领 Free]] 保留 URL，或升级 Personal 永久保留。

### 官网写「站点不限」，插件却说 Guest 只能 1 个？

以**插件报错与计划卡片**为准（见 [[plans/_index|计划说明]]）。产品文案若未同步，以你安装的插件版本 UI 为准。

## 主题与效果

### 原样发布和库里不完全一样？

预期内：只有能静态化的渲染能带走。Dataview 等「运行时查询」类能力通常不能原样进静态站。

### 文件夹为什么不能原样？

多页 + wikilink/图谱需要 Wiki 引擎；UI 会禁用原样并说明原因。

## 旧功能

### Netlify / FTP / 导出静态包还支持吗？

当前发布类型为 **Cloudflare**。README 提到 Netlify/FTP 为遗留路径。本帮助不教这些为主流程；若你本地 Foundry 项目仍残留旧配置，属高级/遗留场景，请以实际面板是否仍暴露入口为准（新 Publish 面板以 CF 分享链接为主）。

### Sync 怎么配？

不在本插件帮助范围。见 Sync 产品：官网 <https://mdfriday.com/products/obsidian-sync/>。

## 相关链接

- [[troubleshooting|排查清单]]
- Discord：<https://discord.gg/t7FHJ6qNzT>
