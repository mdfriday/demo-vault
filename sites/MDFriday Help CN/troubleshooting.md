---
title: 排查清单
weight: 90
tags: [排查]
date: 2026-09-19
---

# 排查清单

按顺序勾选；多数问题在前几步能定位。

## A. 环境

- [ ] Obsidian **桌面端**，插件已启用
- [ ] 版本 ≥ `minAppVersion`（当前 manifest：**1.8.7**）
- [ ] 能打开 <https://mdfriday.com> 与分享域（生产多为 `share.mdfriday.com`）

## B. 入口与对象

- [ ] 右键的是**要发的**笔记或文件夹
- [ ] 面板「发布对象」路径正确（库内找不到路径 → 文件被删/移）
- [ ] 文件与文件夹类型不要混在同一项目里硬切（历史文案要求清空后重选）

## C. 预览

- [ ] 点 **预览**，看是构建失败还是仅上传失败
- [ ] localhost 能开吗？不能 → 端口/权限
- [ ] 空白页 → 换模式（原样/主题）、去掉可疑插件语法、检查图片

## D. Guest 验证

- [ ] 是否卡在 **验证并发布**
- [ ] 是否已在浏览器完成 Turnstile 并**回到 Obsidian**
- [ ] 协议回调是否被系统拦截（`obsidian://mdfriday-publish?...`）

## E. 配额

- [ ] 站点数量：Guest 1 / Free 3 / Personal 不限（插件文案）
- [ ] 存储：5 MB / 50 MB / 1 GB — 超了会挡新发布
- [ ] 清空策略：Guest 日清（UTC）；Free 月初清 — 别误判为「丢数据 bug」

## F. 域名（Personal）

- [ ] 已认证 + 已发布过
- [ ] DNS **短主机名**是否填对
- [ ] 点过验证 / 刷新状态；HTTPS 记录是否齐

## G. 凭证

- [ ] 设置里是否已有 mdf key；换机后是否需要重新认领/导入（按账号站说明）

## 仍未解决

1. 复制面板完整错误文案  
2. 说明：笔记还是文件夹、模式、计划档、是否预览成功  
3. Discord：<https://discord.gg/t7FHJ6qNzT>  
4. 或官网联系入口（页脚邮件 / 关于页）

## 相关链接

- [[faq|常见问题]]
- [[plans/guest-free-personal|计划]]
- [[publish/right-panel|右侧面板]]
