---
type: Reference
title: okftool(Rust 校验器 + linter,三端分发)
description: Rust 实现的可嵌入 OKF 校验器 + linter,同一内核分发为原生 CLI、WASM/npm 包与可嵌入 crate,内置 18 条 lint 规则、3 套 profile。
resource: https://github.com/ryansann/okftool
tags: [okf, 校验, lint, rust, 头部]
lang: zh
timestamp: 2026-06-28T00:00:00Z
---

# okftool(Rust 校验器 + linter,三端分发)

工程成熟度高于一般玩具校验器的 **Rust** 实现:可嵌入的 OKF 校验器 + linter,"one core, three surfaces"——同一内核分发为原生 CLI、WASM/npm 包与可嵌入 crate;内置 18 条 lint 规则、3 套 profile,已连发多个 release。

与本仓库的 `validate_okf.py`、社区的 WitsCode Conformance Suite 等校验器相比,差异在于 Rust 内核 + 三端分发。同 owner 另有轻量查看器 `ryansann/okfview`,两者形态互补,均见 [resources-zh](/docs/resources-zh.md)。

源码:<https://github.com/ryansann/okftool>
