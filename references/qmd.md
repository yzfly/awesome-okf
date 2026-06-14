---
type: Reference
title: qmd(Markdown 本地搜索)
description: 本地 Markdown 搜索引擎,BM25+向量+LLM 重排,可作 OKF 的搜索型 consumer 后端。
resource: https://github.com/tobi/qmd
tags: [okf, 工具, 搜索, consumer]
lang: zh
timestamp: 2026-06-14T00:00:00Z
---

# qmd(Markdown 本地搜索)

Karpathy 在 LLM Wiki 里推荐的本地 Markdown 搜索引擎:混合 BM25 + 向量 + LLM 重排,全程本地;有 CLI 也有 MCP server。

因为 OKF bundle 就是 Markdown 目录,qmd 可以直接当 OKF 的**搜索型 consumer**后端用——当索引(`index.md`)不够用、规模变大时的检索方案。

源码:<https://github.com/tobi/qmd> · 思想来源见 [karpathy-llm-wiki](/references/karpathy-llm-wiki.md)。
