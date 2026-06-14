---
type: Reference
title: 官方参考实现
description: OKF 随规范交付的两个参考实现——BigQuery 富化 agent 与静态 HTML 可视化器。
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
tags: [okf, 官方, 参考实现]
lang: zh
timestamp: 2026-06-14T00:00:00Z
---

# 官方参考实现

OKF 随规范交付的两个 proof-of-concept:

- **富化 agent** —— 遍历 BigQuery 数据集,为每张表/视图起草 OKF 文档,再跑一遍 LLM 补引用、schema、关联路径。源码:<https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf/src/enrichment_agent>
- **静态 HTML 可视化器(viz.html)** —— 把任意 bundle 变成单文件交互图谱,数据不出页面。本仓库的 [okf-to-web](/skills/okf-to-web/SKILL.md) 是同思路的另一实现。

源码:<https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf>
