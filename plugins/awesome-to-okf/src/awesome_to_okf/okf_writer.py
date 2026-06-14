"""把解析出的 awesome 列表写成符合 OKF v0.1 的 bundle。"""
from __future__ import annotations

import re
from pathlib import Path

from .parser import Item, ParsedList


def slugify(text: str) -> str:
    """生成文件名安全的 slug，保留 CJK 字符。"""
    text = text.strip().lower()
    text = re.sub(r"https?://", "", text)
    # 保留字母数字与 CJK，其余替换为连字符
    text = re.sub(r"[^\w一-鿿]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "item"


def _frontmatter(meta: dict) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if v is None or v == "":
            continue
        if isinstance(v, list):
            inner = ", ".join(str(x) for x in v)
            lines.append(f"{k}: [{inner}]")
        else:
            val = str(v)
            if any(c in val for c in ":#") and not val.startswith("http"):
                val = f'"{val}"'
            lines.append(f"{k}: {val}")
    lines.append("---")
    return "\n".join(lines)


def _concept_doc(item: Item, lang: str, timestamp: str) -> str:
    tags = [t for t in [item.section, item.subsection] if t]
    fm = _frontmatter(
        {
            "type": "Resource",
            "title": item.title,
            "description": item.description,
            "resource": item.url,
            "tags": tags,
            "lang": lang,
            "timestamp": timestamp,
        }
    )
    body = [f"\n# {item.title}\n"]
    if item.description:
        body.append(item.description + "\n")
    body.append(f"\n# Citations\n\n[1] [{item.title}]({item.url})\n")
    return fm + "\n" + "".join(body)


def _index(title: str, entries: list[tuple[str, str, str]], okf_version: str | None = None) -> str:
    """entries: (显示名, 相对链接, 描述)。"""
    head = ""
    if okf_version:
        head = f'---\nokf_version: "{okf_version}"\n---\n\n'
    lines = [head + f"# {title}\n"]
    for name, link, desc in entries:
        suffix = f" - {desc}" if desc else ""
        lines.append(f"* [{name}]({link}){suffix}")
    return "\n".join(lines) + "\n"


def write_bundle(
    parsed: ParsedList,
    out_dir: Path,
    *,
    lang: str = "zh",
    timestamp: str = "2026-01-01T00:00:00Z",
    date: str = "2026-01-01",
    source_url: str = "",
) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    sections = parsed.sections()
    stats = {"sections": 0, "items": 0}
    root_entries: list[tuple[str, str, str]] = []

    used_section_slugs: set[str] = set()
    for section, items in sections.items():
        s_slug = slugify(section)
        base = s_slug
        i = 2
        while s_slug in used_section_slugs:
            s_slug = f"{base}-{i}"
            i += 1
        used_section_slugs.add(s_slug)

        sdir = out_dir / s_slug
        sdir.mkdir(parents=True, exist_ok=True)
        sec_entries: list[tuple[str, str, str]] = []
        used: set[str] = set()

        for item in items:
            slug = slugify(item.title)
            base_i = slug
            n = 2
            while slug in used:
                slug = f"{base_i}-{n}"
                n += 1
            used.add(slug)
            (sdir / f"{slug}.md").write_text(
                _concept_doc(item, lang, timestamp), encoding="utf-8"
            )
            sec_entries.append((item.title, f"{slug}.md", item.description))
            stats["items"] += 1

        (sdir / "index.md").write_text(
            _index(section, sec_entries), encoding="utf-8"
        )
        root_entries.append((section, f"{s_slug}/", f"{len(items)} 项"))
        stats["sections"] += 1

    (out_dir / "index.md").write_text(
        _index(parsed.title, root_entries, okf_version="0.1"), encoding="utf-8"
    )
    src = f"（来源:{source_url}）" if source_url else ""
    (out_dir / "log.md").write_text(
        f"# Directory Update Log\n\n## {date}\n"
        f"* **Initialization**: 由 awesome-to-okf 从 awesome 列表导入{src}。\n",
        encoding="utf-8",
    )
    return stats
