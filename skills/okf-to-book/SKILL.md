---
name: okf-to-book
description: "把符合 OKF v0.1 的知识包或项目发布为可视化的文档站(VitePress, Vue 系, 亮色主题), 带侧边栏导航与概念互链. 适用场景包括把一个 OKF bundle 变成可浏览的网站或电子书, 为知识库生成文档门户, 把任意 OKF 项目发布为静态站点. 当用户提到把 OKF 发布成文档站, OKF 转网站或电子书, 可视化知识库, 或为 bundle 生成 docs 站时触发."
type: Skill
title: OKF to Book
lang: zh
tags: [okf, vitepress, 文档站, skill]
license: MIT
---

# OKF to Book

把任意符合 [OKF v0.1](../../docs/okf-spec-zh.md) 的知识包,发布为可视化文档站(像一本可浏览的书)。默认用 **VitePress**(Vue 系)+ **亮色主题**(不启用暗色)。

## 何时使用

- 用户有一个 OKF bundle(自建的,或用 feishu/awesome/obsidian/notion/html 等 producer 导出的),想发布成网站/电子书;
- 想给知识库一个带侧边栏、搜索、概念互链的浏览门户。

## 工作流

1. **确保是合规 bundle**:先跑 `../okf-creator/scripts/validate_okf.py <bundle>`,修到 0 错误。
2. **生成站点**:
   ```bash
   python scripts/okf_to_vitepress.py <bundle 目录> -o ./site --title "我的知识库"
   ```
   - 复制全部概念 `.md`(VitePress 直接消费 OKF 概念,frontmatter 兼容);
   - 按目录自动生成侧边栏;
   - 配置亮色主题(`appearance: false`)、本页目录、GitHub 链接、中文 UI。
3. **预览/构建**:
   ```bash
   cd ./site && npm install && npm run docs:dev      # 本地预览
   npm run docs:build                                # 产出静态站点 docs/.vitepress/dist
   ```
4. **部署**:把 `docs/.vitepress/dist` 丢到任意静态托管(GitHub Pages / Vercel / Cloudflare Pages)。

## 设计取舍

- **为什么 VitePress**:OKF 本就是带 frontmatter 的 Markdown,VitePress 几乎零转换直接消费;Vue 系,符合前端偏好。
- **亮色主题**:按偏好关闭暗色模式。
- **概念互链**:OKF 的包内绝对链接 `/path/x.md` 在 VitePress 里需为 `/path/x`(cleanUrls 已开启,生成器已处理侧边栏链接)。若 bundle 正文里有 `.md` 后缀的内链,VitePress 也能解析。

## 进阶(可按需扩展生成器)

- **图谱视图**:OKF 是图结构,可在站点加一个 D3/force-graph 页面渲染概念关系(类似官方 viz.html)。
- **多语言站点**:bundle 用了 i18n 约定(`lang`/`canonical`)时,可生成 VitePress 的 i18n 多语言路由。
- **HTML 一等公民**:bundle 含 `.html` 概念(见 [提案](../../docs/html-first-class-proposal-zh.md))时,直接作为静态资源挂载。

## 反向关系

- 与 [`book-to-okf`](../book-to-okf/) 互为逆操作:book → OKF → book。
- 任何 producer([`feishu-okf`](../../plugins/feishu-okf/)、[`awesome-importer`](../../plugins/awesome-importer/)、[`obsidian-to-okf`](../../plugins/obsidian-to-okf/)、[`notion-to-okf`](../../plugins/notion-to-okf/)、[`html-to-okf`](../../plugins/html-to-okf/))的产物,都能直接喂给本 Skill 发布。
