"""解析 awesome 列表 Markdown，抽取出分节与链接条目。

awesome 列表的典型结构:
    ## 分节标题
    ### 子分节
    * [名称](URL) - 描述
    - [名称](URL) — 描述

本解析器按 H2/H3 标题维护当前分节路径，逐条抽取列表里的链接。
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# 列表项里的第一个 Markdown 链接 + 其后描述
ITEM_RE = re.compile(
    r"^\s*[-*+]\s+\[(?P<title>[^\]]+)\]\((?P<url>[^)]+)\)\s*(?:[-—–:：]\s*(?P<desc>.+))?$"
)
H2_RE = re.compile(r"^##\s+(?P<t>.+?)\s*$")
H3_RE = re.compile(r"^###\s+(?P<t>.+?)\s*$")
# 跳过常见的非内容分节
SKIP_SECTIONS = {
    "contents", "table of contents", "目录", "contributing", "贡献",
    "license", "许可", "许可证", "acknowledgements", "致谢",
}


@dataclass
class Item:
    title: str
    url: str
    description: str
    section: str          # 一级分节(H2)
    subsection: str = ""  # 二级分节(H3)


@dataclass
class ParsedList:
    title: str = "Awesome List"
    intro: str = ""
    items: list[Item] = field(default_factory=list)

    def sections(self) -> dict[str, list[Item]]:
        out: dict[str, list[Item]] = {}
        for it in self.items:
            out.setdefault(it.section or "未分类", []).append(it)
        return out


def _clean_desc(desc: str | None) -> str:
    if not desc:
        return ""
    # 去掉行尾的徽章/图片 Markdown
    desc = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", desc)
    return desc.strip()


def parse(markdown: str) -> ParsedList:
    lines = markdown.splitlines()
    result = ParsedList()

    # 标题:第一个 H1
    for ln in lines:
        m = re.match(r"^#\s+(.+?)\s*$", ln)
        if m:
            result.title = m.group(1).strip()
            break

    section = ""
    subsection = ""
    in_code = False
    skipping = False

    for ln in lines:
        if ln.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue

        h2 = H2_RE.match(ln)
        if h2:
            section = h2.group("t").strip()
            subsection = ""
            skipping = section.strip().lower() in SKIP_SECTIONS
            continue
        h3 = H3_RE.match(ln)
        if h3:
            subsection = h3.group("t").strip()
            continue

        if skipping:
            continue

        m = ITEM_RE.match(ln)
        if m:
            result.items.append(
                Item(
                    title=m.group("title").strip(),
                    url=m.group("url").strip(),
                    description=_clean_desc(m.group("desc")),
                    section=section or "未分类",
                    subsection=subsection,
                )
            )

    return result
