---
type: Overview
title: Awesome OKF
description: Chinese-first notes and tools for the Open Knowledge Format (OKF), plus converters from common note/doc tools into OKF.
tags: [okf, awesome, en]
lang: en
canonical: /README.md
generated: { by: human:yzfly, at: 2026-06-14T00:00:00Z }
author: 云中江树 (yzfly)
---

# Awesome OKF

English | [中文](./README.md)

Chinese-first notes and tools for the Open Knowledge Format (OKF): a translation of the spec and the launch blog, some background, plus a few small tools that convert Feishu, Obsidian, Notion, GitHub and so on into OKF, with matching Claude Code skills.

> 📌 **The spec is now v0.2**: it adds provenance (`sources`), trust (`generated`/`verified`), lifecycle (`status`/`stale_after`) and attested computations. Two breaking changes: `timestamp` → `generated.at`, and the body `# Citations` list → frontmatter `sources`. This repo (spec translation, validator, all seven plugins, every doc) has been migrated.

The repo itself is a conformant OKF v0.2 bundle — every doc has frontmatter, the root has `index.md` and `log.md`, and `python skills/okf-creator/scripts/validate_okf.py .` checks it.

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

OKF v0.2 leaves some gaps. Three backward-compatible ideas are written up here (docs + reference implementations), none touching any MUST:

- i18n — `lang` + `canonical` (see the [spec translation](./docs/okf-spec-zh.md))
- code support — type vocabulary, `language`/`symbol`/`signature`, line anchors, typed links (see the [research note](./docs/code-support-research-zh.md))
- HTML as a concept type (see the [proposal](./docs/html-first-class-proposal-zh.md))

## Popular repos

| Repo | ★ | Lang | What it is |
|---|---|---|---|
| [knowledge-catalog](./references/knowledge-catalog-repo.md) (official) | [![★](https://img.shields.io/github/stars/GoogleCloudPlatform/knowledge-catalog?style=flat&label=%E2%98%85&color=444)](https://github.com/GoogleCloudPlatform/knowledge-catalog/stargazers) | HTML | Spec + reference impls + sample bundles |
| [open-knowledge-format](https://github.com/GoogleCloudPlatform/open-knowledge-format) | [![★](https://img.shields.io/github/stars/GoogleCloudPlatform/open-knowledge-format?style=flat&label=%E2%98%85&color=444)](https://github.com/GoogleCloudPlatform/open-knowledge-format/stargazers) | HTML | **Official standalone spec repo** (split out of knowledge-catalog, 2026-08): SPEC v0.2 + PoC agent + visualizer + 4 sample bundles; spec commits land here first |
| [openwiki](./references/openwiki.md) (LangChain) | [![★](https://img.shields.io/github/stars/langchain-ai/openwiki?style=flat&label=%E2%98%85&color=444)](https://github.com/langchain-ai/openwiki/stargazers) | TS | LangChain's CLI that writes/maintains agent docs for a codebase, **emits OKF v0.2 bundles** |
| [iwe](./references/iwe.md) | [![★](https://img.shields.io/github/stars/iwe-org/iwe?style=flat&label=%E2%98%85&color=444)](https://github.com/iwe-org/iwe/stargazers) | Rust | Markdown knowledge graph: editor LSP + CLI + MCP; `iwe init --okf`, templates ship as v0.2 and are CI-validated |
| [zosmaai/pi-llm-wiki](https://github.com/zosmaai/pi-llm-wiki) | [![★](https://img.shields.io/github/stars/zosmaai/pi-llm-wiki?style=flat&label=%E2%98%85&color=444)](https://github.com/zosmaai/pi-llm-wiki/stargazers) | TS | Self-maintaining, Obsidian-compatible KB: raw sources → interlinked wiki |
| [fellowgeek/mcp-memory](https://github.com/fellowgeek/mcp-memory) | [![★](https://img.shields.io/github/stars/fellowgeek/mcp-memory?style=flat&label=%E2%98%85&color=444)](https://github.com/fellowgeek/mcp-memory/stargazers) | Python | OKF-backed MCP server: persistent long-term memory + SQL retrieval |
| [coleam00/cole-medin-knowledge-base](https://github.com/coleam00/cole-medin-knowledge-base) | [![★](https://img.shields.io/github/stars/coleam00/cole-medin-knowledge-base?style=flat&label=%E2%98%85&color=444)](https://github.com/coleam00/cole-medin-knowledge-base/stargazers) | JS | OKF knowledge base + Karpathy-style LLM wiki synthesis |
| [UmairBaig8/okf-generator](https://github.com/UmairBaig8/okf-generator) | [![★](https://img.shields.io/github/stars/UmairBaig8/okf-generator?style=flat&label=%E2%98%85&color=444)](https://github.com/UmairBaig8/okf-generator/stargazers) | Python | OKF bundle generator: Claude skill + OpenCode integration |
| [jyjeanne/okf-rs](https://github.com/jyjeanne/okf-rs) | [![★](https://img.shields.io/github/stars/jyjeanne/okf-rs?style=flat&label=%E2%98%85&color=444)](https://github.com/jyjeanne/okf-rs/stargazers) | Rust | Rust toolkit: generate, validate and serve OKF bundles |
| [openknowledge-sh/openknowledge](https://github.com/openknowledge-sh/openknowledge) | [![★](https://img.shields.io/github/stars/openknowledge-sh/openknowledge?style=flat&label=%E2%98%85&color=444)](https://github.com/openknowledge-sh/openknowledge/stargazers) | Go | Go CLI for managing OKF bundles |
| [saschb2b/okf-studio](https://github.com/saschb2b/okf-studio) | [![★](https://img.shields.io/github/stars/saschb2b/okf-studio?style=flat&label=%E2%98%85&color=444)](https://github.com/saschb2b/okf-studio/stargazers) | TS | Native desktop reader for OKF bundles — point it at a folder |
| [aws-samples/sample-okf-llm-wiki](https://github.com/aws-samples/sample-okf-llm-wiki) | [![★](https://img.shields.io/github/stars/aws-samples/sample-okf-llm-wiki?style=flat&label=%E2%98%85&color=444)](https://github.com/aws-samples/sample-okf-llm-wiki/stargazers) | Python | AWS official sample: turn data into OKF bundles and serve them |
| [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | [![★](https://img.shields.io/github/stars/JuneYaooo/lineage-skill?style=flat&label=%E2%98%85&color=444)](https://github.com/JuneYaooo/lineage-skill/stargazers) | Python | Lineage-tracking distillation Agent Skill, emits OKF |
| [psinetron/echoes-vault-opencode](https://github.com/psinetron/echoes-vault-opencode) | [![★](https://img.shields.io/github/stars/psinetron/echoes-vault-opencode?style=flat&label=%E2%98%85&color=444)](https://github.com/psinetron/echoes-vault-opencode/stargazers) | TS | OpenCode persistent-memory plugin, OKF underneath |
| [guhcostan/claude-mega-brain](https://github.com/guhcostan/claude-mega-brain) | [![★](https://img.shields.io/github/stars/guhcostan/claude-mega-brain?style=flat&label=%E2%98%85&color=444)](https://github.com/guhcostan/claude-mega-brain/stargazers) | Python | OKF knowledge-context injection plugin for Claude Code |
| [takeshy/obsidian-gemini-helper](https://github.com/takeshy/obsidian-gemini-helper) | [![★](https://img.shields.io/github/stars/takeshy/obsidian-gemini-helper?style=flat&label=%E2%98%85&color=444)](https://github.com/takeshy/obsidian-gemini-helper/stargazers) | TS | Obsidian Gemini assistant with OKF knowledge sources |
| [coleam00/cole-medin-ai-coding](https://github.com/coleam00/cole-medin-ai-coding) | [![★](https://img.shields.io/github/stars/coleam00/cole-medin-ai-coding?style=flat&label=%E2%98%85&color=444)](https://github.com/coleam00/cole-medin-ai-coding/stargazers) | Python | OKF knowledge bundle for Cole Medin AI-coding videos |
| [okf-gem](./references/okf-gem.md) | [![★](https://img.shields.io/github/stars/serradura/okf?style=flat&label=%E2%98%85&color=444)](https://github.com/serradura/okf/stargazers) | Ruby | Authoring skill + CLI/lib + graph, covering a bundle's whole life |
| [OWOX Model Canvas](./references/owox-model-canvas.md) | [![★](https://img.shields.io/github/stars/OWOX/models?style=flat&label=%E2%98%85&color=444)](https://github.com/OWOX/models/stargazers) | TS | Visual modeling / authoring front-end |
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
| [joshuaswarren/remnic](https://github.com/joshuaswarren/remnic) | [![★](https://img.shields.io/github/stars/joshuaswarren/remnic?style=flat&label=%E2%98%85&color=444)](https://github.com/joshuaswarren/remnic/stargazers) | TS | Memory/context layer for user-aware agents; the memory dir doubles as an OKF bundle, ships `remnic okf lint`, MCP + HTTP |
| [ZeroDot1/LLMWikiNG](https://github.com/ZeroDot1/LLMWikiNG) | [![★](https://img.shields.io/github/stars/ZeroDot1/LLMWikiNG?style=flat&label=%E2%98%85&color=444)](https://github.com/ZeroDot1/LLMWikiNG/stargazers) | Python | Local, privacy-first Karpathy-style LLM Wiki platform (OKF Edition), maintained by AI |
| [jkroepke/okf-crossplane-v2](https://github.com/jkroepke/okf-crossplane-v2) | [![★](https://img.shields.io/github/stars/jkroepke/okf-crossplane-v2?style=flat&label=%E2%98%85&color=444)](https://github.com/jkroepke/okf-crossplane-v2/stargazers) | Python | LLM-wiki for Crossplane v2 — a real domain OKF bundle with CI validation |
| [stjbrown/agent-knowledge](https://github.com/stjbrown/agent-knowledge) | [![★](https://img.shields.io/github/stars/stjbrown/agent-knowledge?style=flat&label=%E2%98%85&color=444)](https://github.com/stjbrown/agent-knowledge/stargazers) | JS | Portable Agent Skills for building/maintaining OKF project wikis in plain Markdown |
| [kiso](https://github.com/oak-invest/kiso) | [![★](https://img.shields.io/github/stars/oak-invest/kiso?style=flat&label=%E2%98%85&color=444)](https://github.com/oak-invest/kiso/stargazers) | Java | Publishing engine: OKF bundle → static site for humans and agents, with an MCP server |
| [kushal-omnius/open-knowledge-compiler](https://github.com/kushal-omnius/open-knowledge-compiler) | [![★](https://img.shields.io/github/stars/kushal-omnius/open-knowledge-compiler?style=flat&label=%E2%98%85&color=444)](https://github.com/kushal-omnius/open-knowledge-compiler/stargazers) | Python | Deterministically compiles Git/PR/test history into a provenance-tracked, queryable KB (v0.2) |
| [Connorrmcd6/surface](https://github.com/Connorrmcd6/surface) | [![★](https://img.shields.io/github/stars/Connorrmcd6/surface?style=flat&label=%E2%98%85&color=444)](https://github.com/Connorrmcd6/surface/stargazers) | Rust | Always-fresh docs: a hub is a conformant OKF concept; adds the freshness check OKF leaves out, fails the build when stale |
| [okfcli/okf](https://github.com/okfcli/okf) | [![★](https://img.shields.io/github/stars/okfcli/okf?style=flat&label=%E2%98%85&color=444)](https://github.com/okfcli/okf/stargazers) | Go | Vendor-neutral Go CLI: create / validate / lint / index / search / graph, built to be driven by agents |
| [DavidROliverBA/aix-format](https://github.com/DavidROliverBA/aix-format) | [![★](https://img.shields.io/github/stars/DavidROliverBA/aix-format?style=flat&label=%E2%98%85&color=444)](https://github.com/DavidROliverBA/aix-format/stargazers) | Python | AIX: a strict superset of OKF v0.2 — stable identity, typed relationships, media identity, federation |
| [W4G1/okf](https://github.com/W4G1/okf) | [![★](https://img.shields.io/github/stars/W4G1/okf?style=flat&label=%E2%98%85&color=444)](https://github.com/W4G1/okf/stargazers) | Rust | Pure-Rust zero-dependency implementation and CLI toolkit |

## Links

Official: [spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) · [repo](https://github.com/GoogleCloudPlatform/knowledge-catalog) · [launch blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/). Lineage: [Karpathy's LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Contributing & license

PRs welcome — anything OKF-related that runs or reads. See [CONTRIBUTING](./CONTRIBUTING.md). Docs are Chinese-first for now (tagged `lang`); English translations are welcome. Maintained by 云中江树 (yzfly). [MIT](./LICENSE).
