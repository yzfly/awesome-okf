---
type: Producer
title: obsidian-to-okf
description: 把 Obsidian vault 转换为符合 OKF v0.1 的知识包,wikilink 自动转为 OKF 链接。
tags: [okf, obsidian, producer, cli]
lang: zh
timestamp: 2026-06-14T00:00:00Z
license: MIT
---

# obsidian-to-okf

把 [Obsidian](https://obsidian.md/) vault 转换为符合 [OKF v0.1](../../docs/okf-spec-zh.md) 的知识包。Obsidian 本就是 Markdown + frontmatter + `[[wikilink]]`,**几乎天生就是 OKF**——本工具只补三件事。

零第三方依赖。

## 安装

```bash
cd plugins/obsidian-to-okf
uv pip install -e .
```

## 用法

```bash
obsidian-to-okf /path/to/vault -o ./out --lang zh
```

## 它做了什么

1. **保证 `type`**:每篇笔记若 frontmatter 缺 `type`,注入默认值(`Note`,可用 `--type` 改),其余字段原样保留;
2. **转换链接**:`[[笔记名]]`、`[[笔记名|别名]]`、`[[笔记名#标题]]` → OKF 包内绝对链接 `[别名](/相对路径.md)`;
3. **生成索引**:各级 `index.md`(根含 `okf_version`)与 `log.md`。

自动跳过 `.obsidian/` 与 `.trash/`。产物用 [`validate_okf.py`](../../skills/okf-creator/scripts/validate_okf.py) 校验。

## 限制

- 嵌入 `![[...]]`、Dataview 查询等 Obsidian 专有语法不做转换;
- 复杂 YAML frontmatter 原样保留(不重排)。
