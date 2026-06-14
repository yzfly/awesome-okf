---
type: Article
title: code-to-okf 代码表示约定(提案)
description: 为 OKF 补齐代码表示能力的向后兼容约定提案——类型词表, 扩展字段, 行号锚点, 有类型链接。
tags: [okf, code, 提案, 约定]
lang: zh
timestamp: 2026-06-14T00:00:00Z
author: 云中江树
---

# code-to-okf 代码表示约定(提案)

> 状态:草案 / 待向官方提交。完整背景见 [代码/PDF/图片支持度调研](../../../docs/code-support-research-zh.md)。
> 全部基于规范 §4.1(生产者可加任意键)+ §11(次版本向后兼容新增),**不动任何 MUST**。

## 1. 问题

OKF v0.1 为数据知识(表/指标/术语)设计,缺代码表示能力:没有代码类型词表、没有符号/签名/语言字段、没有行号锚点、链接无类型(无法表达"调用/依赖")。详见调研报告。

## 2. 类型词表(约定 `type` 取值)

```
Repository | Package | Module | Class | Function | Interface | Config | Script | Notebook
```

生产者统一取值,消费者按 §4.1 容忍未知值;代码 bundle 之间因此可互通。

## 3. 扩展字段

| 字段 | 说明 |
|---|---|
| `language` | 编程语言(如 `python`、`go`、`typescript`) |
| `symbol` | 符号全名(如 `pkg.module.func`) |
| `signature` | 函数/方法签名字符串 |
| `resource` | 源码 URL,**带行号锚点**,见 §4 |

## 4. `resource` 行号锚点

复用 GitHub/GitLab 既有惯例,指到具体行段,且用**提交 SHA**(非分支名)保证稳定:

```
https://github.com/owner/repo/blob/<sha>/path/to/file.py#L20-L48
```

## 5. 有类型链接

在链接前加约定前缀,表达关系种类(人读友好 + 可被简单规则机读):

```markdown
- calls: [B](/functions/b.md)
- called-by: [A](/functions/a.md)
- depends-on: [lib](/packages/lib.md)
- implements: [Iface](/interfaces/iface.md)
- extends: [Base](/classes/base.md)
- deprecated-by: [v2](/functions/v2.md)
```

消费者可用正则 `^- (\w[\w-]*): \[` 提取关系类型,构建带类型的图。

## 6. 正文约定章节

| 标题 | 内容 |
|---|---|
| `# Signature` | 签名,代码块 |
| `# Behavior` | 参数、返回、副作用、异常、复杂度 |
| `# Calls` / `# Cited by` | 调用/被调用(有类型链接) |
| `# Examples` | 最小用例(沿用规范约定标题) |

## 7. 目录组织建议

```
<repo>/
├── index.md
├── repository.md            # type: Repository,总览
├── packages/<pkg>.md        # type: Package
├── modules/<mod>.md         # type: Module
├── classes/<cls>.md         # type: Class
└── functions/<fn>.md        # type: Function
```

## 8. 向后兼容性

纯 v0.1 消费者把以上扩展字段当未知键忽略、把有类型链接当普通链接处理,bundle 依旧合规。本约定属规范 §11 的**次版本**新增。

## 9. 与其他提案的关系

与 [i18n 提案](../../../docs/okf-spec-zh.md#中文生态议题i18n-扩展提案草案)、[HTML 一等公民提案](../../../docs/html-first-class-proposal-zh.md) 同属中文社区向上游贡献的三个口子,共享同一原则:只做向后兼容新增。
