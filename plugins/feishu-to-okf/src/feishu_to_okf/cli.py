"""feishu-to-okf 命令行入口。

凭据通过环境变量提供:
    export FEISHU_APP_ID=cli_xxx
    export FEISHU_APP_SECRET=xxx

用法:
    feishu-to-okf spaces                         # 列出可访问的知识空间
    feishu-to-okf export <space_id> -o ./out     # 导出整个空间为 OKF bundle
"""
from __future__ import annotations

import argparse
import os
import sys

from .client import FeishuClient, FeishuError
from .converter import blocks_to_markdown
from .okf import slugify, write_concept, write_root


def _client() -> FeishuClient:
    app_id = os.environ.get("FEISHU_APP_ID")
    secret = os.environ.get("FEISHU_APP_SECRET")
    if not app_id or not secret:
        print("错误:请先设置 FEISHU_APP_ID 与 FEISHU_APP_SECRET 环境变量。", file=sys.stderr)
        raise SystemExit(2)
    return FeishuClient(app_id, secret)


def cmd_spaces(args) -> int:
    client = _client()
    spaces = client.list_spaces()
    if not spaces:
        print("没有可访问的知识空间(确认应用已被加入空间并有读权限)。")
        return 1
    print("可访问的知识空间:")
    for s in spaces:
        print(f"  {s.get('space_id')}  {s.get('name')}")
    return 0


def cmd_export(args) -> int:
    from pathlib import Path

    client = _client()
    space_id = args.space_id
    out = Path(args.out)

    # 找空间名
    name = space_id
    for s in client.list_spaces():
        if str(s.get("space_id")) == str(space_id):
            name = s.get("name", space_id)
            break

    nodes = client.list_nodes(space_id)
    docx_nodes = [n for n in nodes if n.obj_type == "docx" and n.obj_token]
    print(f"空间「{name}」共 {len(nodes)} 个节点,其中 docx 文档 {len(docx_nodes)} 篇。")

    entries: list[tuple[str, str, str]] = []
    used: set[str] = set()
    for n in docx_nodes:
        try:
            blocks = client.get_doc_blocks(n.obj_token)
        except FeishuError as exc:
            print(f"  ⚠ 跳过《{n.title}》:{exc}", file=sys.stderr)
            continue
        md = blocks_to_markdown(blocks)
        slug = slugify(n.title)
        base, i = slug, 2
        while slug in used:
            slug = f"{base}-{i}"
            i += 1
        used.add(slug)
        rel = f"docs/{slug}.md"
        resource = f"https://feishu.cn/wiki/{n.node_token}"
        write_concept(
            out, rel, n.title, md,
            resource=resource, lang=args.lang,
            timestamp=f"{args.date}T00:00:00Z",
        )
        entries.append((n.title, rel, ""))
        print(f"  ✓ {n.title} -> {rel}")

    write_root(out, name, entries, args.date, name)
    print(f"\n✓ 导出完成:{out}（{len(entries)} 篇文档)")
    print("  用 ../../skills/okf-creator/scripts/validate_okf.py 校验。")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="飞书知识库 -> OKF v0.1 导出器")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("spaces", help="列出可访问的知识空间")
    sp.set_defaults(func=cmd_spaces)

    ex = sub.add_parser("export", help="导出一个空间为 OKF bundle")
    ex.add_argument("space_id", help="知识空间 ID(用 spaces 子命令查看)")
    ex.add_argument("-o", "--out", required=True, help="输出目录")
    ex.add_argument("--lang", default="zh")
    ex.add_argument("--date", default="2026-01-01")
    ex.set_defaults(func=cmd_export)

    args = ap.parse_args(argv)
    try:
        return args.func(args)
    except FeishuError as exc:
        print(f"飞书 API 错误:{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
