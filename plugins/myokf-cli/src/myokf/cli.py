"""myokf —— OKF 统一命令行入口。

把仓库里所有 producer / consumer / 工具收进一个命令,内部分发到各模块。
设计为在 awesome-okf 仓库检出环境下开箱即用(定位仓库根,按需注入路径)。

命令一览:
    myokf validate <bundle> [--strict]         校验 OKF 符合性
    myokf scaffold <dir>                        生成空 bundle 骨架
    myokf from-awesome <owner/repo|url|file> -o ./out
    myokf from-feishu  spaces | export <id> -o ./out
    myokf from-obsidian <vault> -o ./out
    myokf from-notion  <export_dir> -o ./out
    myokf from-html    <file|dir> -o ./out
    myokf from-github  <owner/repo|path> -o ./out [--deep]
    myokf to-book      <bundle> -o ./site [--title T]
    myokf to-web       <bundle> -o okf.html [--title T] [--no-min]
    myokf list                                 列出所有命令

每个子命令的其余参数原样转发给对应工具,用 `myokf <cmd> --help` 查看细节。
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

# 仓库根:.../awesome-okf/plugins/myokf-cli/src/myokf/cli.py -> parents[4]
ROOT = Path(__file__).resolve().parents[4]

# command -> ("module", 相对 src 路径, 模块名) 或 ("script", 相对脚本路径)
MODULES = {
    "from-awesome": ("module", "plugins/awesome-to-okf/src", "awesome_to_okf.cli"),
    "from-feishu": ("module", "plugins/feishu-to-okf/src", "feishu_to_okf.cli"),
    "from-obsidian": ("module", "plugins/obsidian-to-okf/src", "obsidian_to_okf.cli"),
    "from-notion": ("module", "plugins/notion-to-okf/src", "notion_to_okf.cli"),
    "from-html": ("module", "plugins/html-to-okf/src", "html_to_okf.cli"),
    "from-github": ("module", "plugins/github-to-okf/src", "github_to_okf.cli"),
    "validate": ("script", "skills/okf-creator/scripts/validate_okf.py"),
    "scaffold": ("script", "skills/okf-creator/scripts/scaffold_okf.py"),
    "to-book": ("script", "skills/okf-to-book/scripts/okf_to_vitepress.py"),
}

HELP = __doc__


def _run_module(src_rel: str, mod: str, argv: list[str]) -> int:
    env = dict(os.environ)
    src = str(ROOT / src_rel)
    env["PYTHONPATH"] = src + os.pathsep + env.get("PYTHONPATH", "")
    return subprocess.run([sys.executable, "-m", mod, *argv], env=env).returncode


def _run_script(script_rel: str, argv: list[str]) -> int:
    return subprocess.run([sys.executable, str(ROOT / script_rel), *argv]).returncode


def _to_web(argv: list[str]) -> int:
    """build_web 生成 + node minify 压缩,一步到位。"""
    import argparse

    ap = argparse.ArgumentParser(prog="myokf to-web")
    ap.add_argument("bundle")
    ap.add_argument("-o", "--out", default="okf.html")
    ap.add_argument("--title", default="OKF 知识库")
    ap.add_argument("--no-min", action="store_true", help="不压缩,只生成")
    args = ap.parse_args(argv)

    build = ROOT / "skills/okf-to-web/scripts/build_web.py"
    minify = ROOT / "skills/okf-to-web/scripts/minify.mjs"

    if args.no_min:
        return _run_script("skills/okf-to-web/scripts/build_web.py",
                           [args.bundle, "-o", args.out, "--title", args.title])
    with tempfile.TemporaryDirectory() as td:
        raw = str(Path(td) / "raw.html")
        rc = subprocess.run([sys.executable, str(build), args.bundle,
                             "-o", raw, "--title", args.title]).returncode
        if rc != 0:
            return rc
        node = _have("node")
        if not node:
            print("⚠ 未找到 node,跳过压缩,输出未压缩版本。")
            Path(args.out).write_text(Path(raw).read_text(encoding="utf-8"), encoding="utf-8")
            return 0
        return subprocess.run(["node", str(minify), raw, args.out]).returncode


def _have(cmd: str) -> bool:
    from shutil import which

    return which(cmd) is not None


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(HELP)
        return 0
    cmd, rest = argv[0], argv[1:]

    if cmd == "list":
        print("可用命令:")
        for c in [*MODULES, "to-web", "list"]:
            print("  myokf", c)
        return 0
    if cmd == "to-web":
        return _to_web(rest)
    if cmd not in MODULES:
        print(f"未知命令:{cmd}\n用 `myokf help` 查看全部。", file=sys.stderr)
        return 2

    kind, *spec = MODULES[cmd]
    if kind == "module":
        return _run_module(spec[0], spec[1], rest)
    return _run_script(spec[0], rest)


if __name__ == "__main__":
    raise SystemExit(main())
