# 审美资产库 · Agent 操作手册

> 本文件是**接入本库的 agent 的唯一入口**。读完本页再动手。  
> 人类用户：日常浏览请从 [[🏠 主页]] 开始。

## 0. 一分钟理解这个库

```
原子元素 (atlas/)  ──组合──▶  子风格 (atlas/taxonomy/movements/)  ──锁定──▶  配方 (recipes/)
    积木                        风格蓝图                              可直接出图
```

- **`atlas/`**：163 个概念页，14 个维度（发型/妆容/材质/光影/质感/动态/情绪…）
- **`recipes/`**：2 个完整配方，每个 = `.md`（人读 + prompt）+ `.recipe.yml`（机读结构）
- **`raw/`**：只读原料区（书/杂志/扫描件），待编译进 `atlas/`
- **`guides/`**：8 个行为协议（探索/生成/编译/维护/新建风格/配方 schema/图像资产）

**当前收录**：Visual Kei 日系视觉系（家族，4 分支）、Y2K 千禧年（7 子风格）。

## 1. 五种任务的入口

| 用户说         | 你该读                                         | 做什么                      |
| ----------- | ------------------------------------------- | ------------------------ |
| "想要某种风格/感觉" | [[style-exploration]]                       | 按协议提问收敛 → 组装 → 出图 → 沉淀配方 |
| "直接出图/出视频"  | [[image-generation]] + [[video-generation]] | 选配方 → 取 prompt → 出图      |
| "编译这本书/杂志"  | [[ingestion]]                               | 走七步编译管道                  |
| "加个新元素/风格"  | [[maintenance]] + [[new-style-pack]]        | 按 checklist 建，更新索引与日志    |
| "帮我找 XX"    | [[compact]]                                 | 检索索引定位 → 下钻              |

## 2. 铁律（违反即视为未完成）

1. **链接语法**：一律用 `[[文件名]]` wikilink（路径无关，**不需要 Obsidian 也能解析**）。
   - 普通文件：`[[white-foundation]]`（Obsidian 自动解析）
   - **`index.md` 重名**：必须写全路径 `[[atlas/hair/index]]`
   - 带显示文字：`[[white-foundation|白妆]]`
   - `#` 开头是标签不是链接，别混用
2. **改动后必须跑校验**：
   ```bash
   python3 tools/validate.py        # 0 错误才算完成
   python3 tools/build_index.py     # 若增删了概念页
   ```
3. **任何写入后更新**：对应目录的 `index.md` + 根 [[log|log.md]]
4. **不编造 `sources`**；未核实内容标 `status: draft`
5. **`raw/` 只读**，永不修改原件

## 3. 正文章节标准（照抄结构）

### 原子元素页（`atlas/<维度>/*.md`）

```markdown
---
type: Visual Element
title: 中文名（English Name）
description: 一句话
tags: [y2k, <维度>]
status: stable
generated: { by: "agent:<name>", at: "YYYY-MM-DDTHH:mm:ss+08:00" }
---

# 定义 Definition
# 视觉特征 Visual Cues
## Prompt Keywords     ← 英文词组，逗号分隔，必含
# 变体 Variants
# 适用风格 Applies To
# 搭配建议 Pairs With
# 易混 / 反例 Not To Confuse   ← 表格，跨风格边界
# 生成提示 / 常见失败          ← 实战经验，最有价值
# 来源 Sources
```

### 配方（`recipes/<id>.md` + `<id>.recipe.yml`）

双表示规范见 [[recipe-schema]]：

- `.md` 里 **prompt 文本以此为准**
- `.yml` 里 **结构与引用以此为准**
- `locked`（风格签名）/ `tunable`（可替换）
- `taste` 字段：`affinity`(1-5) + `confidence`(low/med/high) — 表达**用户主观偏好**

## 4. 出图时必须遵守（血泪教训）

> [!failure] 真实失败案例（2026-10-12）  
> Y2K 配方按 prompt 出图，结果**完全没有年代感**，看起来是当代高清照片。  
> 四个根因：质感写在末尾被淹没 / 负向词只有内容层 / 没声明拍摄介质 / 画幅只写在文字里。

**做旧/年代风格时**（Y2K、胶片、DV）：

1. **介质锚定句放最前面**：`SHOT ON A 2000s CONSUMER DV CAMCORDER, NOT a modern digital photograph`
2. **负向词两层**：内容层（现代物品）+ **介质层**（`HDR, DSLR, flawless skin, denoised, bokeh, 8k`）
3. **质感强度写明**（轻/中/重）——只写 `VHS grain` 模型取最保守值
4. **画幅用平台原生参数**，不要只写在 prompt 里（实测会被忽略）
5. 详见 [[anti-modern-digital|去现代数码感]]

**做当代戏剧风格时**（视觉系 Kote-kei）：

- **不要**加介质层负向词——它要的就是锐利高清。

## 5. 出图后的回填（强制）

生成结果**必须**回填到配方的「# 产物记录 Outputs」表 + `.recipe.yml` 的 `outputs`：

```yaml
outputs:
  - date: 2026-10-12
    version: v1
    model: "jimeng seedream-5.0-lite"
    dimensions: "1440x2560"
    aspect: "9:16"
    local_path: "assets/recipes/<id>/v1-2026-10-12.png"
    rating: 2                 # 1-5
    verdict: fail             # pass | partial | fail
    issues: ["no retro texture", "wrong aspect ratio"]
```

**图片必须落本地 `assets/`**，不要只留 CDN 链接（会失效）。  
**失败也要记录**——这是本库的复利机制。

## 6. 当前已知问题（别当成已完成）

| 问题                | 严重度  | 说明              |
| ----------------- | ---- | --------------- |
| 77/128 元素页从未被配方使用 | 🔴 高 | "写了"≠"有用"，未经验证  |
| `raw/` 全空         | 🔴 高 | **编译管道从未真实执行过** |
| 元素页几乎无示例图         | 🔴 高 | 审美资产却"看不见"      |
| Y2K v2 prompt 未验证 | 🔴 高 | 修复是结构性的，未经出图验证  |
| 视觉系 3/4 分支无配方     | 🟡 中 | 图鉴建了但不可直接用      |

## 7. 工具与版本控制

```bash
python3 tools/validate.py       # 链接/frontmatter/配方引用/资产/命名
python3 tools/build_index.py    # 生成 index/compact.md 与 graph.json
```

校验器**只查结构不查内容质量**——它查不出"质感描述是否会生效"。**别把它当质量保证。**

### 版本控制（本库已启用 Git）

本库是 Git 仓库。**改动前后建议提交**，这是唯一的回滚手段：

```bash
git status                  # 看改了什么
git diff                    # 看具体改动
git add -A && git commit -m "说明改了什么"
git checkout -- <文件>       # 撤销单个文件的改动
```

**为什么必须有**：库里全是审美决策，改错一次可能损失数月积累。
`.gitignore` 已排除生成物（`index/graph.json`、`index/compact.md`）与
Obsidian 私有状态（`.obsidian/workspace.json`），这些可重建或不该共享。

### 人机同时编辑
人和 agent **不要同时改同一个文件**。改完先提交，再让对方接手——
否则 git 会报冲突，需要手动合并 markdown。

## 7.5 raw/inbox 暂存区

拿不准原料该归到哪个子目录时，**直接丢 `raw/inbox/`**。
不需要先想清楚分类——INGEST 时 agent 会判断归属并登记。
目的是降低"投喂原料"的心理成本。

## 8. 参考

- [[🏠 主页]] · [[🗺️ 风格系谱]] · [[🎬 配方]] · [[🧱 元素图鉴]]
- [[guides/index|协议总览]] · [[log|变更日志]] · [[compact|检索索引]]
- OKF 规范：<https://github.com/GoogleCloudPlatform/open-knowledge-format>
