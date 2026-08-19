---
type: Overview
title: Awesome OKF
description: 中文世界第一个 OKF 落点：规范翻译、工具链、提案，以及一份活的合规范例。
tags: [okf, awesome, 中文]
lang: zh
generated: { by: human:yzfly, at: 2026-06-14T00:00:00Z }
author: 云中江树
---

# Awesome OKF

中文 | [English](./README.en.md)

开放知识格式（OKF）的中文资料和工具。规范翻译、七个 producer 插件、七个 Claude Code skill、三份向上游的扩展提案。

[OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) 是 Google Cloud 发布的一份开放规范——把知识定义为一个目录的 Markdown 文件，带 YAML frontmatter，加一小套约定。没有运行时，没有 SDK。

> 📌 **规范已升到 v0.2**：新增出处（`sources`）、信任（`generated`/`verified`）、生命周期（`status`/`stale_after`）与可验算计算（`Attested Computation`）四个家族；两处破坏性变更是 `timestamp` → `generated.at`、正文 `# Citations` → 头信息 `sources`。本仓库（规范译文、校验器、七个插件、全部文档）已完成迁移，详见 [规范中文版 §13](./docs/okf-spec-zh.md#13-与-v01-的差异)。

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

| 仓库 | ★ | 语言 | 形态 |
|---|---|---|---|
| [knowledge-catalog](./references/knowledge-catalog-repo.md)(官方) | [![★](https://img.shields.io/github/stars/GoogleCloudPlatform/knowledge-catalog?style=flat&label=%E2%98%85&color=444)](https://github.com/GoogleCloudPlatform/knowledge-catalog/stargazers) | HTML | OKF 规范 + 参考实现 + 示例 bundle 总入口 |
| [openwiki](./references/openwiki.md)(LangChain) | [![★](https://img.shields.io/github/stars/langchain-ai/openwiki?style=flat&label=%E2%98%85&color=444)](https://github.com/langchain-ai/openwiki/stargazers) | TS | LangChain 官方:为代码库写并维护 agent 文档的 CLI,**产出 OKF v0.2 bundle**(生态 star 最高) |
| [iwe](./references/iwe.md) | [![★](https://img.shields.io/github/stars/iwe-org/iwe?style=flat&label=%E2%98%85&color=444)](https://github.com/iwe-org/iwe/stargazers) | Rust | Markdown 知识图谱:编辑器 LSP + CLI + MCP,`iwe init --okf` 一等支持,模板以 v0.2 分发并在 CI 校验 |
| [zosmaai/pi-llm-wiki](https://github.com/zosmaai/pi-llm-wiki) | [![★](https://img.shields.io/github/stars/zosmaai/pi-llm-wiki?style=flat&label=%E2%98%85&color=444)](https://github.com/zosmaai/pi-llm-wiki/stargazers) | TS | 自维护、兼容 Obsidian 的知识库,原始资料→互链 wiki |
| [fellowgeek/mcp-memory](https://github.com/fellowgeek/mcp-memory) | [![★](https://img.shields.io/github/stars/fellowgeek/mcp-memory?style=flat&label=%E2%98%85&color=444)](https://github.com/fellowgeek/mcp-memory/stargazers) | Python | OKF 为底的 MCP server,给 agent 持久长期记忆 + SQL 检索 |
| [coleam00/cole-medin-knowledge-base](https://github.com/coleam00/cole-medin-knowledge-base) | [![★](https://img.shields.io/github/stars/coleam00/cole-medin-knowledge-base?style=flat&label=%E2%98%85&color=444)](https://github.com/coleam00/cole-medin-knowledge-base/stargazers) | JS | OKF 知识库 + Karpathy 式 LLM wiki 合成产物 |
| [UmairBaig8/okf-generator](https://github.com/UmairBaig8/okf-generator) | [![★](https://img.shields.io/github/stars/UmairBaig8/okf-generator?style=flat&label=%E2%98%85&color=444)](https://github.com/UmairBaig8/okf-generator/stargazers) | Python | OKF bundle 生成器:Claude skill + OpenCode 集成 |
| [jyjeanne/okf-rs](https://github.com/jyjeanne/okf-rs) | [![★](https://img.shields.io/github/stars/jyjeanne/okf-rs?style=flat&label=%E2%98%85&color=444)](https://github.com/jyjeanne/okf-rs/stargazers) | Rust | Rust 工具链:生成 / 校验 / serve OKF bundle |
| [openknowledge-sh/openknowledge](https://github.com/openknowledge-sh/openknowledge) | [![★](https://img.shields.io/github/stars/openknowledge-sh/openknowledge?style=flat&label=%E2%98%85&color=444)](https://github.com/openknowledge-sh/openknowledge/stargazers) | Go | 管理 OKF bundle 的 Go CLI |
| [saschb2b/okf-studio](https://github.com/saschb2b/okf-studio) | [![★](https://img.shields.io/github/stars/saschb2b/okf-studio?style=flat&label=%E2%98%85&color=444)](https://github.com/saschb2b/okf-studio/stargazers) | TS | OKF bundle 的原生桌面阅读器,指向一个目录即可浏览 |
| [aws-samples/sample-okf-llm-wiki](https://github.com/aws-samples/sample-okf-llm-wiki) | [![★](https://img.shields.io/github/stars/aws-samples/sample-okf-llm-wiki?style=flat&label=%E2%98%85&color=444)](https://github.com/aws-samples/sample-okf-llm-wiki/stargazers) | Python | AWS 官方示例:把数据转成 OKF bundle 并对外提供 |
| [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | [![★](https://img.shields.io/github/stars/JuneYaooo/lineage-skill?style=flat&label=%E2%98%85&color=444)](https://github.com/JuneYaooo/lineage-skill/stargazers) | Python | 带出处(lineage)蒸馏的 Agent Skill,输出 OKF 包 |
| [psinetron/echoes-vault-opencode](https://github.com/psinetron/echoes-vault-opencode) | [![★](https://img.shields.io/github/stars/psinetron/echoes-vault-opencode?style=flat&label=%E2%98%85&color=444)](https://github.com/psinetron/echoes-vault-opencode/stargazers) | TS | OpenCode 持久记忆插件,底层用 OKF |
| [guhcostan/claude-mega-brain](https://github.com/guhcostan/claude-mega-brain) | [![★](https://img.shields.io/github/stars/guhcostan/claude-mega-brain?style=flat&label=%E2%98%85&color=444)](https://github.com/guhcostan/claude-mega-brain/stargazers) | Python | Claude Code 的 OKF 知识上下文注入插件 |
| [takeshy/obsidian-gemini-helper](https://github.com/takeshy/obsidian-gemini-helper) | [![★](https://img.shields.io/github/stars/takeshy/obsidian-gemini-helper?style=flat&label=%E2%98%85&color=444)](https://github.com/takeshy/obsidian-gemini-helper/stargazers) | TS | 支持 OKF 知识源的 Obsidian Gemini 助手 |
| [coleam00/cole-medin-ai-coding](https://github.com/coleam00/cole-medin-ai-coding) | [![★](https://img.shields.io/github/stars/coleam00/cole-medin-ai-coding?style=flat&label=%E2%98%85&color=444)](https://github.com/coleam00/cole-medin-ai-coding/stargazers) | Python | Cole Medin AI 编程视频的 OKF 知识包 |
| [okf-gem](./references/okf-gem.md) | [![★](https://img.shields.io/github/stars/serradura/okf-gem?style=flat&label=%E2%98%85&color=444)](https://github.com/serradura/okf-gem/stargazers) | Ruby | 创作 skill + CLI/库 + 图谱,覆盖 bundle 全生命周期 |
| [OWOX Model Canvas](./references/owox-model-canvas.md) | [![★](https://img.shields.io/github/stars/OWOX/models?style=flat&label=%E2%98%85&color=444)](https://github.com/OWOX/models/stargazers) | TS | 可视化建模 / 创作端(公司维护) |
| [0dust/OKFy](https://github.com/0dust/OKFy) | [![★](https://img.shields.io/github/stars/0dust/OKFy?style=flat&label=%E2%98%85&color=444)](https://github.com/0dust/OKFy/stargazers) | TS | 文档 → agent 可读 OKF bundle 转换器 |
| [okf-knowledge](./references/okf-knowledge.md) | [![★](https://img.shields.io/github/stars/sniperunder123/okf-knowledge?style=flat&label=%E2%98%85&color=444)](https://github.com/sniperunder123/okf-knowledge/stargazers) | Python | Claude Code `/okf` skill |
| [PoorvaJ-WW/okft](https://github.com/PoorvaJ-WW/okft) | [![★](https://img.shields.io/github/stars/PoorvaJ-WW/okft?style=flat&label=%E2%98%85&color=444)](https://github.com/PoorvaJ-WW/okft/stargazers) | Python | OKF 规范校验器(okft lint,适合 CI)+ MCP 服务器(okft serve),pip 安装 |
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

是一个符合 OKF v0.2 的 bundle。每个 `.md` 带 frontmatter 和非空 `type`，根目录有 `index.md` 和 `log.md`：

```bash
python skills/okf-creator/scripts/validate_okf.py .
```

## 贡献

PR 欢迎。标准：跟 OKF 相关，能跑或能读。写 producer 前看 [CONTRIBUTING](./CONTRIBUTING.md)。

## 许可

云中江树 维护，微信公众号：云中江树。[MIT](./LICENSE)。
