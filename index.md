---
okf_version: "0.1"
---

# Awesome OKF

> 本仓库自身就是一个符合 OKF v0.1 的知识包。本文件是 bundle 的根索引(渐进式展开);项目主页见 [README](README.md)。

# 文档与提案

* [README](README.md) - 项目总览与资源大全
* [OKF 规范中文版](docs/okf-spec-zh.md) - 规范全文翻译 + 硬要求/留白标注
* [发布博客中文版](docs/blog-zh.md) - Google Cloud 官方发布文译文
* [OKF 思想源头:Karpathy LLM Wiki](docs/karpathy-llm-wiki-zh.md) - 思想前身梳理
* [代码/PDF/图片支持度调研](docs/code-support-research-zh.md) - 实测 + 代码约定提案
* [HTML 一等公民提案](docs/html-first-class-proposal-zh.md) - 让 .html 成为合法概念
* [全网资料汇总](docs/resources-zh.md) - 官方/新闻/教程/社区
* [dogfooding 说明](docs/dogfooding-zh.md) - 本仓库如何自身合规
* [贡献指南](CONTRIBUTING.md) - 含 producer 插件约定

# Producer 插件(plugins/)

* [myokf-cli](plugins/myokf-cli/) - 统一命令行入口(myokf)
* [feishu-to-okf](plugins/feishu-to-okf/) - 飞书知识库 → OKF
* [awesome-to-okf](plugins/awesome-to-okf/) - GitHub awesome 列表 → OKF
* [obsidian-to-okf](plugins/obsidian-to-okf/) - Obsidian vault → OKF
* [notion-to-okf](plugins/notion-to-okf/) - Notion 导出 → OKF
* [html-to-okf](plugins/html-to-okf/) - HTML → OKF(双表示)
* [github-to-okf](plugins/github-to-okf/) - GitHub 仓库 → OKF

# 外部与官方资源(references/)

* [官方规范 SPEC.md](references/okf-spec.md) - OKF v0.1 规范正文
* [knowledge-catalog 仓库](references/knowledge-catalog-repo.md) - 官方总入口
* [发布博客](references/launch-blog.md) - OKF 官方发布文
* [官方参考实现](references/reference-implementations.md) - 富化 agent 与可视化器
* [官方示例 bundle](references/sample-bundles.md) - GA4 / SO / Bitcoin
* [Metadata as Code](references/metadata-as-code.md) - kcmd / mdcode
* [Karpathy 的 LLM Wiki](references/karpathy-llm-wiki.md) - OKF 思想源头
* [qmd](references/qmd.md) - Markdown 本地搜索,可作 consumer 后端
* [社区头部工具与实现](references/index.md) - 12 个按 star/成熟度择优、提升为一等概念的社区仓库(okf-knowledge / okf-rag / wiki-as-an-mcp / owox-model-canvas 等);完整 60+ 清单见 [resources-zh](docs/resources-zh.md)

# Skills(skills/)

* [okf-creator](skills/okf-creator/) - 从任意输入创建高质量 OKF
* [awesome-to-okf](skills/awesome-to-okf/) - awesome 列表导入并富化
* [book-to-okf](skills/book-to-okf/) - 书/长文拆成概念库
* [code-to-okf](skills/code-to-okf/) - 代码库 → OKF
* [github-to-okf](skills/github-to-okf/) - 仓库 → OKF 富化工作流
* [okf-to-book](skills/okf-to-book/) - OKF 发布为可视化文档站
* [okf-to-web](skills/okf-to-web/) - OKF → 单文件网页(压缩)
