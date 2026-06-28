---
type: Reference
title: okf-rag(本地优先 OKF 检索 / RAG)
description: Rust CLI + stdio MCP server,本地优先的 OKF/Markdown 检索系统,本地 ONNX 嵌入 + 向量混合检索,补上"OKF→RAG"一环。
resource: https://github.com/killop/okf-rag
tags: [okf, rag, 检索, rust, mcp]
lang: zh
timestamp: 2026-06-28T00:00:00Z
---

# okf-rag(本地优先 OKF 检索 / RAG)

把 "OKF → RAG" 这一环补上的代表实现,在生态里 star 较突出。**Rust** 写的 CLI + stdio MCP server,本地优先:用本地 ONNX MiniLM 嵌入(无远程 API)、zvec 向量做混合检索,文件监听变更自动重建索引;附 benchmark(Recall@1 95.35%、5.3ms),随包发预编译二进制免编译。

当 bundle 规模变大、索引(`index.md`)与 grep 不够用时的检索方案,与同为 consumer 后端的 [qmd](/references/qmd.md)、走 MCP 的 [wiki-as-an-mcp](/references/wiki-as-an-mcp.md) 形成互补。

源码:<https://github.com/killop/okf-rag>
