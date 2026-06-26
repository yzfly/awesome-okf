---
type: Reference
title: OKF 全网资料汇总
description: 持续收集整理的开放知识格式(OKF)及其思想源头 LLM Wiki 的官方, 新闻, 分析与教程资料。
tags: [okf, 资料, reference, 汇总]
lang: zh
timestamp: 2026-06-14T00:00:00Z
author: 云中江树(整理)
---

# OKF 全网资料汇总

> 全网检索结果汇总。OKF 发布于 2026-06-12,生态尚新,本页持续收集整理、定期更新,欢迎 PR 补充。

## 一、官方一手资料

- [发布博客:How the Open Knowledge Format can improve data sharing](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/) —— Sam McVeety、Amir Hormati,2026-06-12。([中文译文](./blog-zh.md))
- [规范 SPEC.md(v0.1)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) —— 规范正文。([中文版](./okf-spec-zh.md))
- [knowledge-catalog 仓库](https://github.com/GoogleCloudPlatform/knowledge-catalog) —— 官方总入口。
- [okf/ 目录](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) —— 规范、参考实现、示例 bundle。
- [okf/README.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md) —— 参考实现说明(富化 agent + 可视化器)。
- [okf/src/enrichment_agent](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf/src/enrichment_agent) —— BigQuery 富化 agent 参考实现源码,随规范发布的概念验证。
- [agents/mdcode(Metadata as Code / kcmd)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/agents/mdcode) —— 元数据即代码工具,含 MCP server。
- [okf.md/tools —— OKF 生态工具索引](https://okf.md/tools/) —— 社区维护的 OKF 工具索引页,把转换器 / CLI / skill / 查看器等生态项目集中编目,可作发现新工具的入口。

## 二、思想源头:LLM Wiki(Karpathy)

- ⭐ [Andrej Karpathy, *LLM Wiki* gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) —— 2026-04-04,OKF 的直接思想前身。([中文梳理](./karpathy-llm-wiki-zh.md))
- [karpathy 的 gists 主页](https://gist.github.com/karpathy)

## 三、新闻与分析

- [Google's OKF wants to be the lingua franca for AI agent knowledge(PPC Land)](https://ppc.land/googles-okf-wants-to-be-the-lingua-franca-for-ai-agent-knowledge/)
- [Google Cloud's Open Knowledge Format Enhances AI Interoperability and Efficiency(Welcome.AI)](https://www.welcome.ai/content/google-clouds-open-knowledge-format-enhances-ai-interoperability-and-efficiency)
- [Introducing the Open Knowledge Format(develeap)](https://www.develeap.com/news/introducing-the-open-knowledge-format-51fdffd9/)
- [Google's Open Knowledge Format Could Work For Websites, Too(No Hacks)](https://nohacks.co/blog/okf-website-knowledge-graph) —— 提出 OKF 也适用于网站知识图谱,与本仓库 [HTML 一等公民提案](./html-first-class-proposal-zh.md) 思路呼应。
- [Google Cloud's Open Knowledge Format turns scattered docs into Markdown files for AI agents(The Decoder)](https://the-decoder.com/google-clouds-open-knowledge-format-turns-scattered-docs-into-markdown-files-for-ai-agents/)
- [OKF: Google's New Markdown Format for AI Agents(Suganthan)](https://suganthan.com/blog/open-knowledge-format/) —— 面向开发者的格式解读。
- [OKF: Google AI Agent Standard(explainx.ai)](https://explainx.ai/blog/google-open-knowledge-format-okf-ai-agents-2026) —— OKF 作为 AI agent 知识标准的科普解读。
- [A Standard, or Just a Folder?(Marc Bara, Medium)](https://medium.com/@marc.bara.iniesta/googles-new-format-for-agent-context-a-standard-or-just-a-folder-82fb21d92041) —— 批判性分析:OKF 统一了"包"的结构,却刻意不统一类型/链接词表,"格式互通 ≠ 语义互通"。
- [The Open Standard That Frees Your AI Knowledge(innFactory)](https://innfactory.ai/en/blog/open-knowledge-format-okf-standard-for-ai-knowledge/) —— 面向企业:用 OKF 把分散在 Confluence/代码库/wiki 的知识收敛为可版本化、跨厂商互通的 bundle。
- 采用信号:[Hugo Issue #15035 — Support OKF](https://github.com/gohugoio/hugo/issues/15035) —— 静态站点生成器 Hugo 关于支持 OKF 的兼容讨论,生态采纳的早期迹象。
- [Google Cloud Introduces OKF: A Vendor-Neutral Markdown Spec(MarkTechPost)](https://www.marktechpost.com/2026/06/16/google-cloud-introduces-open-knowledge-format-okf-a-vendor-neutral-markdown-spec-for-giving-ai-agents-curated-context/) —— 偏技术的规范解读:强调"厂商中立、给 agent 喂精选上下文",并梳理参考实现(富化 agent + 可视化器)与三份官方样例 bundle。
- [What It Is, the Spec, and How to Use It(StartupHub.ai)](https://www.startuphub.ai/ai-news/insights/2026/google-open-knowledge-format-okf-explained-2026) —— 从"是什么 / 规范字段 / 怎么用"三段式讲清 OKF,适合入门。
- [The Markdown Standard That Could Replace Your Wiki(Flowtivity)](https://flowtivity.ai/blog/google-open-knowledge-format/) —— 把 OKF 放在"替代传统 wiki"的角度解读。
- [OKF, explained(WitsCode)](https://witscode.com/open-knowledge-format) —— 开发者向的格式拆解。
- [What is OKF? Open Knowledge Format(GitBook)](https://www.gitbook.com/blog/what-is-okf-open-knowledge-format) —— 文档平台 GitBook 官方视角:把"写给工程师/用户的同一批 Markdown"同时当作喂 agent 的知识源,解释 OKF 相对 RAG/元数据目录的"结构化遍历"优势。
- [オープンナレッジフォーマット(OKF)解説(AI-Driven Lab, note.com)](https://note.com/ai_driven/n/n8e2726b98180?hl=en) —— 日文长文,系统讲解 OKF 的设计动机、规范与用法。
- 社区讨论:[Google proposes Open Knowledge Format based on Markdown(Hacker News)](https://news.ycombinator.com/item?id=48517735) —— OKF 发布后的 HN 讨论串,集中呈现开发者社区对"基于 Markdown 的知识格式"的质疑与肯定,可一窥早期接受度。

## 四、生态工具与转换器(社区项目)

> OKF 于 2026-06-12 发布,以下为社区陆续涌现的工具,不少仍处早期,择优收录、持续补充。

- [hdean-ssp/okf-tools](https://github.com/hdean-ssp/okf-tools) —— 查询/导航/创作 OKF bundle 的 CLI 与 Python 库。
- [chapter42/okf-convert](https://github.com/chapter42/okf-convert) —— 把 Markdown / 网页转换为 OKF v0.1 bundle。
- [0dust/OKFy](https://github.com/0dust/OKFy) —— 把文档转换成 agent 可读的 OKF 知识 bundle。
- [tommypacker/okf-generator](https://github.com/tommypacker/okf-generator) —— 从代码仓库生成 OKF 文件的 CLI。
- [scaccogatto/okf-skills](https://github.com/scaccogatto/okf-skills) —— 面向 Claude Code 的 OKF 技能(已发 v0.2.0)。
- [eli-l/okf-builder](https://github.com/eli-l/okf-builder) —— 兼容 Agent Skills 的 OKF bundle 创作 / 读取 / 校验流程。
- [kennyg/obsidian-okf](https://github.com/kennyg/obsidian-okf) —— 在 Obsidian 校验/创作并导出 OKF bundle 的插件。
- [zbodtorf/okf-roam](https://github.com/zbodtorf/okf-roam) —— 为 OKF bundle 提供 Roam 式导航(Emacs)。
- [ametel01/okf-dashboard](https://github.com/ametel01/okf-dashboard) —— OKF 可视化 Dashboard。
- [supachai-j/open-knowledge-format-starter](https://github.com/supachai-j/open-knowledge-format-starter) —— 可 fork 的 AI 维护知识库 starter 模板,含 Claude Code skill、校验器与 EN/TH 双语文档(MIT)。
- [Suganthan OKF Bundle Generator](https://suganthan.com/okf-generator/) —— 免费在线生成器,免注册:贴 URL/sitemap 爬取网站(上限 100 页)即得可下载的 OKF `.zip` bundle 加一张内容/内链结构图,可直接托管到 `yoursite.com/okf/`。

### 多语言实现与更多工具(持续补录)

> 随生态铺开,工具从早期清一色 Python 小工具,扩展到 **Go / Rust / TypeScript / JS / PHP** 多语言实现,并分化出"创作 skill / 一致性校验 lint / 多语言库 / 真实知识库样例"几条线。以下按 GitHub 热度(star)择优补录。

- [sniperunder123/okf-knowledge](https://github.com/sniperunder123/okf-knowledge) —— ⭐ 可移植的 Claude Code skill(`/okf`),创建 / 读取 / 维护 / 可视化 OKF bundle,知识即可 git 版本化的纯 Markdown。本批星标最高(~19⭐)。
- [longsizhuo/okf-frontmatter](https://github.com/longsizhuo/okf-frontmatter) —— 把仓库文档维护成 OKF 形态的 skill,附 `find_docs.py` 做"grep 优先、脚本兜底"的快速 doc/schema 查找。
- [Sudhakaran88/okf-conformance](https://github.com/Sudhakaran88/okf-conformance) —— 专做 OKF 一致性(conformance)判定的工具:一个 bundle 是否正确遵循规范。
- [superops-team/okf](https://github.com/superops-team/okf) —— **Go** 实现,定位为 AI Agent 的项目级知识库。
- [xSAVIKx/okf-skills](https://github.com/xSAVIKx/okf-skills) —— **Go** 实现的 OKF agentic skills(与已收录的 scaccogatto/okf-skills 同名不同源)。
- [openknowledge-sh/openknowledge](https://github.com/openknowledge-sh/openknowledge) —— **Go** CLI,管理 OKF bundle,带独立站点 [openknowledge.sh](https://openknowledge.sh)。
- [W4G1/okf](https://github.com/W4G1/okf) —— **纯 Rust、零依赖**的 OKF 实现,生态里第一个系统级语言实现。
- [inkxel/throughline](https://github.com/inkxel/throughline) —— OKF 原生的代码仓库"记忆层":让"为什么这么做"的上下文跨 AI 编码会话存活,导出为 OKF。
- [rodcar/okf-atlas-mcp](https://github.com/rodcar/okf-atlas-mcp) —— 把 OKF bundle 暴露为 MCP server,让 agent 通过 MCP 直接查询 OKF 知识。
- [dynamicfeed/signed-okf](https://github.com/dynamicfeed/signed-okf) —— 为 OKF bundle 加一层可验证信任:对每个文件做哈希、连同来源信息打包进 manifest 并用 Ed25519 签名(`sign_okf.py` / `verify_okf.py`),消费方可凭公钥校验"来源是否可信、内容是否被篡改"。纯附加、spec 兼容(只加可选 frontmatter 键与一个非保留名的 manifest 文件,删掉即退回普通 bundle),填补 OKF 缺失的防篡改 / 溯源空白,属少见的"信任 / 安全"方向。
- [davebarnwell/okfdump](https://github.com/davebarnwell/okfdump) —— **Go** CLI,把 MySQL / Postgres 数据库 dump 成 OKF v0.1 bundle:为每个 schema / 表 / 列 / 外键关系各写一篇 Markdown,产物静态可提交 git、可直接喂 agent 当数据库上下文,填补"关系库 → OKF"缺口。
- [lars20070/pdf2okf](https://github.com/lars20070/pdf2okf) —— 把 PDF 转换成 OKF 知识库的 producer。
- [021gink/bili2okf](https://github.com/021gink/bili2okf) —— **Python** 转换器:把 B 站视频(元数据 / 字幕或 ASR 转写 + 全量评论去重)蒸馏成 OKF v0.1 md 包,再由会话做"内容提炼 + 讨论观点提炼"两层蒸馏,内置校验;支持 `search` 召回候选。面向中文视频生态的"信源→OKF"转换器,与 pdf2okf 互补。
- [claudiobottari/databricks-okf](https://github.com/claudiobottari/databricks-okf) —— 把 Databricks AWS 官方文档经 llm-wiki 流程编译成 OKF bundle 的真实样例。
- [dorisgyl/okf-export-pack](https://github.com/dorisgyl/okf-export-pack) —— 把 GBrain 知识导出为 OKF v0.1 bundle 的 producer 样例。
- [WitsCode OKF Conformance Suite](https://witscode.com/okf-conformance) —— 免费开源(MIT)的 OKF 一致性校验器:Node 本地零依赖、免账号,逐文件按 spec 给 pass/fail(YAML frontmatter 可解析、`type` 非空、保留文件 index.md/log.md 结构),输出人读摘要 + JSON,退出码可 gate CI;刻意只验互通性、不验语义完整。
- [chasedputnam/okf-cli](https://github.com/chasedputnam/okf-cli) —— **Go**,把文档站/Markdown 目录转为"扩展 OKF"bundle 并以 MCP 供 Claude/Codex/Cursor;主打"filing cabinet"架构:摘要优先导航、双向 backlink、token 预算压缩、`inspect` 在超 ~100 概念/~400K token 时提示该上 RAG。完成度较高。
- [akdira/okf-toolkit](https://github.com/akdira/okf-toolkit) —— **Python** 全功能 CLI(已上 PyPI):init/new/validate/list/show/index/search/graph/stats,覆盖创建、校验、检索、Mermaid 链接图与统计。
- [activetwist/OnyxWriter](https://github.com/activetwist/OnyxWriter) —— 本地优先的 OKF bundle 编辑器(Tauri 桌面壳 + Tiptap 可视化 / CodeMirror 原文双模式),带校验面板与交互式 bundle 图(含坏链高亮);现 alpha 阶段。
- [emanueleielo/deepagents-okf-backend](https://github.com/emanueleielo/deepagents-okf-backend) —— 为 LangChain Deep Agents 提供 OKF 感知的虚拟文件系统后端(已上 PyPI):把 OKF bundle 挂成 agent 的文件系统,按 `type`/`tags`/`title` 语义查询,且每次写入都校验为合法 OKF。
- [EliaszDev/hermes-okf](https://github.com/EliaszDev/hermes-okf) —— 基于 OKF 的 Agent 持久记忆系统(已上 PyPI,可作 Hermes 插件):把决策 / 观察 / 上下文存为 markdown+YAML 的知识图,无需数据库、可版本化,提供 `search/list/show/snapshot/restore` 等命令,并可选接 LangChain / ChromaDB 做 RAG。新生态里 star 较突出。
- [catancs/okf-skill](https://github.com/catancs/okf-skill) —— ⭐ OKF 工具包式 skill:校验 / 查询 / lint / 创建一站式,面向 Claude Code 工作流。本批 skill 类星标较高(~2⭐)。
- [siculo/okf-skills](https://github.com/siculo/okf-skills) —— 创建并维护 OKF bundle 的 AI agent skills(与已收录的 scaccogatto / xSAVIKx 同名不同源)。
- [travisjakel/okf-ingest](https://github.com/travisjakel/okf-ingest) —— 摄取工具:校验 OKF bundle 并载入 DuckDB,支持 R / Python 语义搜索,把 OKF 接到分析栈里查询。
- [chntnm/akasha](https://github.com/chntnm/akasha) —— 3D WebGL 知识图谱浏览器,可加载 OKF bundle 做沉浸式概念关系浏览。
- [ryansann/okfview](https://github.com/ryansann/okfview) —— 轻量 OKF 查看器,渲染并导航 bundle 内容。
- [ryansann/okftool](https://github.com/ryansann/okftool) —— **Rust** 实现的可嵌入 OKF 校验器 + linter,"one core, three surfaces":同一内核分发为原生 CLI、WASM/npm 包与可嵌入 crate;内置 18 条 lint 规则、3 套 profile,已连发多个 release。工程成熟度高于一般玩具校验器,与已收录 okf-lint / WitsCode 形成 Rust 内核 + 三端分发的差异化。
- [MartinForReal/okf-enforcer](https://github.com/MartinForReal/okf-enforcer) —— **TypeScript** Obsidian 插件,在 vault 内强制 OKF v0.1:逐笔记按 spec §9 校验 frontmatter(error/warning 分级)、全库不合规侧栏报告、状态栏指示、非破坏 auto-fix 补全缺失字段,并自动生成 §6 `index.md` 列表与 §7 `log.md` 条目;大库分批非阻塞扫描。区别于已收录 obsidian-okf 的编辑定位,主打"强制 / 治理"。
- [knaisoma/data-olympus](https://github.com/knaisoma/data-olympus) —— **Python**,OKF 兼容的"治理级"知识库 profile(预发布):在 OKF 之上加稳定 `id`、受控 `type`/`status`/`tier` 字段与 `supersedes` 决策溯源链,配单写入者 MCP server(advisory lock + 按会话 worktree + 持久 push 队列)防多 agent 并发写入冲突,纯 git-native、无数据库。任何 OKF consumer 可读其 bundle,角度少见、有真实代码。
- [killop/okf-rag](https://github.com/killop/okf-rag) —— **Rust** CLI + stdio MCP server,本地优先的 OKF/Markdown 检索系统:本地 ONNX MiniLM 嵌入(无远程 API)、zvec 向量做混合检索,文件监听变更自动重建索引,附 benchmark(Recall@1 95.35%、5.3ms)并随包发预编译二进制免编译。把"OKF→RAG"这一环补上,在生态里 star 较突出。
- [agentic-wiki/wiki](https://github.com/agentic-wiki/wiki) —— **Go** 单文件静态二进制 CLI,管理 OKF 包:按 type/tag/path 查询、链接健康检查、列未完成任务、一致性校验(`status`/`list`/`check`/`tasks`),JSON 输出 + 脚本退出码,提供预编译二进制。Go 实现区别于已收录的 Python/JS 校验工具(同组织另有 [agentic-wiki/template](https://github.com/agentic-wiki/template) 模板仓库)。
- [sljm12/llm_wiki_okf_web](https://github.com/sljm12/llm_wiki_okf_web) —— **Next.js + FastAPI** 的 OKF 包 Web 前端:分类浏览、BM25 全文搜索、交互式关系图、时间线视图,后端用 repository 模式抽象数据访问、可在文件系统 / PostgreSQL 后端间切换。OKF Web 浏览器形态,功能完整但仍早期。
- [OWOX/owox-model-canvas](https://github.com/OWOX/owox-model-canvas)([在线版 model.owox.com](https://model.owox.com)) —— 数据平台公司 OWOX 出品的「类 Miro」可视化数据建模编辑器(**TS/React/Vite/Fastify**):在画布上拖拽数据集市(表 / 视图 / SQL)节点与可 join 的关系边、套行业模板、用 AI(Gemini)从 schema 元数据生成「这个模型能回答哪些业务问题」,可一键推送到 OWOX Data Marts,并**读写 / 导出 OKF 规范的 Markdown+YAML bundle**(可往返 round-trip),自我定位为「OKF 格式的可视化创作 / 导出前端」。生态里少见的成型、已公网部署、有公司维护的**可视化建模 / 创作端**。
- [pumblus/okf-harness](https://github.com/pumblus/okf-harness) —— 面向 agent、本地优先的终端 harness(v0.5.1):维护一个 OKF 兼容的 LLM Wiki,把知识当作可 git 版本化的纯 Markdown,在终端里读写 / 检索 bundle。定位偏"agent 的本地知识工作台",区别于纯 CLI / 校验器。
- [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) —— 把视频 / 书籍 / PDF / 笔记蒸馏成"带出处(lineage)"的 Agent Skill,新增 OKF 兼容知识包输出:每条结论可回溯到原始信源。多源信息 → 有溯源的 OKF bundle,与 pdf2okf / bili2okf 等单一信源转换器互补。
- [psinetron/echoes-vault-opencode](https://github.com/psinetron/echoes-vault-opencode) —— OpenCode 的持久记忆插件(EchoesVault),底层用 Google OKF 做纯 Markdown 知识库:把会话记忆 / 上下文沉淀为可版本化的 OKF bundle,跨会话存活。把 OKF 接到 OpenCode 生态的记忆层,与 hermes-okf 同属"agent 持久记忆"方向。
- [OpenDPP/opendpp-knowledge](https://github.com/OpenDPP/opendpp-knowledge) —— 真实 API 采用案例:把 OpenDPP(欧盟数字产品护照)Integration API 从 live OpenAPI 重新生成为 OKF bundle,每个 endpoint/schema/webhook 一篇交叉链接的 Markdown,随 API 版本刷新不漂移。
- [JayOram/MJML-ai-knowledge](https://github.com/JayOram/MJML-ai-knowledge) —— 知识库样例:把 MJML 邮件框架知识同时以 Claude skill 与 OKF bundle 两种格式发布,示范"一份知识、两种 agent 消费形态"。
- [thisismydesign/okf-lint](https://github.com/thisismydesign/okf-lint)(TS linter)/ [okfcli/okf](https://github.com/okfcli/okf)(Go CLI 工具链,带 [落地页](https://github.com/okfcli/okf-site))/ [theesfeld/claude-okf](https://github.com/theesfeld/claude-okf)(skill + 审计 agent + 会话 hook 的 Claude Code 插件)/ [wooserv/wp-knowledge-layer](https://github.com/wooserv/wp-knowledge-layer)(把内容转成 OKF 的 WordPress 插件)/ [betmoar/cc-okf-plugin](https://github.com/betmoar/cc-okf-plugin)(读写 / 校验 / 维护 OKF 的 Claude Code 插件)—— 同期涌现的 lint / CLI / 插件类项目,尚处早期,一并存档。

## 五、LLM Wiki 实践教程(与 OKF 同源)

- [LLM Wiki Revolution(Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2026/04/llm-wiki-by-andrej-karpathy/)
- [Build a Personal Knowledge Base With Claude Code(MindStudio)](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)
- [I Built Karpathy's LLM Wiki for My Day Job(Tom Nguyen, Medium)](https://tomnguyenit.medium.com/i-built-karpathys-llm-wiki-for-my-day-job-here-s-what-actually-works-0d4ec6d1e433)
- [Create your own knowledge base(Urvil Joshi, Medium)](https://medium.com/@urvvil08/andrej-karpathys-llm-wiki-create-your-own-knowledge-base-8779014accd5)
- [LLM Wiki Tutorial(Data Science Dojo)](https://datasciencedojo.com/blog/llm-wiki-tutorial/)
- [Full Breakdown(Nandigam Harikrishna, Substack)](https://nandigamharikrishna.substack.com/p/andrej-karpathys-llm-wiki-full-breakdown)
- [Build a Compounding Knowledge Base(AI Builder Club)](https://www.aibuilderclub.com/blog/karpathy-llm-wiki)
- [The Complete Guide to His Idea File(Agentpedia)](https://agentpedia.codes/blog/karpathy-llm-wiki-idea-file)
- [once as code, once as a .md(Leandro Bernardo, Towards AI)](https://pub.towardsai.net/i-built-karpathys-llm-wiki-twice-once-as-code-once-as-a-md-heres-what-each-one-gives-up-08b31170999a)

## 六、社区项目与镜像

- [supachai-j/llm-wiki-101](https://github.com/supachai-j/llm-wiki-101) —— 含 Karpathy gist 存档与实践。
- [Programming-With-Maury/Karpathy-LLM-Wiki](https://github.com/Programming-With-Maury/Karpathy-LLM-Wiki)
- [tobi/qmd](https://github.com/tobi/qmd) —— 本地 Markdown 搜索引擎(Karpathy 推荐,可作 OKF 的 consumer/search 后端)。

## 七、相关标准 / 邻近概念

- `AGENTS.md` / `CLAUDE.md` —— agent 约定文件家族,OKF 的 schema 层思想来源之一。
- "Metadata as Code" —— 把目录元数据与源码同放的实践。
- Obsidian / Notion / Hugo —— OKF 形态上贴近的既有 Markdown 知识工具。

---

> 收集口径:OKF 直接相关 + 其思想源头 LLM Wiki。新增请按"官方 / 新闻分析 / 教程 / 社区项目"归类提 PR。
