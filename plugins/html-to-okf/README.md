---
type: Producer
title: html-to-okf
description: 把 HTML 文件转换为 OKF 概念,产出机读 .md + 人友好 .html 双表示,实现 HTML 一等公民提案。
tags: [okf, html, producer, cli]
lang: zh
timestamp: 2026-06-14T00:00:00Z
license: MIT
---

# html-to-okf

把 HTML 文件转换为 OKF 概念。它是 [HTML 一等公民提案](../../docs/html-first-class-proposal-zh.md) 的参考实现——产出**双表示**:

- **机读权威** `<slug>.md`:从 HTML 抽取的 Markdown,带 OKF frontmatter,`canonical` 指向 html;
- **人友好** `assets/<slug>.html`:保留原始 HTML(可直接浏览器渲染),顶部注入 `<!--okf ... -->` 元数据注释。

零第三方依赖(标准库 `html.parser`)。

## 安装与用法

```bash
cd plugins/html-to-okf
uv pip install -e .

html-to-okf ./page.html -o ./out          # 单文件
html-to-okf ./site_dir -o ./out --lang zh # 整个目录递归
```

## 它做了什么

1. 解析 HTML(忽略 `script`/`style`),抽取标题、段落、列表、代码块、引用、链接为 Markdown;
2. 每个 HTML → 一个 `.md` 概念(`type: Document`)+ 一份保留原样的 `.html`;
3. 为缺元数据的 HTML 注入 `<!--okf-->` 注释块;
4. 生成根 `index.md`(`okf_version`)与 `log.md`。

产物用 [`validate_okf.py`](../../skills/okf-creator/scripts/validate_okf.py) 校验。

## 为什么要双表示

> 详见提案。简言之:HTML 人看着友好(带样式/可交互),但 agent 一次读取读不全 DOM;Markdown 对 agent 友好但视觉朴素。双表示用 `canonical` 把两者绑成同一概念,各取所长。

## 限制

- 复杂布局 / 表格 / 内联样式不保证完美还原为 Markdown;
- 图片仅在抽取文本中保留引用,未做图说生成(见[图片支持调研](../../docs/code-support-research-zh.md))。
