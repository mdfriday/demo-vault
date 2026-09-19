---
title: 发布文件夹（Wiki）
weight: 32
tags: [发布, Wiki, 文件夹]
date: 2026-09-19
---

# 发布文件夹（Wiki）

## 目标

选中库中的**一个文件夹**，一键发布为带双向链接 / 图谱等能力的 Wiki / 数字花园站点（Quartz 系主题）。

## 前置条件

- 桌面端插件已启用
- 文件夹内有可发布的 Markdown（建议先整理好公开子集，避免误发私密笔记）
- 理解：**文件夹不能「原样发布」**，只能走 Wiki 引擎

## 步骤

1. 在文件树 **右键文件夹** → **发布到 MDFriday**
2. 面板徽标为「文件夹」；发布方式固定为 **Wiki 发布**
3. 在 **Wiki 皮肤** 列表中选择主题（默认倾向 `quartz`；仅展示 Quartz 族可用主题）
4. （可选）打开主题 **Live demo** 对照外观
5. （可选）[[password|访问密码]]、[[local-preview|本地预览]]
6. **发布**，复制 URL

<!-- MEDIA: screenshot — 文件夹 Wiki 皮肤选择 -->
![占位：Wiki 发布](../images/placeholder-wiki-publish.png)

> [!warning] 范围 = 你选中的文件夹
> 只会发布该文件夹范围内内容。整库一键上传不是本产品的默认模型。私密笔记请留在文件夹外，或不要选中包含它们的父目录。

## 结果确认

- 浏览器中可导航多页、跟随 `[[wikilinks]]`（具体能力随 Quartz 主题）
- 项目绑定该**文件夹路径**；改名后插件会尝试迁移 pathConfigs（若失败见排查）

## 相关链接

- [[../themes/wiki-quartz|Wiki / Quartz 主题]]
- <https://mdfriday.com/solutions/digital-garden/>
- [[modes|发布模式]]

## 常见失败

| 现象 | 处理 |
| --- | --- |
| 想选「原样」却不可用 | 设计如此：多页需要 Wiki 引擎 |
| 链接打不开 / 图谱空 | 检查笔记是否在所选文件夹内；wikilink 目标是否也在范围内 |
| 中文路径异常 | 见 [[../faq\|FAQ · 中文路径]] |
