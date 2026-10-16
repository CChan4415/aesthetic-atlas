# 资产库变更日志

>  newest first；日期用 `YYYY-MM-DD`。

## 2026-10-17 · `tools/validate.py` 新增两条校验规则

### 规则 1：`check_escapes()` —— 转义污染
* 检测被反斜杠转义的 Markdown/YAML 语法：行首 `\---`、`\s*\- ` → 直接报 **error**。
* 动机：写入端会自动给 `---` / `-` / `_` 加反斜杠，导致 frontmatter 与列表结构静默失效；
  这类问题此前已发生过两次（`\---`、`\|`），靠事后人工发现必然再漏 → **必须让校验器兜底**。
* 检查前先过 `strip_code()`，避免把文档里的教学示例误判为污染。
* 顺带教训：只报 warning 的问题会被 `0 错误` 掩盖——**导致结构失效的问题应定为 error**。

### 规则 2：`check_material_refs()` —— 原料引用完整性
* `raw/**/_source.md` 的 `material:` 清单必须能在同目录找到真实文件，找不到即报错。

### 验证
* `tools/validate.py`：216 个 Markdown，**0 错误 0 警告**。
* 回归测试：临时还原错误版本 → 如期报出 6 条 error，确认规则真实生效。

## 2026-10-16 · 第十二阶段：首次跑通 raw → atlas → recipe 编译管道（Retro Game CG）

> **里程碑**：这是本库**首次真实执行 `guides/ingestion.md` 七步编译管道**——
> 原料不再是"计划中的占位"，而是真实喂入、抽帧、盘点、提取、合并、链接、沉淀。

### 原料入库
* 4 部视频原料（他人创作，仅作风格学习）：@natural water / @鴉鴉的幻覺 / @龙崎日舞 × 2
* `raw/videos/_source.md` 登记表：含作者署名、用途声明、覆盖维度盘点、与现有风格的关系判断
* `raw/videos/index.md` + `raw/index.md` 更新
* 抽帧：4 视频 × 6 帧（开头/15%/35%/55%/75%/92%），共 24 张入 `assets/raw/videos/<id>/`
* **视频原件不入 Git**（体积大、不可文本化），已在 .gitignore 排除

### 新增风格运动：Retro Game CG · 复古游戏 CG
* **[[retro-game-cg]]** — 1997–2006 年 PS1/PS2 世代游戏渲染美学
* **与 Y2K / Visual Kei 的根本区别**：介质是 **3D 渲染**而非真人摄影
* 视觉语法 7 条（低多边形是结构不是缺陷 / 贴图分辨率低 / vertex wobble / affine texture warping / 固定相机 / 简单光照 / 4:3 画幅）
* 下设 4 个子方向，首个落地：**Low-Poly JK Slice-of-Life**

### 新增原子元素（11 个）
* **grade**（渲染介质）：
  - [[low-poly-3d-render]] — PS1/PS2 实时渲染的三角面/低分辨率贴图/vertex wobble
  - [[ps2-fmv-grade]] — PS2 FMV 预渲染质感（介于低模与当代 3D 之间）
* **camera**：
  - [[security-camera-cctv]] — 监控高角度固定视角
  - [[third-person-game-camera]] — 第三人称游戏跟随视角
* **subject**：
  - [[lowpoly-jk-character]] — 低多边形 JK 角色原型
* **setting**：
  - [[school-corridor-cctv]] — 学校走廊（监控视角）
  - [[underground-passage-tiled]] — 瓷砖地下通道
  - [[school-cafeteria-3d]] — 学校食堂

### 扩展已有元素
* [[digital-overlays]] — 新增**监控 bounding box**、**双语字幕条**、**斜体标语**、**作者水印** 4 个子类
* [[anti-modern-digital]] — 新增「**B. 渲染介质锚定词**」章节，区分**摄影介质**与**渲染介质**两大类；
  补渲染介质专属负向词（`unreal engine 5, ray tracing, photorealistic, subsurface scattering...`）

### 新增配方
* [[ps2-lowpoly-jk-slice-of-life]] — **PS2 低多边形 JK 校园日常**（v1, draft）
  - 双 prompt（image + video）+ 两层负向词（内容层 + 渲染介质层）
  - 介质锚定词：`RENDERED ON A 2000s PS2 GAME CONSOLE, low-poly 3D, NOT a modern photorealistic 3D image`
  - 待出图验证

### 三个配方构成"三介质三极"
| 配方 | 介质 | 主体 | 气质 |
|---|---|---|---|
| Y2K 暖调 DV 千禧偶像 | 真人摄影（DV） | 偶像 | 暖、怀旧、生活化 |
| Visual Kei Kote-kei 冷黑 | 真人摄影（舞台） | 表演者 | 冷、锐利、戏剧化 |
| PS2 Low-Poly JK | **3D 渲染（PS2）** | 虚拟角色 | 孤独、青春、微压抑 |

### 验证
* `python3 tools/validate.py` — **0 错误 0 警告**（216 Markdown / 3 机读配方 / 180 概念页）
* `python3 tools/build_index.py` — 索引重建完成

### 待办（下一步）
- [ ] **出图验证 ps2-lowpoly-jk-slice-of-life 配方**（测试介质锚定词是否有效）
- [ ] 用户复核：风格边界（v3/v4 视频是 3D 动漫渲染而非纯低模，是否需要拆分子风格）
- [ ] 子风格页：`lowpoly-jk-slice-of-life` 待建独立子页（当前作为 retro-game-cg 的直接子方向）

---

## 2026-10-16 · 第十一阶段：Y2K 产物去重 + raw/videos 目录改名

### 修复：Y2K 配方产物 PNG 重复
* **问题**：`assets/recipes/y2k-warm-dv-idol/` 下两个 PNG 文件 MD5 完全一致——
  `v1-2026-10-12.png` 与 `v1-2026-10-12-jimeng.png` 是**同一张图**被存了两次。
* **真相**：recipe.yml 记录的是**两次独立生成**（不同尺寸 2364×1773 vs 1440×2560、不同平台），
  但磁盘上两份文件实际都是后者（1440×2560）。第一张图（CDN 那张 4:3）**本地副本从未真正落盘**。
* **修复**：
  - 删除错误的 `v1-2026-10-12.png`（它其实是 jimeng 那张的副本）
  - `recipe.yml` outputs[0] 的 `local_path` 改为 `null`，issues 追加 `local file lost; only CDN copy remains`
  - `recipe.md` 产物表第一行改为「⚠️ 本地文件丢失；仅有 CDN」
* **教训**：**保存产物时必须核对实际尺寸与声明是否一致**。两张图重名同尺寸时，
  简单的 `cp` 会用后者覆盖前者而无声无息。

### 修复：`raw/vidoes/` → `raw/videos/` 拼写
* 目录名拼写错误，且 `.gitignore` 已同步。

### 修复：`recipes/y2k-warm-dv-idol.recipe.yml` L1 注释错误
* 注释抄成了「Visual Kei · Kote-kei 冷黑肖像（完整版）」—— 改为正确的 Y2K 配方名。

### 新增：整改计划
* 工作区根目录新建 `WBS.md`，列出 5 阶段 24 项任务（含验收标准与时间估算）。
* 关键路径是第 2 阶段——用 `raw/videos/` 4 个 PS1/PS2 风格 3D 短片首次跑通编译管道。

### 验证
* `python3 tools/validate.py` — **0 错误 0 警告**。

---

## 2026-10-16 · 第十阶段：修复表格 wikilink 转义 + frontmatter

### 修复：表格内 wikilink 别名竖线未转义（126 处）
* **问题**：库内 `[[a|b]]` 出现在 Markdown 表格中时，`|` 被当作列分隔符，导致整行错位。
  例：`recipes/y2k-warm-dv-idol.md` 的 Locked Decisions 表（25 行）全部 9 列错位。
* **修复**：全库批量将表格内的 `[[a|b]]` 改为 `[[a\|b]]`（126 处），分布在 16 个文件：
  - `recipes/y2k-warm-dv-idol.md`（24 处，表格同时缺列已重写为 3 列）
  - `recipes/visual-kei-kote-cold-black.md`（14 处）
  - `🏠 主页.md`（22 处）、`🧱 元素图鉴.md`（14）、`🗺️ 风格系谱.md`（11）、`🎬 配方.md`（6）、`index.md`（9）、`guides/index.md`（8）
  - 5 个 `atlas/taxonomy/movements/*.md` 与 2 个 guides
* **同步修订规则**：
  - `rule.md` L85 反向修正："表格里**不要**转义竖线" → "**必须**转义竖线"
  - `AGENTS.md` §2 链接语法条款新增同样条目
* **教训**：Markdown 表格里 `|` 永远是分隔符，wikilink 别名必须 `\|`。validate.py 之前不查这个，需要靠人或新增 lint 规则。

### 修复：`recipes/y2k-warm-dv-idol.md` frontmatter 被 `\---` 转义
* 头部两处分隔符写成了 `\---`（带反斜杠），导致 frontmatter 完全失效。
  validate.py 此前一直报「缺少 frontmatter」警告，今天清零。

### 修复：`tools/validate.py` WIKI_RE 不识别 `\|`
* 旧正则 `[^\]\|#]+` 把 `\|` 当作普通字符读进 target，导致转义后的链接被误判为"无法解析"。
* 新正则 `((?:[^\]\|#\\]|\\.)+?)` 显式允许反斜杠转义序列，恢复正常解析。

### 验证
* `python3 tools/validate.py` — **0 错误 0 警告**（此前 1 警告 0 错误）。
* `python3 tools/build_index.py` — 重建 169 个概念页索引，13 个 type 分组。

---

## 2026-10-12 · 第二阶段：迁移 + 视觉系家族 + 结构性加固

### 迁移
* **迁移到主工作区**：库从 `~/workspace/doubao_workspace/aesthetic-atlas` 迁至
  `~/workspace/AIGC/aesthetic-atlas`（作为正式主库；原位置保留为历史快照）。
  迁移时 160 个 Markdown 文件完整保留，0 断链。

### 新增风格：Visual Kei 日系视觉系（风格家族，与 Y2K 平级）
* **创建家族根页** [[visual-kei|Visual Kei]]——
  含时代脉络（1980s 中→现在，5 个时期）、**视觉语法 7 条**、核心母题。
* **创建四个分支**：
  [[visual-kei-kote-kei|Kote-kei 古典系]]（黑西装/白妆/尖刺发）、
  [[visual-kei-angura|Angura 暗黑哥特系]]（蕾丝/束腰/和洋折衷）、
  [[visual-kei-oshare-kei|Oshare-kei 御洒落系]]（彩发/糖果色）、
  [[visual-kei-kirakira|Kirakira 华丽系]]（亮片/水钻/奢华）。
* **建为"风格家族"而非单一子风格**——依据是四分支共享同一套视觉语法
  （面部即画布、非日常发型、雌雄莫辨、造型即叙事）。

### 新增风格：Y2K 亚文化补充
* [[y2k-cyber-goth|Cyber Goth 赛博哥特]] — 全黑 PVC/护目镜/工业亚文化
* [[y2k-mcbling|McBling 奢华浮夸]] — 水钻皮草/Logo 狂热/炫富美学
* [[y2k-harajuku-shibuya|里原宿 / 涩谷系]] — Decora/Gyaru/日系街头（含 4 变体）

### 新增原子元素（14 个）
* **发型**：尖刺立发、遮眼刘海
* **妆容**：白妆、上挑眼线、深色烟熏眼、泪袋妆、暗色唇
* **材质**：蕾丝与网纱、皮革与金属件、缎面与天鹅绒
* **服装**：黑色修身西装
* **光影**：强单点光
* **质感**：高对比戏剧质感
* **配色**：视觉系·黑白冷调
* **主体**：性别模糊表演者（视觉系核心原型）
* **场景**：空旷舞台与暗厅
* **动态**：舞台表演动态（视频用）

### 新增配方
* [[visual-kei-kote-cold-black|Visual Kei · Kote-kei 冷黑肖像]] — 第二个完整配方（v1）
  含 image/video prompt、负向词、可调参数；与 Y2K 暖调配方构成"冷/暖两极"。

### 结构性加固（补 OKF 的三个缺口）
* **新增协议** [[recipe-schema|配方 schema 规范]] ——
  配方**双表示**（`.md` 人读 + `.recipe.yml` 机读），含权威性规则、字段定义、校验规则、`taste` 主观字段。
  两个配方均已补 `.recipe.yml`。
* **新增协议** [[new-style-pack|新建风格包规范]] ——
  填补"如何新建风格运动/子风格/家族"的空白，含 checklist 与质量门槛。
* **新增协议** [[image-assets|图像资产层规范]] ——
  建立 `assets/` 本地图像层，解决 CDN 依赖风险；含命名、绑定、参数快照约定。
* **新增工具** `tools/validate.py` ——
  一致性校验器：frontmatter/断链/配方引用/资产/索引/命名。当前 **0 错误 0 警告**。
* **新增工具** `tools/build_index.py` ——
  生成 [[compact|`index/compact.md`]] 与 `index/graph.json`（含出链/入链），
  解决"162 个概念页需逐层读 index"的检索退化问题。

### 修复
* 修正新增页面中的跨维度相对链接（movement ↔ 元素页需 `../taxonomy/movements/`，
  深层目录需额外上溯一级）；迁移后断链从 87 条降至 0。
* 根 `index.md` 补 `type` 字段（OKF 唯一必填）。
* 补 `references/eras/`、`atlas/subject/character-archetypes/` 的 `index.md`。
* 校验器增加**代码块剥离**，避免把文档示例误判为真实链接。

### 验证
* **一致性**：192 个 Markdown（162 个概念页），`tools/validate.py` 通过，**0 错误 0 警告**。
* **检索索引**：162 个概念页已索引，9 个 type 分组，关系图含出链/入链。
* **配方**：2 个配方双表示配对完整，引用全部有效。

---

## 2026-10-12 · 第一阶段：初始化
* **初始化**：建立 OKF v0.2 知识包骨架（`atlas/ recipes/ references/ raw/ guides/`）。
* **创建**：五个 agent 协议——风格探索、图片生成、视频生成、原料编译、维护规范。
* **创建**：Y2K 核心包（四大子风格、人物/发型/妆容/服装/配饰/场景/色彩/材质/光影/镜头/质感/动态/声音/情绪全维度原子元素）。
* **创建**：首个完整配方 [[y2k-warm-dv-idol|Y2K · 暖调 DV 千禧偶像]]。
* **产出**：按配方生成暖调 DV 偶像静帧 v1（2364×1773，4:3），写入画布并 `+get` 回读确认。
* **验证**：OKF v0.2 一致性检查通过——160 个 Markdown（133 个概念文件），0 个规范错误、0 个断链。

---

## 2026-10-12 · 第三阶段：用户出图反馈 → 修复现代感问题

### 用户实测产出
* 用户以**即梦 Seedream 5.0 Lite**生成两配方图片，落地到 `assets/recipes/`。
* **Kote-kei 冷黑肖像**：✅ 方向达成（白妆/尖刺发/黑西装/冷调/性别模糊均对）。
* **Y2K 暖调 DV 偶像**：❌ **失败**——用户评价"太现实了，没有 2000s 复古质感"。

### 诊断出的失败根因（4 条）
1. **质感只写在 prompt 末尾一处**，被前 200 词主体描述淹没 → 模型几乎忽略
2. **负向词只有内容层**（现代物品），缺**介质层**（HDR/DSLR/磨皮/降噪）
3. **未声明拍摄介质**（没写 "shot on 2000s DV camcorder"）
4. **画幅只写在 prompt 文字里**，被平台忽略（要 4:3，输出 9:16）

### 修复
* **新增元素页** [[anti-modern-digital|去现代数码感]]——
  负向控制元素，含：介质层负向词库、介质锚定写法、强度分级、**完整失败案例记录**。
  明确区分"内容层（拍什么）"与"介质层（怎么拍的）"。
* **重写 Y2K 配方 prompt（v1→v2）**：
  - 介质锚定句**前置到第 5 词**（原在末尾）
  - 显式写入 `NOT a modern digital photograph`
  - 皮肤改为 `visible powder foundation texture (not airbrushed)`（对抗磨皮）
  - 打光 `touch of flash` → `Harsh on-camera direct flash, slightly overexposed`
  - 正向补 `(NO modern smartphone)`
  - 负向词扩为**两层结构**，介质层覆盖 7/7 关键项
* **重写图片生成规范**（guides/image-generation.md）：
  - 负向词库分内容层/介质层，并给出**按方向取舍表**（怀旧必加、当代戏剧不要加）
  - 新增「介质锚定 Medium Anchoring」段（5 类介质的正向写法）
  - 新增画幅警告：**必须用平台原生参数**，勿只写 prompt
  - 新增「失败归档」机制说明
* **配方产物记录**：两个配方均回填真实产物、评分、verdict、问题清单；
  `.recipe.yml` 的 `outputs` 补 `rating`/`verdict`/`issues` 字段，Y2K 配方 version → 2。

### 关键区分（避免过度修正）
* **Y2K 需要**「去现代数码感」；**Visual Kei Kote-kei 不需要**——
  后者要的是"当代戏剧高清"，加了做旧会削弱锐利感。已在两处显式标注。

### 验证
* `tools/validate.py`：194 个 Markdown、163 个概念页，**0 错误**。
* 结构自检：Y2K v2 prompt 中介质锚定位于**第 5 词**（原末尾）；
  负向词介质层覆盖 7/7 关键项。

---

## 2026-10-12 · 第五阶段：双库架构确立 + 孤儿页修复

### 双库架构（确立）
* 明确 **`aesthetic-atlas`（A 库）= 事实源 SSOT**，`aesthetic-vault`（B 库）= Obsidian 前端。
* **关键依据**：`[[wikilink]]` 是 Obsidian 私有扩展，非标准 Markdown，
  在 GitHub/VS Code/Typora/pandoc 中退化为纯文本，**不符合 OKF 规范**；
  而 Obsidian **能**渲染标准 Markdown 链接——即标准链接是超集。
  → 故两库并存，A 为源、B 为视图，**不可合并**。
* 新增 **`obsidian-setup/sync.py`**：`a2b` / `b2a` / `check` 三命令，
  保护 B 库独有的 `.obsidian/`、MOC 页、`templates/`。首次 `check` 显示仅 2 处分叉，
  `a2b` 后**两库完全一致**。

### 修复孤儿页：57 → 0
* **修复分析器 bug（主因）**：`tools/build_index.py` 此前把所有 `index.md`
  整个跳过，导致**目录索引页的出链不计入入链统计**——
  57 个"孤儿页"中绝大多数其实**被各自的 index.md 正常引用**，只是统计不到。
  已改为：index 页不作概念条目收录，但其出链计入 `linked_from`。
* **补齐真实缺失的引用**：在 [[y2k|Y2K 风格页]] 新增
  「子风格专属元素 / 场景道具 / 视频动态 / 音乐与参考」四个索引段落，
  将此前无任何页面引用的 41 个元素按归属关系登记（motion 14、setting 8、
  references 8、hair 4、wardrobe 4 等）。
* **新增主体链接**：[[visual-kei|Visual Kei]] 根页
  现引用核心主体原型 [[androgynous-performer|性别模糊表演者]]。
* **修复链接深度 bug**：从 `atlas/taxonomy/movements/` 出发的链接需 `../../`，
  指向库根 `references/` 需 `../../../`（首次提交时写错，断链 20+ 条，已修正）。
* **结果**：完全无入链 0 个；仅被 index 页引用 2 个（`guides/ingestion.md`、
  `guides/style-exploration.md`，属协议枢纽页，合理）。

### 验证
* `tools/validate.py`：194 个 Markdown，**0 错误**。
* 入链统计恢复正常：Kote-kei 18 条居首，白妆 12 条——图谱中心性符合预期。

---

## 2026-10-12 · 第六阶段：合并为单库（用户裁定）

### 决策依据（第一性原理复核）
用户质疑"Obsidian 不能移植"的结论。复核后**用户正确，此前判断有误**：

* **错误论断**：wikilink 离开 Obsidian 就失去价值 → 故此必须保留双库。
* **事实**：agent **不"点击"链接**，它读文件内容后用路径/名称访问文件。
  对比解析难度：
  - `[白妆](../../atlas/makeup/white-foundation.md)` —— 需先知道**当前文件所在目录**才能解析 `../..`，**位置相关**
  - `[[white-foundation|白妆]]` —— 按 basename 全局查找，**路径无关**
  → **wikilink 对 agent 更鲁棒，而非更弱。**
* **唯一真实代价**：GitHub 等平台不渲染 wikilink 为可点击链接。
  但这是**渲染层**问题，不影响内容、结构、agent 使用。

### 执行
* 旧 OKF 库归档为 `aesthetic-atlas.okf-backup/`（未删除，可回退）。
* Obsidian 库重命名为 **`aesthetic-atlas/`（唯一主库）**。
* 工作区 `AGENTS.md` 重写：说明单库架构、可移植性、agent 使用方式。
* 库内 `📘 Obsidian 使用指南.md` 更新：删除"双库分叉"章节，改为说明
  **Obsidian 是人的可选项，不是库的依赖**。

### 修复（可移植性实测暴露的真实缺陷）
模拟"复制到新机器 + 删除 `.obsidian/`"，实测发现 **113 个链接无法解析**。逐项修复：
* **图片被误转成 wikilink**：`[v1-2026-10-12.png](../assets/…)` → `[[v1-2026-10-12]]`（丢失路径）。
  已改为 Obsidian 附件语法 `![[v1-2026-10-12.png]]`，共 3 处。
* **非笔记文件被误转**：`tools/validate.py`、`index/graph.json`、`.recipe.yml`
  被转成 wikilink 后无法解析。已改为行内代码引用，共 6 处。
* **校验器补规则**：Obsidian 附件链接按 **basename 全局解析**（可在库内任意位置），
  此前校验器不认，导致误报。

### 验证（可移植性实测）
```
复制到 /tmp/portability-test/ + 删除 .obsidian/ + 全新路径：
  ① tools/validate.py      → 0 错误
  ② 824 个 wikilink 解析    → 0 失败
  ③ tools/build_index.py    → 169 概念页，出/入链完整
  ④ 配方 prompt 提取         → 185 词，正常
  → 无 Obsidian 全功能可用 ✅
```

### 当前状态
* 单库 `aesthetic-atlas/`：203 个 Markdown，0 错误，0 孤儿页，824 wikilink 全通。
* 工作区 `AGENTS.md` + 库内 `AGENTS.md` 均已更新为单库架构。

---

## 2026-10-12 · 第七阶段：整理工作区（参考另一会话建议）

### 背景
参考另一个会话（`obsidian和llm wiki哪个更好用？`）关于 Obsidian 接入 agent 的建议，
**逐条核实后**采纳其中两条真实有价值的改进，其余已在做或不需要。

### 核实结果
| 建议 | 核实结论 | 处理 |
|---|---|---|
| Agent 直接读写 vault 文件夹 | ✅ 已实现（本库设计如此，`build_index.py` 纯 Python 解析） | 无需改动 |
| 使用 `[[双向链接]]` | ✅ 已实现（839 个 wikilink） | 无需改动 |
| `sources/` 只读区 | ✅ 已有 `raw/` 承担该角色 | 无需改动 |
| **`inbox/` 暂存区** | ⚠️ **真实缺口**——此前丢原料必须先想清楚归哪类 | **已采纳** |
| **版本控制/可回滚** | 🔴 **真实缺口**——此前零回滚能力 | **已采纳** |
| Obsidian 官方 CLI | ✅ 核实存在（`/Applications/Obsidian.app/Contents/MacOS/obsidian-cli`） | 未启用（见下） |

### 采纳 1：`raw/inbox/` 暂存区
* 新建 `raw/inbox/`；`raw/index.md` 补充说明；`guides/ingestion.md` 新增 **Step 0：inbox 归位**。
* 规则：拿不准分类就丢 `inbox/`，INGEST 时 agent 判断类型 → 移动到目标目录 → 建 `_source.md` → 登记。
  **移动而非复制**，处理完 `inbox/` 应为空。
* 目的：降低"投喂原料"的心理成本。

### 采纳 2：启用 Git 版本控制
* 此前**无任何版本控制**——改坏无法回滚，是最大的运维缺口。
* `git init` + 首次提交（220 文件），`.gitignore` 排除：
  - 生成物：`index/graph.json`、`index/compact.md`（可重建）
  - Obsidian 私有状态：`.obsidian/workspace.json`（每台机器不同）
  - 系统噪音：`.DS_Store`
* **实测验证回滚可用**：改坏文件 → `git status` 可见 → `git checkout --` 恢复成功。
* 库内 `AGENTS.md` 新增「工具与版本控制」段，含常用命令与"人机勿同时编辑同一文件"提醒。

### 未采纳：Obsidian 官方 CLI
CLI 二进制**确实存在**（建议中该条属实），但**本库不需要**：
* 它要求 Obsidian 应用常驻运行，而本库的设计目标是**不依赖 Obsidian**（已实测删除 `.obsidian/` 后全功能可用）。
* CLI 主要价值是搜索、每日笔记、未解析链接检查——这些我们已有等价实现
  （`build_index.py` 检索索引、`validate.py` 链接校验），且**不需要运行 GUI**。
* 若将来需要"在 Obsidian 内操作每日笔记"之类能力，可再启用。

### 验证
* `tools/validate.py`：203 个 Markdown，**0 错误**。
* 索引重建正常；Git 已提交，回滚实测通过。

---

## 2026-10-12 · 第八阶段：清理归档 + 关联 GitHub

### 删除归档
* 删除 `aesthetic-atlas.okf-backup/`（13MB）——删除前再次核实**独有文件数 = 0**，
  且主库已有 Git 兜底。

### 关联 GitHub 远程
* 远程：**https://github.com/CChan4415/aesthetic-atlas**
* SSH 认证核实：`Hi CChan4415! You've successfully authenticated` ✅
* 本地调整：
  - 作者 `cc <cc@local>` → `CChan4415 <CChan4415@users.noreply.github.com>`（重写历史，使其关联 GitHub 账号）
  - 分支 `master` → `main`（GitHub 默认）
  - `git remote add origin` + `git push -u origin main`（220 文件）
* 已验证：本地 HEAD == origin/main。

### 修复 clone 后断链（实测发现）
* 首次推送后**真实克隆测试**发现：`index/compact.md` 被 `.gitignore` 排除，
  但被 **5 个文档**用 `[[compact]]` 引用 → **新机器 clone 后立即断链**。
* 修复：`index/` 产物改为**入库**（它可随时用 `tools/build_index.py` 重建，入库无副作用）。
* 重新克隆验证：**222 文件、203 Markdown、0 错误、824 wikilink 全部解析** ✅

### 教训
"本地校验通过"≠"克隆后可用"。**生成物与引用它的文档必须一起入库**，
否则库在别人机器上是坏的。这次是靠真实 clone 测试才发现的。

---

## 2026-10-13 · 第九阶段：添加 README + 记录视频编译计划

### 添加 README.md
* 新增 [README.md](README.md) —— GitHub 首页入口，30 个链接全部有效。
* **链接语法差异**：README 用**标准 Markdown 链接**（`[文字](path.md)`），
  而非库内通用的 wikilink——因为 **GitHub 不渲染 `[[ ]]`**，
  若用 wikilink 则 README 在 GitHub 上全是纯文本。这是刻意的例外。
* 内容：快速开始（人/agent 双路径）、库组织、收录风格、可用配方、
  设计取舍（为何 wikilink / 为何一概念一文件 / 为何记录失败）、**已知短板诚实清单**。

### 记录视频编译计划
* 用户预告：**将提供一个视频资源，要求整理风格并维护进库**。
* 在 `AGENTS.md` 新增 **§7.6 待办：视频资源编译**，含 8 步流程与 3 项待确认事项。
* 关键提醒（已写入协议）：
  - **视频的特有信息在"运动"中**，抽帧只是图片 → 重点是 `atlas/motion/` 补充
  - 介质判断（DV/胶片/数码）→ `atlas/grade/`
  - 音频维度（若有音乐风格信息）→ `atlas/audio/`
  - 他人视频需标注来源与用途

### 用户反馈：视觉系风格精准度
* 用户实测 Kote-kei 冷黑肖像：**方向对，但"还不是我想要的风格"**。
* Y2K v2 验证**暂缓**（用户指示）。
* 已更新 `AGENTS.md` 已知问题表：将"Y2K v2 未验证"替换为
  "视觉系风格精准度待收敛"，等待参考视频提供后处理。

### 验证
* `tools/validate.py`：204 个 Markdown，**0 错误**。
* README 链接自检：30 个有效，0 断链。
