---
type: guide
title: 📘 Obsidian 使用指南
description: 本 vault 的人类使用说明——打开方式、导航、图谱配色、编辑约定、模板与维护命令。
tags: [guide, obsidian, moc]
status: stable
created: 2026-10-12
---

# 📘 Obsidian 使用指南

> 这是本库的**人类使用说明**。agent 请读 [[AGENTS|Agent 手册]]（或工作区的 `AGENTS.md`）。

## 🚀 第一次打开

1. 启动 Obsidian → 点 **"Open folder as vault"**
2. 选择本库文件夹（`aesthetic-atlas/`，路径随你放在哪）
3. 信任作者 → 打开后会自动显示 [[🏠 主页]]

> 若想设为默认库：Obsidian 设置 → 关于 → 切换库。

## 🗺️ 导航方式

| 想做什么 | 怎么做 |
|---|---|
| **从头开始逛** | 打开 [[🏠 主页]]（可设为启动页） |
| **找风格** | [[🗺️ 风格系谱]] — 按家族分组 |
| **找配方** | [[🎬 配方]] — 含状态看板与评分 |
| **找元素** | [[🧱 元素图鉴]] — 14 维度入口 |
| **搜关键词** | `Cmd + O`（快速切换）或 `Cmd + Shift + F`（全文搜索） |
| **看关系网** | `Cmd + G` — 图谱视图，**已配色分组** |
| **看反向链接** | 右侧边栏「Backlinks」面板 |
| **按标签找** | 右侧「Tags」面板，或用 `tag:#visual-kei` 搜索 |

## 🎨 图谱视图配色（已配置）

按 `Cmd + G` 打开后，节点已按层级着色：

- 🟠 **橙红** = 风格运动/子风格（`atlas/taxonomy/movements`）
- 🟡 **金黄** = 配方（`recipes`）
- 🔵 **蓝** = 质感/光影/配色（`grade` `lighting` `color`）
- 🟣 **紫粉** = 妆容/发型（`makeup` `hair`）
- 🟢 **绿** = agent 协议（`guides`）
- 🟤 **棕** = 参考资料（`references`）

调整：图谱设置面板 → Groups（颜色分组）可自行改。

## ✍️ 编辑约定

### 链接
- **一律用 `[[wikilink]]`**，不要写 `[文字](路径.md)`
- 显示不同文字：`[[white-foundation|白妆]]`
- `index.md` 有 29 个重名 → **必须写全路径**：`[[atlas/hair/index]]`
- 已有 919 个 wikilink 全部可解析 ✅

### Frontmatter（务必保留）
每个概念页都有 YAML frontmatter，字段含义：

| 字段 | 含义 |
|---|---|
| `type` | OKF 唯一必填字段：`Visual Element` / `Style Recipe` / `Guide` 等 |
| `title` / `description` | 中文标题与一句话说明 |
| `tags` | 标签，用于标签面板筛选 |
| `status` | `draft` → `stable` → `deprecated` |
| `generated` | 谁在何时产出（`by` / `at`）|
| `verified` | 人工审阅记录（有则代表已复核）|

### 标签体系
- 风格：`#visual-kei` `#y2k` `#kote-kei`
- 维度：`#hair` `#makeup` `#material` `#grade` `#motion`
- 类型：`#recipe` `#guide` `#moc` `#reference`

## 🧩 模板

`templates/` 下有三个模板（需启用 Templates 插件，已配置好）：

- `元素页模板.md` — 新建原子元素
- `子风格模板.md` — 新建子风格
- `配方模板.md` — 新建配方

插入方式：`Cmd + P` → "Insert template"。

## 🛠️ 维护命令

在 vault 根目录运行：

```bash
python3 tools/validate.py       # 校验：链接/frontmatter/配方引用/命名
python3 tools/build_index.py    # 重建检索索引 index/
```

**改完必跑**，0 错误才算完成。

## ⚠️ 重要说明

### 这个库需要 Obsidian 吗？
**不需要。** 它就是一个**普通文件夹**（纯 Markdown + YAML），
Obsidian 只是**人的可选项**——用来获得图谱视图、双链面板、标签筛选。

- **Agent 使用**：直接读文件夹即可，无需 Obsidian（链接是路径无关的 `[[basename]]`）
- **复制到别的机器**：整个目录拷过去就能用，无绝对路径、无数据库、无二进制依赖
- **人使用**：推荐用 Obsidian 打开（体验最好），但 VS Code / Typora 等也能编辑

**唯一的注意点**：`[[wikilink]]` 是 Obsidian 语法，
在 GitHub 上浏览时会显示成纯文本（不渲染为可点击链接）——但**内容与文件结构完全不受影响**。

### 图片
配方产物在 `assets/recipes/`，用 Obsidian 附件语法 `![[文件名.png]]` 引用。
新图请存到 `assets/recipes/<配方id>/`。

### 已知短板（诚实列表）
- **77/128 元素页从未被配方使用** —— "写了"不等于"有用"
- **元素页几乎没有示例图** —— 审美资产却"看不见"
- **`raw/` 是空的** —— 编译管道从未真实执行过
- **Y2K 配方 v2 未验证** —— 修复是结构性的，尚未重新出图

> 详见 [[AGENTS]] 第 6 节。
