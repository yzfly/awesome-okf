"""awesome-importer 命令行入口。

用法:
    # 从 GitHub 仓库导入(自动找 README)
    awesome-importer owner/repo -o ./out

    # 从 raw URL 或本地文件导入
    awesome-importer https://raw.githubusercontent.com/x/y/main/README.md -o ./out
    awesome-importer ./README.md -o ./out
"""
from __future__ import annotations

import argparse
import sys
import urllib.request
from pathlib import Path

from .okf_writer import write_bundle
from .parser import parse

RAW = "https://raw.githubusercontent.com/{repo}/{branch}/{file}"
BRANCHES = ("main", "master")
README_NAMES = ("README.md", "readme.md", "Readme.md")


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-importer"})
    with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
        return resp.read().decode("utf-8")


def resolve_markdown(source: str) -> tuple[str, str]:
    """返回 (markdown 文本, 来源说明)。"""
    p = Path(source)
    if p.is_file():
        return p.read_text(encoding="utf-8"), str(p)
    if source.startswith("http"):
        return _fetch(source), source
    # 视作 owner/repo
    if "/" in source and " " not in source:
        for branch in BRANCHES:
            for name in README_NAMES:
                url = RAW.format(repo=source, branch=branch, file=name)
                try:
                    return _fetch(url), url
                except Exception:  # noqa: BLE001
                    continue
    raise SystemExit(f"无法解析来源:{source}（不是文件、URL，也找不到 GitHub README）")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="把 GitHub awesome 列表转换为 OKF v0.1 知识包"
    )
    ap.add_argument("source", help="owner/repo、raw URL 或本地 Markdown 文件")
    ap.add_argument("-o", "--out", type=Path, required=True, help="输出 bundle 目录")
    ap.add_argument("--lang", default="zh", help="正文语言(BCP 47),默认 zh")
    ap.add_argument("--date", default="2026-01-01", help="ISO 日期,用于时间戳")
    args = ap.parse_args(argv)

    markdown, src = resolve_markdown(args.source)
    parsed = parse(markdown)
    if not parsed.items:
        print("⚠ 没有解析到任何链接条目,确认这是一个 awesome 风格列表。", file=sys.stderr)
        return 1

    stats = write_bundle(
        parsed,
        args.out,
        lang=args.lang,
        timestamp=f"{args.date}T00:00:00Z",
        date=args.date,
        source_url=src,
    )
    print(f"✓ 已生成 OKF bundle:{args.out}")
    print(f"  标题:{parsed.title}")
    print(f"  分节:{stats['sections']} · 条目:{stats['items']}")
    print("  下一步:用 okf-creator/scripts/validate_okf.py 校验。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
