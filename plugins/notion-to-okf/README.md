---
type: Producer
title: notion-to-okf
description: 把 Notion 的 Markdown 导出转换为符合 OKF v0.1 的知识包,去哈希并补全 frontmatter。
tags: [okf, notion, producer, cli]
lang: zh
timestamp: 2026-06-14T00:00:00Z
license: MIT
---

# notion-to-okf

把 [Notion](https://www.notion.so/) 的 **Markdown 导出**(Export → Markdown & CSV)转换为符合 [OKF v0.1](../../docs/okf-spec-zh.md) 的知识包。

零第三方依赖,离线运行——无需 Notion API,直接处理你导出的文件夹。

## 准备

在 Notion 里:`...` → **Export** → 格式选 **Markdown & CSV** → 下载并解压。

## 安装与用法

```bash
cd plugins/notion-to-okf
uv pip install -e .

notion-to-okf "/path/to/Notion 导出目录" -o ./out --lang zh
```

## 它做了什么

1. **去哈希**:Notion 在文件名/目录名尾部加的 32 位十六进制 ID 一律剥除,得到干净的 concept ID;
2. **补 frontmatter**:为每页注入 `type: Note` + `title`(取首个 H1)+ `lang` + `timestamp`;
3. **重写链接**:URL 解码 + 逐段去哈希,使页面间链接重新可用;
4. **生成索引**:各级 `index.md`(根含 `okf_version`)与 `log.md`。

产物用 [`validate_okf.py`](../../skills/okf-creator/scripts/validate_okf.py) 校验。

## 限制

- 数据库导出的 `.csv` 当前不转换(会提示数量;后续可每行转为一个概念);
- Notion 的 callout / toggle 等富块在导出 Markdown 时已被 Notion 自身降级,本工具按降级后的 Markdown 处理。
