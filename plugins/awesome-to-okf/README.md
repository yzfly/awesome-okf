---
type: Producer
title: awesome-to-okf
description: 把 GitHub awesome-xx 列表转换为符合 OKF v0.1 的知识包,让社区海量精选列表成为 agent 可读的知识。
tags: [okf, awesome, github, producer, cli]
lang: zh
timestamp: 2026-06-14T00:00:00Z
license: MIT
---

# awesome-to-okf

把 GitHub 上海量的 **awesome-xx** 精选列表,一键转换成符合 [OKF v0.1](../../docs/okf-spec-zh.md) 的知识包(bundle)。这样社区里成千上万份"教程/工具/资源"列表,就能被 AI 智能体直接当知识检索,而不只是给人看的链接墙。

零第三方依赖,纯标准库,开箱即跑。

## 安装

```bash
cd plugins/awesome-to-okf
uv pip install -e .        # 或:pip install -e .
```

也可不安装直接跑:`PYTHONPATH=src python -m awesome_to_okf.cli ...`

## 用法

```bash
# 从 GitHub 仓库导入(自动找 README 与默认分支)
awesome-to-okf sindresorhus/awesome -o ./out

# 从 raw URL 导入
awesome-to-okf https://raw.githubusercontent.com/x/y/main/README.md -o ./out

# 从本地文件导入
awesome-to-okf ./README.md -o ./out --lang zh --date 2026-06-14
```

## 它做了什么

- 解析 awesome 列表的 `##` / `###` 分节与 `* [名称](URL) - 描述` 条目;
- 自动跳过 `Contents` / `目录` / `License` / `Contributing` 等非内容分节;
- 每个链接 → 一个 OKF 概念文档(`type: Resource`,带 `title`/`description`/`resource`/`tags`/`lang`);
- 每个分节 → 一个子目录 + `index.md`(渐进式展开);
- 生成根 `index.md`(带 `okf_version`)与 `log.md`。

产物可直接用 [`validate_okf.py`](../../skills/okf-creator/scripts/validate_okf.py) 校验,用 [`okf-to-book`](../../skills/okf-to-book/) 发布为文档站。

## 输出结构示例

```
out/
├── index.md          # 根索引(okf_version: "0.1")
├── log.md
├── tools/
│   ├── index.md
│   ├── ripgrep.md
│   └── fd.md
└── 教程/
    ├── index.md
    └── rust-圣经.md
```

## 限制

- 只解析 Markdown 列表里的链接条目;复杂表格 / 嵌套结构会被简化。
- 概念正文来自列表里的一句话描述;要更丰富的正文,把产物交给 [`okf-creator`](../../skills/okf-creator/) Skill 富化。

## 配套 Skill

[`awesome-to-okf`](../../skills/awesome-to-okf/) —— 引导 AI 用本工具完成"选列表 → 导入 → 富化 → 校验"的完整流程。
