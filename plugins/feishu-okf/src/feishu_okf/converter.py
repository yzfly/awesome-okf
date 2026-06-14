"""把飞书 docx 块(blocks)转换为 Markdown。

飞书 docx v1 的 block_type 整数映射(常用部分):
  2 文本 | 3-11 标题1-9 | 12 无序列表 | 13 有序列表 | 14 代码块
  15 引用 | 17 待办 | 22 分割线 | 其余按文本兜底
每个块的内容在以类型命名的键下,如 block["text"]["elements"]。
"""
from __future__ import annotations

# block_type -> 处理方式
HEADING = {3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 6, 10: 6, 11: 6}
TYPE_KEY = {
    2: "text", 3: "heading1", 4: "heading2", 5: "heading3",
    6: "heading4", 7: "heading5", 8: "heading6", 9: "heading7",
    10: "heading8", 11: "heading9", 12: "bullet", 13: "ordered",
    14: "code", 15: "quote", 17: "todo",
}

# 飞书代码块 language 枚举 -> Markdown 语言标识(取常用)
CODE_LANG = {
    1: "plaintext", 8: "c", 9: "csharp", 12: "cpp", 22: "go", 24: "html",
    27: "java", 28: "javascript", 29: "json", 43: "python", 49: "rust",
    52: "shell", 53: "sql", 54: "swift", 60: "typescript", 63: "yaml",
}


def _text_from(elements: list) -> str:
    parts = []
    for el in elements or []:
        run = el.get("text_run")
        if not run:
            # 兼容公式/提及等,尽量取 content
            for v in el.values():
                if isinstance(v, dict) and "content" in v:
                    parts.append(str(v["content"]))
            continue
        content = run.get("content", "")
        style = run.get("text_element_style", {}) or {}
        if style.get("inline_code"):
            content = f"`{content}`"
        if style.get("bold"):
            content = f"**{content}**"
        if style.get("italic"):
            content = f"*{content}*"
        link = style.get("link", {}) or {}
        if link.get("url"):
            from urllib.parse import unquote

            content = f"[{content}]({unquote(link['url'])})"
        parts.append(content)
    return "".join(parts)


def blocks_to_markdown(blocks: list[dict]) -> str:
    """按文档顺序渲染块为 Markdown。块由 API 以顺序返回。"""
    lines: list[str] = []
    ordered_idx = 0
    for blk in blocks:
        bt = blk.get("block_type")
        if bt == 1:  # page 根块,跳过
            continue
        if bt == 22:  # divider
            lines.append("\n---\n")
            ordered_idx = 0
            continue
        key = TYPE_KEY.get(bt)
        if key is None:
            continue
        node = blk.get(key, {}) or {}
        text = _text_from(node.get("elements"))

        if bt in HEADING:
            lines.append(f"\n{'#' * HEADING[bt]} {text}\n")
            ordered_idx = 0
        elif bt == 12:
            lines.append(f"- {text}")
        elif bt == 13:
            ordered_idx += 1
            lines.append(f"{ordered_idx}. {text}")
        elif bt == 14:
            lang = CODE_LANG.get((node.get("style") or {}).get("language"), "")
            lines.append(f"\n```{lang}\n{text}\n```\n")
        elif bt == 15:
            lines.append(f"> {text}")
        elif bt == 17:
            checked = (node.get("style") or {}).get("done")
            lines.append(f"- [{'x' if checked else ' '}] {text}")
        else:  # 普通文本
            if text.strip():
                lines.append(f"\n{text}\n")
            ordered_idx = 0
    md = "\n".join(lines)
    # 压缩多余空行
    while "\n\n\n" in md:
        md = md.replace("\n\n\n", "\n\n")
    return md.strip() + "\n"
