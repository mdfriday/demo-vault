---
title: 自定义域名
weight: 38
tags: [域名, Personal]
date: 2026-09-19
---

# 自定义域名

## 目标

把已发布站点绑到自己的域名（如 `www.example.com`），并开通 HTTPS。

## 前置条件

- **Personal** 计划（Guest / Free 在 UI 中锁定）
- 已完成账号认证，且该项目**至少成功发布过一次**
- 你能修改该域名的 DNS
- Personal 配额：**最多 3 个**自定义域名（产品文案）

## 步骤（面板向导）

1. 发布 Tab → **高级选项** → **自定义域名**
2. **步骤 1**：输入子域名（例如 `www.example.com`）→ 下一步
3. **步骤 2**：在 DNS 控制台按表格添加记录  
   - 主机记录填**短名称**（不要重复拼主域名，避免 `…example.com.example.com`）
   - 等待生效后点 **「我已添加，开始验证」**
4. **步骤 3**：按提示添加 HTTPS 相关记录；可用 **刷新状态** / **持续检查**
5. 绑定生效后，**再发布一次**，即可用该域名访问

<!-- MEDIA: screenshot — 域名 DNS 表格 -->
![占位：自定义域名向导](../images/placeholder-custom-domain.png)

## 结果确认

- 状态 pill：**已生效**
- 浏览器访问你的域名可打开站点（HTTPS）

## 解除绑定

使用 **解除绑定**：站点改回分享链接；证书可能保留以便日后快速绑到其他项目。若域名已绑在别的站点，需先在那一侧解绑。

## 相关链接

- [[../plans/guest-free-personal|计划对比]]
- [[../plans/claim-and-upgrade|升级 Personal]]
- 定价说明：<https://mdfriday.com/pricing/>

## 常见失败

| 状态文案 | 含义 |
| --- | --- |
| 需先认证 | 先完成账号侧认证 |
| 发布后可绑定 | 先成功发布一次 |
| 升级后可用 | 当前非 Personal |
| 等待生效 / 配置有误 | 检查 DNS 主机记录与验证 TXT/CNAME；点刷新状态 |
