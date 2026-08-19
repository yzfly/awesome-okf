#!/usr/bin/env python3
"""OKF v0.2 符合性校验器。

按规范 §11 检查一个目录是否为合规的 OKF bundle:
  1. 每个非保留的 .md 文件含有可解析的 YAML 头信息块;
  2. 每个头信息块含有非空的 `type` 字段;
  3. 保留文件名(index.md / log.md)在出现时遵循 §8 / §9 结构。

v0.2 新增的出处 / 信任 / 生命周期(§5)、执行者约定(§7)与
可验算计算(§10)家族全部可选,出现时按 SHOULD 级别校验并给告警;
缺失永远不构成错误(§11)。

v0.1 遗留写法会被识别并提示迁移(§13.1):
  - `timestamp` 已被 `generated.at` 取代;
  - 正文 `# Citations` 列表已被头信息 `sources` 取代。

零第三方依赖(优先用 PyYAML,缺失时回退到最小解析器;
回退模式下嵌套结构无法解析,相关检查会自动跳过)。

用法:
    python validate_okf.py <bundle 目录> [--strict] [--legacy-ok]

    --strict     把 SHOULD 级别的告警也算作失败。
    --legacy-ok  不提示 v0.1 遗留写法(迁移期使用)。

退出码:0 = 合规;1 = 存在硬性错误;2 = 用法错误。
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

RESERVED = {"index.md", "log.md"}
DATE_HEADING = re.compile(r"^##\s+\d{4}-\d{2}-\d{2}\s*$")
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# §7 执行者约定:human:<id> / process:<id> / <producer>/<version>
ACTOR = re.compile(r"^(human:[^\s]+|process:[^\s]+|[^\s/]+/[^\s]+)$")
STATUS_VALUES = {"draft", "stable", "deprecated"}
SUPPORTED_VERSIONS = {"0.2"}
LEGACY_VERSIONS = {"0.1"}

HAVE_YAML = True
try:
    import yaml  # type: ignore

    def parse_yaml(block: str) -> dict:
        data = yaml.safe_load(block) or {}
        if not isinstance(data, dict):
            raise ValueError("头信息不是 YAML 映射")
        return data
except ImportError:  # 最小回退解析器:只取顶层 key: value
    HAVE_YAML = False

    def parse_yaml(block: str) -> dict:
        data: dict = {}
        for line in block.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line[0] in " \t":  # 跳过嵌套/列表续行
                continue
            m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
            if m:
                data[m.group(1)] = m.group(2).strip()
        return data


def strip_fences(body: str) -> str:
    """去掉围栏代码块,避免把示例里的标题当成正文标题(§4.2)。"""
    return re.sub(r"^([ \t]*)(```+|~~~+).*?^\1\2[ \t]*$", "", body, flags=re.DOTALL | re.MULTILINE)


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """返回 (头信息原文, 正文)。无头信息时头信息为 None。"""
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    return m.group(1), m.group(2)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path, msg: str) -> None:
        self.errors.append(f"✗ {path}: {msg}")

    def warn(self, path: Path, msg: str) -> None:
        self.warnings.append(f"! {path}: {msg}")


def _is_iso_datetime(value: object) -> bool:
    if isinstance(value, datetime):
        return True
    if isinstance(value, date):
        return True
    if not isinstance(value, str):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def _is_iso_date(value: object) -> bool:
    if isinstance(value, date) and not isinstance(value, datetime):
        return True
    return isinstance(value, str) and bool(ISO_DATE.match(value))


def _as_date(value: object) -> date | None:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str) and ISO_DATE.match(value):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def _check_actor(path: Path, field: str, value: object, rep: Report) -> None:
    """§7 执行者约定。"""
    if not isinstance(value, str) or not ACTOR.match(value.strip()):
        rep.warn(
            path,
            f"`{field}` 应符合执行者约定:`human:<id>` / `process:<id>` / "
            f"`<producer>/<version>`,发现:{value!r}(§7)",
        )


def check_generated(path: Path, meta: dict, rep: Report) -> None:
    """§5.2 generated: { by, at }。"""
    gen = meta.get("generated")
    if gen is None:
        return
    if not isinstance(gen, dict):
        rep.warn(path, "`generated` 应为 `{ by, at }` 映射(§5.2)")
        return
    if not str(gen.get("by", "")).strip():
        rep.warn(path, "`generated.by` 在 `generated` 内为必填(§5.2)")
    else:
        _check_actor(path, "generated.by", gen.get("by"), rep)
    if "at" in gen and not _is_iso_datetime(gen.get("at")):
        rep.warn(path, f"`generated.at` 应为 ISO 8601 时间,发现:{gen.get('at')!r}(§5.2)")


def check_verified(path: Path, meta: dict, rep: Report) -> None:
    """§5.2 verified:列表;裸映射按单元素列表处理。"""
    ver = meta.get("verified")
    if ver is None:
        return
    entries = [ver] if isinstance(ver, dict) else ver
    if not isinstance(entries, list):
        rep.warn(path, "`verified` 应为验证事件列表或单个 `{ by, at }` 映射(§5.2)")
        return
    for i, ent in enumerate(entries):
        loc = f"verified[{i}]"
        if not isinstance(ent, dict):
            rep.warn(path, f"`{loc}` 应为 `{{ by, at }}` 映射(§5.2)")
            continue
        if not str(ent.get("by", "")).strip():
            rep.warn(path, f"`{loc}.by` 为必填(§5.2)")
        else:
            _check_actor(path, f"{loc}.by", ent.get("by"), rep)
        if "at" not in ent:
            rep.warn(path, f"`{loc}.at` 为必填(§5.2)")
        elif not _is_iso_datetime(ent.get("at")):
            rep.warn(path, f"`{loc}.at` 应为 ISO 8601 时间,发现:{ent.get('at')!r}(§5.2)")


def check_sources(path: Path, meta: dict, rep: Report) -> None:
    """§5.1 sources 与 usage_window。"""
    src = meta.get("sources")
    if src is not None:
        if not isinstance(src, list):
            rep.warn(path, "`sources` 应为列表(§5.1)")
        else:
            seen_ids: set[str] = set()
            for i, ent in enumerate(src):
                loc = f"sources[{i}]"
                if not isinstance(ent, dict):
                    rep.warn(path, f"`{loc}` 应为映射(§5.1)")
                    continue
                if not str(ent.get("resource", "")).strip():
                    rep.warn(path, f"`{loc}.resource` 在条目内为必填(§5.1)")
                sid = ent.get("id")
                if sid is not None:
                    if str(sid) in seen_ids:
                        rep.warn(path, f"`{loc}.id` 重复:{sid}(§5.1 用作脚注 join key)")
                    seen_ids.add(str(sid))
                if "author" in ent:
                    _check_actor(path, f"{loc}.author", ent.get("author"), rep)
                if "usage_count" in ent and not isinstance(ent["usage_count"], int):
                    rep.warn(path, f"`{loc}.usage_count` 应为整数(§5.1)")
                if "last_modified" in ent and not _is_iso_date(ent["last_modified"]):
                    rep.warn(path, f"`{loc}.last_modified` 应为 `YYYY-MM-DD`(§5.1)")

    win = meta.get("usage_window")
    if win is not None:
        if not isinstance(win, dict) or not {"from", "to"} <= set(win):
            rep.warn(path, "`usage_window` 应为 `{ from, to }` 日期区间(§5.1)")
        else:
            for k in ("from", "to"):
                if not _is_iso_date(win[k]):
                    rep.warn(path, f"`usage_window.{k}` 应为 `YYYY-MM-DD`(§5.1)")


def check_lifecycle(path: Path, meta: dict, rep: Report) -> None:
    """§5.4 status / §5.5 stale_after。"""
    if "status" in meta:
        status = str(meta["status"]).strip()
        if status not in STATUS_VALUES:
            rep.warn(
                path,
                f"`status` 应为 draft / stable / deprecated 之一,发现:{status!r}(§5.4)",
            )
    if "stale_after" in meta:
        val = meta["stale_after"]
        if not _is_iso_date(val):
            rep.warn(path, f"`stale_after` 应为绝对日期 `YYYY-MM-DD`,发现:{val!r}(§5.5)")
        else:
            when = _as_date(val)
            if when and date.today() >= when:
                rep.warn(path, f"内容已过期:stale_after={when}(§5.5)")


def check_computation(path: Path, meta: dict, body: str, rep: Report) -> None:
    """§10 可验算计算(Attested Computation)。"""
    if str(meta.get("type", "")).strip() != "Attested Computation":
        return
    if not str(meta.get("runtime", "")).strip():
        rep.warn(path, "`Attested Computation` 需要 `runtime`(§10.2)")

    params = meta.get("parameters")
    if params is not None:
        if not isinstance(params, list):
            rep.warn(path, "`parameters` 应为列表(§10.2)")
        else:
            for i, ent in enumerate(params):
                if not isinstance(ent, dict):
                    rep.warn(path, f"`parameters[{i}]` 应为 `{{ name, type, required }}` 映射(§10.2)")
                    continue
                missing = [k for k in ("name", "type", "required") if k not in ent]
                if missing:
                    rep.warn(path, f"`parameters[{i}]` 缺少:{missing}(§10.2)")

    for field in ("executor", "attester"):
        val = meta.get(field)
        if val is None:
            continue
        if not isinstance(val, dict):
            rep.warn(path, f"`{field}` 应为映射(§10.2)")
            continue
        if not str(val.get("resource", "")).strip():
            rep.warn(path, f"`{field}.resource` 为必填(§10.2)")
    executor = meta.get("executor")
    if isinstance(executor, dict) and "receipt" in executor:
        if not isinstance(executor["receipt"], list):
            rep.warn(path, "`executor.receipt` 应为字段名列表(§10.2)")

    # §10.3:计算体要么是 `computation` 路径,要么是正文 `# Computation`
    has_path = bool(str(meta.get("computation", "")).strip())
    has_heading = re.search(r"^#\s+Computation\s*$", strip_fences(body), re.MULTILINE) is not None
    if not has_path and not has_heading:
        rep.warn(path, "缺少计算体:需要 `computation` 路径或正文 `# Computation` 段(§10.3)")


def check_legacy(path: Path, meta: dict, body: str, rep: Report) -> None:
    """§13.1:v0.1 遗留写法。"""
    if "timestamp" in meta and "generated" not in meta:
        rep.warn(
            path,
            "`timestamp` 是 v0.1 写法,已被 `generated: { by, at }` 取代(§13.1)",
        )
    if re.search(r"^#\s+Citations\s*$", strip_fences(body), re.MULTILINE):
        rep.warn(
            path,
            "正文 `# Citations` 是 v0.1 写法,已被头信息 `sources` 取代(§13.1)",
        )


def check_concept(path: Path, text: str, rep: Report, legacy_ok: bool = False) -> None:
    fm, body = split_frontmatter(text)
    if fm is None:
        rep.error(path, "缺少 YAML 头信息块(§11.1)")
        return
    try:
        meta = parse_yaml(fm)
    except Exception as exc:  # noqa: BLE001
        rep.error(path, f"头信息无法解析:{exc}(§11.1)")
        return

    type_val = str(meta.get("type", "")).strip()
    if not type_val:
        rep.error(path, "缺少非空的 `type` 字段(§11.2)")

    # SHOULD 级别提示
    if not str(meta.get("description", "")).strip():
        rep.warn(path, "建议补 `description`(用于索引与搜索摘要)")

    if not legacy_ok:
        check_legacy(path, meta, body, rep)

    if not HAVE_YAML:
        # 回退解析器读不到嵌套结构,跳过 v0.2 家族检查以免误报
        return
    check_generated(path, meta, rep)
    check_verified(path, meta, rep)
    check_sources(path, meta, rep)
    check_lifecycle(path, meta, rep)
    check_computation(path, meta, body, rep)


def check_index(path: Path, text: str, is_root: bool, rep: Report) -> None:
    fm, _ = split_frontmatter(text)
    if fm is None:
        return
    meta = {}
    try:
        meta = parse_yaml(fm)
    except Exception:  # noqa: BLE001
        pass
    allowed = {"okf_version"} if is_root else set()
    extra = set(meta) - allowed
    if extra:
        rep.error(
            path,
            f"index.md 不应含头信息(根目录仅允许 okf_version),发现:{sorted(extra)}(§8/§12)",
        )
    version = str(meta.get("okf_version", "")).strip()
    if version and version not in SUPPORTED_VERSIONS:
        if version in LEGACY_VERSIONS:
            rep.warn(path, f"声明的 okf_version 为 {version},当前规范为 0.2(§12/§13)")
        else:
            rep.warn(path, f"未知的 okf_version:{version}(§12)")


def check_log(path: Path, text: str, rep: Report) -> None:
    fm, body = split_frontmatter(text)
    if fm is not None:
        rep.warn(path, "log.md 通常不含头信息(§9)")
        text = body
    headings = [ln for ln in text.splitlines() if ln.startswith("## ")]
    for h in headings:
        if not DATE_HEADING.match(h):
            rep.warn(path, f"日期标题应为 ISO `## YYYY-MM-DD`,发现:{h.strip()}(§9)")


def validate(root: Path, rep: Report, legacy_ok: bool = False) -> None:
    md_files = sorted(root.rglob("*.md"))
    if not md_files:
        rep.error(root, "目录下没有任何 .md 文件,不像一个 bundle")
        return
    for path in md_files:
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        name = path.name
        if name == "index.md":
            check_index(rel, text, is_root=(path.parent == root), rep=rep)
        elif name == "log.md":
            check_log(rel, text, rep)
        else:
            check_concept(rel, text, rep, legacy_ok=legacy_ok)


def main() -> int:
    ap = argparse.ArgumentParser(description="OKF v0.2 符合性校验器")
    ap.add_argument("bundle", type=Path, help="bundle 目录")
    ap.add_argument("--strict", action="store_true", help="告警也算失败")
    ap.add_argument(
        "--legacy-ok", action="store_true", help="不提示 v0.1 遗留写法(迁移期使用)"
    )
    args = ap.parse_args()

    if not args.bundle.is_dir():
        print(f"错误:{args.bundle} 不是目录", file=sys.stderr)
        return 2

    rep = Report()
    validate(args.bundle, rep, legacy_ok=args.legacy_ok)

    for line in rep.errors:
        print(line)
    for line in rep.warnings:
        print(line)

    n_md = len(list(args.bundle.rglob("*.md")))
    print(
        f"\n扫描 {n_md} 个 .md 文件 · 错误 {len(rep.errors)} · 告警 {len(rep.warnings)}"
    )
    if not HAVE_YAML:
        print("提示:未安装 PyYAML,已跳过 v0.2 嵌套字段(§5/§10)检查")
    if rep.errors or (args.strict and rep.warnings):
        print("结果:✗ 不符合 OKF v0.2")
        return 1
    print("结果:✓ 符合 OKF v0.2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
