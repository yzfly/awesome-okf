---
type: Reference
title: OpenWiki(LangChain 官方,产出 OKF v0.2 bundle)
description: LangChain 官方的 agent 文档 CLI,为代码库撰写并持续自更新文档,两种模式都产出 OKF v0.2 bundle;目前 OKF 生态 star 最高的项目。
resource: https://github.com/langchain-ai/openwiki
tags: [okf, v0.2, langchain, 文档, cli, 生态信号]
lang: zh
generated: { by: human:yzfly, at: 2026-08-19T00:00:00Z }
sources:
  - id: repo
    resource: https://github.com/langchain-ai/openwiki
    title: langchain-ai/openwiki 仓库与 README
  - id: blog
    resource: https://www.langchain.com/blog/openwiki-0-2-adds-okf-support
    title: OpenWiki 0.2 adds OKF support(LangChain 官方博客)
---

# OpenWiki(LangChain 官方,产出 OKF v0.2 bundle)

**目前 OKF 生态 star 最高的项目(15k+★,TypeScript,MIT)**,也是本轮最重要的生态信号:OKF 第一次被一个主流 agent 基础设施厂商当作**默认知识产物格式**,而不再只是社区自发实现。

OpenWiki 本身是一个 CLI——为你的代码库撰写并维护 agent 文档,并可通过 GitHub Actions / GitLab CI / Bitbucket Pipelines **自更新**。它与 OKF 的关系不是"多支持一种导出",而是把 OKF 当成产物本身:[^blog]

- 两种运行模式都产出 **OKF v0.2 bundle**,因此产物可移植到任意 OKF 消费者;
- 每个概念文档带 YAML 头信息与非空 `type`(§11 的硬要求),其余标准字段可选;
- 概念之间用标准 Markdown 链接表达关系(§6);
- `index.md` 与 `log.md` 按保留文件名处理,根索引声明 `okf_version: "0.2"`(§8/§9/§12);
- **生产者自定义扩展字段在更新与迁移中被保留**——正好对应 §4.1"消费者应当在往返读写时保留未知键";
- 附带经过校验的 Mermaid 图。[^repo]

# 为什么值得单列

生态里的工具大多是"社区个人实现",而 OpenWiki 的意义在于**需求方向的确认**:写文档的工具主动选择 OKF 作为输出,说明 OKF 想解决的"知识在工具之间可移植"确实被产业侧需要。它同时也是 v0.2 的一个事实标准参考——想知道一个真实世界的 v0.2 bundle 长什么样,读它的产出比读规范更快。

与本仓库的关系:[`github-to-okf`](/plugins/github-to-okf/) 与 [`code-to-okf`](/skills/code-to-okf/) 处理的是同一场景(代码库 → 知识),但走的是确定性抽取 + 中文富化;OpenWiki 走的是 agent 撰写 + CI 自更新,可互为参照。

源码:<https://github.com/langchain-ai/openwiki> · 官方博客:<https://www.langchain.com/blog/openwiki-0-2-adds-okf-support>
