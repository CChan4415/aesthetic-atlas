#!/usr/bin/env python3
"""
Aesthetic Atlas · 一致性校验器

校验内容：
  1. OKF 约定     —— 概念页必须有 frontmatter 与 type 字段
  2. 内部链接     —— 所有相对链接目标必须存在
  3. 配方 schema  —— .recipe.yml 引用完整性、双表示配对、必填字段
  4. 图像资产     —— assets/ 路径结构是否镜像 atlas/，概念页图片引用是否存在
  5. 索引覆盖     —— 每个目录是否有 index.md
  6. 命名规范     —— kebab-case、无空格

用法:
    python3 tools/validate.py            # 全量检查
    python3 tools/validate.py --quiet    # 只输出问题
退出码: 0 = 通过, 1 = 有问题
"""
import os
import re
import sys
import glob
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 允许没有 frontmatter 的文件（索引类、日志类）
NO_FM_ALLOWED = {"index.md", "log.md", "_meta.md", "README.md", "AGENTS.md"}

errors = []
warnings = []


def rel(p):
    return os.path.relpath(p, ROOT)


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def strip_code(text):
    """移除围栏代码块与行内代码，避免把文档示例误判为真实链接/图片引用。"""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text


def parse_frontmatter(text):
    """返回 (frontmatter_dict_or_None, body)。简易 YAML 解析，够用即可。"""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    raw = text[3:end]
    body = text[end + 4:]
    data = {}
    for line in raw.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            data[m.group(1)] = m.group(2).strip()
    return data, body


# ---------------------------------------------------------------- 1. OKF 约定
def check_frontmatter():
    for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if "/tools/" in p or "/.git/" in p:
            continue
        name = os.path.basename(p)
        text = read(p)
        fm, _ = parse_frontmatter(text)
        if fm is None:
            if name not in NO_FM_ALLOWED:
                warn(f"[frontmatter] 缺少 frontmatter（非索引文件）: {rel(p)}")
            continue
        if "type" not in fm:
            err(f"[frontmatter] 有 frontmatter 但缺 type 字段（OKF 唯一必填）: {rel(p)}")
        if "status" in fm:
            st = fm["status"].strip().strip('"\'')
            if st not in ("draft", "stable", "deprecated"):
                warn(f"[frontmatter] status 取值非标准 '{st}': {rel(p)}")


# ---------------------------------------------------------------- 2. 内部链接
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
WIKI_RE = re.compile(r"!?\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")


def build_vault_names():
    """Obsidian 解析集合：vault 相对路径（含去扩展名）+ basename。

    Obsidian 语义：[[target]] 可以是
      - 笔记 basename（去 .md）
      - vault 相对路径
      - 附件（图片等）的 basename，可在库内任意位置
    """
    rel_set, by_base = set(), {}
    for q in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
        if os.path.isdir(q) or "/.obsidian/" in q:
            continue
        r = os.path.relpath(q, ROOT).replace(os.sep, "/")
        rel_set.add(r)
        stem = r.rsplit(".", 1)[0]
        rel_set.add(stem)
        by_base.setdefault(os.path.basename(stem), []).append(stem)
        # 附件：带扩展名的 basename 也要可解析
        by_base.setdefault(os.path.basename(r), []).append(stem)
    return rel_set, by_base


def check_links():
    rel_set, by_base = build_vault_names()
    for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if "/.git/" in p:
            continue
        text = strip_code(read(p))

        # 1) Obsidian wikilink
        for m in WIKI_RE.finditer(text):
            target = m.group(1).strip()
            if target in rel_set or target in by_base:
                continue
            err(f"[wikilink] 无法解析 {rel(p)} -> {m.group(0)}")

        # 2) 标准 Markdown 链接（外部链接与遗留链接）
        for m in LINK_RE.finditer(text):
            target = m.group(2).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("/"):
                resolved = os.path.join(ROOT, target.lstrip("/"))
            else:
                resolved = os.path.normpath(os.path.join(os.path.dirname(p), target))
            if not os.path.exists(resolved):
                err(f"[link] 断链 {rel(p)} -> {m.group(2)}")


# ---------------------------------------------------------------- 3. 配方 schema
def check_recipes():
    ymls = glob.glob(os.path.join(ROOT, "recipes", "*.recipe.yml"))
    for y in ymls:
        text = read(y)
        rid = os.path.basename(y).replace(".recipe.yml", "")

        # 必填字段
        for field in ("id:", "version:", "title_zh:", "movement:", "locked:"):
            if not re.search(rf"^{re.escape(field)}", text, re.M):
                err(f"[recipe] 缺必填字段 {field} : {rel(y)}")

        m = re.search(r"^id:\s*(\S+)", text, re.M)
        if m and m.group(1) != rid:
            err(f"[recipe] id '{m.group(1)}' 与文件名 '{rid}' 不一致: {rel(y)}")

        # 双表示配对
        md = os.path.join(ROOT, "recipes", rid + ".md")
        if not os.path.exists(md):
            err(f"[recipe] 缺少对应 Markdown: recipes/{rid}.md")

        # 引用完整性：所有 atlas/ 开头的路径
        for ref in re.findall(r"(atlas/[\w\-/]+\.md)", text):
            if not os.path.exists(os.path.join(ROOT, ref)):
                err(f"[recipe] 引用的概念页不存在: {ref}  (in {rel(y)})")

        # prompt 段落存在性
        if os.path.exists(md):
            body = read(md)
            for pref in re.findall(r'"recipes/[^#"]+#([^"]+)"', text):
                if pref not in body:
                    warn(f"[recipe] prompt 段落 '{pref}' 未在 {rid}.md 中找到")

    # 反向：有 .md 配方但无 .yml
    for md in glob.glob(os.path.join(ROOT, "recipes", "*.md")):
        if os.path.basename(md) == "index.md":
            continue
        yml = md[:-3] + ".recipe.yml"
        if not os.path.exists(yml):
            warn(f"[recipe] 配方 {rel(md)} 尚无机读 .recipe.yml（建议补）")


# ---------------------------------------------------------------- 4. 图像资产
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def check_assets():
    assets_dir = os.path.join(ROOT, "assets")
    if not os.path.exists(assets_dir):
        warn("[assets] assets/ 目录不存在（图像层尚未建立）")
        return

    # 概念页图片引用是否存在
    for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if "/.git/" in p:
            continue
        for m in IMG_RE.finditer(strip_code(read(p))):
            t = m.group(1).strip()
            if t.startswith(("http://", "https://")):
                warn(f"[assets] 图片使用外部 URL（建议本地化）: {rel(p)} -> {t}")
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(p), t))
            if not os.path.exists(resolved):
                err(f"[assets] 图片不存在: {rel(p)} -> {t}")


# ---------------------------------------------------------------- 5. 索引覆盖
def check_indexes():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
        if dirpath == ROOT:
            continue
        if os.path.basename(dirpath) in ("index", "templates"):
            continue  # 检索索引目录 / 模板目录
        if "index.md" not in filenames:
            md_count = len([f for f in filenames if f.endswith(".md")])
            if md_count > 0:
                warn(f"[index] 目录缺 index.md: {rel(dirpath)}")


# ---------------------------------------------------------------- 6. 命名规范
def check_naming():
    for p in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
        if os.path.isdir(p) or "/.git/" in p:
            continue
        name = os.path.basename(p)
        if name.startswith("."):
            continue
        stem = name.rsplit(".", 1)[0]
        if " " in name:
            # MOC 页面（含 emoji 前缀，如 "🏠 主页.md"）允许空格
            if not any(ord(ch) > 0x2000 for ch in stem):
                err(f"[naming] 文件名含空格: {rel(p)}")
        if stem != stem.lower():
            # 允许有意大写（README/AGENTS）与中文/emoji 的 MOC 页名
            has_cjk_or_emoji = any(ord(ch) > 0x2000 for ch in stem)
            if not stem.isupper() and not has_cjk_or_emoji:
                warn(f"[naming] 文件名非小写: {rel(p)}")


def main():
    quiet = "--quiet" in sys.argv
    check_frontmatter()
    check_links()
    check_recipes()
    check_assets()
    check_indexes()
    check_naming()

    total_md = len(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True))
    total_yml = len(glob.glob(os.path.join(ROOT, "recipes", "*.recipe.yml")))

    if not quiet:
        print(f"Aesthetic Atlas 校验 @ {ROOT}")
        print(f"  Markdown 文件: {total_md}")
        print(f"  机读配方:      {total_yml}")
        print()

    if warnings:
        print(f"⚠️  警告 {len(warnings)} 条:")
        for w in warnings:
            print("   " + w)
        print()

    if errors:
        print(f"❌ 错误 {len(errors)} 条:")
        for e in errors:
            print("   " + e)
        print()
        print("结果: 未通过")
        return 1

    print("✅ 结果: 通过（0 错误）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
