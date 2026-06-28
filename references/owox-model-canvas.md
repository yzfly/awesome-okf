---
type: Reference
title: OWOX Model Canvas(可视化建模 / 创作端)
description: 数据平台公司 OWOX 出品、已公网部署的"类 Miro"可视化数据建模编辑器,读写 / 导出 OKF Markdown+YAML bundle 并可往返,自我定位为 OKF 的可视化创作前端。
resource: https://github.com/OWOX/owox-model-canvas
tags: [okf, 可视化, 建模, 创作, 公司维护, 头部]
lang: zh
timestamp: 2026-06-28T00:00:00Z
---

# OWOX Model Canvas(可视化建模 / 创作端)

生态里少见的、成型且有公司维护的**可视化建模 / 创作端**:数据平台公司 OWOX 出品,已公网部署于 [model.owox.com](https://model.owox.com)。一个"类 Miro"的可视化数据建模编辑器(TS / React / Vite / Fastify):

- 在画布上拖拽数据集市(表 / 视图 / SQL)节点与可 join 的关系边,套行业模板;
- 用 AI(Gemini)从 schema 元数据生成"这个模型能回答哪些业务问题";
- 可一键推送到 OWOX Data Marts;
- **读写 / 导出 OKF 规范的 Markdown+YAML bundle**,可往返 round-trip。

它自我定位为"OKF 格式的可视化创作 / 导出前端"。与本仓库走静态产物路线的 [okf-to-web](/skills/okf-to-web/SKILL.md)、官方的 viz.html(见 [reference-implementations](/references/reference-implementations.md))相比,它是面向人工建模的交互式创作端。

源码:<https://github.com/OWOX/owox-model-canvas>
