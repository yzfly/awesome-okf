---
type: Article
title: Upstream proposal — HTML as a concept file type (draft)
description: English issue text and SPEC.md PR diff for first-class .html concepts. Drafted, not yet submitted.
tags: [okf, html, 提案, upstream]
lang: en
canonical: /docs/html-first-class-proposal-zh.md
timestamp: 2026-06-14T00:00:00Z
author: 云中江树
---

# Upstream proposal: HTML as a concept file type

- Status: **drafted, not yet submitted** — the most ambitious of the three; send last, after [i18n #49](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/49) and the code proposal have traction.
- Chinese background: [让 HTML 成为 OKF 一等公民](../html-first-class-proposal-zh.md)
- Reference implementation: [html-to-okf](../../plugins/html-to-okf/)

## Issue text

> Title: Proposal: allow HTML as a concept file type (first-class `.html` concepts)

### Summary

Let `.html` be a concept file alongside `.md`. An HTML concept carries OKF metadata in a leading `<!--okf … -->` comment (YAML, same fields as frontmatter). Reserved files (`index.md`, `log.md`) stay markdown. Pure-markdown producers and consumers are unaffected.

### Motivation

Some knowledge is better as HTML: it renders directly in a browser (styling, diagrams, interactivity) while its source is still plain text an agent can parse — semantic tags (`<h1>`, `<table>`, `<article>`) are arguably *more* structured than markdown. Today §9 makes only `.md` files concepts, so HTML can only be linked via `resource` or flattened to markdown, losing the "human-friendly + agent-friendly" combination.

### Proposal

An HTML concept carries OKF metadata via one of (consumers SHOULD support at least A):

- **(A, recommended)** a leading HTML comment containing YAML:
  ```html
  <!--okf
  type: Guide
  title: Quickstart
  lang: en
  -->
  ```
  Invisible in the browser; parsed exactly like frontmatter.
- **(B)** `<meta name="okf:type" content="…">` in `<head>`.
- **(C)** `<script type="application/okf+yaml">…</script>`.

Optionally, an HTML concept MAY embed an agent-friendly markdown mirror in `<script type="text/markdown" id="okf-body">…</script>`; otherwise consumers extract text from the semantic HTML.

**Dual representation:** a concept MAY ship both `.html` (for humans) and `.md` (authoritative for agents), linked by `canonical` (see the i18n proposal) so consumers treat them as one concept.

### Conformance change

Relax §9.1–9.2 from "every non-reserved `.md`" to "every non-reserved concept file (`.md` or `.html`)". Markdown rules are unchanged; reserved `index.md`/`log.md` stay markdown.

### Backward compatibility

Pure-markdown consumers ignore `.html` files (treat as unknown files); all markdown rules are untouched; a markdown-only bundle is unaffected. Backward-compatible minor-version addition under §11. (This one does touch §9 wording, so it warrants the most discussion of the three.)

### Open questions

1. Which metadata encoding should the spec bless — just (A), or all three?
2. Should `index.html` be permitted as a render-friendly directory page (with `index.md` remaining authoritative)?
3. Is broadening "concept = `.md`" acceptable in principle, or would you rather keep concepts markdown-only and treat HTML purely as a linked `resource`?

## SPEC.md PR diff (draft)

```diff
diff --git a/okf/SPEC.md b/okf/SPEC.md
--- a/okf/SPEC.md
+++ b/okf/SPEC.md
@@ §4 — new subsection after 4.4, before `## 5. Cross-linking`
+### 4.6 HTML concepts (optional)
+
+A concept MAY be an `.html` file instead of `.md`. An HTML concept carries
+its OKF metadata in a leading HTML comment whose body is YAML using the same
+fields as §4.1:
+
+```html
+<!--okf
+type: Guide
+title: Quickstart
+lang: en
+-->
+```
+
+Consumers SHOULD support this comment form; `<meta name="okf:*">` and
+`<script type="application/okf+yaml">` are OPTIONAL alternatives. An HTML
+concept MAY embed an agent-friendly markdown mirror in
+`<script type="text/markdown" id="okf-body">`. A concept MAY ship both a
+`.html` (human-facing) and a `.md` (agent-facing) variant linked by
+`canonical`. Reserved files (`index.md`, `log.md`) remain markdown.
@@ §9 — conformance
-1. Every non-reserved `.md` file in the tree contains a parseable YAML
-   frontmatter block.
-2. Every frontmatter block contains a non-empty `type` field.
+1. Every non-reserved concept file (`.md`, or `.html` per §4.6) carries
+   parseable OKF metadata.
+2. That metadata contains a non-empty `type` field.
```
