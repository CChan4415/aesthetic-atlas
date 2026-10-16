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
   - **表格内必须转义竖线**：写 `[[white-foundation\|白妆]]`，否则 `|` 会被 Markdown 当作列分隔符导致整行错位
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

| 问题                | 严重度  | 说明                           |
| ----------------- | ---- | ---------------------------- |
| 77/128 元素页从未被配方使用 | 🔴 高 | "写了"≠"有用"，未经验证               |
| `raw/` 全空         | 🔴 高 | **编译管道从未真实执行过**              |
| 元素页几乎无示例图         | 🔴 高 | 审美资产却"看不见"                   |
| 视觉系风格精准度          | 🟡 中 | 用户实测：方向对但"还不是想要的风格"，待用参考视频收敛 |
| 视觉系 3/4 分支无配方     | 🟡 中 | 图鉴建了但不可直接用                   |

## 7. 工具与版本控制

```bash
python3 tools/validate.py       # 链接/frontmatter/配方引用/资产/命名
python3 tools/build_index.py    # 生成 index/compact.md 与 graph.json
```

校验器**只查结构不查内容质量**——它查不出"质感描述是否会生效"。**别把它当质量保证。**

### 版本控制（Git + GitHub）

本库是 Git 仓库，远程同步到 \*\*<https://github.com/CChan4415/aesthetic-atlas\*\*（私有）。>  
**改动前后建议提交**，这是唯一的回滚手段：

```bash
git status                  # 看改了什么
git diff                    # 看具体改动
git add -A && git commit -m "说明改了什么"
git push                    # 同步到 GitHub
git checkout -- <文件>       # 撤销单个文件的改动
```

**在别的机器上使用**：

```bash
git clone git@github.com:CChan4415/aesthetic-atlas.git
# 无需任何额外安装即可使用（含校验与索引工具）
```

**为什么必须有**：库里全是审美决策，改错一次可能损失数月积累。

`.gitignore` 的取舍（**曾经踩坑，勿轻易改**）：

- ✅ `index/compact.md`、`index/graph.json` **入库** —— 它们被多篇文档用 `[[compact]]` 引用，  
  若排除则**新机器 clone 后立即断链**（实测过）。它们随时可用 `tools/build_index.py` 重建，入库无副作用。
- ❌ `.obsidian/workspace.json` 排除 —— 每台机器的窗口布局状态，含噪音且易冲突。
- ❌ `.DS_Store` 排除 —— 系统噪音。

> **通用教训**：「本地校验通过」≠「克隆后可用」。  
> 生成物若被文档引用，就必须和引用它的文档一起入库。

### 人机同时编辑

人和 agent **不要同时改同一个文件**。改完先提交，再让对方接手——  
否则 git 会报冲突，需要手动合并 markdown。

## 7.5 raw/inbox 暂存区

拿不准原料该归到哪个子目录时，**直接丢 `raw/inbox/`**。  
不需要先想清楚分类——INGEST 时 agent 会判断归属并登记。  
目的是降低"投喂原料"的心理成本。

## 7.6 待办：视频资源编译（用户预告）

> **用户将提供一个视频资源，要求：整理其风格并维护进本库。**

计划流程（等资源到位后执行）：

1. **接收**：视频放入 `raw/inbox/`（用户不必先想好归类）
2. **归位**：按内容判断 → `raw/articles/` 或新建 `raw/videos/`，建 `_source.md` 登记
3. **解析**：抽帧（建议按镜头切分，每镜头 3–5 帧代表帧）+ 提取音频特征（若有音乐风格信息）
   - 工具：`ffmpeg`（本机未见，需确认）或用户提供截图
4. **盘点**：逐帧归纳覆盖的维度（人物/发型/妆容/服装/配饰/场景/配色/材质/光影/镜头/质感/动态/情绪/声音）
5. **提取**：每个可复用元素 → 候选原子概念页；**视频特有维度重点补充**：
   - `atlas/motion/` 运镜与动作（这是视频相对图片的最大信息增量）
   - `atlas/grade/` 画面质感与介质（是否是 DV / 胶片 / 数码）
   - `atlas/audio/` 音乐风格与音效（若有）
6. **去重合并**：与 `atlas/` 现有概念比对，优先**补充**而非新建
7. **沉淀配方**：若整体风格完整可复用 → 写 `recipes/<id>.md` + `.recipe.yml`
8. **登记**：更新各 `index.md`、根 `log.md`、`index/` 索引

**注意**：

- 视频抽帧是**图片**，但风格信息在**运动**中 —— 不要只当静帧处理
- 若视频是他人的（MV/影视），在 `_source.md` 与 `sources` 字段**明确标注来源与用途**
- 编译产物写入 `atlas/`，**不在 `raw/` 内改写**

### 待确认

- [ ] 视频来源与类型（自拍素材？MV？影视？参考片？）
- [ ] 期望产出：只要元素图鉴，还是要一个完整配方？
- [ ] 是否有音频维度需求（音乐风格/音效）

## 8. 参考

- [[🏠 主页]] · [[🗺️ 风格系谱]] · [[🎬 配方]] · [[🧱 元素图鉴]]
- [[guides/index|协议总览]] · [[log|变更日志]] · [[compact|检索索引]]
- OKF 规范：<https://github.com/GoogleCloudPlatform/open-knowledge-format>
