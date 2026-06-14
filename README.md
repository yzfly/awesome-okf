---
type: Overview
title: Awesome OKF
description: 中文世界第一个 OKF 落点：规范翻译、工具链、提案，以及一份活的合规范例。
tags: [okf, awesome, 中文]
lang: zh
timestamp: 2026-06-14T00:00:00Z
author: 云中江树
---

# Awesome OKF

中文 | [English](./README.en.md)

开放知识格式（OKF）的中文资料和工具。规范翻译、七个 producer 插件、七个 Claude Code skill、三份向上游的扩展提案。

[OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) 是 Google Cloud 发布的一份开放规范——把知识定义为一个目录的 Markdown 文件，带 YAML frontmatter，加一小套约定。没有运行时，没有 SDK。

## 快速开始

```bash
# 安装
pip install myokf-cli

# 从一个 GitHub 仓库拉取 OKF bundle
myokf from-github yzfly/awesome-okf -o ./kb

# 校验
myokf validate ./kb

# 打包成单文件网页
myokf to-web ./kb -o kb.html
```

## 内容

**工具（plugins/）**

| 工具 | 输入 → OKF |
|---|---|
| [feishu-to-okf](./plugins/feishu-to-okf/) | 飞书知识空间 / 文档 |
| [obsidian-to-okf](./plugins/obsidian-to-okf/) | Obsidian vault（wikilink → OKF 链接） |
| [notion-to-okf](./plugins/notion-to-okf/) | Notion Markdown 导出 |
| [github-to-okf](./plugins/github-to-okf/) | GitHub 仓库（提取代码符号） |
| [awesome-to-okf](./plugins/awesome-to-okf/) | GitHub awesome-xx 列表 |
| [html-to-okf](./plugins/html-to-okf/) | HTML 文件 |
| [myokf-cli](./plugins/myokf-cli/) | 以上工具的统一 CLI 入口 |

全部零第三方依赖，标准库，产物通过符合性校验。

**Skill（skills/）** —— Claude Code 配套工作流

| Skill | 用途 |
|---|---|
| [okf-creator](./skills/okf-creator/) | 从零创建高质量 OKF 知识库 |
| [awesome-to-okf](./skills/awesome-to-okf/) | 导入 awesome 列表并富化 |
| [book-to-okf](./skills/book-to-okf/) | 书 / 长文拆成互链概念库 |
| [code-to-okf](./skills/code-to-okf/) | 代码库转 OKF |
| [github-to-okf](./skills/github-to-okf/) | 仓库 → OKF 富化工作流 |
| [okf-to-book](./skills/okf-to-book/) | OKF 发布为 VitePress 文档站 |
| [okf-to-web](./skills/okf-to-web/) | OKF 打包成单文件网页（含图谱） |

**文档（docs/）**

- [OKF 规范中文版](./docs/okf-spec-zh.md) —— 全文翻译，标注硬要求与留白
- [发布博客中文版](./docs/blog-zh.md)
- [Karpathy 的 LLM Wiki](./docs/karpathy-llm-wiki-zh.md) —— OKF 的思想来源
- [代码 / PDF / 图片支持度调研](./docs/code-support-research-zh.md)
- [全网资料汇总](./docs/resources-zh.md)
- [仓库自身怎么做成 OKF bundle 的](./docs/dogfooding-zh.md)

**三份扩展提案** —— 向后兼容，不动任何 MUST

- [i18n](./docs/okf-spec-zh.md#中文生态议题i18n-扩展提案草案) —— `lang` + `canonical`
- [代码支持](./docs/code-support-research-zh.md) —— 类型词表、符号引用、行号锚点
- [HTML 一等公民](./docs/html-first-class-proposal-zh.md) —— `.html` 概念，双表示

## 这个仓库本身

是一个符合 OKF v0.1 的 bundle。每个 `.md` 带 frontmatter 和非空 `type`，根目录有 `index.md` 和 `log.md`：

```bash
python skills/okf-creator/scripts/validate_okf.py .
```

## 贡献

PR 欢迎。标准：跟 OKF 相关，能跑或能读。写 producer 前看 [CONTRIBUTING](./CONTRIBUTING.md)。

## 许可

云中江树 维护，微信公众号：云中江树。[MIT](./LICENSE)。