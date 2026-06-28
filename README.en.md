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

## Popular repos

| Repo | ★ | Lang | What it is |
|---|---|---|---|
| [knowledge-catalog](./references/knowledge-catalog-repo.md) (official) | [![★](https://img.shields.io/github/stars/GoogleCloudPlatform/knowledge-catalog?style=flat&label=%E2%98%85&color=444)](https://github.com/GoogleCloudPlatform/knowledge-catalog/stargazers) | HTML | Spec + reference impls + sample bundles |
| [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | [![★](https://img.shields.io/github/stars/JuneYaooo/lineage-skill?style=flat&label=%E2%98%85&color=444)](https://github.com/JuneYaooo/lineage-skill/stargazers) | Python | Lineage-tracking distillation Agent Skill, emits OKF |
| [psinetron/echoes-vault-opencode](https://github.com/psinetron/echoes-vault-opencode) | [![★](https://img.shields.io/github/stars/psinetron/echoes-vault-opencode?style=flat&label=%E2%98%85&color=444)](https://github.com/psinetron/echoes-vault-opencode/stargazers) | TS | OpenCode persistent-memory plugin, OKF underneath |
| [OWOX Model Canvas](./references/owox-model-canvas.md) | [![★](https://img.shields.io/github/stars/OWOX/owox-model-canvas?style=flat&label=%E2%98%85&color=444)](https://github.com/OWOX/owox-model-canvas/stargazers) | TS | Visual modeling / authoring front-end |
| [0dust/OKFy](https://github.com/0dust/OKFy) | [![★](https://img.shields.io/github/stars/0dust/OKFy?style=flat&label=%E2%98%85&color=444)](https://github.com/0dust/OKFy/stargazers) | TS | Docs → agent-readable OKF bundle converter |
| [okf-knowledge](./references/okf-knowledge.md) | [![★](https://img.shields.io/github/stars/sniperunder123/okf-knowledge?style=flat&label=%E2%98%85&color=444)](https://github.com/sniperunder123/okf-knowledge/stargazers) | Python | Claude Code `/okf` skill |
| [longsizhuo/okf-frontmatter](https://github.com/longsizhuo/okf-frontmatter) | [![★](https://img.shields.io/github/stars/longsizhuo/okf-frontmatter?style=flat&label=%E2%98%85&color=444)](https://github.com/longsizhuo/okf-frontmatter/stargazers) | Python | Skill that keeps repo docs in OKF shape |
| [hermes-okf](./references/hermes-okf.md) | [![★](https://img.shields.io/github/stars/EliaszDev/hermes-okf?style=flat&label=%E2%98%85&color=444)](https://github.com/EliaszDev/hermes-okf/stargazers) | Python | OKF-based agent persistent memory (PyPI) |
| [pumblus/okf-harness](https://github.com/pumblus/okf-harness) | [![★](https://img.shields.io/github/stars/pumblus/okf-harness?style=flat&label=%E2%98%85&color=444)](https://github.com/pumblus/okf-harness/stargazers) | TS | Local-first agent terminal harness |
| [scaccogatto/okf-skills](https://github.com/scaccogatto/okf-skills) | [![★](https://img.shields.io/github/stars/scaccogatto/okf-skills?style=flat&label=%E2%98%85&color=444)](https://github.com/scaccogatto/okf-skills/stargazers) | Python | OKF skills for Claude Code |
| [wiki-as-an-mcp](./references/wiki-as-an-mcp.md) | [![★](https://img.shields.io/github/stars/taikunudel/wiki-as-an-mcp?style=flat&label=%E2%98%85&color=444)](https://github.com/taikunudel/wiki-as-an-mcp/stargazers) | Python | First general Wiki MCP server |
| [superops-team/okf](./references/superops-okf.md) | [![★](https://img.shields.io/github/stars/superops-team/okf?style=flat&label=%E2%98%85&color=444)](https://github.com/superops-team/okf/stargazers) | Go | Project-level knowledge base |
| [xSAVIKx/okf-skills](https://github.com/xSAVIKx/okf-skills) | [![★](https://img.shields.io/github/stars/xSAVIKx/okf-skills?style=flat&label=%E2%98%85&color=444)](https://github.com/xSAVIKx/okf-skills/stargazers) | Go | OKF agentic skills in Go |
| [okf-rag](./references/okf-rag.md) | [![★](https://img.shields.io/github/stars/killop/okf-rag?style=flat&label=%E2%98%85&color=444)](https://github.com/killop/okf-rag/stargazers) | Rust | Local-first OKF retrieval / RAG |
| [Sudhakaran88/okf-conformance](https://github.com/Sudhakaran88/okf-conformance) | [![★](https://img.shields.io/github/stars/Sudhakaran88/okf-conformance?style=flat&label=%E2%98%85&color=444)](https://github.com/Sudhakaran88/okf-conformance/stargazers) | JS | OKF conformance checker |

## Links

Official: [spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) · [repo](https://github.com/GoogleCloudPlatform/knowledge-catalog) · [launch blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/). Lineage: [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Contributing & license

PRs welcome — anything OKF-related that runs or reads. See [CONTRIBUTING](./CONTRIBUTING.md). Docs are Chinese-first for now (tagged `lang`); English translations are welcome. Maintained by 云中江树 (yzfly). [MIT](./LICENSE).
