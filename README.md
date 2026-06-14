---
type: Overview
title: Awesome OKF
description: 开放知识格式(OKF)的中文资料整理,以及几个把常见笔记/文档工具转成 OKF 的小工具。
tags: [okf, awesome, 中文]
lang: zh
timestamp: 2026-06-14T00:00:00Z
author: 云中江树
---

# Awesome OKF

中文 | [English](./README.en.md)

开放知识格式(OKF)的中文资料整理:规范和博客的翻译、一些背景梳理,外加几个把飞书、Obsidian、Notion、GitHub 等转成 OKF 的小工具,和配套的 Claude Code skill。

这个仓库本身也是一个符合 OKF v0.1 的 bundle——每篇文档都带 frontmatter,根目录有 `index.md` 和 `log.md`,跑 `python skills/okf-creator/scripts/validate_okf.py .` 能验证。

## OKF 是什么

Google Cloud 在 2026-06-12 发布的一份开放规范,把"用 LLM 维护 wiki"这件事标准化了:知识就是**一个目录的 Markdown 文件,带 YAML frontmatter,外加一小套约定**。没有运行时、没有 SDK、没有中央注册表。能 `cat` 就能读,能 `git clone` 就能分发。

想快点搞懂取舍,直接看 [规范中文版](./docs/okf-spec-zh.md),里面标了哪些是硬要求、哪些是留白。

## 这里有什么

一个统一命令行 [`myokf`](./plugins/myokf-cli/) 把下面能 CLI 化的功能收在一起,例如:

```bash
myokf from-github yzfly/awesome-okf -o ./kb   # 仓库转成 OKF
myokf validate ./kb                            # 校验
myokf to-web ./kb -o kb.html                   # 生成单文件网页
```

**把各种来源转成 OKF 的工具(plugins/):**

| 工具 | 作用 |
|---|---|
| [feishu-okf](./plugins/feishu-okf/) | 飞书知识库 / 文档 |
| [awesome-importer](./plugins/awesome-importer/) | GitHub 上的 awesome-xx 列表 |
| [obsidian-to-okf](./plugins/obsidian-to-okf/) | Obsidian vault(wikilink 会转成 OKF 链接) |
| [notion-to-okf](./plugins/notion-to-okf/) | Notion 的 Markdown 导出 |
| [html-to-okf](./plugins/html-to-okf/) | HTML 文件 |
| [github-to-okf](./plugins/github-to-okf/) | GitHub 仓库(会提取代码符号) |
| [myokf-cli](./plugins/myokf-cli/) | 上面这些的统一入口 |

**配套的 skill(skills/):**

| Skill | 作用 |
|---|---|
| [okf-creator](./skills/okf-creator/) | 从零把资料整理成 OKF,重点在正文质量 |
| [awesome-to-okf](./skills/awesome-to-okf/) | 导入 awesome 列表再富化 |
| [book-to-okf](./skills/book-to-okf/) | 把书 / 长文拆成互链的概念库 |
| [code-to-okf](./skills/code-to-okf/) | 代码库转 OKF 的约定与流程 |
| [github-to-okf](./skills/github-to-okf/) | 仓库转 OKF 的富化流程 |
| [okf-to-book](./skills/okf-to-book/) | OKF 发布成 VitePress 文档站 |
| [okf-to-web](./skills/okf-to-web/) | OKF 打包成单个网页(带图谱,压缩) |

这些工具都只用标准库,产物都过了符合性校验。

## 文档

- [OKF 规范中文版](./docs/okf-spec-zh.md) —— 规范全文翻译,标注了硬要求和留白
- [发布博客中文版](./docs/blog-zh.md)
- [Karpathy 的 LLM Wiki](./docs/karpathy-llm-wiki-zh.md) —— OKF 的思想来源,附原始 gist
- [代码 / PDF / 图片支持度调研](./docs/code-support-research-zh.md)
- [全网资料汇总](./docs/resources-zh.md)
- [仓库自身怎么做成 OKF bundle 的](./docs/dogfooding-zh.md)

## 几个想往上游提的扩展

OKF v0.1 留了一些空白。这里写了三份扩展想法,都是向后兼容的小改动(不动任何硬要求),既有文档也有参考实现:

- [多语言(i18n)](./docs/okf-spec-zh.md#中文生态议题i18n-扩展提案草案) —— `lang` + `canonical`
- [代码支持](./docs/code-support-research-zh.md) —— 类型词表、`language`/`symbol`/`signature`、行号锚点、有类型链接
- [HTML 作为一等公民](./docs/html-first-class-proposal-zh.md) —— `.html` 也能当概念,人看 html、机读 md

## 官方资源

- [规范 SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
- [knowledge-catalog 仓库](https://github.com/GoogleCloudPlatform/knowledge-catalog)
- [发布博客](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/)

## 贡献

欢迎 PR。收录的标准就一条:跟 OKF 相关,而且能跑 / 能读。写 producer 的话,参考 [CONTRIBUTING](./CONTRIBUTING.md) 里的约定。文档目前以中文为主(都带了 `lang` 标记),英文翻译也欢迎。

## 作者与许可

云中江树 维护,微信公众号:云中江树。[MIT](./LICENSE)。
