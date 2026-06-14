"""github-to-okf 核心:语言识别、符号提取、OKF 写入。"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

LANG_EXT = {
    ".py": "python", ".go": "go", ".js": "javascript", ".mjs": "javascript",
    ".ts": "typescript", ".tsx": "typescript", ".jsx": "javascript",
    ".rs": "rust", ".java": "java", ".rb": "ruby", ".c": "c", ".h": "c",
    ".cpp": "cpp", ".cc": "cpp", ".hpp": "cpp", ".cs": "csharp",
    ".php": "php", ".swift": "swift", ".kt": "kotlin", ".scala": "scala",
    ".sh": "shell", ".sql": "sql", ".lua": "lua", ".dart": "dart", ".vue": "vue",
}

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist",
             "build", ".idea", ".vscode", "vendor", ".next", "target", ".ruff_cache"}

SYMBOL_PATTERNS: dict[str, list[tuple[str, re.Pattern]]] = {
    "python": [("function", re.compile(r"^\s*(?:async\s+)?def\s+(\w+)")),
               ("class", re.compile(r"^\s*class\s+(\w+)"))],
    "go": [("function", re.compile(r"^func\s+(?:\([^)]*\)\s*)?(\w+)")),
           ("type", re.compile(r"^type\s+(\w+)"))],
    "javascript": [("function", re.compile(r"^\s*(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s+(\w+)")),
                   ("class", re.compile(r"^\s*(?:export\s+)?(?:default\s+)?class\s+(\w+)"))],
    "rust": [("function", re.compile(r"^\s*(?:pub\s+)?(?:async\s+)?fn\s+(\w+)")),
             ("struct", re.compile(r"^\s*(?:pub\s+)?struct\s+(\w+)")),
             ("trait", re.compile(r"^\s*(?:pub\s+)?trait\s+(\w+)"))],
    "java": [("class", re.compile(r"^\s*(?:public|private|protected)?\s*(?:final\s+|abstract\s+)?class\s+(\w+)")),
             ("interface", re.compile(r"^\s*(?:public\s+)?interface\s+(\w+)"))],
}
SYMBOL_PATTERNS["typescript"] = SYMBOL_PATTERNS["javascript"]


@dataclass
class Symbol:
    kind: str
    name: str


@dataclass
class FileConcept:
    relpath: str               # 仓库内相对路径
    language: str
    symbols: list[Symbol] = field(default_factory=list)
    resource: str = ""         # 源码 URL 或相对路径
    is_doc: bool = False
    body: str = ""             # 文档正文(md 文件用)


def detect_language(path: str) -> str:
    return LANG_EXT.get(Path(path).suffix.lower(), "")


def extract_symbols(content: str, language: str) -> list[Symbol]:
    pats = SYMBOL_PATTERNS.get(language, [])
    out: list[Symbol] = []
    for line in content.splitlines():
        for kind, pat in pats:
            m = pat.match(line)
            if m:
                out.append(Symbol(kind, m.group(1)))
    return out


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w一-鿿]+", "-", text, flags=re.UNICODE)
    return re.sub(r"-{2,}", "-", text).strip("-") or "item"


def _fm(meta: dict) -> str:
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


def write_bundle(out: Path, repo_name: str, overview: str, concepts: list[FileConcept],
                 *, lang: str, timestamp: str, date: str, source: str) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    stats = {"docs": 0, "code": 0}

    # 仓库总览概念
    (out / "repository.md").write_text(
        _fm({"type": "Repository", "title": repo_name,
             "description": f"{repo_name} 的 OKF 知识包",
             "resource": source, "lang": lang, "timestamp": timestamp})
        + f"\n\n# {repo_name}\n\n{overview}\n",
        encoding="utf-8",
    )

    root_entries = [("仓库总览", "repository.md", "")]
    used: set[str] = set()
    for c in concepts:
        slug = slugify(c.relpath.replace("/", "-"))
        base, i = slug, 2
        while slug in used:
            slug = f"{base}-{i}"; i += 1
        used.add(slug)
        if c.is_doc:
            sub, dtype = "docs", "Document"
            body = c.body
        else:
            sub, dtype = "code", "Module"
            syms = "\n".join(f"- {s.kind}: `{s.name}`" for s in c.symbols) or "（未提取到符号或为浅扫描)"
            body = f"`{c.relpath}`\n\n# Symbols\n\n{syms}\n"
        d = out / sub
        d.mkdir(exist_ok=True)
        meta = {"type": dtype, "title": c.relpath,
                "description": f"{c.relpath}"[:80],
                "resource": c.resource, "language": c.language,
                "lang": lang, "timestamp": timestamp}
        (d / f"{slug}.md").write_text(
            _fm(meta) + f"\n\n# {c.relpath}\n\n{body}\n", encoding="utf-8")
        root_entries.append((c.relpath, f"{sub}/{slug}.md", ""))
        stats["docs" if c.is_doc else "code"] += 1

    lines = ['---\nokf_version: "0.1"\n---\n', f"# {repo_name}\n"]
    for name, link, desc in root_entries:
        lines.append(f"* [{name}]({link})" + (f" - {desc}" if desc else ""))
    (out / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "log.md").write_text(
        f"# Directory Update Log\n\n## {date}\n"
        f"* **Initialization**: 由 github-to-okf 从 {source or repo_name} 导入。\n",
        encoding="utf-8",
    )
    return stats
