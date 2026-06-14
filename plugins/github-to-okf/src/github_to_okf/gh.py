"""GitHub API 轻客户端(标准库 urllib)。支持可选 GITHUB_TOKEN 提高限额。"""
from __future__ import annotations

import json
import os
import urllib.request

API = "https://api.github.com"
RAW = "https://raw.githubusercontent.com"


def _headers() -> dict:
    h = {"Accept": "application/vnd.github+json", "User-Agent": "github-to-okf"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def _get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=_headers())
    with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
        return json.loads(resp.read().decode("utf-8"))


def get_repo(owner: str, repo: str) -> dict:
    return _get_json(f"{API}/repos/{owner}/{repo}")


def get_head_sha(owner: str, repo: str, branch: str) -> str:
    data = _get_json(f"{API}/repos/{owner}/{repo}/commits/{branch}")
    return data.get("sha", branch)


def get_tree(owner: str, repo: str, sha: str) -> list[dict]:
    data = _get_json(f"{API}/repos/{owner}/{repo}/git/trees/{sha}?recursive=1")
    return [t for t in data.get("tree", []) if t.get("type") == "blob"]


def get_raw(owner: str, repo: str, sha: str, path: str) -> str:
    from urllib.parse import quote

    url = f"{RAW}/{owner}/{repo}/{sha}/{quote(path)}"
    req = urllib.request.Request(url, headers={"User-Agent": "github-to-okf"})
    with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
        return resp.read().decode("utf-8", errors="replace")


def blob_url(owner: str, repo: str, sha: str, path: str) -> str:
    return f"https://github.com/{owner}/{repo}/blob/{sha}/{path}"
