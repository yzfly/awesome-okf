---
type: Reference
title: 贡献指南
description: 如何为 awesome-okf 贡献资源, producer 插件, consumer 与提案,含 producer 插件约定。
tags: [okf, contributing, 约定]
lang: zh
timestamp: 2026-06-14T00:00:00Z
---

# 贡献指南

欢迎为中文 OKF 生态添砖加瓦。收录与合并标准只有一条:**与 OKF 直接相关,且能跑 / 能读**。

## 贡献类型

- **资源**:OKF 相关的文章、教程、工具、项目 → 加到 [`README.md`](./README.md) 或 [`docs/resources-zh.md`](./docs/resources-zh.md),一行说明 + 链接。
- **Producer(导出插件)**:把某种来源转成 OKF bundle → 放进 `plugins/`,遵循下方约定。
- **Consumer**:读取/浏览/在 OKF 上推理的工具 → 放进 `plugins/` 或在 README 的 Consumers 区登记。
- **提案**:对规范的向后兼容扩展 → 放进 `docs/`,参考现有三份提案(i18n / 代码 / HTML)的写法。

## Producer 插件约定

为了让"各种 xx-to-okf 插件"彼此一致、产物可互换,所有 producer 遵循:

1. **契约**:输入(某来源)→ 输出一个**能通过 `skills/okf-creator/scripts/validate_okf.py` 的 bundle**。这是唯一硬性要求。
2. **命名**:`<来源>-to-okf` 或 `<来源>-importer`,CLI 同名。
3. **必产出**:根 `index.md`(带 `okf_version: "0.1"`)、`log.md`(`## YYYY-MM-DD` 前缀),每个概念有非空 `type`。
4. **建议**:尽量零第三方依赖(纯标准库),`--lang` 默认 `zh`,`resource` 指回原始来源,中文标题生成 CJK slug。
5. **自带 README**:本身也是一个 OKF 概念(`type: Producer`,带 frontmatter),说明安装、用法、限制。
6. **可测**:能离线跑一个最小样例并通过校验(参考现有插件的测试方式)。

> 现有参考实现:[`feishu-okf`](./plugins/feishu-okf/)、[`awesome-importer`](./plugins/awesome-importer/)、[`obsidian-to-okf`](./plugins/obsidian-to-okf/)、[`notion-to-okf`](./plugins/notion-to-okf/)、[`html-to-okf`](./plugins/html-to-okf/)。照着抄即可。

## 本仓库自身是 OKF bundle

任何 `.md` 改动后,请跑校验确保仓库仍合规:

```bash
python skills/okf-creator/scripts/validate_okf.py .
```

新增非保留 `.md` 时,记得加 YAML 头信息和非空 `type`(详见 [dogfooding 说明](./docs/dogfooding-zh.md))。

## 许可

贡献即同意以 [MIT](./LICENSE) 授权。署名保留(作者:云中江树)。
