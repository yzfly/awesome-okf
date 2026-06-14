"""把 Obsidian vault 转换为 OKF v0.1 bundle。

Obsidian 本就是 markdown + frontmatter + [[wikilink]],几乎天生符合 OKF。
本工具只补三件事:
  1. 保证每篇有非空 `type`(缺省 Note);
  2. 把 [[wikilink]] 转成 OKF 的 Markdown 链接(包内绝对路径);
  3. 生成各级 index.md(带根 okf_version)与 log.md。

用法:
    obsidian-to-okf <vault 目录> -o ./out [--lang zh] [--type Note]
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
TYPE_LINE = re.compile(r"^type\s*:", re.MULTILINE)


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") or text.startswith("---\r\n")


def split_fm(text: str) -> tuple[str | None, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    return (m.group(1), m.group(2)) if m else (None, text)


def first_h1(body: str) -> str:
    for ln in body.splitlines():
        m = re.match(r"^#\s+(.+)", ln)
        if m:
            return m.group(1).strip()
    return ""


def build_index(vault: Path) -> dict[str, str]:
    """basename(不含扩展名) -> 相对 vault 的 POSIX 路径(不含 .md)。"""
    idx: dict[str, str] = {}
    for p in vault.rglob("*.md"):
        if ".obsidian" in p.parts or ".trash" in p.parts:
            continue
        rel = p.relative_to(vault).with_suffix("").as_posix()
        idx[p.stem] = rel
    return idx


def convert_links(body: str, index: dict[str, str]) -> str:
    def repl(m: re.Match) -> str:
        target = m.group(1).strip()
        alias = (m.group(2) or target).strip()
        rel = index.get(target, target)
        return f"[{alias}](/{rel}.md)"

    return WIKILINK.sub(repl, body)


def ensure_frontmatter(text: str, *, title: str, lang: str, default_type: str,
                       timestamp: str) -> str:
    fm, body = split_fm(text)
    if fm is not None:
        if not TYPE_LINE.search(fm):
            fm = f"type: {default_type}\n" + fm
        if "lang:" not in fm:
            fm = fm + f"\nlang: {lang}"
        return f"---\n{fm}\n---\n{body}"
    # 无 frontmatter:新建
    new = (
        f"---\ntype: {default_type}\ntitle: {title}\n"
        f"lang: {lang}\ntimestamp: {timestamp}\n---\n\n"
    )
    return new + text


def write_indexes(out: Path) -> None:
    for d in sorted(p for p in out.rglob("*") if p.is_dir()):
        _dir_index(out, d, is_root=False)
    _dir_index(out, out, is_root=True)


def _dir_index(out: Path, d: Path, is_root: bool) -> None:
    entries = []
    for child in sorted(d.iterdir()):
        if child.name in ("index.md", "log.md"):
            continue
        if child.is_dir():
            entries.append((child.name, f"{child.name}/", "目录"))
        elif child.suffix == ".md":
            entries.append((child.stem, child.name, ""))
    if not entries:
        return
    head = '---\nokf_version: "0.1"\n---\n\n' if is_root else ""
    title = "知识库" if is_root else d.name
    lines = [head + f"# {title}\n"]
    for name, link, desc in entries:
        lines.append(f"* [{name}]({link})" + (f" - {desc}" if desc else ""))
    (d / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Obsidian vault -> OKF v0.1")
    ap.add_argument("vault", type=Path, help="Obsidian vault 目录")
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--lang", default="zh")
    ap.add_argument("--type", dest="default_type", default="Note")
    ap.add_argument("--date", default="2026-01-01")
    args = ap.parse_args(argv)

    if not args.vault.is_dir():
        print(f"错误:{args.vault} 不是目录")
        return 2

    index = build_index(args.vault)
    count = 0
    for p in args.vault.rglob("*.md"):
        if ".obsidian" in p.parts or ".trash" in p.parts:
            continue
        text = p.read_text(encoding="utf-8")
        body_for_title = split_fm(text)[1]
        title = first_h1(body_for_title) or p.stem
        text = convert_links(text, index)
        text = ensure_frontmatter(
            text, title=title, lang=args.lang,
            default_type=args.default_type, timestamp=f"{args.date}T00:00:00Z",
        )
        dest = args.out / p.relative_to(args.vault)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        count += 1

    write_indexes(args.out)
    (args.out / "log.md").write_text(
        f"# Directory Update Log\n\n## {args.date}\n"
        f"* **Initialization**: 由 obsidian-to-okf 从 Obsidian vault 导入。\n",
        encoding="utf-8",
    )
    print(f"✓ 已转换 {count} 篇笔记 -> {args.out}")
    print("  用 ../../skills/okf-creator/scripts/validate_okf.py 校验。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
