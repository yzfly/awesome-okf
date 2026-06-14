#!/usr/bin/env python3
"""把 OKF v0.1 bundle 打包成单个自包含 HTML(数据内嵌,不出页面)。

产出一个 okf.html:左侧按类型分组的导航 + 中间 Markdown 阅读器 + 概念关系图谱。
随后用同目录 minify.mjs(node)压缩。

用法:
    python build_web.py <bundle 目录> -o okf.html [--title "我的知识库"]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def parse(text: str) -> tuple[dict, str]:
    m = FM.match(text)
    if not m:
        return {}, text
    meta = {}
    for ln in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", ln)
        if km:
            meta[km.group(1)] = km.group(2).strip().strip('"')
    return meta, m.group(2)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="OKF bundle -> 单文件 HTML")
    ap.add_argument("bundle", type=Path)
    ap.add_argument("-o", "--out", type=Path, default=Path("okf.html"))
    ap.add_argument("--title", default="OKF 知识库")
    args = ap.parse_args(argv)

    nodes = []
    id_set = set()
    for md in sorted(args.bundle.rglob("*.md")):
        rel = md.relative_to(args.bundle).as_posix()
        cid = rel[:-3]
        meta, body = parse(md.read_text(encoding="utf-8", errors="replace"))
        id_set.add(cid)
        nodes.append({"id": cid, "rel": rel, "meta": meta, "body": body})

    # 出边:正文里指向其他概念的链接
    edges = []
    for n in nodes:
        for _, href in LINK.findall(n["body"]):
            tgt = href.split("#")[0]
            if tgt.startswith("/"):
                tgt = tgt[1:]
            else:  # 相对当前概念目录
                base = "/".join(n["rel"].split("/")[:-1])
                tgt = re.sub(r"[^/]+/\.\./", "", f"{base}/{tgt}") if base else tgt
            tgt = tgt.removesuffix(".md")
            if tgt in id_set and tgt != n["id"]:
                edges.append([n["id"], tgt])

    data = {
        "title": args.title,
        "nodes": [{"id": n["id"], "title": n["meta"].get("title", n["id"]),
                   "type": n["meta"].get("type", "Concept"),
                   "desc": n["meta"].get("description", ""),
                   "body": n["body"]} for n in nodes],
        "edges": edges,
    }
    # 转义 </ 防止正文里的 </script> 提前闭合内嵌脚本(<\/ 在 JSON 中合法)
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.replace("/*__DATA__*/", payload)
    args.out.write_text(html, encoding="utf-8")
    print(f"✓ 生成 {args.out}（{len(nodes)} 概念, {len(edges)} 关系, {len(html)} 字节,未压缩)")
    return 0


TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>OKF 知识库</title>
<style>
:root{--bg:#fff;--fg:#1d2129;--sub:#86909c;--line:#e5e6eb;--brand:#165dff;--code:#f7f8fa}
*{box-sizing:border-box}body{margin:0;font:15px/1.7 -apple-system,"PingFang SC","Microsoft YaHei",sans-serif;color:var(--fg);background:var(--bg)}
#app{display:grid;grid-template-columns:280px 1fr 360px;height:100vh}
aside{border-right:1px solid var(--line);overflow:auto;padding:16px}
main{overflow:auto;padding:32px 48px;max-width:860px}
#graph{border-left:1px solid var(--line);overflow:hidden}
h1.t{font-size:18px;margin:0 0 12px}
input{width:100%;padding:8px 10px;border:1px solid var(--line);border-radius:8px;margin-bottom:12px;font-size:14px}
.grp{font-size:12px;color:var(--sub);margin:14px 0 4px;text-transform:uppercase;letter-spacing:.5px}
.it{padding:5px 8px;border-radius:6px;cursor:pointer;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.it:hover{background:var(--code)}.it.on{background:#e8f0ff;color:var(--brand)}
.tag{display:inline-block;font-size:12px;color:var(--brand);background:#e8f0ff;border-radius:4px;padding:1px 7px;margin-bottom:8px}
main h1,main h2,main h3{line-height:1.3}main h1{font-size:26px}main h2{font-size:20px;border-bottom:1px solid var(--line);padding-bottom:6px;margin-top:28px}
main code{background:var(--code);padding:2px 5px;border-radius:4px;font-size:90%}
main pre{background:var(--code);padding:14px;border-radius:8px;overflow:auto}main pre code{background:none;padding:0}
main table{border-collapse:collapse;width:100%}main th,main td{border:1px solid var(--line);padding:6px 10px;text-align:left}
main a{color:var(--brand);text-decoration:none}main a:hover{text-decoration:underline}
circle{cursor:pointer}text{font-size:10px;fill:var(--sub);pointer-events:none}
@media(max-width:1100px){#app{grid-template-columns:240px 1fr}#graph{display:none}}
</style></head>
<body><div id="app">
<aside><h1 class="t" id="ttl"></h1><input id="q" placeholder="搜索概念…"><div id="nav"></div></aside>
<main id="doc"></main>
<svg id="graph"></svg>
</div>
<script type="application/json" id="okf-data">/*__DATA__*/</script>
<script>
var D=JSON.parse(document.getElementById('okf-data').textContent);
document.title=D.title;document.getElementById('ttl').textContent=D.title;
var byId={};D.nodes.forEach(function(n){byId[n.id]=n});
function md(s){
 var lines=s.split('\n'),o=[],i,inC=false,inT=false;
 function esc(t){return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
 function inl(t){return esc(t).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/\[([^\]]+)\]\(([^)]+)\)/g,function(m,a,h){var id=h.replace(/^\//,'').replace(/#.*/,'').replace(/\.md$/,'');return byId[id]?'<a href="#'+id+'">'+a+'</a>':'<a href="'+h+'" target="_blank">'+a+'</a>'})}
 for(i=0;i<lines.length;i++){var l=lines[i];
  if(/^```/.test(l)){if(inC){o.push('</code></pre>');inC=false}else{o.push('<pre><code>');inC=true}continue}
  if(inC){o.push(esc(l));continue}
  if(/^\|(.+)\|$/.test(l)){var c=l.split('|').slice(1,-1);if(/^[\s:|-]+$/.test(l))continue;var tag=inT?'td':'th';if(!inT){o.push('<table>');inT=true}o.push('<tr>'+c.map(function(x){return '<'+tag+'>'+inl(x.trim())+'</'+tag+'>'}).join('')+'</tr>');continue}
  if(inT){o.push('</table>');inT=false}
  var h=l.match(/^(#{1,4})\s+(.*)/);if(h){o.push('<h'+h[1].length+'>'+inl(h[2])+'</h'+h[1].length+'>');continue}
  if(/^[-*]\s+/.test(l)){o.push('<li>'+inl(l.replace(/^[-*]\s+/,''))+'</li>');continue}
  if(/^\d+\.\s+/.test(l)){o.push('<li>'+inl(l.replace(/^\d+\.\s+/,''))+'</li>');continue}
  if(/^>\s?/.test(l)){o.push('<blockquote>'+inl(l.replace(/^>\s?/,''))+'</blockquote>');continue}
  if(l.trim()==='')o.push('');else o.push('<p>'+inl(l)+'</p>')
 }
 if(inC)o.push('</code></pre>');if(inT)o.push('</table>');
 return o.join('\n').replace(/(<li>[\s\S]*?<\/li>)(?!\s*<li>)/g,'<ul>$1</ul>')
}
function nav(f){var g={},nv=document.getElementById('nav');nv.innerHTML='';
 D.nodes.forEach(function(n){if(f&&(n.title+n.id).toLowerCase().indexOf(f.toLowerCase())<0)return;(g[n.type]=g[n.type]||[]).push(n)});
 Object.keys(g).sort().forEach(function(t){var d=document.createElement('div');d.className='grp';d.textContent=t;nv.appendChild(d);
  g[t].forEach(function(n){var e=document.createElement('div');e.className='it';e.textContent=n.title;e.dataset.id=n.id;e.onclick=function(){location.hash=n.id};nv.appendChild(e)})})}
function show(id){var n=byId[id]||D.nodes[0];if(!n)return;
 document.getElementById('doc').innerHTML='<div class="tag">'+n.type+'</div>'+md(n.body);
 document.querySelectorAll('.it').forEach(function(e){e.classList.toggle('on',e.dataset.id===n.id)});
 document.getElementById('doc').scrollTop=0}
function graph(){var s=document.getElementById('graph'),W=s.clientWidth||360,H=s.clientHeight||600,N=D.nodes,cx=W/2,cy=H/2,R=Math.min(W,H)/2-40,pos={};
 N.forEach(function(n,i){var a=2*Math.PI*i/N.length;pos[n.id]=[cx+R*Math.cos(a),cy+R*Math.sin(a)]});
 var h='';D.edges.forEach(function(e){var a=pos[e[0]],b=pos[e[1]];if(a&&b)h+='<line x1="'+a[0]+'" y1="'+a[1]+'" x2="'+b[0]+'" y2="'+b[1]+'" stroke="#e5e6eb"/>'});
 N.forEach(function(n){var p=pos[n.id];h+='<circle cx="'+p[0]+'" cy="'+p[1]+'" r="5" fill="#165dff" onclick="location.hash=\''+n.id+'\'"><title>'+n.title+'</title></circle>'});
 s.setAttribute('viewBox','0 0 '+W+' '+H);s.innerHTML=h}
window.onhashchange=function(){show(decodeURIComponent(location.hash.slice(1)))};
document.getElementById('q').oninput=function(){nav(this.value)};
nav('');graph();show(decodeURIComponent(location.hash.slice(1))||D.nodes[0].id);
</script></body></html>"""


if __name__ == "__main__":
    raise SystemExit(main())
