---
type: Article
title: 提案——让 HTML 成为 OKF 一等公民
description: OKF v0.1 只把 .md 当概念。本提案让 .html 也成为合法概念文件,人看着友好,底层结构对 agent 友好,且向后兼容。
tags: [okf, html, 提案, 双表示]
lang: zh
timestamp: 2026-06-14T00:00:00Z
author: 云中江树
---

# 提案:让 HTML 成为 OKF 一等公民

> 状态:草案 / 待向官方提交
> 关联:[OKF 规范中文版](./okf-spec-zh.md) §4(概念文档)、§9(符合性)、§11(版本)

## 一、动机

OKF v0.1 规定:**只有 `.md` 文件是概念**(规范 §9)。但很多知识天然是 HTML 更合适:

- **人看着友好**:HTML 可直接在浏览器渲染,带样式、可交互、可嵌图表/公式/示意图——比裸 Markdown 视觉体验好得多;
- **底层对 agent 友好**:HTML 源码仍是纯文本,语义标签(`<h1>`、`<table>`、`<article>`)甚至比 Markdown 更结构化,内嵌 JSON-LD / microdata 还能携带机读结构。

现状下,HTML 只能作为 `resource` 被链接,或被抽取成 Markdown 才进 bundle——白白丢掉了它"人友好 + 机友好"双重优势。本提案让 `.html` 与 `.md` 平起平坐。

## 二、设计:`.html` 概念文件

### 2.1 元数据编码(解决 HTML 没有 YAML frontmatter 的问题)

HTML 概念必须携带 OKF 元数据。提供三种编码,**推荐第一种**:

**(A) 前置 OKF 注释块(推荐)** —— 文件最前面的 HTML 注释,内含 YAML:

```html
<!--okf
type: Guide
title: 快速上手
description: 五分钟跑通第一个 bundle。
lang: zh
timestamp: 2026-06-14T00:00:00Z
-->
<!DOCTYPE html>
<html>…人看着友好的渲染内容…</html>
```

- 浏览器**不渲染**注释,视觉零干扰;
- 解析器读取 `<!--okf` 与 `-->` 之间的 YAML,规则与 §4.1 frontmatter 完全一致;
- 对人对机都直观。

**(B) `<head>` 中的 meta 标签**(更 HTML 原生):

```html
<meta name="okf:type" content="Guide">
<meta name="okf:title" content="快速上手">
```

**(C) 内嵌脚本块**(适合工具生成):

```html
<script type="application/okf+yaml">
type: Guide
title: 快速上手
</script>
```

消费者**应当**至少支持 (A);(B)(C) 为可选增强。

### 2.2 机读正文:推荐"双表示"

为了让 agent 不必解析整个 DOM,推荐 HTML 概念内嵌一份纯文本/Markdown 镜像:

```html
<script type="text/markdown" id="okf-body">
# 快速上手
1. 安装 …
2. 运行 …
</script>
```

agent 直接取 `#okf-body` 即可;浏览器忽略该脚本。若不内嵌,消费者**应当**回退到从语义 HTML 抽取文本。

### 2.3 交叉链接

沿用规范 §5:用标准 `<a href="/path/x.html">` 或指向 `.md`。链接语义不变。

### 2.4 保留文件名

`index.md` / `log.md` 仍以 Markdown 为准;**可选**允许 `index.html` 作为渲染友好的目录页(其机读信息仍以同目录 `index.md` 为权威,避免二义)。

## 三、对符合性(§9)的最小改动

把 §9 第 1、2 条从"每个非保留 `.md`"放宽为"每个非保留**概念文件**(`.md` 或 `.html`)":

1. 每个非保留 `.md`/`.html` 含可解析的 OKF 元数据(`.md` 用 YAML frontmatter;`.html` 用 §2.1 三种编码之一);
2. 元数据含非空 `type`;
3. 保留文件名结构不变。

**向后兼容性**:
- 纯 Markdown 生产/消费者**完全不受影响**——`.md` 规则一字未改;
- 不认识 `.html` 概念的旧消费者按"未知文件"忽略即可,bundle 对它仍是合规的 markdown 子集;
- 属规范 §11 定义的**次版本**向后兼容新增。

## 四、双表示的最佳实践(配套约定)

一个概念同时提供 `.html`(人)与 `.md`(机)时,用 `canonical` 串起来,避免重复被当成两个概念:

```
guides/
├── quickstart.html      # 渲染友好,<!--okf--> 注释含 canonical: /guides/quickstart.md
└── quickstart.md        # 机读权威,type 同
```

`.html` 的 OKF 注释里写 `canonical: /guides/quickstart.md`;消费者去重时以 `canonical` 为准。

## 五、参考实现

本仓库的 [`html-to-okf`](../plugins/html-to-okf/) 插件演示该提案:

- 输入任意 `.html`,产出符合 OKF 的概念——保留原 HTML(人友好)+ 抽取出 `.md` 镜像(机友好)+ 用 `canonical` 互链;
- 为缺元数据的 HTML 注入 `<!--okf ... -->` 注释块。

> 这份提案与 [i18n 提案](./okf-spec-zh.md#中文生态议题i18n-扩展提案草案)、[代码支持提案](./code-support-research-zh.md)一道,构成中文社区向 OKF 上游贡献的三个口子:**多语言、代码、HTML 一等公民**。三者都遵循同一原则——只做向后兼容的次版本新增,不动任何 MUST。
