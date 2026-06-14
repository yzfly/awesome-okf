---
type: Reference
title: OKF 全网资料汇总
description: 截至 2026-06-14 收集的开放知识格式(OKF)及其思想源头 LLM Wiki 的官方, 新闻, 分析与教程资料。
tags: [okf, 资料, reference, 汇总]
lang: zh
timestamp: 2026-06-14T00:00:00Z
author: 云中江树(整理)
---

# OKF 全网资料汇总

> 截至 2026-06-15 的全网检索结果。OKF 发布于 2026-06-12,生态尚新,本页持续更新,欢迎 PR 补充。

## 一、官方一手资料

- [发布博客:How the Open Knowledge Format can improve data sharing](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/) —— Sam McVeety、Amir Hormati,2026-06-12。([中文译文](./blog-zh.md))
- [规范 SPEC.md(v0.1)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) —— 规范正文。([中文版](./okf-spec-zh.md))
- [knowledge-catalog 仓库](https://github.com/GoogleCloudPlatform/knowledge-catalog) —— 官方总入口。
- [okf/ 目录](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) —— 规范、参考实现、示例 bundle。
- [okf/README.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md) —— 参考实现说明(富化 agent + 可视化器)。
- [okf/src/enrichment_agent](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf/src/enrichment_agent) —— BigQuery 富化 agent 参考实现源码,随规范发布的概念验证。
- [agents/mdcode(Metadata as Code / kcmd)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/agents/mdcode) —— 元数据即代码工具,含 MCP server。

## 二、思想源头:LLM Wiki(Karpathy)

- ⭐ [Andrej Karpathy, *LLM Wiki* gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) —— 2026-04-04,OKF 的直接思想前身。([中文梳理](./karpathy-llm-wiki-zh.md))
- [karpathy 的 gists 主页](https://gist.github.com/karpathy)

## 三、新闻与分析

- [Google's OKF wants to be the lingua franca for AI agent knowledge(PPC Land)](https://ppc.land/googles-okf-wants-to-be-the-lingua-franca-for-ai-agent-knowledge/)
- [Google Cloud's Open Knowledge Format Enhances AI Interoperability and Efficiency(Welcome.AI)](https://www.welcome.ai/content/google-clouds-open-knowledge-format-enhances-ai-interoperability-and-efficiency)
- [Introducing the Open Knowledge Format(develeap)](https://www.develeap.com/news/introducing-the-open-knowledge-format-51fdffd9/)
- [Google's Open Knowledge Format Could Work For Websites, Too(No Hacks)](https://nohacks.co/blog/okf-website-knowledge-graph) —— 提出 OKF 也适用于网站知识图谱,与本仓库 [HTML 一等公民提案](./html-first-class-proposal-zh.md) 思路呼应。
- [Google Cloud's Open Knowledge Format turns scattered docs into Markdown files for AI agents(The Decoder)](https://the-decoder.com/google-clouds-open-knowledge-format-turns-scattered-docs-into-markdown-files-for-ai-agents/)
- [OKF: Google's New Markdown Format for AI Agents(Suganthan)](https://suganthan.com/blog/open-knowledge-format/) —— 面向开发者的格式解读。
- [OKF: Google AI Agent Standard(explainx.ai)](https://explainx.ai/blog/google-open-knowledge-format-okf-ai-agents-2026) —— OKF 作为 AI agent 知识标准的科普解读。
- 采用信号:[Hugo Issue #15035 — Support OKF](https://github.com/gohugoio/hugo/issues/15035) —— 静态站点生成器 Hugo 关于支持 OKF 的兼容讨论,生态采纳的早期迹象。

## 四、生态工具与转换器(社区,首周项目)

> OKF 于 2026-06-12 发布,以下为本周涌现的社区工具,多数尚处早期(star 个位数),择优收录。

- [hdean-ssp/okf-tools](https://github.com/hdean-ssp/okf-tools) —— 查询/导航/创作 OKF bundle 的 CLI 与 Python 库。
- [chapter42/okf-convert](https://github.com/chapter42/okf-convert) —— 把 Markdown / 网页转换为 OKF v0.1 bundle。
- [0dust/OKFy](https://github.com/0dust/OKFy) —— 把文档转换成 agent 可读的 OKF 知识 bundle。
- [tommypacker/okf-generator](https://github.com/tommypacker/okf-generator) —— 从代码仓库生成 OKF 文件的 CLI。
- [scaccogatto/okf-skills](https://github.com/scaccogatto/okf-skills) —— 面向 Claude Code 的 OKF 技能(已发 v0.2.0)。
- [eli-l/okf-builder](https://github.com/eli-l/okf-builder) —— 兼容 Agent Skills 的 OKF bundle 创作 / 读取 / 校验流程。
- [kennyg/obsidian-okf](https://github.com/kennyg/obsidian-okf) —— 在 Obsidian 校验/创作并导出 OKF bundle 的插件。
- [zbodtorf/okf-roam](https://github.com/zbodtorf/okf-roam) —— 为 OKF bundle 提供 Roam 式导航(Emacs)。
- [ametel01/okf-dashboard](https://github.com/ametel01/okf-dashboard) —— OKF 可视化 Dashboard。

## 五、LLM Wiki 实践教程(与 OKF 同源)

- [LLM Wiki Revolution(Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2026/04/llm-wiki-by-andrej-karpathy/)
- [Build a Personal Knowledge Base With Claude Code(MindStudio)](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)
- [I Built Karpathy's LLM Wiki for My Day Job(Tom Nguyen, Medium)](https://tomnguyenit.medium.com/i-built-karpathys-llm-wiki-for-my-day-job-here-s-what-actually-works-0d4ec6d1e433)
- [Create your own knowledge base(Urvil Joshi, Medium)](https://medium.com/@urvvil08/andrej-karpathys-llm-wiki-create-your-own-knowledge-base-8779014accd5)
- [LLM Wiki Tutorial(Data Science Dojo)](https://datasciencedojo.com/blog/llm-wiki-tutorial/)
- [Full Breakdown(Nandigam Harikrishna, Substack)](https://nandigamharikrishna.substack.com/p/andrej-karpathys-llm-wiki-full-breakdown)
- [Build a Compounding Knowledge Base(AI Builder Club)](https://www.aibuilderclub.com/blog/karpathy-llm-wiki)
- [The Complete Guide to His Idea File(Agentpedia)](https://agentpedia.codes/blog/karpathy-llm-wiki-idea-file)
- [once as code, once as a .md(Leandro Bernardo, Towards AI)](https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a)

## 六、社区项目与镜像

- [supachai-j/llm-wiki-101](https://github.com/supachai-j/llm-wiki-101) —— 含 Karpathy gist 存档与实践。
- [Programming-With-Maury/Karpathy-LLM-Wiki](https://github.com/Programming-With-Maury/Karpathy-LLM-Wiki)
- [tobi/qmd](https://github.com/tobi/qmd) —— 本地 Markdown 搜索引擎(Karpathy 推荐,可作 OKF 的 consumer/search 后端)。

## 七、相关标准 / 邻近概念

- `AGENTS.md` / `CLAUDE.md` —— agent 约定文件家族,OKF 的 schema 层思想来源之一。
- "Metadata as Code" —— 把目录元数据与源码同放的实践。
- Obsidian / Notion / Hugo —— OKF 形态上贴近的既有 Markdown 知识工具。

---

> 收集口径:OKF 直接相关 + 其思想源头 LLM Wiki。新增请按"官方 / 新闻分析 / 教程 / 社区项目"归类提 PR。
