---
type: Reference
title: okf-gem(OKF 全链路 harness:创作 skill + CLI/库 + 图谱)
description: 覆盖 bundle 全生命周期的 harness:agent skill 负责创作与维护,CLI / 库做确定性校验与检索,图谱供人浏览,100% 本地运行。
resource: https://github.com/serradura/okf-gem
tags: [okf, harness, skill, cli, 图谱, ruby, 社区]
lang: zh
generated: { by: human:yzfly, at: 2026-07-21T00:00:00Z }
---

# okf-gem(OKF 全链路 harness:创作 skill + CLI/库 + 图谱)

生态里的工具大多只占 bundle 生命周期的一端:producer 只管写,linter 只管校验,查看器只管看。okf-gem 把这条环路合上,三部分各自对应一个角色:

* **Agent skill(创作端)** —— agent 从你已有的代码与文档里写出并持续维护概念,人保留编辑权。`okf skill .claude` / `okf skill .agents` 装进任意支持 skill 的 agent。
* **CLI / 库(确定性检查)** —— 给 agent 和 CI 一个可信的判据。`validate` 只判 OKF v0.1 §9 的硬合规,`lint` 只报策展质量(可读性、链接、时效),两者**刻意分开**:§9 明确要求 consumer 容忍坏链与缺失可选字段,所以校验器不该因为跨文件链接坏了就判不合规。另有排序检索 `search`,以及 `index` / `dirs` / `types` / `tags` / `catalog` / `stats` / `graph` 等视图,全部可 `--json`;同一套能力也能作为库在进程内调用。
* **图谱(阅读端)** —— `okf server` 起交互式知识图谱,`okf render` 把同一个页面导出成单文件、自包含的静态 HTML,让不装任何东西的读者也能读。服务端本身是可挂载的 Rack app,能直接嵌进 Rails 路由。在线示例:<https://demo.okfgem.com>

另有一层 per-user registry 给每个 bundle 起名:`okf registry set ./docs` 之后,`@docs` 在任何目录下都等价于路径,一条 `okf server` 就把已注册的多个 bundle 挂在同一个 hub 下。

项目对自己的定位是「让知识有一个持久的家」:agent 不必每次会话重新推导上下文,新同事与新 agent 读同一份文件,知识随时间累积而不是随会话蒸发。全程本地运行,无账号、无遥测、不上传任何内容。

实现语言是 **Ruby**(Apache-2.0,RubyGems 上的 `okf`),也是生态里第一个 Ruby 实现;不想装 Ruby 可以走官方 Docker 镜像。依赖克制:Ruby ≥ 2.4(与 rack 同一底线,系统自带的 Ruby 就能跑)、运行时只依赖 `rack` / `webrick` / `minifts`,无 ActiveSupport、无原生扩展、无前端构建。仓库自身用 `.okf/` 做 dogfooding——它的设计文档就是一个可以用它自己打开的 bundle。

与已收录项目的关系:[okftool](/references/okftool.md)(专做校验 / lint)与 [kiso](/references/kiso.md)(发布 / 阅读端)各占一环,okf-gem 的差异在于一个包覆盖创作到浏览的全链路。

源码:<https://github.com/serradura/okf-gem> ;站点与文档:<https://okfgem.com>
