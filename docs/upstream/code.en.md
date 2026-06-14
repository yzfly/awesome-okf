---
type: Article
title: Upstream proposal — source code conventions (draft)
description: English issue text and SPEC.md PR diff for representing source code in OKF. Drafted, not yet submitted.
tags: [okf, code, 提案, upstream]
lang: en
canonical: /docs/code-support-research-zh.md
timestamp: 2026-06-14T00:00:00Z
author: 云中江树
---

# Upstream proposal: source code conventions

- Status: **drafted, not yet submitted** — hold until [i18n #49](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/49) gets a direction.
- Chinese background: [代码 / PDF / 图片支持度调研](../code-support-research-zh.md)
- Reference implementation: [github-to-okf](../../plugins/github-to-okf/) + [code-to-okf](../../skills/code-to-okf/)

## Issue text

> Title: Proposal: optional conventions for representing source code (language / symbol / signature, line anchors, typed links)

### Summary

A set of **optional** fields and conventions so codebases can be represented as OKF bundles. Nothing mandated — recommended `type` values, three optional frontmatter fields, a `resource` line-anchor convention, and an optional typed-link convention. No MUST changes.

### Motivation

OKF reads as data-knowledge oriented today (the three sample bundles are all tables / datasets / metrics). When you point it at a codebase there is no agreed way to say a concept *is* a function vs *describes* one, what language it is, what its signature is, or what it calls. Cross-links are untyped (§5.3), so a call graph or dependency graph can't be reconstructed without NLP on prose. The result is that every team representing code in OKF reinvents the same ad-hoc keys, and bundles don't interoperate at the code level.

These are all expressible today via "producers MAY add keys" (§4.1) — the value is agreeing on *names* so different producers and consumers line up.

### Proposal

**1. A recommended (not registered) `type` vocabulary for code:**
`Repository`, `Package`, `Module`, `Class`, `Function`, `Interface`, `Config`, `Script`, `Notebook`. Consumers still tolerate unknown types per §4.1.

**2. Three optional frontmatter fields:**
- `language` — the programming language (`python`, `go`, `typescript`, …).
- `symbol` — the fully-qualified symbol name (`pkg.module.func`).
- `signature` — the function/method signature, as a string.

**3. A `resource` line-anchor convention:**
Reuse the existing GitHub/GitLab convention `#L<start>-L<end>`, and prefer a commit SHA over a branch name so the anchor stays valid:
`https://github.com/owner/repo/blob/<sha>/path.py#L20-L48`

**4. Optional typed links (addresses §5.3):**
Convey relationship kind with a link-text prefix — human-readable and trivially machine-parseable:
```
- calls: [helper](/functions/helper.md)
- depends-on: [pyyaml](/packages/pyyaml.md)
- implements: [Reader](/interfaces/reader.md)
```

### Backward compatibility

Everything is optional or conventional. No MUST changes. Unknown fields are ignored per §4.1/§9; typed-link prefixes are just ordinary link text to a consumer that doesn't parse them. Backward-compatible minor-version addition under §11.

### Open questions

1. Typed links — worth a sentence in §5, or leave entirely to convention?
2. Field names — `language`/`symbol`/`signature` OK?
3. Is a recommended type vocabulary in-scope, given §1 lists "fixed taxonomy of concept types" as a non-goal? (Intent here is *recommended*, not registered.)

## SPEC.md PR diff (draft)

```diff
diff --git a/okf/SPEC.md b/okf/SPEC.md
--- a/okf/SPEC.md
+++ b/okf/SPEC.md
@@ §4.1 — after the `timestamp` field, before **Extensions:**
 - `timestamp` — ISO 8601 datetime of last meaningful change.
+
+**Code concepts (optional):** For concepts that describe source code,
+producers SHOULD use the following optional fields so that code bundles
+interoperate:
+
+- `language` — the programming language (e.g. `python`, `go`, `typescript`).
+- `symbol` — the fully-qualified symbol name (e.g. `pkg.module.func`).
+- `signature` — the function or method signature, as a string.
+
+For such concepts, `resource` SHOULD point at the exact source range using
+the conventional `#L<start>-L<end>` line anchor, preferably pinned to a
+commit SHA so the anchor remains valid.
 
 **Extensions:** Producers MAY include any additional keys. Consumers
@@ §5.3 — after the untyped-relationship paragraph
 Consumers that build a graph view typically treat all links as
 directed edges of an untyped relationship.
+
+Producers MAY make a relationship's kind explicit by prefixing the link
+text with a label, e.g. `calls:`, `depends-on:`, `implements:`. This stays
+human-readable and lets graph consumers recover typed edges; consumers that
+ignore the prefix simply see an untyped link.
```
