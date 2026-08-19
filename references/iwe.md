---
type: Reference
title: IWE(Markdown 知识图谱,OKF 一等支持)
description: Rust 写的 Markdown 知识图谱,编辑器 LSP + CLI + MCP 记忆后端;iwe init --okf 脚手架合规 bundle,官方 workspace 模板以 OKF v0.2 分发并在 CI 校验。
resource: https://github.com/iwe-org/iwe
tags: [okf, v0.2, rust, lsp, mcp, 知识图谱]
lang: zh
generated: { by: human:yzfly, at: 2026-08-19T00:00:00Z }
sources:
  - id: repo
    resource: https://github.com/iwe-org/iwe
    title: iwe-org/iwe 仓库与 README
  - id: docs
    resource: https://iwe.md/docs/agentic/okf/
    title: IWE 官方文档 · OKF 章节
---

# IWE(Markdown 知识图谱,OKF 一等支持)

**Rust,Apache-2.0,1.5k+★。** 生态里少见的"OKF 不是附加导出,而是一等能力"的实现,而且它比 OKF 更早存在——IWE 本来就在管理"带 YAML 头信息的 Markdown 目录",OKF 发布后它发现自己管的正是同一种东西。[^repo]

三种形态共用同一份笔记:

- **编辑器 LSP** —— VS Code / Neovim / Zed / Helix 里的搜索、重构、重命名、补全;
- **CLI** —— 批处理与脚本化;
- **MCP server** —— 给 agent 提供父级上下文与结构化导航。

OKF 相关的三条能力:[^docs]

| 命令 | 作用 |
|---|---|
| `iwe init --okf` | 脚手架出一个合规 bundle |
| `iwe schema validate` | 机械校验合规性 |
| `iwe find --filter '{type: …}'` | 直接按 OKF 头信息查询 |

官方两个 workspace 模板——[marketing-workspace](https://github.com/iwe-org/marketing-workspace)(营销 agent 的活动记忆)与 [dev-workspace](https://github.com/iwe-org/dev-workspace)(编码 agent 的项目记忆)——**以 OKF v0.2 bundle 形式分发,并在每次提交的 CI 里校验**。这是生态里为数不多"把 v0.2 合规性纳入持续集成"的做法,可直接抄。

# 主张

IWE 的口号是**按结构检索,而不是靠相似度猜**:链接构成图,同一篇笔记可以属于多个主题而无需复制文件;agent 拿到的是结构化的父级上下文,而不是向量检索命中的碎片。这与本仓库收录的 [okf-rag](/references/okf-rag.md)(本地嵌入 + 向量混合检索)构成路线上的对照——一个走结构,一个走相似度,规模变大后各有取舍。性能上号称 20000 个文件亚秒级处理。

源码:<https://github.com/iwe-org/iwe> · 文档:<https://iwe.md/docs/agentic/okf/>
