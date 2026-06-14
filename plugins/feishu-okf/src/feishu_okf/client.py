"""飞书开放平台 API 轻客户端(仅用标准库)。

文档:
  - 鉴权 tenant_access_token: /open-apis/auth/v3/tenant_access_token/internal
  - 知识空间:                /open-apis/wiki/v2/spaces
  - 空间节点:                /open-apis/wiki/v2/spaces/{space_id}/nodes
  - 文档块:                  /open-apis/docx/v1/documents/{doc_id}/blocks
"""
from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass

BASE = "https://open.feishu.cn/open-apis"


@dataclass
class Node:
    node_token: str
    obj_token: str       # 文档 id
    obj_type: str        # docx / doc / sheet / bitable ...
    title: str
    has_child: bool
    parent_token: str = ""


class FeishuError(RuntimeError):
    pass


class FeishuClient:
    def __init__(self, app_id: str, app_secret: str) -> None:
        self.app_id = app_id
        self.app_secret = app_secret
        self._token: str | None = None

    # ---- 底层请求 ----
    def _request(self, method: str, path: str, *, params=None, body=None, auth=True) -> dict:
        url = BASE + path
        if params:
            from urllib.parse import urlencode

            url += "?" + urlencode(params)
        headers = {"Content-Type": "application/json; charset=utf-8"}
        if auth:
            headers["Authorization"] = f"Bearer {self._tenant_token()}"
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
            payload = json.loads(resp.read().decode("utf-8"))
        if payload.get("code", 0) != 0:
            raise FeishuError(f"{path} 返回错误 {payload.get('code')}: {payload.get('msg')}")
        return payload.get("data", {})

    def _tenant_token(self) -> str:
        if self._token:
            return self._token
        url = BASE + "/auth/v3/tenant_access_token/internal"
        body = json.dumps({"app_id": self.app_id, "app_secret": self.app_secret}).encode()
        req = urllib.request.Request(
            url, data=body, headers={"Content-Type": "application/json"}, method="POST"
        )
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
            payload = json.loads(resp.read().decode("utf-8"))
        if payload.get("code", 0) != 0:
            raise FeishuError(f"鉴权失败 {payload.get('code')}: {payload.get('msg')}")
        self._token = payload["tenant_access_token"]
        return self._token

    def _paged(self, path: str, params: dict, item_key: str = "items"):
        params = dict(params)
        while True:
            data = self._request("GET", path, params=params)
            yield from data.get(item_key, [])
            token = data.get("page_token")
            if not data.get("has_more") or not token:
                break
            params["page_token"] = token

    # ---- 业务接口 ----
    def list_spaces(self) -> list[dict]:
        return list(self._paged("/wiki/v2/spaces", {"page_size": 50}))

    def list_nodes(self, space_id: str, parent: str = "") -> list[Node]:
        """递归列出空间内所有节点(深度优先)。"""
        out: list[Node] = []
        params = {"page_size": 50}
        if parent:
            params["parent_node_token"] = parent
        for it in self._paged(f"/wiki/v2/spaces/{space_id}/nodes", params):
            node = Node(
                node_token=it["node_token"],
                obj_token=it.get("obj_token", ""),
                obj_type=it.get("obj_type", ""),
                title=it.get("title", "未命名"),
                has_child=it.get("has_child", False),
                parent_token=parent,
            )
            out.append(node)
            if node.has_child:
                out.extend(self.list_nodes(space_id, node.node_token))
        return out

    def get_doc_blocks(self, document_id: str) -> list[dict]:
        return list(
            self._paged(
                f"/docx/v1/documents/{document_id}/blocks",
                {"page_size": 500, "document_revision_id": -1},
            )
        )
