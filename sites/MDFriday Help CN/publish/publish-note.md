---
title: 发布一篇笔记
weight: 31
tags: [发布, 单篇]
date: 2026-09-19
---

# 发布一篇笔记

## 目标

把**当前这一篇** Markdown 变成公开（或密码保护）的网页链接，而不暴露库里其他笔记。

## 前置条件

- 已启用 MDFriday Publish（桌面端）
- 选中的是**文件**，不是文件夹

## 步骤

1. 在文件列表或编辑器中定位该笔记
2. **右键** → **发布到 MDFriday**（或先 **在 MDFriday 中打开** 再点发布）
3. 在右侧面板确认 **发布对象** 为该文件（徽标「文件」）
4. 选择发布方式：
   - **原样发布**（默认推荐）：贴近 Obsidian 本地预览
   - **单页主题**：从 Notes 族主题中选（默认倾向 `paper`）
5. （可选）高级选项里设置 [[password|访问密码]]
6. （可选）[[local-preview|预览]]
7. 点 **发布** / **验证并发布**，完成后 **复制** URL

<!-- MEDIA: screenshot — 单篇发布模式切换：原样 / 单页主题 -->
![占位：单篇模式](../images/placeholder-note-modes.png)

## 结果确认

- 结果页显示 **已发布** + 公开 URL
- 同一路径再次打开会 **记住** 模式 / 主题 / 密码开关
- 再次发布通常更新**同一站点**（mdf key / Guest 凭证会持久化）

## 相关链接

- [[modes|发布模式]]
- [[../themes/notes-themes|Notes 主题]]
- 官网方案：<https://mdfriday.com/solutions/share-a-note/>

## 常见失败

| 现象 | 处理 |
| --- | --- |
| 想发文件夹却停在单篇 UI | 对文件夹右键，见 [[publish-folder\|发布文件夹]] |
| 原样效果和库内不一致 | 社区插件/自定义语法未必都能进静态页；可改试单页主题或简化笔记 |
| Guest 站点已满 | 认领 Free 或撤销旧站，见 [[../plans/guest-free-personal\|计划]] |
