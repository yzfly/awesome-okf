"""把 HTML 文件转换为 OKF 概念。

实现 docs/html-first-class-proposal-zh.md 的"双表示":
  - 机读权威:抽取出的 .md(带 OKF frontmatter,canonical 指向 html);
  - 人友好:原 HTML 复制到 assets/,顶部注入 <!--okf ... --> 元数据注释。

用法:
    html-to-okf <html 文件或目录> -o ./out [--lang zh]
"""
from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path

BLOCK = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "pre", "blockquote"}
HEADING = {"h1": "#", "h2": "##", "h3": "###", "h4": "####", "h5": "#####", "h6": "######"}


class Extractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.out: list[str] = []
        self._buf: list[str] = []
        self._tag = ""
        self._skip = 0
        self._in_title = False
        self._list = []  # 'ul'/'ol' 栈
        self._ol_idx = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
            return
        if tag == "title":
            self._in_title = True
        if tag in ("ul", "ol"):
            self._list.append(tag)
            self._ol_idx.append(0)
        if tag in BLOCK:
            self._flush()
            self._tag = tag
        if tag == "a":
            href = dict(attrs).get("href", "")
            self._buf.append("\x00" + href + "\x01")  # 占位,见 handle_data
        if tag == "br":
            self._buf.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = max(0, self._skip - 1)
            return
        if tag == "title":
            self._in_title = False
        if tag in ("ul", "ol"):
            if self._list:
                self._list.pop()
                self._ol_idx.pop()
        if tag == "a":
            self._buf.append("\x02")  # 链接结束标记
        if tag in BLOCK:
            self._flush()
            self._tag = ""

    def handle_data(self, data):
        if self._skip:
            return
        if self._in_title:
            self.title += data
            return
        if data.strip() or data == " ":
            self._buf.append(data)

    def _flush(self):
        if not self._buf:
            return
        text = "".join(self._buf)
        # 还原链接占位:\x00href\x01文字\x02 -> [文字](href)
        text = re.sub(r"\x00([^\x01]*)\x01([^\x02]*)\x02",
                      lambda m: f"[{m.group(2).strip()}]({m.group(1)})", text)
        text = text.replace("\x00", "").replace("\x01", "").replace("\x02", "")
        text = re.sub(r"[ \t]+", " ", text).strip()
        self._buf = []
        if not text:
            return
        tag = self._tag
        if tag in HEADING:
            self.out.append(f"\n{HEADING[tag]} {text}\n")
        elif tag == "li":
            if self._list and self._list[-1] == "ol":
                self._ol_idx[-1] += 1
                self.out.append(f"{self._ol_idx[-1]}. {text}")
            else:
                self.out.append(f"- {text}")
        elif tag == "pre":
            self.out.append(f"\n```\n{text}\n```\n")
        elif tag == "blockquote":
            self.out.append(f"> {text}")
        else:
            self.out.append(f"\n{text}\n")

    def markdown(self) -> str:
        self._flush()
        md = "\n".join(self.out)
        while "\n\n\n" in md:
            md = md.replace("\n\n\n", "\n\n")
        return md.strip() + "\n"


def slugify(text: str) -> str:
    text = (text or "page").strip().lower()
    text = re.sub(r"[^\w一-鿿]+", "-", text, flags=re.UNICODE)
    return re.sub(r"-{2,}", "-", text).strip("-") or "page"


def okf_comment(meta: dict) -> str:
    lines = ["<!--okf"]
    for k, v in meta.items():
        if v:
            lines.append(f"{k}: {v}")
    lines.append("-->")
    return "\n".join(lines) + "\n"


def convert_file(html_path: Path, out: Path, lang: str, timestamp: str) -> tuple[str, str]:
    raw = html_path.read_text(encoding="utf-8", errors="replace")
    ex = Extractor()
    ex.feed(raw)
    title = ex.title.strip() or slugify(html_path.stem)
    slug = slugify(title)
    md_body = ex.markdown()
    desc = next((ln.strip() for ln in md_body.splitlines()
                 if ln.strip() and not ln.startswith(("#", "-", ">"))), "")[:80]

    # 人友好:原 HTML + 注入 okf 注释
    assets = out / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    html_out = assets / f"{slug}.html"
    comment = ""
    if "<!--okf" not in raw:
        comment = okf_comment({
            "type": "Document", "title": title, "lang": lang,
            "canonical": f"/{slug}.md", "timestamp": timestamp,
        })
    html_out.write_text(comment + raw, encoding="utf-8")

    # 机读权威:.md
    md = (
        f"---\ntype: Document\ntitle: {title}\n"
        f"description: {desc}\nresource: assets/{slug}.html\n"
        f"lang: {lang}\ntimestamp: {timestamp}\n---\n\n"
        f"# {title}\n\n{md_body}\n"
        f"# Source\n\n人友好版本:[{slug}.html](assets/{slug}.html)\n"
    )
    (out / f"{slug}.md").write_text(md, encoding="utf-8")
    return title, slug


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="HTML -> OKF 概念(双表示)")
    ap.add_argument("source", type=Path, help="HTML 文件或目录")
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--lang", default="zh")
    ap.add_argument("--date", default="2026-01-01")
    args = ap.parse_args(argv)

    files = ([args.source] if args.source.is_file()
             else sorted(args.source.rglob("*.html")))
    if not files:
        print("没有找到 .html 文件")
        return 1

    ts = f"{args.date}T00:00:00Z"
    entries = []
    for f in files:
        title, slug = convert_file(f, args.out, args.lang, ts)
        entries.append((title, f"{slug}.md"))
        print(f"  ✓ {f.name} -> {slug}.md (+ assets/{slug}.html)")

    lines = ['---\nokf_version: "0.1"\n---\n', "# HTML 知识库\n"]
    for title, link in entries:
        lines.append(f"* [{title}]({link})")
    (args.out / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (args.out / "log.md").write_text(
        f"# Directory Update Log\n\n## {args.date}\n"
        f"* **Initialization**: 由 html-to-okf 转换 {len(files)} 个 HTML 文件。\n",
        encoding="utf-8",
    )
    print(f"\n✓ 转换 {len(files)} 个 HTML -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
