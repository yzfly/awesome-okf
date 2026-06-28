---
type: Reference
title: okf-cli(Go,filing cabinet 架构 + MCP)
description: Go 实现的 CLI,把文档站/Markdown 目录转为"扩展 OKF"bundle 并以 MCP 供 Claude/Codex/Cursor,主打摘要优先导航与 token 预算压缩。
resource: https://github.com/chasedputnam/okf-cli
tags: [okf, cli, go, mcp]
lang: zh
timestamp: 2026-06-28T00:00:00Z
---

# okf-cli(Go,filing cabinet 架构 + MCP)

完成度较高的 **Go** 实现:把文档站 / Markdown 目录转为"扩展 OKF"bundle,并以 MCP 供 Claude / Codex / Cursor 使用。主打"filing cabinet"架构——摘要优先导航、双向 backlink、token 预算压缩,`inspect` 在超过约 100 概念 / 约 400K token 时提示该上 RAG。

是 OKF 的 Go 生态里偏完整的 CLI+MCP 一体实现,与 Python 的 [okf-toolkit](/references/okf-toolkit.md)、Rust 的 [okf-rag](/references/okf-rag.md) 形成多语言对照。

源码:<https://github.com/chasedputnam/okf-cli>
