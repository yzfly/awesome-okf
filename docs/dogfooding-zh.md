---
type: Article
title: 本仓库自身就是一个 OKF bundle(dogfooding)
description: awesome-okf 仓库刻意做成符合 OKF v0.2 的知识包,既是资源大全,也是一份活的范例与符合性证明。
tags: [okf, dogfooding, 自举]
lang: zh
generated: { by: human:yzfly, at: 2026-06-14T00:00:00Z }
author: 云中江树
---

# 本仓库自身就是一个 OKF bundle

最好的规范示范,是自己先遵守它。`awesome-okf` 这个仓库**本身**就是一个符合 [OKF v0.2](./okf-spec-zh.md) 的知识包(bundle)——既能当资源大全用,也是一份"活的范例"和符合性证明。

## 怎么做到的

1. **每个非保留 `.md` 都是合法概念**:`README.md`、`docs/*.md`、各插件 `README.md`、各 `SKILL.md`、参考文档——全部带 YAML 头信息且有非空 `type`(规范 §11 的唯一硬要求)。
2. **保留文件名守规矩**:根 `index.md` 带 `okf_version: "0.2"`(§12 唯一允许 frontmatter 的地方),各级 `index.md` 做渐进式展开,`log.md` 用 `## YYYY-MM-DD` 日期前缀(§8/§9)。
3. **概念类型词表**:`Overview`(README)、`Specification`(规范)、`Article`(文章/提案)、`Reference`(参考)、`Producer`(导出插件)、`Skill`(技能)、`Resource`(收录条目)。
4. **多语言扩展**:中文文档统一标 `lang: zh`,为 [i18n 提案](./okf-spec-zh.md#中文生态议题i18n-扩展提案草案) 打样。
5. **交叉链接成图**:文档之间用 Markdown 链接互连(规范↔提案↔调研↔插件↔技能)。
6. **v0.2 信任家族**:每个概念用 `generated: { by, at }` 记录"谁、何时写的"(§5.2),执行者遵循 §7 约定——手写内容用 `human:` 前缀,
   插件产出的 bundle 用 `<插件名>/<版本>`(如 `awesome-to-okf/0.1.0`)。

## v0.1 → v0.2 是怎么迁的

上游规范在 v0.2 做了两处破坏性变更(§13.1),本仓库照着走了两步:

| 步骤 | 动作 | 影响面 |
|---|---|---|
| 1 | `timestamp: X` → `generated: { by: human:yzfly, at: X }` | 44 个 `.md` |
| 2 | 正文 `# Citations` 列表 → 头信息 `sources` + 脚注归属 | 规范译文与 `awesome-to-okf` 产出 |

根 `index.md` 的 `okf_version` 同步改成 `"0.2"`,七个 producer 插件的产出与校验器一并升级。
其余 v0.2 家族(`verified` / `status` / `stale_after` / 可验算计算)全部可选,本仓库按需使用——**不写也是合规的 v0.2 包**。

## 如何验证

仓库自带的校验器可证明它合规:

```bash
python skills/okf-creator/scripts/validate_okf.py .
```

> 这正是 OKF 的妙处:一个 GitHub 仓库,不需要任何额外构建,既是人读的项目主页,又是 agent 可消费的知识包,还能被 [`okf-to-book`](../skills/okf-to-book/) 一键发布成文档站。

## 关于 SKILL.md 的小说明

各 `SKILL.md` 同时满足两套 frontmatter:Claude Code Skill 需要的 `name`/`description`,与 OKF 需要的 `type`。两者共存——OKF 明确允许生产者加任意额外键(§4.1),Skill 加载器也忽略它不认识的键。一份文件,两种身份。
