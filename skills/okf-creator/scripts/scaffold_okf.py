#!/usr/bin/env python3
"""OKF bundle 脚手架生成器。

快速生成一个符合 OKF v0.1 的空 bundle 骨架:根 index.md(带 okf_version)、
log.md,以及一个示例概念文档。

用法:
    python scaffold_okf.py <目标目录> [--title "我的知识库"] [--lang zh]
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT_INDEX = """---
okf_version: "0.1"
---

# {title}

* [示例概念](concepts/example.md) - 一个最小的概念文档,替换或删除它。
"""

LOG = """# Directory Update Log

## {date}
* **Initialization**: 创建 bundle 骨架。
"""

EXAMPLE = """---
type: Reference
title: 示例概念
description: 一个最小的 OKF 概念文档,演示头信息与正文结构。
tags: [example]
lang: {lang}
timestamp: {date}T00:00:00Z
---

# 概述

把你的知识写在这里。偏好结构化 Markdown(标题、列表、表格、代码块)。

# 关联

用普通 Markdown 链接指向其他概念,例如 [根索引](/index.md)。
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="OKF bundle 脚手架生成器")
    ap.add_argument("target", type=Path, help="目标目录")
    ap.add_argument("--title", default="我的 OKF 知识库")
    ap.add_argument("--lang", default="zh")
    ap.add_argument("--date", default="2026-01-01", help="ISO 日期,用于时间戳")
    args = ap.parse_args()

    root: Path = args.target
    (root / "concepts").mkdir(parents=True, exist_ok=True)

    (root / "index.md").write_text(
        ROOT_INDEX.format(title=args.title), encoding="utf-8"
    )
    (root / "log.md").write_text(LOG.format(date=args.date), encoding="utf-8")
    (root / "concepts" / "example.md").write_text(
        EXAMPLE.format(lang=args.lang, date=args.date), encoding="utf-8"
    )

    print(f"✓ 已在 {root} 生成 OKF bundle 骨架")
    print("  ├── index.md (含 okf_version)")
    print("  ├── log.md")
    print("  └── concepts/example.md")
    print("\n下一步:用 validate_okf.py 校验,或交给 okf-creator Skill 填充内容。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
