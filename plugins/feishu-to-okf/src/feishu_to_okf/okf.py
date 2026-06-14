"""把飞书导出的文档写成 OKF v0.1 bundle。"""
from __future__ import annotations

import re
from pathlib import Path


def slugify(text: str) -> str:
    text = (text or "untitled").strip().lower()
    text = re.sub(r"[^\w一-鿿]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "untitled"


def frontmatter(meta: dict) -> str:
    out = ["---"]
    for k, v in meta.items():
        if v in (None, "", []):
            continue
        if isinstance(v, list):
            out.append(f"{k}: [{', '.join(map(str, v))}]")
        else:
            s = str(v)
            if (":" in s or "#" in s) and not s.startswith("http"):
                s = f'"{s}"'
            out.append(f"{k}: {s}")
    out.append("---")
    return "\n".join(out)


def write_concept(
    out_dir: Path,
    rel_path: str,
    title: str,
    body_md: str,
    *,
    resource: str = "",
    lang: str = "zh",
    timestamp: str = "2026-01-01T00:00:00Z",
    doc_type: str = "Document",
) -> Path:
    # 取正文首句做 description
    first = next((ln.strip() for ln in body_md.splitlines()
                  if ln.strip() and not ln.startswith("#")), "")
    desc = first[:80]
    fm = frontmatter({
        "type": doc_type,
        "title": title,
        "description": desc,
        "resource": resource,
        "lang": lang,
        "timestamp": timestamp,
    })
    path = out_dir / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(fm + "\n\n# " + title + "\n\n" + body_md, encoding="utf-8")
    return path


def write_root(out_dir: Path, title: str, entries: list[tuple[str, str, str]],
               date: str, source: str) -> None:
    lines = ['---\nokf_version: "0.1"\n---\n', f"# {title}\n"]
    for name, link, desc in entries:
        lines.append(f"* [{name}]({link})" + (f" - {desc}" if desc else ""))
    (out_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out_dir / "log.md").write_text(
        f"# Directory Update Log\n\n## {date}\n"
        f"* **Initialization**: 由 feishu-to-okf 从飞书知识空间「{source}」导出。\n",
        encoding="utf-8",
    )
