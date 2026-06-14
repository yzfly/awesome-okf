---
name: github-to-okf
description: "把一个 GitHub 仓库(远程或本地)转换并富化为符合 OKF v0.1 的知识包(bundle), 让仓库的文档与代码成为 AI 智能体可检索的知识. 适用场景包括为开源项目生成知识库, 把代码仓库变成 agent 可问答的上下文, 建立仓库的架构与 API 知识图谱. 当用户提到 github to okf, 把仓库转 OKF, 为某个 repo 生成知识库, 或导入某个 GitHub 项目为知识时触发."
type: Skill
title: GitHub to OKF
lang: zh
tags: [okf, github, code, skill]
license: MIT
---

# GitHub to OKF

把一个 GitHub 仓库转成 OKF 知识包,并富化成 agent 真正用得上的项目知识。

## 何时使用

- 用户给一个仓库(`owner/repo` 或本地路径),想要可检索/可问答的项目知识库;
- 想把"散在代码、README、几位核心开发者脑子里"的上下文沉淀下来。

## 工作流

1. **导入(机械)**:用 [`github-to-okf`](../../plugins/github-to-okf/) 生成基础 bundle。
   ```bash
   github-to-okf <owner/repo 或 本地路径> -o ./out [--deep]
   ```
   产出仓库总览 + 代码概念(带 `language`、符号、blob 行级 `resource`)+ 文档概念。

2. **富化(AI,关键)** —— 按 [code-to-okf 约定](../code-to-okf/) 提升正文:
   - 给 `Repository` 总览补**架构图景**:核心模块、数据流、关键设计决策;
   - 给重要 `Module`/`Function` 补 `# Behavior`(参数/返回/副作用/复杂度)、`# Examples`;
   - 补**有类型链接**:`calls:` / `depends-on:` / `implements:`,形成调用/依赖图谱。

3. **取舍**:别每个文件都精修;优先公共 API、核心算法、易踩坑处。

4. **校验**:`../okf-creator/scripts/validate_okf.py ./out`。

5. **发布**:[`okf-to-web`](../okf-to-web/)(单文件可视化)或 [`okf-to-book`](../okf-to-book/)(文档站)。

## 注意

- 远程大仓用 `--deep` 会触发很多请求,先设 `GITHUB_TOKEN`;或先 `git clone` 再用本地模式(更快、能拿 blob 行级 resource);
- `resource` 行号锚点用提交 SHA,代码变动后仍有效;
- 符号提取是轻量正则,富化时以实际代码为准、不要编造行为。
