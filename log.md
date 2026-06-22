# Directory Update Log

> 本仓库持续收集整理,不按日期记快照。下面按"初始化"与"持续补录"两类归档。

### 初始化建立
* **Initialization**: 建立 awesome-okf——中文世界第一个 OKF 落点。
* **Creation**: OKF 规范中文版、发布博客译文、Karpathy LLM Wiki 思想梳理、全网资料汇总。
* **Creation**: 三份向上游提案——i18n、代码支持、HTML 一等公民。
* **Creation**: producer 插件——feishu / awesome-to-okf / obsidian / notion / html / github,以及统一入口 myokf-cli。
* **Creation**: Skill——okf-creator / awesome-to-okf / book-to-okf / code-to-okf / github-to-okf / okf-to-book / okf-to-web。
* **Creation**: 英文 README(README.en.md),中英双语 + i18n 约定(lang/canonical)。
* **Update**: 把仓库自身做成符合 OKF v0.1 的 bundle 并通过校验(dogfooding)。
* **Update**: 全量自检——所有脚本编译/加载、producer 产物端到端校验、SKILL frontmatter 合法。

### 持续收集整理
* **Update**: resources-zh 建「生态工具与转换器」小节,收录社区工具(okf-tools / okf-convert / OKFy / okf-generator / okf-skills / okf-builder / obsidian-okf / okf-roam / okf-dashboard / supachai-j starter),标注早期项目;并单列 references/okf-tools.md。
* **Update**: resources-zh「多语言实现与更多工具」子节——按 star 择优补录 GitHub 新项目:sniperunder123/okf-knowledge(~19⭐,/okf skill)、longsizhuo/okf-frontmatter、Sudhakaran88/okf-conformance、superops-team/okf、xSAVIKx/okf-skills、openknowledge-sh/openknowledge、W4G1/okf(首个纯 Rust 实现)、inkxel/throughline、claudiobottari/databricks-okf,以及 okf-lint / okfcli / claude-okf / wp-knowledge-layer。记录生态从 Python 扩展到 Go/Rust/TS/JS/PHP 多语言的信号。
* **Update**: resources-zh「新闻与分析」持续补录解读文章——Suganthan / explainx.ai / The Decoder / Marc Bara《A Standard, or Just a Folder?》/ innFactory / MarkTechPost / StartupHub.ai / Flowtivity / WitsCode,并记录 Hugo Issue #15035 这一生态采用信号。
* **Note**: 收录口径——OKF 直接相关 + 思想源头 LLM Wiki,按 star 择优;已存在条目(如 0dust/OKFy、scaccogatto/okf-skills、supachai-j starter)查重后跳过;纯启动报道(TechTimes / Search Engine Journal / Let's Data Science / NPowerUser 等)按"不扩列单纯报道"的口径不收。
* **Update**: resources-zh 补录新形态工具与样例——rodcar/okf-atlas-mcp(OKF→MCP server)、lars20070/pdf2okf(PDF→OKF)、dorisgyl/okf-export-pack(GBrain→OKF producer 样例),并补一篇日文解读(AI-Driven Lab, note.com);其余候选(0dust/OKFy、sniperunder123/okf-knowledge、longsizhuo/okf-frontmatter、Sudhakaran88/okf-conformance、W4G1/okf、kennyg/obsidian-okf、wooserv/wp-knowledge-layer、claudiobottari/databricks-okf、MarkTechPost、StartupHub.ai、Marc Bara)查重后均已收录,跳过。
* **Update**: resources-zh 补录在线工具、校验器与编辑器等新形态——WitsCode OKF Conformance Suite(MIT,本地零依赖、可 gate CI 的一致性校验器)、Suganthan OKF Bundle Generator(免注册的 URL/sitemap→OKF 在线生成器)、chasedputnam/okf-cli(Go,"filing cabinet"架构 + MCP + token 压缩)、akdira/okf-toolkit(Python 全功能 CLI,PyPI)、activetwist/OnyxWriter(本地优先 OKF 编辑器)、emanueleielo/deepagents-okf-backend(LangChain Deep Agents 的 OKF 虚拟文件系统后端)、OpenDPP/opendpp-knowledge(欧盟数字产品护照 API 从 live OpenAPI 再生成的真实 OKF 采用案例);「新闻与分析」补 GitBook 官方解读《What is OKF》。
* **Note**: openknowledge-sh/openknowledge、thisismydesign/okf-lint、scaccogatto/okf-skills 查重后已存在,跳过;hanfang5057-byte/okf-tool(0★ TS 库,与现有 TS 生态条目重叠)、hdean-ssp/okf-mcp(0★,同 owner 的 okf-tools + okf-atlas-mcp 已覆盖 CLI/MCP 形态)信噪比不足,跳过。
