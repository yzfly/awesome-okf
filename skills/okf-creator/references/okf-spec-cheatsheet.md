---
type: Reference
title: OKF v0.1 速查表
description: 开放知识格式 v0.1 的字段, 保留文件名, 链接规则与符合性要点速查.
tags: [okf, 速查, reference]
lang: zh
timestamp: 2026-06-14T00:00:00Z
---

# OKF v0.1 速查表

> 完整中文规范见 [docs/okf-spec-zh.md](../../../docs/okf-spec-zh.md)。本表只列高频要点。

## 一句话模型

一个 **bundle** = 一个目录;一个 **concept** = 一个 `.md` 文件;**concept ID** = 去掉 `.md` 的路径。

## 头信息字段

| 字段 | 必需 | 说明 |
|---|---|---|
| `type` | ✅ **唯一硬要求** | 概念种类,自由字符串,消费者须容忍未知值 |
| `title` | 推荐 | 显示名,省略则从文件名推导 |
| `description` | 推荐 | 一句话摘要,索引/搜索摘要用 |
| `resource` | 推荐 | 底层资产的规范 URI,抽象概念可省 |
| `tags` | 可选 | 短字符串列表,横切分类 |
| `timestamp` | 可选 | 最后修改时间,ISO 8601 |
| 任意其他键 | 可选 | 生产者扩展,消费者须保留、不得因此拒绝 |

## 保留文件名

| 文件 | 含义 | 头信息 |
|---|---|---|
| `index.md` | 目录清单(渐进式展开) | 无;**仅根** `index.md` 可含 `okf_version` |
| `log.md` | 变更历史,日期标题 `## YYYY-MM-DD` | 无 |

其余所有 `.md` 都是概念文档。

## 约定的正文标题

`# Schema`(列/字段结构) · `# Examples`(用例代码) · `# Citations`(外部来源,编号)。

## 交叉链接

- 推荐**包内绝对路径**:`[customers](/tables/customers.md)`(文件移动仍稳定)。
- 也支持相对路径:`[x](./other.md)`。
- 链接 = 一条**无类型**关系边;具体关系靠周围文字表达。
- 消费者**必须容忍坏链接**(可能是尚未写的知识)。

## 符合性(§9)三条硬要求

1. 每个非保留 `.md` 有可解析 YAML 头信息;
2. 每个头信息有非空 `type`;
3. `index.md` / `log.md` 出现时遵循其结构。

消费者**绝不可**因以下原因拒绝 bundle:缺可选字段、未知 `type`、未知额外键、坏链接、缺 `index.md`。

## 本仓库扩展约定

- **i18n**:`lang`(BCP 47)+ `canonical`(主语言版本概念 ID)。见 [okf-spec-zh.md 末尾](../../../docs/okf-spec-zh.md#中文生态议题i18n-扩展提案草案)。
- **代码**:类型词表 + `language`/`symbol`/`signature` + 行号锚点 + 有类型链接。见 [code-support-research-zh.md](../../../docs/code-support-research-zh.md)。
