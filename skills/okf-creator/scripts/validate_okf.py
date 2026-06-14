#!/usr/bin/env python3
"""OKF v0.1 符合性校验器。

按规范 §9 检查一个目录是否为合规的 OKF bundle:
  1. 每个非保留的 .md 文件含有可解析的 YAML 头信息块;
  2. 每个头信息块含有非空的 `type` 字段;
  3. 保留文件名(index.md / log.md)在出现时遵循 §6 / §7 结构。

零第三方依赖(优先用 PyYAML,缺失时回退到最小解析器)。

用法:
    python validate_okf.py <bundle 目录> [--strict]

    --strict  把 SHOULD 级别的告警也算作失败。

退出码:0 = 合规;1 = 存在硬性错误;2 = 用法错误。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

RESERVED = {"index.md", "log.md"}
DATE_HEADING = re.compile(r"^##\s+\d{4}-\d{2}-\d{2}\s*$")

try:
    import yaml  # type: ignore

    def parse_yaml(block: str) -> dict:
        data = yaml.safe_load(block) or {}
        if not isinstance(data, dict):
            raise ValueError("头信息不是 YAML 映射")
        return data
except ImportError:  # 最小回退解析器:只取顶层 key: value
    def parse_yaml(block: str) -> dict:
        data: dict = {}
        for line in block.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line[0] in " \t":  # 跳过嵌套/列表续行
                continue
            m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
            if m:
                data[m.group(1)] = m.group(2).strip()
        return data


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """返回 (头信息原文, 正文)。无头信息时头信息为 None。"""
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    return m.group(1), m.group(2)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path, msg: str) -> None:
        self.errors.append(f"✗ {path}: {msg}")

    def warn(self, path: Path, msg: str) -> None:
        self.warnings.append(f"! {path}: {msg}")


def check_concept(path: Path, text: str, rep: Report) -> None:
    fm, _ = split_frontmatter(text)
    if fm is None:
        rep.error(path, "缺少 YAML 头信息块(§9.1)")
        return
    try:
        meta = parse_yaml(fm)
    except Exception as exc:  # noqa: BLE001
        rep.error(path, f"头信息无法解析:{exc}(§9.1)")
        return
    type_val = str(meta.get("type", "")).strip()
    if not type_val:
        rep.error(path, "缺少非空的 `type` 字段(§9.2)")
    # SHOULD 级别提示
    if not str(meta.get("description", "")).strip():
        rep.warn(path, "建议补 `description`(用于索引与搜索摘要)")


def check_index(path: Path, text: str, is_root: bool, rep: Report) -> None:
    fm, _ = split_frontmatter(text)
    if fm is not None:
        meta = {}
        try:
            meta = parse_yaml(fm)
        except Exception:  # noqa: BLE001
            pass
        allowed = {"okf_version"} if is_root else set()
        extra = set(meta) - allowed
        if extra:
            rep.error(
                path,
                f"index.md 不应含头信息(根目录仅允许 okf_version),发现:{sorted(extra)}(§6/§11)",
            )


def check_log(path: Path, text: str, rep: Report) -> None:
    fm, body = split_frontmatter(text)
    if fm is not None:
        rep.warn(path, "log.md 通常不含头信息(§7)")
        text = body
    headings = [ln for ln in text.splitlines() if ln.startswith("## ")]
    for h in headings:
        if not DATE_HEADING.match(h):
            rep.warn(path, f"日期标题应为 ISO `## YYYY-MM-DD`,发现:{h.strip()}(§7)")


def validate(root: Path, rep: Report) -> None:
    md_files = sorted(root.rglob("*.md"))
    if not md_files:
        rep.error(root, "目录下没有任何 .md 文件,不像一个 bundle")
        return
    for path in md_files:
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        name = path.name
        if name == "index.md":
            check_index(rel, text, is_root=(path.parent == root), rep=rep)
        elif name == "log.md":
            check_log(rel, text, rep)
        else:
            check_concept(rel, text, rep)


def main() -> int:
    ap = argparse.ArgumentParser(description="OKF v0.1 符合性校验器")
    ap.add_argument("bundle", type=Path, help="bundle 目录")
    ap.add_argument("--strict", action="store_true", help="告警也算失败")
    args = ap.parse_args()

    if not args.bundle.is_dir():
        print(f"错误:{args.bundle} 不是目录", file=sys.stderr)
        return 2

    rep = Report()
    validate(args.bundle, rep)

    for line in rep.errors:
        print(line)
    for line in rep.warnings:
        print(line)

    n_md = len(list(args.bundle.rglob("*.md")))
    print(
        f"\n扫描 {n_md} 个 .md 文件 · 错误 {len(rep.errors)} · 告警 {len(rep.warnings)}"
    )
    if rep.errors or (args.strict and rep.warnings):
        print("结果:✗ 不符合 OKF v0.1")
        return 1
    print("结果:✓ 符合 OKF v0.1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
