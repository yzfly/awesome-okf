---
type: Producer
title: feishu-to-okf
description: 把飞书(Feishu/Lark)知识空间与文档导出为符合 OKF v0.1 的知识包,让团队飞书知识被 AI 智能体直接消费。
tags: [okf, feishu, lark, producer, cli, wiki]
lang: zh
timestamp: 2026-06-14T00:00:00Z
license: MIT
---

# feishu-to-okf

把飞书(Feishu / Lark)的**知识空间(Wiki)与文档**,一键导出为符合 [OKF v0.1](../../docs/okf-spec-zh.md) 的知识包(bundle)。团队沉淀在飞书里的知识,从此可以被 AI 智能体直接检索,也能用 [`okf-to-book`](../../skills/okf-to-book/) 发布成文档站。

零第三方依赖,纯标准库。

## 准备:创建飞书自建应用

1. 到[飞书开放平台](https://open.feishu.cn/)创建一个**企业自建应用**,拿到 `App ID` 与 `App Secret`。
2. 开通权限:`wiki:wiki:readonly`(读知识空间)、`docx:document:readonly`(读文档)。
3. 把应用**加入**要导出的知识空间(否则列不到)。

## 安装与配置

```bash
cd plugins/feishu-to-okf
uv pip install -e .        # 或 pip install -e .

export FEISHU_APP_ID=cli_xxxxxxxx
export FEISHU_APP_SECRET=xxxxxxxxxxxxxxxx
```

## 用法

```bash
# 1. 列出应用可访问的知识空间,拿到 space_id
feishu-to-okf spaces

# 2. 导出整个空间为 OKF bundle
feishu-to-okf export 7012345678901234567 -o ./out --lang zh --date 2026-06-14
```

## 它做了什么

- 用 `tenant_access_token` 鉴权;
- 递归遍历知识空间的全部节点;
- 对每篇 `docx` 文档拉取块(blocks)并转成 Markdown(标题、列表、代码块、引用、待办、加粗/斜体/行内码/链接);
- 每篇文档 → 一个 OKF 概念(`type: Document`,`resource` 指向飞书 wiki 链接,带 `lang`);
- 生成根 `index.md`(`okf_version: "0.1"`)与 `log.md`。

产物用 [`validate_okf.py`](../../skills/okf-creator/scripts/validate_okf.py) 校验。

## 限制(v0.1)

- 表格、画板、多维表格(bitable)、电子表格暂不深度转换,以文本兜底;
- 文档层级目前平铺到 `docs/` 下,后续可按 Wiki 树还原目录;
- 图片仅保留飞书链接,未做下载与图说生成(可后续接多模态,见[代码/图片支持调研](../../docs/code-support-research-zh.md))。

## 配套 Skill

无需单独 Skill;在 [`okf-creator`](../../skills/okf-creator/) 流程里把本工具作为"飞书来源"的 producer 调用即可。
