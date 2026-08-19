---
type: Specification
title: 开放知识格式(OKF)规范 · 中文版
description: OKF v0.2 规范 SPEC.md 的完整中文翻译,附硬要求与留白标注、v0.1→v0.2 迁移说明,以及 i18n 扩展提案草案。
tags: [okf, 规范, 翻译, 提案, v0.2]
lang: zh
canonical: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
generated: { by: human:yzfly, at: 2026-08-19T00:00:00Z }
author: 云中江树(译)
---

# 开放知识格式(OKF)规范 · 中文版

> **版本 0.2**。本文是 [OKF 官方规范 SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) 的完整中文翻译,附译注。
> 规范用词遵循 RFC 2119 惯例:**必须**(MUST)、**绝不可**(MUST NOT)、**应当**(SHOULD)、**可以**(MAY)。
> 从 v0.1 升上来的读者,可直接跳到 [§13 与 v0.1 的差异](#13-与-v01-的差异)。

OKF 是一种开放的、对人与智能体都友好的**知识**表示格式:围绕数据与系统的元数据、上下文与经过策展的洞见。它被设计成由人撰写、由智能体生成、在组织间交换,并被双方共同消费。

这个格式刻意保持极简:**一个目录的 Markdown 文件,带 YAML 头信息**。没有 schema 注册表,没有中心权威,也不要求任何工具链。你能 `cat` 一个文件,你就能读 OKF;你能 `git clone` 一个仓库,你就能分发它。

本文自包含:生产和消费 OKF v0.2 所需的一切都在这里。与 v0.1 的差异汇总在 §13。

---

## 1. 动机

面向 AI 智能体的知识表示领域演进很快,各种互不兼容的约定正在涌现。OKF 的立场是:知识最好用**普遍可读、已经成熟**的格式来表示,这样的格式应当:

- 人**无需工具**即可**阅读**。
- 智能体**无需专用 SDK** 即可**解析**。
- 在版本控制里可**diff**。
- 跨工具、跨组织、跨时间可**移植**。

而且越来越明显的是:一个知识语料库不再是"写一次、然后被读",而是**由智能体持续书写与维护**。当大多数概念都由机器生成时,消费者需要几个"纯 Markdown + 头信息"这一层约定无法一等公民化地回答的问题:

1. 这份内容是从什么材料来的、又是怎么被核实的?(**出处 / provenance**)
2. 我该信它到什么程度?(**信任 / trust**)
3. 它现在还成立吗?(**新鲜度 / freshness**)
4. 它是当前版本吗?(**生命周期 / lifecycle**)
5. 这个数字是不是按我们规定的方式算出来的?(**认证 / attestation**)

OKF v0.2 把出处、信任、生命周期与认证做成一等公民,同时保持格式本身的"最小主张":它只标准化那一小套让知识语料库**自描述**所必需的结构约定,此外的一切都留给生产者。

### 目标

1. 定义一个**生产者**(人、智能体、导出管线)可以写入的通用格式。
2. 指导**消费者**(智能体、UI、搜索索引、确定性代码)应当如何读取与遍历它。
3. 促进知识在系统与组织之间**交换**。
4. 标准化那一小套让"智能体维护的语料库"**可被信任**的头信息字段,同时不规定任何运行时。

### 非目标

- 定义一套固定的概念类型分类法。
- 规定存储、服务或查询基础设施。
- 取代领域特定 schema(Avro、Protobuf、OpenAPI 等)。OKF **引用**它们,不吞并它们。
- 为 executor / attester 所指向的代码规定打包或调用标准。**OKF 钉死接口,不钉死打包方式。**

---

## 2. 术语

- **知识包(Knowledge Bundle,简称 bundle)**:自包含、有层级的知识文档集合,是分发的单位。
- **概念(Concept)**:包内的一个知识单元,对应一个 Markdown 文档。它可以描述一个有形资产(一张表、一个 API)、一个抽象想法(一个指标、一个业务流程),或介于两者之间的任何东西。
- **概念 ID**:该概念文件在包内的路径,去掉 `.md` 后缀。
- **头信息(Frontmatter)**:Markdown 文件顶部由 `---` 包裹的 YAML 元数据块。
- **正文(Body)**:头信息之后的全部内容。
- **链接(Link)**:从一个概念指向另一个概念的标准 Markdown 链接,用来表达隐式父子层级之外的关系。
- **来源(Source)**:某个概念所依据的材料,可以在包外也可以在包内,记录在 `sources` 头信息字段中。
- **出处(Provenance)**:一个概念所依据的来源集合。
- **可信度信号(Credibility signal)**:关于单个来源的客观事实(`author`、`usage_count`、`last_modified`),用于推断信任。**OKF 记录信号,不记录结论**(见 §5.1)。
- **执行者(Actor)**:标识"谁或什么执行了某个动作"的字符串,约定为智能体用 `<producer>/<version>`、人用 `human:<id>`、自动化流程用 `process:<id>`(见 §7)。
- **信任层级(Trust tier)**:由概念的 `verified` 字段推导出的等级——未验证、机器确认、人工复核(见 §5.3)。
- **可验算计算(Attested Computation)**:一种概念(`type: Attested Computation`),携带计算某个值的"官方认可做法",使消费者能确认该值确实是跑这段计算得到的(见 §10)。
- **执行者程序(Executor)**:执行计算并返回回执的运行说明或代码(见 §10.2)。
- **回执(Receipt)**:一次运行返回的证据,形状由 `executor.receipt` 规定;它是**运行时产物,不存进包里**(见 §10)。
- **认证器(Attester)**:检查回执并给出裁决的确定性代码(**不含 LLM**)(见 §10.2)。

---

## 3. 包结构

一个包就是一棵 Markdown 文件的目录树。目录结构与领域无关:生产者按知识本身的合理组织方式来摆放概念。

```
path/to/bundle/
  index.md                      # 可选。目录清单,用于渐进式展开。
  log.md                        # 可选。更新历史(按时间)。
  <concept>.md                  # 包根目录下的一个概念。
  <subdirectory>/               # 子目录把概念分组。
    index.md
    <concept>.md
    <subdirectory>/
      ...
```

一个包**可以**通过以下方式分发:

- 一个 git 仓库(**推荐**,因为它自带历史、署名与 diff)。
- 该目录的 tarball 或 zip 归档。
- 更大仓库中的一个子目录。

### 3.1 保留文件名

以下文件名在层级的任意一级都有既定含义,**绝不可**用作概念文档:

| 文件名     | 用途                 |
|------------|----------------------|
| `index.md` | 目录清单。见 §8。    |
| `log.md`   | 更新历史。见 §9。    |

其余所有 `.md` 文件都是概念文档。

标签(tag)通过 `tags` 头信息字段保持一等公民地位(§4.1)。OKF **不**为"按标签聚合文档"规定单独的文件格式;想要标签浏览视图的消费者,可以在消费时扫描头信息自行合成。

---

## 4. 概念文档

每个概念都是一个 UTF-8 的 Markdown 文件,由两部分组成:

1. 一个 **YAML 头信息块**,以独占一行的 `---` 开始于文件开头,并以独占一行的 `---` 结束。
2. 一个 **Markdown 正文**,内容自由。

### 4.1 头信息

```yaml
---
type: <类型名>                     # 必须
title: <可选的展示名>
description: <可选的一句话摘要>
resource: <可选的底层资产规范 URI>
tags: [<tag>, <tag>, ...]          # 可选
# … 信任、生命周期、出处与计算家族(见 §5、§10)
# … 其他由生产者自定义的键值对
---
```

**必须:**

- `type`:一个短字符串,标识概念的种类。消费者用它做路由、过滤与呈现。示例取值:`BigQuery Table`、`BigQuery Dataset`、`API Endpoint`、`Metric`、`Playbook`、`Reference`、`Attested Computation`。

  类型取值**不做中心注册**。生产者**应当**选择自解释、描述性的取值;消费者**必须**优雅地容忍未知类型,通常做法是当成通用概念处理。

`type` 是唯一永远必填的键;**一个只带 `type` 的概念就是完全合规的**(§11)。

**推荐:**

- `title`:人类可读的展示名。省略时消费者**可以**从文件名推导。
- `description`:一句话摘要。被 `index.md` 生成器、搜索摘要与预览使用。
- `resource`:唯一标识该概念所描述的底层资产的 URI。描述抽象想法而非实体资源的概念没有这一项。
- `tags`:短字符串的 YAML 列表,用于横切分类。

可选的**出处**、**信任**、**生命周期**家族(§5),以及可验算计算概念的**计算**字段(§10),也可以出现在这里。

**扩展:** 生产者**可以**加入任意额外的键。消费者在往返读写时**应当**保留未知键,并且**绝不可**因为存在无法识别的字段而拒绝文档。

### 4.2 正文

正文是标准 Markdown。生产者**应当**优先使用结构化 Markdown(标题、列表、表格、围栏代码块)而不是散文,因为结构同时有利于人阅读与智能体检索。

没有任何必需的正文章节。以下标题具有**约定**含义,适用时**应当**使用:

| 标题            | 用途                                             |
|-----------------|--------------------------------------------------|
| `# Schema`      | 对资产字段 / 列的结构化描述。                    |
| `# Examples`    | 具体用法示例,通常是围栏代码块。                 |
| `# Computation` | 可验算计算的官方认可算法。见 §10。               |

针对单条论断的来源归属,使用**以 `sources` 条目为键的 Markdown 脚注**,而不是正文里的引用清单(§5.1)。

> 🔄 **v0.1 迁移提示**:v0.1 的正文 `# Citations` 列表已被头信息 `sources` 取代(§13.1)。

### 4.3 示例:一个绑定到资源的概念

```markdown
---
type: BigQuery Table
title: Customer Orders
description: One row per completed customer order across all channels.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, orders, revenue]
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-05-28T14:30:00Z }
---

# Schema

| Column        | Type      | Description                              |
|---------------|-----------|------------------------------------------|
| `order_id`    | STRING    | Globally unique order identifier.        |
| `customer_id` | STRING    | Foreign key into [customers](/tables/customers.md). |
| `total_usd`   | NUMERIC   | Order total in US dollars.               |
| `placed_at`   | TIMESTAMP | When the customer submitted the order.   |

# Joins

Joined with [customers](/tables/customers.md) on `customer_id`.
```

### 4.4 示例:一个不绑定资源的概念

```markdown
---
type: Playbook
title: "Incident response: data freshness alert"
description: Steps to triage a freshness alert on the orders pipeline.
tags: [oncall, incident]
generated: { by: human:ahormati, at: 2026-04-12T09:00:00Z }
---

# Trigger

A freshness alert fires when `orders` lags more than 30 minutes behind its
expected SLA. See the [orders table](/tables/orders.md).

# Steps

1. Check the [ingestion job dashboard](https://example.com/dash).
2. ...
```

---

## 5. 出处、信任与生命周期

这几个头信息家族,让"它从哪来""该信多少""是否还成立"这三件事可以直接从头信息里回答。**它们全部可选。** 它们的缺失本身也携带信息:一个未验证的概念与一个已验证的概念是可区分的,但前者永远不会因此被拒绝(§11)。

### 5.1 出处:`sources`

`sources` 记录一个概念所依据的材料,可以在包外,也可以在包内。

```yaml
sources:
  - id: ga4-schema
    resource: https://developers.google.com/analytics/bigquery/export-schema
    title: GA4 BigQuery Export schema
    author: team:ga4-docs
    usage_count: 5000
    last_modified: 2026-05-30
usage_window: { from: 2026-06-01, to: 2026-06-30 }
```

每个 `sources` 条目:

- `resource`:**条目内必填**。它要么指名一个消费者可以跟过去的具体产物(绝对 URL、包内相对路径,或指向 `references/` 子目录的路径,§6),要么是一个消费者跟不过去的**总体或范围描述**(例如 `all queries in BigQuery project X`)。
- `id`:可选。用于归属单条论断的稳定键。当正文引用该来源时**应当**提供。
- `title`:可选。给人看的来源标签。
- 可选的可信度信号 `author`、`usage_count`、`last_modified`,见下。

**来源可信度信号。** OKF 记录**客观的、按来源计的**信号,使消费者能通过"它是从什么材料里抽出来的"来判断一个概念可信到什么程度。它**不存储可信度分数**:分数是主观的、跨消费者不可移植、而且会过期。可信度和信任层级一样是被**推断**出来的(§5.3),不是被存下来的。每个信号都可选,都挂在某个 `sources` 条目上:

- `author`:谁 / 什么产出了这个来源,使用执行者约定(§7)。这是**权威性**信号。
- `usage_count`:在 `usage_window` 期间 `resource` 被使用了多少次(仪表盘浏览、查询执行、页面阅读)。这是**采纳度与存活度**信号。对单个产物就是它自身的使用次数;对范围描述则是该范围内触及此概念的使用次数。
- `last_modified`:来源自身最后一次变更的时间(`YYYY-MM-DD`)。这是**新近度**信号,区别于记录"概念何时被写"的 `generated.at`(§5.2)。
- `usage_window`:作为 `sources` 的兄弟键写一次,用 `{ from, to }` 日期区间为所有 `usage_count` 提供口径。单个条目**可以**带自己的 `usage_window` 覆盖共享值。

`usage_count` 是一个**粗粒度**信号。它在"活着还是死了"以及数量级层面可比,也可与来源自身的历史趋势相比,但**不能**当作跨种类的精确排序:一个定时查询的执行次数,和一个人主动查看仪表盘的次数,权重并不相等。消费者**应当**把它读作存活度与趋势,而不是分数。

**血缘(lineage)通过链接表达,而不是专门字段。** 当某个 `resource` 指向另一个 OKF 概念时,派生关系这条边已经存在于包的图里(§6),因此消费者**可以**递归进入那个来源自身的 `sources`,让可信度沿链传播。外部叶子来源只携带其自身的固有信号。更深的血缘(显式的外部 `derived_from`,或数据血缘)不在 v0.2 范围内。

**按论断归属。** 要把某条具体论断归到某个来源,使用**标签为 `sources[].id` 的 Markdown 脚注**:

```markdown
The `events_` table is sharded daily as `events_YYYYMMDD`.[^ga4-schema]

[^ga4-schema]: GA4 BigQuery Export schema
```

脚注标签就是连回 `sources` 的 join key;消费者通过匹配条目来解析归属,而不是去解析脚注的散文内容。之所以用**键**而不是位置(`sources[0]`):智能体会不断重写这些文档,一旦列表被重排,位置索引会静默错配,而稳定的 `id` 能扛过重排。

### 5.2 信任:`generated` 与 `verified`

`generated` 记录当前内容是**怎么产生**的。`verified` 记录**谁 / 什么确认过**内容与其来源或 `resource` 一致。二者刻意分开,因为**写**这个概念的人未必是**确认**它的人。

```yaml
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
```

- `generated.by`:**`generated` 内必填**。一个执行者(§7)。
- `generated.at`:ISO 8601 日期时间,标记内容最后一次有意义的变更。消费者用它区分"刚改过"和"陈年旧事"。

```yaml
verified:
  - { by: human:ahormati, at: 2026-06-25T09:00:00Z }
  - { by: process:finance-nightly, at: 2026-06-26T02:00:00Z }
```

- `verified`:验证事件的列表,每项含 `by`(执行者)与 `at`(ISO 8601 日期时间)。多个条目用来记录彼此独立的检查,例如一次人工签字加一个夜间流程。"多近验证过"取最新的 `at`。
- `verified` 与 `generated.at` 相互独立:内容可以变了却没被重新确认,事实也可以被重新确认而无需重新生成。
- 单个验证者**可以**写成一个不带列表短横的 `{ by, at }` 映射。消费者**必须**把裸映射当成单元素列表处理:

```yaml
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
```

### 5.3 信任层级

消费者从 `verified` 推导信任层级,由低到高:

- 没有 `verified` 键 ⇒ **未验证(unverified)**。
- `verified` 仅由非 `human:` 执行者签署 ⇒ **机器确认(machine-confirmed)**。
- `verified` 中含 `human:<id>` 执行者 ⇒ **人工复核(human-reviewed)**。

没有任何信任头信息的概念**仍然可消费**;消费者**绝不可**因此拒绝它(§11)。**信任层级是建议性信号,不是访问控制。**

### 5.4 生命周期:`status`

```yaml
status: stable        # draft | stable | deprecated
```

- `draft`:尚未复核,可能不完整。
- `stable`:默认值,可供消费。
- `deprecated`:为链接与历史保留,已不再是当前内容。

缺省 `status` ⇒ 视为 `stable`。

### 5.5 生命周期:`stale_after`

```yaml
stale_after: 2026-09-23   # 绝对日期;当天及之后内容视为过期
```

可选。一个绝对日期(`YYYY-MM-DD`)。当 `today >= stale_after` 时该概念过期。**用绝对日期而不是相对 TTL**,是为了让过期判断退化成一次纯粹的日期比较,不需要引用"这份内容是什么时候被读的"。

---

## 6. 交叉链接与路径

### 6.1 概念之间的链接

概念**可以**用标准 Markdown 链接指向其他概念。支持两种形式:

- **绝对(包内相对)**:以 `/` 开头,相对包根解释。这是**推荐**形式,因为文档在其子目录内移动时它依然稳定。

  ```markdown
  See the [customers table](/tables/customers.md) for the join key.
  ```

- **相对**:标准 Markdown 相对路径。

  ```markdown
  See the [neighboring concept](./other.md).
  ```

从概念 A 到概念 B 的链接断言了一种**关系**。具体是哪种关系(父子、引用、可 join、依赖)由周围的散文表达,而不是由链接本身表达。构建图视图的消费者通常把所有链接当作**无类型关系的有向边**。

消费者**必须**容忍坏链接:目标不存在于包内的链接并不算格式错误,它可能只是**尚未写出的知识**。

### 6.2 取路径值的字段

有几个字段的取值是路径或 URI:`resource`、`sources[].resource`、`computation`、`executor.resource` 与 `attester.resource`(§10)。其中 `sources[].resource` 也可以是范围描述(§5.1),那种情况下它不是路径。每个取路径值的字段接受:

- 绝对 URL(例如 `https://...`),
- 以 `/` 开头的包内相对路径,或
- 相对路径(例如 `../computations/revenue.md`)。

### 6.3 `references/` 约定

`references/` 子目录按约定用来把外部材料、运行说明或代码**镜像成包内的一等概念**。来源、执行者程序与认证器常常指向它(例如 `references/attesters/revenue.py`)。这是命名约定,不是要求。

---

## 7. 执行者约定

记录身份的字段(`generated.by`、`verified[].by`)使用统一的执行者约定:

- 智能体与工具用 `<producer>/<version>`,例如 `reference_agent/gemini-2.5-pro`。
- 人用 `human:<id>`,例如 `human:ahormati`。
- 自动化流程用 `process:<id>`,例如 `process:finance-nightly`。

做信任分层的消费者(§5.3)依赖 `human:` 前缀来判定,因此对于手写或经人确认的内容,生产者**必须**使用该前缀。

---

## 8. 索引文件

`index.md` **可以**出现在任意目录,包括包根。它枚举该目录的内容,以支持**渐进式展开**:让人或智能体在打开具体文档之前,先看到有些什么。

索引文件**不含头信息**,只有一个例外:**包根**的 `index.md` **可以**带一个 `okf_version` 键(§12)。正文由一个或多个章节组成,每节在一个标题下聚合若干概念:

```markdown
# Section / Group Heading

* [Title 1](relative-url-1) - short description of item 1
* [Title 2](relative-url-2) - short description of item 2

# Another Section

* [Subdirectory](subdir/) - short description of the subdirectory
```

条目**应当**带上所链接概念头信息里的 `description`。生产者**可以**自动生成 `index.md`;消费者也**可以**在没有索引时即时合成一个。

---

## 9. 日志文件

`log.md` **可以**出现在层级的任意一级,记录该范围内的变更历史。格式是**按日期分组、最新在前**的扁平列表:

```markdown
# Directory Update Log

## 2026-05-22
* **Update**: Added a BigQuery table reference for [Customer Metrics](/tables/customer-metrics.md).
* **Creation**: Established the [Dataplex Playbook](/playbooks/dataplex.md).

## 2026-05-15
* **Initialization**: Created foundational directory structure.
```

日期标题**必须**使用 ISO 8601 的 `YYYY-MM-DD` 形式。日志条目是散文;开头加粗的那个词(`**Update**`、`**Creation**`、`**Deprecation**`)是约定,不是要求。

---

## 10. 可验算计算概念

可验算计算概念不仅携带一个值**意味着什么**,还携带**官方认可的算法**,从而让消费者能确认智能体跑的是这段被认可的计算,而不是自己即兴发挥的版本。出处(§5.1)回答"这条论断从哪来";**认证回答"这个数字是不是按我们规定的方式产生的"**。OKF 记录计算本身以及核对它的手段;**它自己不执行任何东西**。

### 10.1 一段计算就是一个独立概念

被认可的计算是一个 `type: Attested Computation` 的独立概念。需要这个值的概念(一个 `Metric`、一张 `BigQuery Table`)用普通 Markdown 链接指向它(§6)。三个性质决定了它必须独立成概念:

- **`runtime` 定义了 `parameters` 的含义。** 一个参数究竟是 SQL 绑定变量、dbt var,还是 Python 实参,取决于运行时。把 `runtime` 与 `parameters` 放进同一份头信息,绑定语义才是自明的。
- **一段计算,多个消费者。** 同一段计算可以同时支撑一个指标、一个仪表盘概念和一份报表;做成概念就只需被引用一次、被复用多次。
- **信任状态是按计算走的。** `verified`、`stale_after` 与单个 `attester` 描述的是**一件事**。收入、利润、毛利率各自独立验证与认证,那就是三个概念,而不是一份头信息里的三个条目。

### 10.2 契约字段

契约就是该概念的顶层头信息。除了出处、信任与生命周期家族(§5),一个可验算计算概念还携带:

- `runtime`:**本类型必填**。它是"这段计算怎么跑"的唯一字段,也因此决定了执行者程序与认证器如何解释它、以及 `parameters` 意味着什么。示例取值:`bigquery`、`postgres`、`dbt`、`python`、`Looker`。
- `parameters`:一个列表,列出智能体可以填的、有类型的具名空位。每项形如 `{ name, type, required }`。绑定语义随 `runtime` 而定。
- `computation`:可选。指向存放计算的文件的路径(§6.2),用来替代正文内联围栏(见 §10.3)。缺省 ⇒ 正文的 `# Computation` 围栏即为计算本体。
- `executor`:计算怎么被运行。`resource` 指名运行说明或代码,由一个 runner(智能体,或确定性的消费者代码)照着执行。`receipt` 声明一次运行必须返回哪些字段,也就是认证器要检查的证据(例如 BigQuery 的 `job_id` 与该 job 实际执行的 SQL)。
- `attester`:确定性检查。`resource` 指名一段代码(**不含 LLM**),它接收回执并返回裁决。它设计成在**消费者侧**运行。

`resource` 背后到底是一个 Skill、一个脚本还是一个容器,属于打包选择;**OKF 钉死接口,不钉死打包方式**(§1)。

```markdown
---
type: Attested Computation
title: Revenue for fiscal year
description: Recognized revenue for a fiscal year, per Finance's definition.
status: stable
runtime: bigquery
parameters:
  - { name: year, type: integer, required: true }
executor:
  resource: references/skills/run-on-bq.md
  receipt: [job_id, executed_sql, result]
attester:
  resource: references/attesters/revenue.py
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
verified: { by: human:ahormati, at: 2026-06-25T09:00:00Z }
stale_after: 2026-09-23
sources:
  - id: rev-policy
    resource: https://wiki.acme/finance/revenue-recognition
    title: Revenue recognition policy
---

# Computation

    SELECT SUM(amount) AS revenue
    FROM finance.recognized_revenue
    WHERE fiscal_year = @year

The computation binds only the declared `parameters`, per the recognition
policy.[^rev-policy]

[^rev-policy]: Revenue recognition policy
```

### 10.3 计算本体

用以下两种方式之一提供计算:

- **内联**:正文 `# Computation` 之下的一个围栏代码块。适合与契约放在一起复核的短计算。
- **文件**:把 `computation` 设为一个路径(§6.2),并省略正文围栏。适合长的或自动生成的计算,或者本来就作为真实文件与非 OKF 工具共享的计算。

```yaml
runtime: bigquery
computation: references/computations/lib/revenue.sql
parameters:
  - { name: year, type: integer, required: true }
```

智能体**只可以**为已声明的 `parameters` 提供**取值**;它**绝不可**撰写或修改计算本身。把 `computation` 与参数值绑定成可执行产物是消费者的职责,而认证器会**独立地**重新推导同一次绑定,用来与实际跑的东西比对。因为比对的是回执携带的**展开后、编译后的产物**(`executed_sql`、`compiled_sql`),所以被重写的查询、被掉包的计算文件、被篡改的依赖都会检查失败。**一个有类型、只开放参数的接口面,正是"被认可的东西有没有真的跑"这件事能变成机械比对、而不是主观判断的原因。**

### 10.4 使用计算的概念

一份文档很少只包含一段计算。一份同时讨论收入、利润与毛利率的利润表概览,仍然保持为**一个可读概念**,并为每个数字链接到一个可验算计算:

```markdown
---
type: Metric
title: Revenue
description: Recognized revenue for a fiscal year.
tags: [finance, revenue]
status: stable
generated: { by: reference_agent/gemini-2.5-pro, at: 2026-06-20T22:53:05Z }
---

# Definition

Recognized revenue sums `amount` over rows booked to the fiscal year,
computed by [the revenue computation](../computations/revenue.md).
```

因为每段计算都是独立概念,所以收入可以是新鲜的、而利润已经过了它的 `stale_after`,并且各自在自己的运行上做认证。把它们放在一起,是**目录层面的选择**(一个带 `index.md` 的 `computations/` 目录),而不是头信息层面的选择。

### 10.5 消费者怎么用它(资料性)

本小节是资料性的,非规范性。下面提到的运行时产物**不**存进包里。

1. **发现**:通过 `type: Attested Computation` 这一头信息信号(可被提升进 `index.md`);消费者可以直接抵达它,也可以从使用它的概念顺着链接找过来。
2. **加载**:从头信息加载契约,从正文(或 `computation` 指名的文件)加载计算。
3. **参数化**:智能体为已声明的参数提供取值。
4. **执行**:执行者程序运行绑定后的计算,返回一份形状由 `executor.receipt` 规定的回执。
5. **认证**:消费者在回执上运行认证器。它确认**出处**(实际跑的计算等于 `computation` 与所声称参数的绑定结果,而不是智能体自己写的 SQL)与**保真度**(展示出来的值与回执的权威来源一致——按 job id 重新读取,而不是采信智能体文本里的数字)。
6. **闸门**:认证失败则拒绝展示;当 `today >= stale_after` 时告警或拒绝。成功时把裁决暴露出来(例如给出 job 日志链接),让信任是可见的。

### 10.6 验证 vs 认证

`verified`(§5.2)与认证是两件事,而且两者都需要:

- `verified` 确认**定义**仍然符合政策。它是**文档级**的、慢的,存在包里。
- 认证确认**单次运行**是按被认可的方式产出该值的。它是**按调用**的、运行时的,不存在包里。

一个定义已经陈旧的概念仍然可以认证通过,而一个刚刚验证过的定义在每次运行时依然需要认证——这就是两者都必需的原因。

---

## 11. 符合性

一个包**符合** OKF v0.2,当且仅当:

1. 目录树中每个非保留的 `.md` 文件,都含有一个可解析的 YAML 头信息块。
2. 每个头信息块都含有一个非空的 `type` 字段。
3. 每个保留文件名(`index.md`、`log.md`)在出现时,分别遵循 §8 与 §9 所述结构。

当信任、生命周期、出处或计算家族出现时,生产者**应当**遵循 §5 至 §10,并且消费者:

- **必须**把裸的 `verified` 映射当作单元素列表处理(§5.2)。
- **绝不可**因为缺少任何可选家族而拒绝一个概念(§5.3)。
- **应当**只依据本规范所定义的字段推导信任层级与过期状态,并且**应当**把失败的认证**暴露出来而不是静默丢弃**(§10.5)。

消费者**应当**把其他所有约束都视为软性指引。特别地,消费者**绝不可**因为以下原因拒绝一个包:

- 缺少可选头信息字段。
- 未知的 `type` 取值。
- 未知的额外头信息键。
- 坏的交叉链接。
- 缺少 `index.md` 文件。

> 🧭 **这就是全部硬要求。** 整份规范真正的 MUST,产出侧核心仍然是上面三条(其中 1、2 是产出门槛,3 仅在文件存在时适用)。门槛几乎为零——**任何带 `type` 的 md 都合规**。v0.2 新增的 MUST 全部落在**消费者**一侧(怎么读裸 `verified`、不许因缺字段而拒绝、别吞掉失败的认证),生产门槛一点没抬。**互操作靠的是约定与作品质量,而非校验器。**

---

## 12. 版本管理

本文件规定 OKF 版本 **0.2**。修订以 `<主>.<次>` 形式版本化:

- **次版本**号提升,引入向后兼容的新增内容(新的可选字段、新的约定章节标题)。
- **主版本**号提升,可能带来破坏性变更(重命名必须字段、更改保留文件名)。

包**可以**声明它面向的 OKF 版本,方式是在包根目录的 `index.md` 头信息块里写入 `okf_version: "0.2"`(这是 `index.md` 中唯一允许出现头信息的地方)。不理解所声明版本的消费者,**应当**尽力做"尽最大努力的消费",而非拒绝该包。

### 已考虑但推迟的内容

以下内容有意留给未来修订:

- 完整的运行时协议:回执与裁决的传输格式,以及一次运行前后的认证生命周期。
- 认证器 ABI、可移植性与沙箱,大概率会与未来的"服务与 Skills"工作打包在一起。
- 认证结果缓存。
- 语义层模板(Looker、dbt),在那里认证器的比对会从 SQL 等价转成"模型与绑定"等价。

---

## 13. 与 v0.1 的差异

v0.2 取代 OKF v0.1,按 §12 属于一次**次版本**提升,但有两处**刻意的破坏性变更**——因为它们重命名或退役了 v0.1 的字段,所以单独列出。一个 v0.1 包在下述回退规则下仍可被 v0.2 消费者消费。

### 13.1 破坏性变更

- **`timestamp` 被 `generated.at` 取代。** 概念最后一次内容变更现在记录为 `generated: { by, at }`(§5.2)。当 `generated` 缺席时,消费者**可以**回退到遗留的 `timestamp`。
- **正文 `# Citations` 列表被 `sources` 取代。** 出处移进头信息(§5.1)。消费者**应当**读 `sources`,并且对 v0.1 文档**可以**仍然解析遗留的 `# Citations` 正文列表。

### 13.2 新增内容

以下全部是新增:新的可选键、一个新概念类型、一个新约定标题。它们缺席时,得到的就是一个朴素的 v0.1 概念。

- 新的头信息家族:`sources` 及其按来源的可信度信号(`author`、`usage_count`、`last_modified`)与兄弟键 `usage_window`;`generated`、`verified`;`status`、`stale_after`(§5)。
- 新概念类型 `Attested Computation` 及其计算键 `runtime`、`parameters`、`computation`、`executor`、`attester`(§10)。
- 新的约定正文标题 `# Computation`(§4.2)。
- 用于 `generated.by` 与 `verified[].by` 的执行者约定(§7)。

其余一切(包结构、保留文件名、必填的 `type`、推荐的 `title`/`description`/`resource`/`tags`、交叉链接、索引文件、日志文件、宽容的符合性)原样延续。

> 🧭 **译注:升级成本。** 对一个已有的 v0.1 包来说,升到 v0.2 的**最小**动作只有两步:把 `timestamp: X` 改写成 `generated: { by: <执行者>, at: X }`,把正文 `# Citations` 列表搬进头信息 `sources`。其余家族(`verified`/`status`/`stale_after`/可验算计算)全部可选,不写也是合规的 v0.2 包。本仓库自身就是按这两步迁移的,可参考 [dogfooding 说明](./dogfooding-zh.md)。

---

## 与其他格式的关系

OKF 刻意地贴近若干已有模式:

- **LLM "维基" 仓库**——用 Markdown + 头信息作为智能体可读的知识库。
- **个人知识工具**,如 Obsidian 和 Notion——使用带交叉链接的层级 Markdown。
- **"元数据即代码"**——把目录元数据与源代码放在一起,而非放进单独的注册表。

OKF 的主要区别在于它**被规范化了**——钉死了互操作所需的那一小套规则,同时不对工具链发号施令。v0.2 在这条线上又前进一步:它把"这份知识可不可信"也做成了可移植的、纯文本的约定,而不是某个平台的私有字段。

---

## 附录 A:完整示例——一张利润表

官方规范用一个同时演练所有家族的例子收尾:一张含两个数字(收入与毛利)的利润表,从 v0.1 迁到 v0.2。

**v0.1 形态**——两个数字挤在一个概念里,SQL 以散文形式存在(智能体可以读、可以忽略、也可以改写),引用是一个扁平列表,唯一的时间戳是 `timestamp`:

```markdown
---
type: Metric
title: Income statement (fiscal year)
description: Headline income-statement figures for a fiscal year.
tags: [finance, income-statement]
timestamp: '2026-05-28T22:53:05+00:00'
---

# Definition
The income statement reports revenue and gross profit for a fiscal year.

# Revenue
Recognized revenue sums `amount` over rows booked to the fiscal year:

    SELECT SUM(amount) AS revenue
    FROM finance.recognized_revenue
    WHERE fiscal_year = <year>

# Gross profit
Gross profit by segment, per the cost-allocation standard:

    SELECT gross_profit FROM fct_income_statement
    WHERE fiscal_year = <year> AND segment = <segment>

# Citations
- https://wiki.acme/finance/fpa-handbook
- https://wiki.acme/finance/revenue-recognition
- https://wiki.acme/finance/cost-allocation
```

**v0.2 形态**——两个数字被拆成两个可验算计算,由一个叙述性概念链接过去;所有家族都被填满,并且两段计算被刻意置于不同状态,于是同一个消费者会得到两种裁决:

```
bundles/finance/
  index.md
  income-statement.md              # 叙述性概念,链接到两段计算
  computations/
    index.md
    revenue.md                     # type: Attested Computation
    gross-profit.md                # type: Attested Computation
  references/
    skills/run-on-bq.md            # executor
    attesters/revenue.py           # attester
```

完整逐文件内容见[官方规范附录 A](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#appendix-a-worked-example-an-income-statement)。要点是:叙述留在一个可读概念里,而每个数字各自拥有契约、信任状态与认证路径。

---

## 中文生态议题:i18n 扩展提案草案

> 这部分不属于官方规范,是本仓库基于 §4.1"生产者可加入任意额外键"提出的、**向后兼容**的多语言约定,供讨论与向官方提案。
>
> **v0.2 复核结论:该提案依然成立且依然必要**——v0.2 新增了出处、信任、生命周期与认证四个家族,但**仍然没有任何"语言"概念**。

**问题:** OKF 至今没有任何"语言"概念。一份知识库若同时面向中英读者(以及中英两种消费智能体),无法表达"这是同一概念的中文版"。

**提案(作为 v0.x 次版本的可选字段):**

```yaml
---
type: BigQuery Table
title: 订单表
lang: zh                        # BCP 47 语言标签,标注本概念正文的语言
canonical: /tables/orders.md    # 指向同一概念的"主语言"版本(概念 ID)
---
```

约定:

1. `lang` — 可选字段,BCP 47 语言标签(如 `zh`、`zh-Hans`、`en`)。缺省时,消费者**应当**视为生产者未声明语言。
2. `canonical` — 可选字段,指向同一概念主语言版本的概念 ID。多语言变体彼此通过 `canonical` 收敛到同一主版本。
3. 文件组织两种皆可,生产者自选:
   - **并列文件**:`tables/orders.md`(主)与 `tables/orders.zh.md`(中文变体);
   - **并列目录**:`en/tables/orders.md` 与 `zh/tables/orders.md`。
4. 完全向后兼容:不认识 `lang`/`canonical` 的消费者按 §4.1 忽略未知键即可,bundle 仍然合规。

**与 v0.2 的衔接:** 翻译本身就是一次派生,因此中文变体**应当**在 `sources` 里把主语言版本列为来源,并用 `generated.by` 记录译者(人工翻译写 `human:<id>`,机翻写 `<producer>/<version>`)——这样"这份中文是谁译的、从哪一版译的、有没有人复核过"就全部落在了 v0.2 已有的字段上,`lang`/`canonical` 只需补上"是哪门语言、对应哪个主版本"这最后一块:

```yaml
lang: zh
canonical: /tables/orders.md
sources:
  - id: en-source
    resource: /tables/orders.md
    title: Orders table (English source)
generated: { by: human:yzfly, at: 2026-08-19T00:00:00Z }
verified: { by: human:yzfly, at: 2026-08-19T00:00:00Z }
```

**为什么这个口子是干净的:** 它只新增可选字段,不动任何 MUST,不改保留文件名——正好落在规范 §12 定义的"次版本可做向后兼容新增"里,也正好落在官方"明确欢迎扩展提案"的邀请里。

> 配套实现:本仓库的 [`feishu-to-okf`](../plugins/feishu-to-okf/) 导出时会写入 `lang: zh`,[`okf-creator`](../skills/okf-creator/) Skill 也内置这套约定。即"提案 + 参考实现"一起出。
