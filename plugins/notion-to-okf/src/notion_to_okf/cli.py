"""把 Notion 的 Markdown 导出(Export → Markdown & CSV)转换为 OKF v0.1 bundle。

Notion 导出的特征:
  - 文件/目录名尾部带 32 位十六进制 ID,如 `项目计划 a1b2c3...e9.md`;
  - 页面内链接是 URL 编码的相对路径;
  - 页面正文首行通常是 H1 标题,无 frontmatter。

本工具:去掉文件名里的 Notion 哈希,补 OKF frontmatter,重写内部链接,生成索引。

用法:
    notion-to-okf <Notion 导出目录> -o ./out [--lang zh]
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote

HASH = re.compile(r"\s+[0-9a-fA-F]{32}")
MD_LINK = re.compile(r"\]\(([^)]+)\)")


def clean_name(name: str) -> str:
    return HASH.sub("", name)


def first_h1(text: str) -> str:
    for ln in text.splitlines():
        m = re.match(r"^#\s+(.+)", ln)
        if m:
            return m.group(1).strip()
    return ""


def clean_link(target: str) -> str:
    if target.startswith(("http://", "https://", "#", "mailto:")):
        return target
    dec = unquote(target)
    # 去掉每段路径里的哈希
    parts = [HASH.sub("", seg) for seg in dec.split("/")]
    return "/".join(parts)


def rewrite_links(text: str) -> str:
    return MD_LINK.sub(lambda m: f"]({clean_link(m.group(1))})", text)


def write_indexes(out: Path) -> None:
    for d in sorted(p for p in out.rglob("*") if p.is_dir()):
        _index(d, is_root=False)
    _index(out, is_root=True)


def _index(d: Path, is_root: bool) -> None:
    entries = []
    for c in sorted(d.iterdir()):
        if c.name in ("index.md", "log.md"):
            continue
        if c.is_dir():
            entries.append((c.name, f"{c.name}/", "目录"))
        elif c.suffix == ".md":
            entries.append((c.stem, c.name, ""))
    if not entries:
        return
    head = '---\nokf_version: "0.1"\n---\n\n' if is_root else ""
    title = "知识库" if is_root else d.name
    lines = [head + f"# {title}\n"]
    for name, link, desc in entries:
        lines.append(f"* [{name}]({link})" + (f" - {desc}" if desc else ""))
    (d / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Notion Markdown 导出 -> OKF v0.1")
    ap.add_argument("export_dir", type=Path, help="Notion 导出目录")
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--lang", default="zh")
    ap.add_argument("--date", default="2026-01-01")
    args = ap.parse_args(argv)

    if not args.export_dir.is_dir():
        print(f"错误:{args.export_dir} 不是目录")
        return 2

    count = 0
    for p in args.export_dir.rglob("*.md"):
        text = p.read_text(encoding="utf-8")
        title = first_h1(text) or clean_name(p.stem)
        text = rewrite_links(text)
        fm = (
            f"---\ntype: Note\ntitle: {title}\n"
            f"lang: {args.lang}\ntimestamp: {args.date}T00:00:00Z\n---\n\n"
        )
        # 目标路径:逐段去哈希
        rel = p.relative_to(args.export_dir)
        clean_parts = [clean_name(part) for part in rel.parts]
        dest = args.out.joinpath(*clean_parts)
        dest = dest.with_name(clean_name(dest.stem) + ".md")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(fm + text, encoding="utf-8")
        count += 1

    # CSV 数据库导出:提示(暂不深度转换)
    csvs = list(args.export_dir.rglob("*.csv"))
    if csvs:
        print(f"  注:发现 {len(csvs)} 个 Notion 数据库 CSV,当前版本未转换(可后续每行转为概念)。")

    write_indexes(args.out)
    (args.out / "log.md").write_text(
        f"# Directory Update Log\n\n## {args.date}\n"
        f"* **Initialization**: 由 notion-to-okf 从 Notion 导出导入。\n",
        encoding="utf-8",
    )
    print(f"✓ 已转换 {count} 篇页面 -> {args.out}")
    print("  用 ../../skills/okf-creator/scripts/validate_okf.py 校验。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
