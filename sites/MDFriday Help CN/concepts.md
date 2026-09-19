---
title: 和 Obsidian Publish / Quartz 的差异
weight: 20
tags: [概念, 对比]
date: 2026-09-19
---

# 和 Obsidian Publish / Quartz 的差异

> [!quote] 写给选型中的你
> 下面只写**当前 MDFriday Publish 插件能兑现的事实**，不把官网路线图当成已上线能力。

## 一句话

| 方案 | 一句话 |
| --- | --- |
| **MDFriday Publish** | 在 Obsidian 里选笔记/文件夹 → 本地构建 → 一键上传到 MDFriday CDN；Guest 可无账号试用 |
| **Obsidian Publish** | 官方托管阅读器；偏「库 / 站点」订阅式发布 |
| **自建 Quartz** | 免费、能力强；需要 Node / 仓库 / CLI 或 CI |

## 对照（诚实版）

来源：官网产品页对比表 + 插件实现（Cloudflare 发布、原样/主题/Wiki 分叉）。

| 维度 | MDFriday Publish | Obsidian Publish | 自建 Quartz / Hugo |
| --- | --- | --- | --- |
| 发布范围 | **单篇或文件夹**（你选什么发什么） | 偏整库 / 站点工作流 | 项目目录，需自己划边界 |
| 构建位置 | **本地**构建；上传的是静态产物 | 托管侧为主 | 本地或 CI |
| 源 Markdown 是否上传作编辑副本 | 产品定位：**源笔记留在设备**；云端托管构建输出 | 托管优先 | 通常进 Git 仓库 |
| 本地预览 | ✓ 插件内本地服务 | — | ✓（自己起） |
| 无账号试用 | ✓ **Guest** | 通常需要 Obsidian 账号与订阅 | 不涉及「账号试用」 |
| 外观 | **原样发布**（贴近库内阅读视图）或 **Notes / Quartz 主题** | 官方阅读器外观 | 主题生态自运维 |
| Wiki 能力 | 文件夹 → Quartz 系 Wiki 主题（图谱、双向链接等） | 官方功能集 | Quartz 原版你自己运维 |
| 自定义域名 | **Personal** 计划（最多 3 个，自动 HTTPS） | 官方栈支持 | DIY |
| 历史回滚 | **Personal** | 有限 / 产品相关 | Git DIY |
| 运维负担 | 插件内完成；无需自备 CLI | 低（官方托管） | 高（工具链 + 配置） |

## 两个发布行为（产品分叉）

插件按选择类型分叉（见 `publish-config` 与 UI 文案）：

1. **单篇笔记**
   - **原样发布（faithful）**：默认推荐；尽量保留本地预览感（主题、社区插件渲染、CSS snippets）
   - **单页主题（themed）**：选用 Notes 族主题（默认 slug：`paper`）
2. **文件夹**
   - **仅 Wiki 发布（themed）**：不能原样；需要 Wiki 引擎处理多页、双向链接与图谱（默认 slug：`quartz`）

详见 [[publish/modes|发布模式]]、[[themes/_index|主题]]。

## 和旧版「Friday」帮助的区别

旧 **Friday Help** 常把 **Sync + Publish** 写在一起，并提到 Netlify / FTP / 大量 Hugo 主题导出等。

当前 **MDFriday Publish**：

- 发布方式以 **Cloudflare V2** 为主（`PublishMethod = 'cloudflare'`）
- Guest → 分享链接是默认试用路径
- README 仍提到 Netlify / FTP 为**遗留路径**；**本帮助不以它们为主路径**，避免教你走已弱化的流程
- Sync 请看独立 Sync 产品，不要在本插件里找「整库实时同步」教程

## 相关链接

- [[get-started|安装与首次发布]]
- <https://mdfriday.com/products/obsidian-publish/>
- <https://mdfriday.com/solutions/share-a-note/>
- <https://mdfriday.com/solutions/digital-garden/>
