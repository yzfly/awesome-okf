"""github-to-okf 命令行入口。

把一个 GitHub 仓库(远程 owner/repo 或本地路径)转换为 OKF 知识包,
应用 code-to-okf 约定(type 词表、language、符号、blob 行级 resource)。

用法:
    # 本地仓库(全量:读文件、提取符号)
    github-to-okf ./my-repo -o ./out

    # 远程仓库(默认浅扫描:只用 tree;加 --deep 下载并提取符号)
    github-to-okf owner/repo -o ./out [--deep]
    # 远程建议设 GITHUB_TOKEN 提高 API 限额
"""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from . import gh
from .core import (
    LANG_EXT, SKIP_DIRS, FileConcept, detect_language, extract_symbols, write_bundle,
)

MAX_BYTES = 200_000
DOC_EXT = {".md", ".markdown"}


def _git(path: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(path), *args],
                              capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:  # noqa: BLE001
        return ""


def from_local(path: Path) -> tuple[str, str, list[FileConcept]]:
    name = path.name
    # 推断 blob 基址(若是 git 仓库)
    remote = _git(path, "config", "--get", "remote.origin.url")
    sha = _git(path, "rev-parse", "HEAD")
    base = ""
    if "github.com" in remote and sha:
        slug = remote.split("github.com")[-1].lstrip(":/").removesuffix(".git")
        base = f"https://github.com/{slug}/blob/{sha}"
    source = remote or str(path)

    overview = ""
    concepts: list[FileConcept] = []
    for f in sorted(path.rglob("*")):
        if not f.is_file() or any(p in SKIP_DIRS for p in f.parts):
            continue
        rel = f.relative_to(path).as_posix()
        suffix = f.suffix.lower()
        if suffix not in DOC_EXT and suffix not in LANG_EXT:
            continue
        try:
            if f.stat().st_size > MAX_BYTES:
                continue
            content = f.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue
        resource = f"{base}/{rel}" if base else rel
        if suffix in DOC_EXT:
            if rel.lower() == "readme.md":
                overview = content
                continue
            concepts.append(FileConcept(rel, "", resource=resource, is_doc=True, body=content))
        else:
            lang = detect_language(rel)
            concepts.append(FileConcept(rel, lang, extract_symbols(content, lang), resource))
    return name, overview, concepts


def from_remote(owner: str, repo: str, deep: bool) -> tuple[str, str, list[FileConcept]]:
    meta = gh.get_repo(owner, repo)
    branch = meta.get("default_branch", "main")
    sha = gh.get_head_sha(owner, repo, branch)
    tree = gh.get_tree(owner, repo, sha)

    desc = meta.get("description") or ""
    topics = meta.get("topics") or []
    overview = (f"{desc}\n\n- 主语言:{meta.get('language')}\n"
                f"- Stars:{meta.get('stargazers_count')}\n"
                f"- 默认分支:{branch}\n"
                f"- Topics:{', '.join(topics)}\n")
    try:
        overview += "\n---\n\n" + gh.get_raw(owner, repo, sha, "README.md")
    except Exception:  # noqa: BLE001
        pass

    concepts: list[FileConcept] = []
    for t in tree:
        path = t["path"]
        suffix = Path(path).suffix.lower()
        if any(p in SKIP_DIRS for p in Path(path).parts):
            continue
        if suffix not in DOC_EXT and suffix not in LANG_EXT:
            continue
        if path.lower() == "readme.md":
            continue
        resource = gh.blob_url(owner, repo, sha, path)
        if suffix in DOC_EXT:
            body = ""
            if deep:
                try:
                    body = gh.get_raw(owner, repo, sha, path)
                except Exception:  # noqa: BLE001
                    pass
            concepts.append(FileConcept(path, "", resource=resource, is_doc=True, body=body))
        else:
            lang = detect_language(path)
            syms = []
            if deep:
                try:
                    syms = extract_symbols(gh.get_raw(owner, repo, sha, path), lang)
                except Exception:  # noqa: BLE001
                    pass
            concepts.append(FileConcept(path, lang, syms, resource))
    return f"{owner}/{repo}", overview, concepts


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="GitHub 仓库 -> OKF v0.1")
    ap.add_argument("source", help="本地路径 或 owner/repo")
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--deep", action="store_true", help="远程模式下载文件并提取符号")
    ap.add_argument("--lang", default="zh")
    ap.add_argument("--date", default="2026-01-01")
    args = ap.parse_args(argv)

    p = Path(args.source)
    if p.is_dir():
        name, overview, concepts = from_local(p)
        source = name
    elif "/" in args.source and not args.source.startswith("http"):
        owner, _, repo = args.source.partition("/")
        name, overview, concepts = from_remote(owner, repo, args.deep)
        source = f"https://github.com/{owner}/{repo}"
        if not args.deep:
            print("  注:远程浅扫描(未提取符号)。加 --deep 可下载文件并提取符号。")
    else:
        print(f"无法识别来源:{args.source}(给本地目录或 owner/repo)")
        return 2

    stats = write_bundle(
        args.out, name, overview or "（无 README)", concepts,
        lang=args.lang, timestamp=f"{args.date}T00:00:00Z",
        date=args.date, source=source,
    )
    print(f"✓ 已生成 OKF bundle:{args.out}")
    print(f"  文档概念:{stats['docs']} · 代码概念:{stats['code']}")
    print("  用 ../../skills/okf-creator/scripts/validate_okf.py 校验。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
