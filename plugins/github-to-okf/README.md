---
type: Producer
title: github-to-okf
description: 把 GitHub 仓库(远程 owner/repo 或本地路径)转换为符合 OKF v0.1 的知识包,应用 code-to-okf 约定。
tags: [okf, github, code, producer, cli]
lang: zh
timestamp: 2026-06-14T00:00:00Z
license: MIT
---

# github-to-okf

把一个 GitHub 仓库转换为 OKF 知识包——README/文档 → `Document` 概念,代码文件 → `Module` 概念(带 `language`、提取出的符号、指向源码的 `resource`)。它是 [code-to-okf 约定](../../skills/code-to-okf/references/code-okf-conventions.md) 的落地 producer,与转 awesome **列表**的 [`awesome-importer`](../awesome-importer/) 区分开:本工具转**仓库本身**。

零第三方依赖。

## 安装

```bash
cd plugins/github-to-okf
uv pip install -e .
```

## 用法

```bash
# 本地仓库(全量:读文件、提取符号;若是 git 仓库自动生成 blob 行级 resource)
github-to-okf ./my-repo -o ./out

# 远程仓库(默认浅扫描:只用 git tree,不下载文件)
github-to-okf yzfly/awesome-okf -o ./out

# 远程深扫描(下载文件并提取符号;建议设 GITHUB_TOKEN 提高 API 限额)
export GITHUB_TOKEN=ghp_xxx
github-to-okf yzfly/awesome-okf -o ./out --deep
```

## 它做了什么

- **仓库总览** `repository.md`(`type: Repository`):README + 元数据(语言、stars、默认分支、topics);
- **代码概念**(`type: Module`):每个代码文件一篇,带 `language`、`# Symbols`(函数/类/类型,正则提取)、`resource`(GitHub blob URL,远程用提交 SHA 稳定锚点);
- **文档概念**(`type: Document`):仓库内的 `.md`;
- 根 `index.md`(`okf_version`)+ `log.md`。

支持的语言符号提取:Python、Go、JS/TS、Rust、Java(其余语言仍建概念,只是不提取符号)。自动跳过 `node_modules`、`.git`、`dist` 等目录与超过 200KB 的文件。

产物用 [`validate_okf.py`](../../skills/okf-creator/scripts/validate_okf.py) 校验;用 [`okf-to-web`](../../skills/okf-to-web/) 或 [`okf-to-book`](../../skills/okf-to-book/) 发布。

## 限制

- 符号提取是轻量正则,不做完整 AST;复杂签名/嵌套定义可能漏;
- 远程浅扫描不含符号(用 `--deep`);
- 调用图(calls / cited-by 有类型链接)需后续接 AST 或交给 [`code-to-okf`](../../skills/code-to-okf/) Skill 富化。
