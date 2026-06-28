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

## OKF 热门仓库

_★ 徽章为 GitHub 实时 star(点击进仓库);行序按 2026-06-28 的 star 快照排,完整 60+ 仓库见 [resources-zh](./docs/resources-zh.md#四生态工具与转换器社区项目)。_

| 仓库 | ★ | 语言 | 形态 |
|---|---|---|---|
| [knowledge-catalog](./references/knowledge-catalog-repo.md)(官方) | [![★](https://img.shields.io/github/stars/GoogleCloudPlatform/knowledge-catalog?style=flat&label=%E2%98%85&color=444)](https://github.com/GoogleCloudPlatform/knowledge-catalog/stargazers) | HTML | OKF 规范 + 参考实现 + 示例 bundle 总入口 |
| [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | [![★](https://img.shields.io/github/stars/JuneYaooo/lineage-skill?style=flat&label=%E2%98%85&color=444)](https://github.com/JuneYaooo/lineage-skill/stargazers) | Python | 带出处(lineage)蒸馏的 Agent Skill,输出 OKF 包 |
| [psinetron/echoes-vault-opencode](https://github.com/psinetron/echoes-vault-opencode) | [![★](https://img.shields.io/github/stars/psinetron/echoes-vault-opencode?style=flat&label=%E2%98%85&color=444)](https://github.com/psinetron/echoes-vault-opencode/stargazers) | TS | OpenCode 持久记忆插件,底层用 OKF |
| [OWOX Model Canvas](./references/owox-model-canvas.md) | [![★](https://img.shields.io/github/stars/OWOX/owox-model-canvas?style=flat&label=%E2%98%85&color=444)](https://github.com/OWOX/owox-model-canvas/stargazers) | TS | 可视化建模 / 创作端(公司维护) |
| [0dust/OKFy](https://github.com/0dust/OKFy) | [![★](https://img.shields.io/github/stars/0dust/OKFy?style=flat&label=%E2%98%85&color=444)](https://github.com/0dust/OKFy/stargazers) | TS | 文档 → agent 可读 OKF bundle 转换器 |
| [okf-knowledge](./references/okf-knowledge.md) | [![★](https://img.shields.io/github/stars/sniperunder123/okf-knowledge?style=flat&label=%E2%98%85&color=444)](https://github.com/sniperunder123/okf-knowledge/stargazers) | Python | Claude Code `/okf` skill |
| [longsizhuo/okf-frontmatter](https://github.com/longsizhuo/okf-frontmatter) | [![★](https://img.shields.io/github/stars/longsizhuo/okf-frontmatter?style=flat&label=%E2%98%85&color=444)](https://github.com/longsizhuo/okf-frontmatter/stargazers) | Python | 把仓库文档维护成 OKF 形态的 skill |
| [hermes-okf](./references/hermes-okf.md) | [![★](https://img.shields.io/github/stars/EliaszDev/hermes-okf?style=flat&label=%E2%98%85&color=444)](https://github.com/EliaszDev/hermes-okf/stargazers) | Python | 基于 OKF 的 Agent 持久记忆(PyPI) |
| [pumblus/okf-harness](https://github.com/pumblus/okf-harness) | [![★](https://img.shields.io/github/stars/pumblus/okf-harness?style=flat&label=%E2%98%85&color=444)](https://github.com/pumblus/okf-harness/stargazers) | TS | 本地优先的 agent 终端 harness |
| [scaccogatto/okf-skills](https://github.com/scaccogatto/okf-skills) | [![★](https://img.shields.io/github/stars/scaccogatto/okf-skills?style=flat&label=%E2%98%85&color=444)](https://github.com/scaccogatto/okf-skills/stargazers) | Python | Claude Code 的 OKF 技能 |
| [wiki-as-an-mcp](./references/wiki-as-an-mcp.md) | [![★](https://img.shields.io/github/stars/taikunudel/wiki-as-an-mcp?style=flat&label=%E2%98%85&color=444)](https://github.com/taikunudel/wiki-as-an-mcp/stargazers) | Python | 首个通用 Wiki MCP server |
| [superops-team/okf](./references/superops-okf.md) | [![★](https://img.shields.io/github/stars/superops-team/okf?style=flat&label=%E2%98%85&color=444)](https://github.com/superops-team/okf/stargazers) | Go | 项目级知识库 |
| [xSAVIKx/okf-skills](https://github.com/xSAVIKx/okf-skills) | [![★](https://img.shields.io/github/stars/xSAVIKx/okf-skills?style=flat&label=%E2%98%85&color=444)](https://github.com/xSAVIKx/okf-skills/stargazers) | Go | Go 实现的 OKF agentic skills |
| [okf-rag](./references/okf-rag.md) | [![★](https://img.shields.io/github/stars/killop/okf-rag?style=flat&label=%E2%98%85&color=444)](https://github.com/killop/okf-rag/stargazers) | Rust | 本地优先 OKF 检索 / RAG |
| [Sudhakaran88/okf-conformance](https://github.com/Sudhakaran88/okf-conformance) | [![★](https://img.shields.io/github/stars/Sudhakaran88/okf-conformance?style=flat&label=%E2%98%85&color=444)](https://github.com/Sudhakaran88/okf-conformance/stargazers) | JS | OKF 一致性校验器 |

## 这个仓库本身

是一个符合 OKF v0.1 的 bundle。每个 `.md` 带 frontmatter 和非空 `type`，根目录有 `index.md` 和 `log.md`：

```bash
python skills/okf-creator/scripts/validate_okf.py .
```

## 贡献

PR 欢迎。标准：跟 OKF 相关，能跑或能读。写 producer 前看 [CONTRIBUTING](./CONTRIBUTING.md)。

## 许可

云中江树 维护，微信公众号：云中江树。[MIT](./LICENSE)。