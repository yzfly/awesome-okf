---
type: Reference
title: wiki-as-an-mcp(首个通用 Wiki MCP server)
description: 首个遵循 OKF 的通用 Wiki MCP server,把一个 OKF bundle 当 wiki 通过 MCP 暴露给 agent 直接读写检索。
resource: https://github.com/taikunudel/wiki-as-an-mcp
tags: [okf, mcp, wiki, 社区, 头部]
lang: zh
timestamp: 2026-06-28T00:00:00Z
---

# wiki-as-an-mcp(首个通用 Wiki MCP server)

OKF 的 MCP 形态里星标较高的头部项目(~10⭐):首个遵循 OKF 的**通用 Wiki MCP server**。把一个 OKF bundle 当作 wiki,通过 MCP 暴露给 agent,让 agent 直接读写、检索其中的知识。

和 [okf-rag](/references/okf-rag.md)、[qmd](/references/qmd.md) 一样属于"consumer 端":区别在于它走 MCP 协议、定位是通用 wiki 接口,而非检索引擎。另一个把 OKF 暴露成 MCP 的实现是 `rodcar/okf-atlas-mcp`,见 [resources-zh](/docs/resources-zh.md)。

源码:<https://github.com/taikunudel/wiki-as-an-mcp>
