#!/usr/bin/env python3
"""把 OKF v0.1 bundle 发布为 VitePress 文档站(Vue 系,亮色主题)。

生成可直接 `npm install && npm run docs:dev` 的 VitePress 项目:
  out/
  ├── package.json
  └── docs/
      ├── .vitepress/config.mjs   # 侧边栏按目录自动生成,亮色主题
      └── **/*.md                 # 复制自 bundle(VitePress 直接消费 OKF 概念)

用法:
    python okf_to_vitepress.py <bundle 目录> -o ./site [--title "我的知识库"]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def fm_get(text: str, key: str) -> str:
    m = FM.match(text)
    if not m:
        return ""
    for ln in m.group(1).splitlines():
        km = re.match(rf"^{key}\s*:\s*(.+)$", ln)
        if km:
            return km.group(1).strip().strip('"')
    return ""


def title_of(path: Path) -> str:
    t = fm_get(path.read_text(encoding="utf-8", errors="replace"), "title")
    return t or path.stem


def build_sidebar(docs: Path) -> list:
    items = []
    for d in sorted(p for p in docs.iterdir() if p.is_dir() and p.name != ".vitepress"):
        children = []
        for md in sorted(d.rglob("*.md")):
            if md.name in ("log.md",):
                continue
            link = "/" + md.relative_to(docs).as_posix().removesuffix(".md")
            text = "📁 " + md.parent.name if md.name == "index.md" else title_of(md)
            if md.name == "index.md":
                continue
            children.append({"text": text, "link": link})
        if children:
            items.append({"text": d.name, "collapsed": False, "items": children})
    # 根目录下的散页
    for md in sorted(docs.glob("*.md")):
        if md.name in ("index.md", "log.md"):
            continue
        items.append({"text": title_of(md), "link": "/" + md.stem})
    return items


CONFIG_TMPL = """import {{ defineConfig }} from 'vitepress'

// 由 okf-to-book 生成 · 亮色主题(字节风偏好)
export default defineConfig({{
  title: {title},
  description: {desc},
  appearance: false, // 不启用暗色模式
  lastUpdated: true,
  cleanUrls: true,
  themeConfig: {{
    outline: {{ level: [2, 3], label: '本页目录' }},
    sidebar: {sidebar},
    socialLinks: [
      {{ icon: 'github', link: 'https://github.com/yzfly/awesome-okf' }}
    ],
    docFooter: {{ prev: '上一篇', next: '下一篇' }},
    footer: {{ message: '由 OKF bundle 生成 · okf-to-book', copyright: '© 云中江树' }}
  }}
}})
"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="OKF bundle -> VitePress 文档站")
    ap.add_argument("bundle", type=Path)
    ap.add_argument("-o", "--out", type=Path, required=True)
    ap.add_argument("--title", default="")
    args = ap.parse_args(argv)

    if not args.bundle.is_dir():
        print(f"错误:{args.bundle} 不是目录")
        return 2

    docs = args.out / "docs"
    if docs.exists():
        shutil.rmtree(docs)
    docs.mkdir(parents=True)

    # 复制 bundle 的所有 .md(VitePress 直接读 OKF 概念)
    n = 0
    for md in args.bundle.rglob("*.md"):
        rel = md.relative_to(args.bundle)
        dest = docs / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md, dest)
        n += 1

    title = args.title or title_of(args.bundle / "index.md") if (args.bundle / "index.md").exists() else args.title
    title = title or args.bundle.name

    # 首页(VitePress home)
    home_links = ""
    for it in build_sidebar(docs):
        if "items" in it:
            home_links += f"\n## {it['text']}\n\n"
            for c in it["items"]:
                home_links += f"- [{c['text']}]({c['link']})\n"
    (docs / "index.md").write_text(
        f"---\ntitle: {title}\n---\n\n# {title}\n\n"
        f"> 由 OKF 知识包生成的文档站。\n{home_links}\n",
        encoding="utf-8",
    )

    # 配置
    vp = docs / ".vitepress"
    vp.mkdir(exist_ok=True)
    sidebar = json.dumps(build_sidebar(docs), ensure_ascii=False, indent=2)
    (vp / "config.mjs").write_text(
        CONFIG_TMPL.format(
            title=json.dumps(title, ensure_ascii=False),
            desc=json.dumps(f"{title} · OKF 文档站", ensure_ascii=False),
            sidebar=sidebar,
        ),
        encoding="utf-8",
    )

    # package.json
    (args.out / "package.json").write_text(
        json.dumps(
            {
                "name": "okf-book",
                "private": True,
                "scripts": {
                    "docs:dev": "vitepress dev docs",
                    "docs:build": "vitepress build docs",
                    "docs:preview": "vitepress preview docs",
                },
                "devDependencies": {"vitepress": "^1.5.0"},
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"✓ 已生成 VitePress 站点:{args.out}（{n} 篇)")
    print("  cd", args.out, "&& npm install && npm run docs:dev")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
