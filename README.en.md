---
type: Overview
title: Awesome OKF
description: Chinese-first notes and tools for the Open Knowledge Format (OKF), plus converters from common note/doc tools into OKF.
tags: [okf, awesome, en]
lang: en
canonical: /README.md
timestamp: 2026-06-14T00:00:00Z
author: 云中江树 (yzfly)
---

# Awesome OKF

English | [中文](./README.md)

Chinese-first notes and tools for the Open Knowledge Format (OKF): a translation of the spec and the launch blog, some background, plus a few small tools that convert Feishu, Obsidian, Notion, GitHub and so on into OKF, with matching Claude Code skills.

The repo itself is a conformant OKF v0.1 bundle — every doc has frontmatter, the root has `index.md` and `log.md`, and `python skills/okf-creator/scripts/validate_okf.py .` checks it.

## What OKF is

An open spec from Google Cloud (2026-06-12) that standardizes the "maintain a wiki with an LLM" pattern: knowledge is just **a directory of markdown files with YAML frontmatter plus a small set of conventions**. No runtime, no SDK, no central registry.

## What's here

A single CLI [`myokf`](./plugins/myokf-cli/) ties the command-line tools together:

```bash
myokf from-github yzfly/awesome-okf -o ./kb
myokf validate ./kb
myokf to-web ./kb -o kb.html
```

**Converters into OKF (plugins/):** feishu-to-okf, awesome-to-okf, obsidian-to-okf, notion-to-okf, html-to-okf, github-to-okf, and the unified myokf-cli.

**Skills (skills/):** okf-creator, awesome-to-okf, book-to-okf, code-to-okf, github-to-okf, okf-to-book, okf-to-web.

All tools are standard-library only; their output passes the conformance check.

## A few proposed extensions

OKF v0.1 leaves some gaps. Three backward-compatible ideas are written up here (docs + reference implementations), none touching any MUST:

- i18n — `lang` + `canonical` (see the [spec translation](./docs/okf-spec-zh.md))
- code support — type vocabulary, `language`/`symbol`/`signature`, line anchors, typed links (see the [research note](./docs/code-support-research-zh.md))
- HTML as a concept type (see the [proposal](./docs/html-first-class-proposal-zh.md))

## Links

Official: [spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) · [repo](https://github.com/GoogleCloudPlatform/knowledge-catalog) · [launch blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/). Lineage: [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Contributing & license

PRs welcome — anything OKF-related that runs or reads. See [CONTRIBUTING](./CONTRIBUTING.md). Docs are Chinese-first for now (tagged `lang`); English translations are welcome. Maintained by 云中江树 (yzfly). [MIT](./LICENSE).
