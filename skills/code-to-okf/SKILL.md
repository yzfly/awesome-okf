---
name: code-to-okf
description: "把源代码仓库转换为符合 OKF v0.1 的知识包(bundle), 用一套代码表示约定(类型词表, language/symbol/signature 字段, 行号锚点, 有类型链接)弥补 OKF 对代码的薄弱支持. 适用场景包括为代码库生成 agent 可读的知识文档, 把仓库的模块函数类整理为概念库, 建立代码知识图谱. 当用户提到 code to okf, 代码库转 OKF, 为代码生成知识, 或把仓库变成 agent 可检索的知识时触发."
type: Skill
title: Code to OKF
lang: zh
tags: [okf, code, 代码, skill, 提案]
license: MIT
---

# Code to OKF

把源代码仓库转换为 OKF 知识包。OKF 原生对代码支持薄弱(见[支持度调研](../../docs/code-support-research-zh.md)),本 Skill 用一套向后兼容的**代码表示约定**补齐——详见 [references/code-okf-conventions.md](references/code-okf-conventions.md)。

## 何时使用

- 为一个代码库生成 agent 可检索的知识(架构、模块、关键函数、依赖关系);
- 把"只有资深工程师脑子里才有"的代码上下文沉淀成可移植知识。

## 拆解模型(一个代码对象一个概念)

`type` 用统一词表:`Repository | Package | Module | Class | Function | Interface | Config | Script | Notebook`。

不要逐文件粗暴转储。按**知识价值**取舍:先覆盖架构、公共 API、核心算法、易踩坑处,而非每个 getter。

## 头信息扩展字段

```yaml
---
type: Function
title: parse_frontmatter
description: 解析 Markdown 头信息,返回 (meta, body)。
resource: https://github.com/owner/repo/blob/<sha>/path.py#L20-L48   # 带行号锚点
language: python
symbol: module.parse_frontmatter
signature: "parse_frontmatter(text: str) -> tuple[dict, str]"
lang: zh
---
```

## 正文结构(别只贴代码)

```markdown
# Signature      # 签名(代码块)
# Behavior       # 行为:参数、返回、副作用、异常、复杂度
# Calls          # 调用了谁(有类型链接)
# Cited by       # 被谁调用
# Examples       # 最小用例
```

## 有类型链接(解决 OKF 无类型链接痛点)

用前缀表达关系,人读友好且可被简单规则机读:

```markdown
- calls: [helper](/functions/helper.md)
- depends-on: [pyyaml](/packages/pyyaml.md)
- implements: [Reader](/interfaces/reader.md)
- deprecated-by: [parse_v2](/functions/parse_v2.md)
```

## 工作流

1. **扫架构**:先产出 `Repository` 总览 + 各 `Package`/`Module` 概念,描述职责与依赖。
2. **挑要点**:列出值得单独建页的 `Class`/`Function`(公共 API、核心逻辑、复杂处)。
3. **逐个写**:头信息(含 `language`/`symbol`/`signature`/带锚点的 `resource`)+ 结构化正文 + 有类型链接。
4. **建图**:`Calls`/`Cited by` 互链,形成调用/依赖图谱。
5. **校验**:`../okf-creator/scripts/validate_okf.py`。
6. **(可选)发布**:[`okf-to-book`](../okf-to-book/) 出文档站。

## 注意

- `resource` 行号锚点用提交 SHA 而非分支名,避免代码变动后失效;
- 不要把整个文件塞进一个概念;
- 这套约定是提案,产出的 bundle 在纯 v0.1 消费者眼里仍然合规(扩展字段会被安全忽略)。
