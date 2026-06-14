---
name: okf-creator
description: "把任意输入(代码库, 文档, 数据表结构, 笔记)梳理成符合开放知识格式(OKF v0.1)的知识包(bundle), 强调正文质量而不只是结构合规. 适用场景包括从零创建 OKF 知识库, 为代码库生成知识文档, 把零散资料整理为可被 AI 智能体消费的 Markdown 概念库, 校验和修复 bundle 的符合性. 当用户提到 OKF, 开放知识格式, 知识包, knowledge bundle, 或需要把资料整理成 agent 可读的结构化知识时触发."
type: Skill
title: OKF Creator
lang: zh
tags: [okf, skill, 知识库, 代码]
license: MIT
---

# OKF Creator

把任意输入整理成**符合 OKF v0.1 且正文质量过关**的知识包。OKF 的硬要求极低(任何带 `type` 的 Markdown 就合规),所以本 Skill 的真正价值不在"产出合规文件",而在"产出**读了就懂、agent 检索得动**的知识"。

## 何时使用

- 从零创建一个 OKF 知识库;
- 为一个代码库 / 文档站 / 数据表生成知识文档;
- 把零散笔记、Wiki、PDF 抽取文本整理成概念库;
- 校验并修复一个 bundle 的 OKF 符合性。

## 核心原则(顺序很重要)

1. **先定边界,再动手。** 问清楚:知识的来源是什么?消费者是人还是 agent?要覆盖哪些概念?不要一上来就铺目录。
2. **一个概念一个文件。** 文件路径即概念身份(concept ID)。按领域而非按文件类型组织。
3. **正文用结构,不用流水账。** 偏好标题 / 列表 / 表格 / 代码块。规范只约定 `# Schema`、`# Examples`、`# Citations` 三个标题——适用就用。
4. **链接成图。** 概念之间用普通 Markdown 链接互连,推荐包内绝对路径 `/path/to/x.md`。
5. **质量自检。** 每个概念问自己:一个没上下文的人/agent,只读这一篇,能用起来吗?不能就补。

## 工作流

1. **梳理来源**,列出要捕获的概念清单(先列再写)。
2. 用 `scripts/scaffold_okf.py` 生成骨架(根 `index.md` + `log.md` + 目录)。
3. 逐个写概念文档:头信息(`type` 必填)+ 结构化正文 + 交叉链接 + 必要的 `# Citations`。
4. 写 / 更新各级 `index.md`(渐进式展开)与根 `log.md`。
5. 用 `scripts/validate_okf.py <bundle>` 校验,修到 0 错误。

## 头信息规范

```yaml
---
type: <必填,概念种类>      # 唯一硬要求
title: <显示名>
description: <一句话摘要>   # 强烈建议:索引/搜索靠它
resource: <底层资产 URI>   # 抽象概念可省略
tags: [<标签>, ...]
timestamp: <ISO 8601>
lang: zh                   # 本仓库 i18n 约定(可选扩展)
---
```

详细字段、保留文件名、链接规则见 [references/okf-spec-cheatsheet.md](references/okf-spec-cheatsheet.md)。

## 处理代码 / PDF / 图片(OKF 原生支持弱,按本约定补)

> 背景见 [docs/code-support-research-zh.md](../../docs/code-support-research-zh.md)。

- **代码**:`type` 用 `Repository|Package|Module|Class|Function|Interface|Config|Script|Notebook`;加扩展字段 `language`、`symbol`、`signature`;`resource` 用 GitHub permalink 带行号锚点 `#L10-L40`;关系链接用 `calls:` / `depends-on:` / `deprecated-by:` 前缀。正文必写 `# Signature` 和行为说明,别只贴代码。
- **PDF**:原件放 `assets/`,正文承载**抽取出的文本/表格**,`# Source` 注明页码。
- **图片**:原件放 `assets/`,正文写**图说 / OCR 文本**(用多模态模型生成),否则图里的知识 agent 读不到。

## 反模式(别这么干)

- ❌ 把整本文档塞进一个巨型概念文件;
- ❌ 正文全是散文、没有结构,导致 agent 检索不到要点;
- ❌ 只贴代码不解释行为;
- ❌ 图片直接 `![](...)` 嵌入就完事,不写图说;
- ❌ 跳过 `validate_okf.py`。

## 配套脚本

- `scripts/scaffold_okf.py` — 生成空 bundle 骨架。
- `scripts/validate_okf.py` — OKF v0.1 符合性校验(可独立使用)。

## 相关 Skill

- `awesome-to-okf` — 专门把 GitHub awesome 列表转成 OKF。
- `book-to-okf` — 把长文 / 书稿拆成 OKF 概念库。
- `okf-to-book` — 把 OKF bundle 发布为可视化文档站。
