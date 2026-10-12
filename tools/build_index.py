#!/usr/bin/env python3
"""
Aesthetic Atlas · 检索索引生成器

从所有概念页抽取结构化索引，供 agent 快速定位（避免逐层读 index.md）。

产物（均为可再生成产物，不要手工编辑）：
    index/graph.json    —— 完整概念图（含 frontmatter 字段与出链）
    index/compact.md    —— 紧凑可读清单（agent 首选阅读入口）

用法:
    python3 tools/build_index.py
"""
import os
import re
import json
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "index")

SKIP_DIRS = {".git", "tools", "index", "assets", "__pycache__", "templates"}
NO_FM = {"index.md", "log.md", "_meta.md", "README.md"}


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    data = {}
    for line in text[3:end].splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            v = m.group(2).strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
            else:
                v = v.strip("\"'")
            data[m.group(1)] = v
    return data


def first_paragraph(body):
    """取正文中第一段有信息量的文字作为一句话描述。"""
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", ">", "-", "*", "|", "!", "[")):
            continue
        if line.startswith("```"):
            continue
        clean = re.sub(r"[*`\[\]]|\([^)]*\)", "", line).strip()
        if len(clean) > 10:
            return clean[:140]
    return ""


def extract_keywords(body):
    m = re.search(r"##\s*Prompt Keywords\s*\n+(.*?)(?=\n#|\Z)", body, re.S)
    if not m:
        return []
    raw = m.group(1).strip()
    return [k.strip() for k in re.split(r"[,\n]", raw) if k.strip()]


WIKI_RE = re.compile(r"!?\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")


def build_vault_names():
    """Obsidian 解析集合：vault 相对路径（含去扩展名）与 basename 映射。"""
    rel_set, by_base = set(), {}
    for q in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
        if os.path.isdir(q) or "/.obsidian/" in q:
            continue
        r = os.path.relpath(q, ROOT).replace(os.sep, "/")
        rel_set.add(r)
        stem = r.rsplit(".", 1)[0]
        rel_set.add(stem)
        by_base.setdefault(os.path.basename(stem), []).append(r)
    return rel_set, by_base


def outlinks(path, text, by_base):
    """解析出链：wikilink（basename 或全路径）+ 标准 md 链接。"""
    links = []
    text_nc = re.sub(r"```.*?```", "", text, flags=re.S)
    text_nc = re.sub(r"`[^`\n]*`", "", text_nc)

    for m in WIKI_RE.finditer(text_nc):
        target = m.group(1).strip()
        hit = None
        if target in by_base:
            hit = by_base[target]
        else:
            cands = [v for k, vs in by_base.items() for v in vs if v.rsplit(".",1)[0] == target]
            hit = cands or None
        if hit:
            links.append(hit[0])

    for m in re.finditer(r"\[[^\]]*\]\(([^)#]+)(?:#[^)]*)?\)", text_nc):
        t = m.group(1).strip()
        if not t or t.startswith(("http", "mailto")):
            continue
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), t))
        if os.path.exists(resolved):
            links.append(os.path.relpath(resolved, ROOT))
    return sorted(set(links))


def main():
    os.makedirs(OUT, exist_ok=True)
    _, by_base_v = build_vault_names()
    entries = []

    for p in sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(p, ROOT)
        top = rel.split(os.sep)[0]
        if top in SKIP_DIRS or "/.git/" in p:
            continue
        name = os.path.basename(p)
        if name in NO_FM:
            continue

        text = read(p)
        fm = parse_frontmatter(text)
        body = text
        if text.startswith("---"):
            end = text.find("\n---", 3)
            body = text[end + 4:] if end != -1 else text

        entries.append({
            "id": rel[:-3],
            "path": rel,
            "type": fm.get("type", "Unknown"),
            "title": fm.get("title", name),
            "description": fm.get("description", ""),
            "tags": fm.get("tags", []),
            "status": fm.get("status", ""),
            "one_liner": first_paragraph(body),
            "keywords": extract_keywords(body),
            "links_to": outlinks(p, text, by_base_v),
        })

    # 反向索引：谁引用了这个概念
    inbound = {}
    for e in entries:
        for t in e["links_to"]:
            inbound.setdefault(t, []).append(e["path"])
    for e in entries:
        e["linked_from"] = sorted(inbound.get(e["path"], []))

    graph = {
        "generated_by": "tools/build_index.py",
        "note": "可再生成产物，请勿手工编辑",
        "count": len(entries),
        "entries": entries,
    }
    with open(os.path.join(OUT, "graph.json"), "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=1)

    # 紧凑清单
    by_type = {}
    for e in entries:
        by_type.setdefault(e["type"], []).append(e)

    lines = [
        "---",
        "type: index",
        "title: 检索索引（自动生成）",
        "description: 全部概念页的紧凑清单，agent 优先读本文件定位，再下钻。",
        "---",
        "",
        "# 检索索引",
        "",
        f"> 自动生成，共 **{len(entries)}** 个概念页。**请勿手工编辑**——由 `tools/build_index.py` 产出。",
        "> 完整数据（含关键词与出/入链）见 `graph.json`。",
        "",
        "## 用法（给 agent）",
        "",
        "1. 在本文件按 `type` / 标签 / 关键词定位候选页",
        "2. 只读候选页，不要遍历全部 index.md",
        "3. 需要关系数据（谁引用了谁）时读 `graph.json`",
        "",
    ]
    for t in sorted(by_type):
        lines.append(f"## {t}（{len(by_type[t])}）")
        lines.append("")
        for e in sorted(by_type[t], key=lambda x: x["path"]):
            desc = e["description"] or e["one_liner"]
            lines.append(f"- [{e['title']}](../{e['path']}) — {desc[:100]}")
        lines.append("")

    with open(os.path.join(OUT, "compact.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"生成 index/graph.json —— {len(entries)} 个概念页")
    print(f"生成 index/compact.md —— {len(by_type)} 个 type 分组")


if __name__ == "__main__":
    main()
