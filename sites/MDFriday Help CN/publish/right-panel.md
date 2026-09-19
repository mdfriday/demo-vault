---
title: 右侧面板
weight: 36
tags: [UI, 面板]
date: 2026-09-19
---

# 右侧面板

## 目标

认清 MDFriday Publish 的主界面：右侧边栏（side leaf），不是居中弹窗。

## 面板结构（发布 Tab）

1. 标题区 + **计划 pill**（Guest / Free / Personal，可点开对比）
2. Tab：**发布** | **历史**
3. **项目条**：未发布 / 已发布 / 已撤销；公开 URL；「已记住上次设置」；本地预览进行中时可停止
4. **发布对象**（可切换已发布过的目标）
5. **发布方式**（随文件/文件夹分叉）
6. 主题列表（需要时）+ Live demo / 官网主题入口
7. Guest/Free **横幅**（配额与清空策略提示）
8. **高级选项**：访问密码、自定义域名
9. 底部粘性栏：**预览** + **发布** / **验证并发布** / **再次发布**

<!-- MEDIA: screenshot — 右侧面板全貌 -->
![占位：右侧面板](../images/placeholder-right-panel.png)

## 历史 Tab

- **Personal**：版本列表、查看、回滚、撤销发布
- **Guest / Free**：锁定空态，提示升级 Personal

详见 [[history|发布历史与回滚]]。

## 状态机（你会看到的几种屏）

| 状态 | 含义 |
| --- | --- |
| Idle | 配置与主操作 |
| Verify | Guest 首次需人机验证 |
| Building | 预览或发布构建中 |
| Result | 预览成功或发布成功 |
| Soft-gate | 引导认领 Free |

## 相关链接

- [[../plans/_index|计划]]
- [[custom-domain|自定义域名]]
