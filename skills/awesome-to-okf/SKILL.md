---
name: awesome-to-okf
description: "把 GitHub 上的 awesome-xx 精选列表转换并富化为符合 OKF v0.1 的知识包(bundle), 让社区海量教程和资源列表成为 AI 智能体可检索的知识. 适用场景包括把某个 awesome 列表导入为 OKF, 为列表里的条目补充结构化正文, 校验产物符合性. 当用户提到 awesome 列表, GitHub 精选列表转 OKF, 或想把某个 awesome-xx 变成知识库时触发."
type: Skill
title: Awesome to OKF
lang: zh
tags: [okf, awesome, github, skill]
license: MIT
---

# Awesome to OKF

把 GitHub 上的 **awesome-xx** 列表转成符合 [OKF v0.1](../../docs/okf-spec-zh.md) 的知识包,并富化成 agent 真正用得上的知识。

## 何时使用

- 用户给一个 awesome 仓库(如 `sindresorhus/awesome`)或列表 URL,想转成 OKF;
- 想让一份"链接墙"变成可被智能体检索/问答的结构化知识。

## 工作流

1. **导入(机械)**:用 [`awesome-importer`](../../plugins/awesome-importer/) 把列表转成基础 bundle。
   ```bash
   python -m awesome_importer.cli <owner/repo 或 URL 或本地文件> -o ./out --lang zh
   ```
   每个链接 → 一个 `type: Resource` 概念;每个分节 → 一个目录 + `index.md`。

2. **富化(AI,关键)**:逐个概念把"一句话描述"扩写成有用正文——
   - 这个工具/资源**解决什么问题**、**何时该用**、**和同类的区别**;
   - 适用就加 `# Examples`(最小用例)、`# Citations`(官方文档/出处);
   - 在相关概念间补**交叉链接**(如"X 是 Y 的替代品" → 互链)。
   > 富化标准见 [`okf-creator`](../okf-creator/) 的"核心原则":一个没上下文的人/agent 只读这一篇能不能用起来。

3. **去噪**:跳过 `Contents`/`License`/`Contributing` 等已被自动过滤的非内容分节;合并明显重复项。

4. **校验**:`python ../okf-creator/scripts/validate_okf.py ./out`,修到 0 错误。

5. **(可选)发布**:用 [`okf-to-book`](../okf-to-book/) 把 bundle 发布为可视化文档站。

## 注意

- awesome 列表里中文标题会生成 CJK slug,正常;
- 富化时**不要编造**——拿不准的事实标注"待核实"或去 `# Citations` 找一手来源;
- 大列表(上千条)分批富化,先覆盖高价值分节。
