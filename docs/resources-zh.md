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

> 截至 2026-06-14 的全网检索结果。OKF 发布于 2026-06-12,生态尚新,本页持续更新,欢迎 PR 补充。

## 一、官方一手资料

- [发布博客:How the Open Knowledge Format can improve data sharing](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/) —— Sam McVeety、Amir Hormati,2026-06-12。([中文译文](./blog-zh.md))
- [规范 SPEC.md(v0.1)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) —— 规范正文。([中文版](./okf-spec-zh.md))
- [knowledge-catalog 仓库](https://github.com/GoogleCloudPlatform/knowledge-catalog) —— 官方总入口。
- [okf/ 目录](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) —— 规范、参考实现、示例 bundle。
- [okf/README.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md) —— 参考实现说明(富化 agent + 可视化器)。
- [agents/mdcode(Metadata as Code / kcmd)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/agents/mdcode) —— 元数据即代码工具,含 MCP server。

## 二、思想源头:LLM Wiki(Karpathy)

- ⭐ [Andrej Karpathy, *LLM Wiki* gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) —— 2026-04-04,OKF 的直接思想前身。([中文梳理](./karpathy-llm-wiki-zh.md))
- [karpathy 的 gists 主页](https://gist.github.com/karpathy)

## 三、新闻与分析

- [Google's OKF wants to be the lingua franca for AI agent knowledge(PPC Land)](https://ppc.land/googles-okf-wants-to-be-the-lingua-franca-for-ai-agent-knowledge/)
- [Google Cloud's Open Knowledge Format Enhances AI Interoperability and Efficiency(Welcome.AI)](https://www.welcome.ai/content/google-clouds-open-knowledge-format-enhances-ai-interoperability-and-efficiency)
- [Introducing the Open Knowledge Format(develeap)](https://www.develeap.com/news/introducing-the-open-knowledge-format-51fdffd9/)
- [Google's Open Knowledge Format Could Work For Websites, Too(No Hacks)](https://nohacks.co/blog/okf-website-knowledge-graph) —— 提出 OKF 也适用于网站知识图谱,与本仓库 [HTML 一等公民提案](./html-first-class-proposal-zh.md) 思路呼应。

## 四、LLM Wiki 实践教程(与 OKF 同源)

- [LLM Wiki Revolution(Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2026/04/llm-wiki-by-andrej-karpathy/)
- [Build a Personal Knowledge Base With Claude Code(MindStudio)](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)
- [I Built Karpathy's LLM Wiki for My Day Job(Tom Nguyen, Medium)](https://tomnguyenit.medium.com/i-built-karpathys-llm-wiki-for-my-day-job-here-s-what-actually-works-0d4ec6d1e433)
- [Create your own knowledge base(Urvil Joshi, Medium)](https://medium.com/@urvvil08/andrej-karpathys-llm-wiki-create-your-own-knowledge-base-8779014accd5)
- [LLM Wiki Tutorial(Data Science Dojo)](https://datasciencedojo.com/blog/llm-wiki-tutorial/)
- [Full Breakdown(Nandigam Harikrishna, Substack)](https://nandigamharikrishna.substack.com/p/andrej-karpathys-llm-wiki-full-breakdown)
- [Build a Compounding Knowledge Base(AI Builder Club)](https://www.aibuilderclub.com/blog/karpathy-llm-wiki)
- [The Complete Guide to His Idea File(Agentpedia)](https://agentpedia.codes/blog/karpathy-llm-wiki-idea-file)
- [once as code, once as a .md(Leandro Bernardo, Towards AI)](https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a)

## 五、社区项目与镜像

- [supachai-j/llm-wiki-101](https://github.com/supachai-j/llm-wiki-101) —— 含 Karpathy gist 存档与实践。
- [Programming-With-Maury/Karpathy-LLM-Wiki](https://github.com/Programming-With-Maury/Karpathy-LLM-Wiki)
- [tobi/qmd](https://github.com/tobi/qmd) —— 本地 Markdown 搜索引擎(Karpathy 推荐,可作 OKF 的 consumer/search 后端)。

## 六、相关标准 / 邻近概念

- `AGENTS.md` / `CLAUDE.md` —— agent 约定文件家族,OKF 的 schema 层思想来源之一。
- "Metadata as Code" —— 把目录元数据与源码同放的实践。
- Obsidian / Notion / Hugo —— OKF 形态上贴近的既有 Markdown 知识工具。

---

> 收集口径:OKF 直接相关 + 其思想源头 LLM Wiki。新增请按"官方 / 新闻分析 / 教程 / 社区项目"归类提 PR。
