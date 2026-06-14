---
type: Article
title: OKF 对代码 / PDF / 图片的支持度调研
description: 实测官方仓库后的结论——OKF v0.1 面向数据知识,对源代码、PDF、图片的原生支持薄弱,附可落地的扩展约定提案。
tags: [okf, 代码, pdf, 图片, 调研, 提案]
lang: zh
timestamp: 2026-06-14T00:00:00Z
author: 云中江树
---

# OKF 对代码 / PDF / 图片的支持度调研

> 结论先行:**OKF v0.1 是为"数据知识"设计的(表、数据集、指标、术语表、操作手册),对源代码、PDF、图片缺乏原生表达能力。其中代码最弱。** 这不是 bug,是 scope 的边界——但对中文社区想做的"教程/代码库 → 知识"场景,这正是必须补的口子。

## 一、调研方法与证据

直接核查官方仓库 [`GoogleCloudPlatform/knowledge-catalog`](https://github.com/GoogleCloudPlatform/knowledge-catalog):

1. **三个官方示例 bundle 全是数据类**:`crypto_bitcoin`、`ga4`、`stackoverflow`——内容是 BigQuery 表、数据集、指标(metrics)、引用术语(references)。没有一个代码 bundle。
2. **`agents/mdcode`(Metadata as Code / `kcmd`)名字像"代码",实则讲元数据即代码**:用 YAML+Markdown 管理 Dataplex 目录条目(表、术语表、Entry Group),做 `pull`/`push` 同步。它管的是"数据资产的元数据",不是"源代码这一知识对象"。
3. **规范 §9 明确:只有 `.md` 文件是概念**。非 `.md`(PDF、PNG、`.py`、`.go`)**本身不是概念**,在 bundle 里没有一等地位。
4. README 里出现的 "collaborate on source code" 是**比喻**(像协作代码一样协作知识),不是"把代码当知识表示"。

## 二、逐项支持度

### 2.1 代码(最弱)

OKF 没有任何代码专用约定。你想把一个代码库变成知识,目前只能这样拼:

| 你想表达的 | OKF v0.1 现状 | 缺什么 |
|---|---|---|
| "这个概念就是一个函数/模块/类" | 没有 `type: Function` 之类,只能自己取 `type` 字符串 | 类型词表不互通 |
| 指向某段源码 | 放进 `resource` URI(如 GitHub permalink) | 没有行号锚点约定 |
| 这段代码是什么语言 | 无字段 | 没有 `language` 字段 |
| 函数 A 调用 B / 依赖 C | 普通 Markdown 链接(§5.3 **无类型**) | 调用图/依赖图无法机读 |
| 函数签名 | 只能写进 `# Schema` 或正文表格,自由发挥 | 没有签名结构约定 |
| 这个概念"是"代码 vs "描述"代码 | 无法区分 | 无 |

**一句话**:OKF 能容纳代码(塞进围栏代码块、用 `resource` 链接文件),但不能**理解**代码的结构。对 RAG/agent 检索,意味着"靠正文散文 + 无类型链接",检索质量取决于产出时写得多好。

### 2.2 PDF

- PDF **不是概念**。只能:① 用 `resource`/Markdown 链接指过去;② 由生产者把内容**抽取成 Markdown**(文本、表格)后才成为知识。
- 缺:页码/区域锚点约定、扫描件 OCR 的约定、图文混排的保真。
- 可行路径:写一个 producer,PDF →(解析/OCR)→ 每个章节一个概念文档,`resource` 指向原 PDF + 页码。

### 2.3 图片

- 图片**不是概念**。规范连 `# Schema/Examples/Citations` 之外都没约定,自然也没有图片的 alt/caption/OCR 约定。
- 只能:① Markdown 图片语法嵌在正文里(但图里的知识机器读不到);② 由生产者用多模态模型生成**图说/OCR 文本**写进正文,`resource` 指向原图。

## 三、提案:OKF-Code 约定(向后兼容扩展)

> 全部基于规范 §4.1"生产者可加入任意额外键" + §11"次版本可做向后兼容新增",**不动任何 MUST**,符合 v0.1 的 bundle 升级到这套约定后仍然合规。

### 3.1 代码类型词表(约定 `type` 取值)

```
Repository | Package | Module | Class | Function | Interface | Config | Script | Notebook
```

消费者按 §4.1 容忍未知类型;但产出方统一用这套词表,代码 bundle 之间就能互通。

### 3.2 扩展字段

```yaml
---
type: Function
title: parse_frontmatter
description: 解析 Markdown 文件顶部的 YAML 头信息,返回 (meta, body)。
resource: https://github.com/yzfly/awesome-okf/blob/main/skills/okf-creator/scripts/validate_okf.py#L20-L48
language: python              # 扩展:编程语言
symbol: parse_frontmatter     # 扩展:符号名(函数/类/模块全名)
signature: "parse_frontmatter(text: str) -> tuple[dict, str]"  # 扩展:签名
lang: zh                      # 正文语言(沿用 i18n 提案)
tags: [code, parser]
timestamp: 2026-06-14T00:00:00Z
---

# Signature

```python
def parse_frontmatter(text: str) -> tuple[dict, str]: ...
```

# Behavior

…正文用结构化 Markdown 描述行为、参数、返回、副作用、异常…

# Calls

- 调用 [yaml.safe_load](/packages/pyyaml/safe_load.md)

# Cited by

- 被 [validate_okf](/scripts/validate_okf.md) 使用
```

### 3.3 `resource` 行号锚点约定

复用 GitHub/GitLab 既有惯例 `#L<start>-L<end>`,让 `resource` 不止指到文件,而是指到具体行段。这样无需新语法,工具直接可点。

### 3.4 有类型链接(可选,解决 §5.3 无类型链接痛点)

在链接文字里用约定前缀表达关系,既人读友好又可被简单规则机读:

```markdown
- calls: [parse_frontmatter](/functions/parse_frontmatter.md)
- depends-on: [pyyaml](/packages/pyyaml.md)
- deprecated-by: [parse_fm_v2](/functions/parse_fm_v2.md)
```

### 3.5 PDF / 图片:抽取为正文 + 原件留痕

- 二进制原件**不入** bundle 概念,但可放进 `assets/` 目录,由概念用 `resource` 指向。
- 概念正文承载**抽取出的知识**:PDF → 文本/表格;图片 → 图说/OCR(多模态生成)。
- 约定 `# Source` 章节注明来源页码/坐标,便于回溯。

## 四、这对我们意味着什么

1. **代码库 → OKF 是真空地带**,GitHub 海量 README/教程/awesome 列表想进 OKF,需要专门 producer。本仓库的 [`awesome-importer`](../plugins/awesome-importer/) 与 [`feishu-okf`](../plugins/feishu-okf/) 先各占一格;代码库 producer 是下一个高价值目标。
2. **3.1–3.4 的代码约定**值得连同 [i18n 提案](./okf-spec-zh.md#中文生态议题i18n-扩展提案草案)一起,作为"提案 + 参考实现"向官方提。
3. okf-creator Skill 已内置这套代码约定,产出代码类 bundle 时直接采用。

> 调研基于 2026-06-14 时的官方主分支。来源:[SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)、[okf/README.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/README.md)、[agents/mdcode](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/agents/mdcode)、三个官方示例 bundle。
