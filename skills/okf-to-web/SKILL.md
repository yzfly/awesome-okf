---
name: okf-to-web
description: "把符合 OKF v0.1 的知识包打包成单个自包含且经过压缩(minify)的 HTML 文件, 内嵌导航, Markdown 阅读器与概念关系图谱, 数据不出页面, 无需后端. 适用场景包括把 OKF bundle 变成一个可分享的单文件网页, 离线浏览知识库, 生成对标官方 viz.html 的可视化. 当用户提到 okf to web, OKF 转单文件网页, 可视化 OKF, minify 知识库, 或要一个自包含 HTML 时触发."
type: Skill
title: OKF to Web
lang: zh
tags: [okf, web, minify, 可视化, skill]
license: MIT
---

# OKF to Web

把任意符合 [OKF v0.1](../../docs/okf-spec-zh.md) 的知识包,打包成**单个自包含、压缩过的 `.html`**——左侧分组导航 + 中间 Markdown 阅读器 + 右侧概念关系图谱。数据全部内嵌,**不出页面**,无后端、无安装,双击即开。对标官方 `viz.html`。

与 [`okf-to-book`](../okf-to-book/) 的区别:那个生成多页 VitePress 站点(需 npm 构建);本 Skill 产出**一个文件**,适合分享、归档、离线。

## 前置

- Python 3(生成)+ Node.js(压缩,本机已具备)。

## 工作流

1. **校验** bundle:`../okf-creator/scripts/validate_okf.py <bundle>`。
2. **生成**单文件:
   ```bash
   python scripts/build_web.py <bundle 目录> -o okf.html --title "我的知识库"
   ```
3. **压缩**(minify,零依赖 node 脚本):
   ```bash
   node scripts/minify.mjs okf.html okf.min.html
   ```
   保护 `<pre>`/`<script>`/`<style>` 与内嵌 JSON 数据,折叠标签间空白、删注释、压 CSS/JS。
4. 把 `okf.min.html` 直接分享 / 部署到任意静态托管,或本地双击打开。

## 设计要点

- **单文件自包含**:所有概念以 JSON 内嵌 `<script type="application/json">`,JS 用极小的内联 Markdown 渲染器 + SVG 图谱,无任何外部请求 → 数据安全、可离线。
- **嵌入安全**:正文里的 `</script>` 会被转义为 `<\/script>`,不会提前闭合脚本。
- **图谱**:概念间正文链接 → 关系边;点节点跳转概念。
- **亮色主题、中文 UI**(字节风),响应式(窄屏自动隐藏图谱)。
- **压缩比说明**:大头是内嵌知识文本(本就不应破坏性压缩),所以体积下降主要来自 HTML/CSS/JS 外壳,属正常。

## 可扩展

- 想要力导向图谱、全文搜索高亮、暗色切换,可在 `build_web.py` 的内联 JS 模板里加;
- 想要真正激进的 JS 压缩,可改用 `npx terser`(需联网安装),本脚本默认走零依赖安全压缩。

## 配套

任何 producer 的产物(feishu / awesome / obsidian / notion / html / github)都能直接喂给本 Skill。反向见 [`book-to-okf`](../book-to-okf/)。
