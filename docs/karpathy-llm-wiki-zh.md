---
type: Article
title: OKF 的思想源头——Karpathy 的 LLM Wiki
description: Andrej Karpathy 2026-04-04 发布的 llm-wiki gist 的中文梳理与原文链接,以及 OKF 如何从中长出。
tags: [okf, karpathy, llm-wiki, 思想源头]
lang: zh
canonical: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
timestamp: 2026-04-04T00:00:00Z
author: 云中江树(整理)
---

# OKF 的思想源头:Karpathy 的 LLM Wiki

> 原文:[Andrej Karpathy, *LLM Wiki* (GitHub gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · 发布于 2026-04-04
> OKF 官方发布博客明确引用了这篇 gist,称它"把这个想法说得最为干脆"。要理解 OKF 为什么长这样,得先读这篇。

## 一句话

> "Obsidian 是 IDE;LLM 是程序员;wiki 是代码库。"——Karpathy

把知识当代码来"编译":不要每次提问都对原始文档做 RAG 检索(等于每次从零重新发现知识),而是让 LLM **增量地构建并维护一座持久的 wiki**——一堆互相链接的 Markdown 页面,夹在你和原始资料之间。知识只编译一次,然后持续保鲜,而非每次重新推导。

## 核心区别:RAG vs LLM Wiki

| | RAG | LLM Wiki |
|---|---|---|
| 知识 | 每次查询临时检索片段 | 一次编译成持久产物,持续累积 |
| 交叉引用 | 每次重新拼 | 已经在那儿了 |
| 矛盾/过时 | 不处理 | 已被标注 |
| 随时间 | 不增值 | 越用越富 |

**关键词:持久、复利(compounding)。** 你负责找源、探索、问对问题;LLM 负责总结、交叉引用、归档、记账这些"没人愿意干但让知识库真正有用"的脏活。

## 三层架构(OKF 的直接前身)

1. **Raw sources(原始资料)**——你精选的源文档,**不可变**,LLM 只读不改,是事实来源。
2. **The wiki**——LLM 生成的 Markdown 目录:摘要、实体页、概念页、对比、总览、综合。这一层 LLM 完全拥有,你只读。
3. **The schema**——一份告诉 LLM "wiki 怎么组织、有哪些约定、各种工作流怎么走"的文档,如 `CLAUDE.md` / `AGENTS.md`。它让 LLM 成为有纪律的 wiki 维护者,而非泛泛的聊天机器人。

## 三种操作

- **Ingest(摄入)**:丢一个新源进来 → LLM 读它、和你讨论要点、写摘要页、更新索引、更新相关实体/概念页、往 log 追加一条。一个源可能动 10–15 个页面。
- **Query(查询)**:对 wiki 提问 → LLM 找相关页、读、带引用综合作答。**好答案可以回填成新页面**,让探索也复利。
- **Lint(体检)**:定期让 LLM 健康检查——找矛盾、过时论断、孤儿页、缺页的重要概念、缺失的交叉引用、可补的数据缺口。

## 两个特殊文件(OKF §6/§7 的来源)

- **`index.md`**:面向内容的目录,每页一条链接 + 一句话摘要 + 可选元数据,按类别组织,每次 ingest 更新。先读索引再钻页面——在中等规模(~100 源、数百页)出奇地好用,免掉了 embedding RAG 基建。
- **`log.md`**:面向时间的只读追加记录。小技巧:每条以一致前缀开头(如 `## [2026-04-02] ingest | 文章标题`),日志就能被 unix 工具解析:`grep "^## \[" log.md | tail -5`。

> 📌 **OKF 正是把这套"个人约定"标准化了**:`index.md`(渐进式展开)、`log.md`(日期前缀的时间线)几乎原样进入了 [OKF 规范](./okf-spec-zh.md) §6、§7。OKF 干的事,就是给 Karpathy 这套自用模式补上"不同生产者/消费者之间互通"的那一小层契约。

## 一个被 OKF 继承的痛点:图片

Karpathy 原文专门提醒:**"LLM 无法在一次读取里原生读懂含内嵌图片的 Markdown"**——变通办法是先读文字、再单独看引用的图片。

这恰好印证了本仓库 [代码/PDF/图片支持调研](./code-support-research-zh.md) 的判断:图片在 OKF 里不是一等公民,图里的知识必须先被抽成文字才能被 agent 用上。

## 配套工具(原文提到)

- [qmd](https://github.com/tobi/qmd)——本地 Markdown 搜索引擎(BM25+向量+LLM 重排),有 CLI 也有 MCP server;
- Obsidian Web Clipper(网页转 Markdown)、Obsidian 图谱视图、Marp(Markdown 幻灯片)。

## 延伸阅读(社区对 LLM Wiki 的实践)

- [LLM Wiki Revolution(Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2026/04/llm-wiki-by-andrej-karpathy/)
- [How to Build a Personal Knowledge Base With Claude Code(MindStudio)](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)
- [I built Karpathy's LLM Wiki twice — once as code, once as a .md(Towards AI)](https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a)
- [LLM Wiki Tutorial(Data Science Dojo)](https://datasciencedojo.com/blog/llm-wiki-tutorial/)

完整外部资料见 [resources-zh.md](./resources-zh.md)。
