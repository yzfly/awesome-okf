---
type: Reference
title: OKF v0.2 速查表
description: 开放知识格式 v0.2 的字段, 出处/信任/生命周期家族, 保留文件名, 链接规则与符合性要点速查.
tags: [okf, 速查, reference, v0.2]
lang: zh
generated: { by: human:yzfly, at: 2026-08-19T00:00:00Z }
---

# OKF v0.2 速查表

> 完整中文规范见 [docs/okf-spec-zh.md](../../../docs/okf-spec-zh.md)。本表只列高频要点。
> 从 v0.1 升级?看最下面的[迁移两步走](#v01--v02-迁移两步走)。

## 一句话模型

一个 **bundle** = 一个目录;一个 **concept** = 一个 `.md` 文件;**concept ID** = 去掉 `.md` 的路径。

## 头信息:基础字段

| 字段 | 必需 | 说明 |
|---|---|---|
| `type` | ✅ **唯一硬要求** | 概念种类,自由字符串,消费者须容忍未知值 |
| `title` | 推荐 | 显示名,省略则从文件名推导 |
| `description` | 推荐 | 一句话摘要,索引/搜索摘要用 |
| `resource` | 推荐 | 底层资产的规范 URI,抽象概念可省 |
| `tags` | 可选 | 短字符串列表,横切分类 |
| 任意其他键 | 可选 | 生产者扩展,消费者须保留、不得因此拒绝 |

## 头信息:v0.2 新增家族(全部可选)

**出处(§5.1)**

```yaml
sources:
  - id: rev-policy                      # 可选,正文脚注 [^rev-policy] 的 join key
    resource: https://wiki.acme/...     # 条目内必填;URL / 包内路径 / 范围描述
    title: Revenue recognition policy   # 可选
    author: team:ga4-docs               # 可选,权威性信号
    usage_count: 5000                   # 可选,采纳度信号(整数)
    last_modified: 2026-05-30           # 可选,来源自身的新近度
usage_window: { from: 2026-06-01, to: 2026-06-30 }   # 为 usage_count 提供口径
```

**信任(§5.2)**

```yaml
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
verified:                               # 也可写成单个 { by, at } 裸映射
  - { by: human:ahormati, at: 2026-06-25T09:00:00Z }
```

- `generated.by` 在 `generated` 内必填;`generated.at` 记录内容最后一次有意义变更。
- 信任层级(§5.3):无 `verified` = 未验证 · 仅非 `human:` = 机器确认 · 含 `human:` = 人工复核。

**生命周期(§5.4 / §5.5)**

```yaml
status: stable          # draft | stable | deprecated,缺省视为 stable
stale_after: 2026-09-23 # 绝对日期;today >= 它即为过期
```

**执行者约定(§7)**:`human:<id>` · `process:<id>` · `<producer>/<version>`。
做信任分层的消费者认 `human:` 前缀,所以手写/人工确认的内容**必须**用它。

## 可验算计算(§10)

`type: Attested Computation` 是 v0.2 唯一新增的类型,让"这个数字是不是按规定算的"可被机械核验:

| 字段 | 说明 |
|---|---|
| `runtime` | **本类型必填**。`bigquery` / `postgres` / `dbt` / `python` / `Looker` … 它决定 `parameters` 的绑定语义 |
| `parameters` | `{ name, type, required }` 列表;智能体**只能填值,不能改计算** |
| `computation` | 可选。计算文件路径;缺省则用正文 `# Computation` 围栏 |
| `executor` | `resource`(运行说明/代码)+ `receipt`(一次运行必须返回的字段) |
| `attester` | `resource`:确定性检查代码(**不含 LLM**),消费者侧运行 |

`verified` 确认**定义**仍符合政策(文档级、存在包里);认证确认**单次运行**按认可方式产出该值(运行时、不存包里)。两者都需要(§10.6)。

## 保留文件名

| 文件 | 含义 | 头信息 |
|---|---|---|
| `index.md` | 目录清单(渐进式展开) | 无;**仅根** `index.md` 可含 `okf_version: "0.2"` |
| `log.md` | 变更历史,日期标题 `## YYYY-MM-DD` | 无 |

其余所有 `.md` 都是概念文档。

## 约定的正文标题

`# Schema`(列/字段结构) · `# Examples`(用例代码) · `# Computation`(可验算计算的算法,§10)。

> ⚠️ v0.1 的 `# Citations` 已被头信息 `sources` 取代。按条目归属改用**脚注**,标签即 `sources[].id`:
>
> ```markdown
> events_ 表按天分片。[^ga4-schema]
>
> [^ga4-schema]: GA4 BigQuery Export schema
> ```

## 交叉链接

- 推荐**包内绝对路径**:`[customers](/tables/customers.md)`(文件移动仍稳定)。
- 也支持相对路径:`[x](./other.md)`。
- 链接 = 一条**无类型**关系边;具体关系靠周围文字表达。
- 消费者**必须容忍坏链接**(可能是尚未写的知识)。
- 取路径值的字段(§6.2):`resource`、`sources[].resource`、`computation`、`executor.resource`、`attester.resource`。
- `references/` 是约定目录,用来把外部材料/运行说明/认证器代码镜像成一等概念(§6.3)。

## 符合性(§11)三条硬要求

1. 每个非保留 `.md` 有可解析 YAML 头信息;
2. 每个头信息有非空 `type`;
3. `index.md` / `log.md` 出现时遵循其结构。

消费者**绝不可**因以下原因拒绝 bundle:缺可选字段、未知 `type`、未知额外键、坏链接、缺 `index.md`。

v0.2 新增的 MUST 全部在**消费者**一侧:裸 `verified` 映射当单元素列表读、不因缺任何可选家族而拒绝、别静默丢掉失败的认证。**生产门槛没变——一个只带 `type` 的 md 依然完全合规。**

## v0.1 → v0.2 迁移两步走

| 动作 | v0.1 | v0.2 |
|---|---|---|
| 1. 时间戳 | `timestamp: 2026-06-28T00:00:00Z` | `generated: { by: human:you, at: 2026-06-28T00:00:00Z }` |
| 2. 引用 | 正文 `# Citations` 列表 | 头信息 `sources` + 正文脚注 |

其余家族全部可选,不写也是合规的 v0.2 包。根 `index.md` 顺手把 `okf_version` 改成 `"0.2"`。
校验:`python skills/okf-creator/scripts/validate_okf.py <bundle>`(遗留写法会给出迁移提示;迁移期可加 `--legacy-ok` 静默)。

## 本仓库扩展约定

- **i18n**:`lang`(BCP 47)+ `canonical`(主语言版本概念 ID)。**v0.2 仍无语言概念**,该提案依然必要。见 [okf-spec-zh.md 末尾](../../../docs/okf-spec-zh.md#中文生态议题i18n-扩展提案草案)。
- **代码**:类型词表 + `language`/`symbol`/`signature` + 行号锚点 + 有类型链接。**v0.2 补的是信任而非代码表达**,该提案同样依然必要。见 [code-support-research-zh.md](../../../docs/code-support-research-zh.md)。
