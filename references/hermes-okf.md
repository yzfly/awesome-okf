---
type: Reference
title: hermes-okf(基于 OKF 的 Agent 持久记忆)
description: 基于 OKF 的 Agent 持久记忆系统(已上 PyPI,可作 Hermes 插件),把决策·观察·上下文存为可版本化的 markdown+YAML 知识图。
resource: https://github.com/EliaszDev/hermes-okf
tags: [okf, 记忆, agent, pypi, 社区]
lang: zh
timestamp: 2026-06-28T00:00:00Z
---

# hermes-okf(基于 OKF 的 Agent 持久记忆)

把 OKF 用作 **Agent 持久记忆层**的代表项目,新生态里 star 较突出。已发布到 PyPI,可作 Hermes 插件:把决策、观察、上下文存成 markdown+YAML 的知识图,无需数据库、可 git 版本化,提供 `search / list / show / snapshot / restore` 等命令,并可选接 LangChain / ChromaDB 做 RAG。

和它同属"OKF 当 agent 记忆 / 上下文层"方向的还有 `inkxel/throughline`(代码仓库记忆层)与 `pumblus/okf-harness`(本地 agent harness),见 [resources-zh](/docs/resources-zh.md)。

源码:<https://github.com/EliaszDev/hermes-okf>
