---
type: Producer
title: myokf-cli
description: OKF 统一命令行入口,把所有 producer, consumer 与工具收进一个 myokf 命令。
tags: [okf, cli, 统一入口]
lang: zh
timestamp: 2026-06-14T00:00:00Z
license: MIT
---

# myokf-cli

一个命令搞定所有 OKF 操作。`myokf` 把本仓库的所有 producer、consumer 与工具统一成子命令,内部分发到各模块——装一个就够。

## 安装

```bash
cd plugins/myokf-cli
uv pip install -e .
# 在 awesome-okf 仓库检出环境下开箱即用(会自动定位各工具)
```

## 命令一览

```bash
myokf list                      # 列出全部命令
myokf validate <bundle>         # 校验 OKF v0.1 符合性
myokf scaffold <dir>            # 生成空 bundle 骨架

# Producers(来源 → OKF)
myokf from-awesome  <owner/repo|url|file> -o ./out
myokf from-feishu   spaces | export <space_id> -o ./out
myokf from-obsidian <vault> -o ./out
myokf from-notion   <export_dir> -o ./out
myokf from-html     <file|dir> -o ./out
myokf from-github   <owner/repo|path> -o ./out [--deep]

# Consumers(OKF → 发布)
myokf to-book <bundle> -o ./site [--title T]    # VitePress 文档站
myokf to-web  <bundle> -o okf.html [--title T]  # 单文件网页(自动 build+minify)
```

每个子命令的其余参数原样转发给对应工具,`myokf <cmd> --help` 看细节。

## 典型流水线

```bash
# GitHub 仓库 → OKF → 单文件可视化网页,一条龙
myokf from-github yzfly/awesome-okf -o ./kb
myokf validate ./kb
myokf to-web ./kb -o awesome-okf.html
```

## 说明

- 当前依托仓库检出布局自动定位各工具(零额外依赖);
- `to-web` 的压缩步骤需要 Node.js(无 node 时自动降级为未压缩输出);
- `from-feishu` 需要 `FEISHU_APP_ID` / `FEISHU_APP_SECRET` 环境变量。
