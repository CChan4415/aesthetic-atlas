# Aesthetic Atlas · 审美图鉴

> 个人视觉风格资产库。沉淀、组合、复用图片与视频创作的**审美决策**，
> 让接入的 AI agent 能与你共同探索风格、编译外部书籍杂志、调用现成风格配方。

**这不是一堆参考图。** 它把审美拆成可组合的原子元素，组装成子风格，锁定为可直接出图/出视频的配方 —— 并且**记录每次失败**，让经验复利。

---

## 快速开始

### 我是人，想浏览

```bash
git clone git@github.com:CChan4415/aesthetic-atlas.git
```

用 **Obsidian** 打开该文件夹（`Open folder as vault`）→ 从 `🏠 主页` 开始。
你会得到图谱视图、双链面板、标签筛选。

> 不用 Obsidian 也行 —— 它就是一个普通 Markdown 文件夹，任何编辑器都能看。

### 我是 agent，要使用这个库

**先读 [`AGENTS.md`](AGENTS.md)**，那是接入的唯一入口。

最短路径：

| 你的任务 | 读这个 |
|---|---|
| 定位已有概念 | [`index/compact.md`](index/compact.md) — 全部概念页紧凑清单 |
| 与用户探索新风格 | [`guides/style-exploration.md`](guides/style-exploration.md) |
| 直接出图 / 出视频 | [`recipes/`](recipes/index.md) → 取 prompt |
| 编译一本书 / 杂志 | [`guides/ingestion.md`](guides/ingestion.md) |
| 新增元素或风格 | [`guides/maintenance.md`](guides/maintenance.md) + [`guides/new-style-pack.md`](guides/new-style-pack.md) |

---

## 这个库怎么组织

```
原子元素 (atlas/)  ──组合──▶  子风格 (taxonomy/)  ──锁定──▶  配方 (recipes/)
   积木                        风格蓝图                    可直接出图
```

| 目录 | 作用 |
|---|---|
| [`atlas/`](atlas/index.md) | **原子图鉴** —— 163 个概念页，14 个维度（发型 / 妆容 / 材质 / 光影 / 质感 / 动态 / 情绪…）|
| [`recipes/`](recipes/index.md) | **风格配方** —— 已锁定的完整风格，每个含 `.md`（人读 + prompt）+ `.recipe.yml`（机读结构）|
| [`references/`](references/index.md) | **参考资料** —— 时代、品牌、创作者、作品、视觉符号 |
| [`raw/`](raw/index.md) | **原料区** —— 待编译的书 / 杂志 / 扫描件（只读）|
| [`guides/`](guides/index.md) | **agent 协议** —— 8 个行为规范 |
| [`index/`](index/compact.md) | **检索索引** —— 自动生成，agent 首选入口 |
| [`assets/`](assets/index.md) | **图像资产** —— 本地图片与生成参数快照 |
| [`tools/`](tools/validate.py) | **校验与索引工具** |

---

## 当前收录的风格

### Visual Kei · 日系视觉系（风格家族）

1980s 中起源于日本摇滚场景的视觉化美学。**不是 Y2K 的子风格**，有独立脉络。

| 分支 | 特征 |
|---|---|
| [Kote-kei 古典系](atlas/taxonomy/movements/visual-kei-kote-kei.md) | 全黑西装、石膏白妆、尖刺立发 |
| [Angura 暗黑哥特系](atlas/taxonomy/movements/visual-kei-angura.md) | 蕾丝束腰、和洋折衷、华美颓废 |
| [Oshare-kei 御洒落系](atlas/taxonomy/movements/visual-kei-oshare-kei.md) | 彩发糖果色、明快甜美 |
| [Kirakira 华丽系](atlas/taxonomy/movements/visual-kei-kirakira.md) | 亮片水钻、极致炫耀 |

### Y2K · 千禧年风格（约 1997–2006）

[Cyber Metal](atlas/taxonomy/movements/y2k-cyber-metal.md) · [Sweet Candy](atlas/taxonomy/movements/y2k-sweet-candy.md) · [Retro Future](atlas/taxonomy/movements/y2k-retro-future.md) · [Grunge Glam](atlas/taxonomy/movements/y2k-grunge-glam.md) · [Cyber Goth](atlas/taxonomy/movements/y2k-cyber-goth.md) · [McBling](atlas/taxonomy/movements/y2k-mcbling.md) · [里原宿/涩谷系](atlas/taxonomy/movements/y2k-harajuku-shibuya.md)

---

## 可用配方

| 配方 | 气质 | 状态 |
|---|---|---|
| [Visual Kei · Kote-kei 冷黑肖像](recipes/visual-kei-kote-cold-black.md) | 冷、锐利、舞台化 | ✅ 方向达成 |
| [Y2K · 暖调 DV 千禧偶像](recipes/y2k-warm-dv-idol.md) | 暖、怀旧、生活化 | ⚠️ v2 待验证 |

每个配方含组装好的 **image prompt**、**negative prompt**、**video prompt**，可直接用于即梦 / Midjourney / 可灵 / ComfyUI。

---

## 使用与维护

```bash
cd aesthetic-atlas
python3 tools/validate.py       # 校验链接 / frontmatter / 配方引用（0 错误才算完成）
python3 tools/build_index.py    # 重建检索索引
```

**改完必跑。** 详细规范见 [`AGENTS.md`](AGENTS.md)。

---

## 一些设计取舍

**为什么用 `[[wikilink]]` 而不是相对路径？**
两者内容完全相同，但 wikilink **路径无关** —— agent 按 basename 全局查找即可解析；
相对路径需要先知道当前文件所在目录，拿到片段就失效。
代价是 GitHub 上不渲染为可点击链接（**本 README 因此用标准链接**，库内文档用 wikilink）。

**为什么一个概念一个文件？**
为了可组合。改一个元素页，所有引用它的配方自动受益 —— **引用而非复制**。

**为什么记录失败？**
审美是长尾问题，同类失败会反复发生。库里的
[`anti-modern-digital`](atlas/grade/anti-modern-digital.md) 就是一次真实失败（生成的图完全没有年代感）
的产物 —— 现在它记录了介质层负向词库和画幅陷阱。

---

## 已知短板（诚实清单）

| 问题 | 说明 |
|---|---|
| 🔴 77/128 元素页从未被配方使用 | "写了" ≠ "有用"，未经过生成验证 |
| 🔴 `raw/` 为空 | **编译管道从未真实执行过** |
| 🔴 元素页几乎无示例图 | 审美资产却"看不见" |
| 🟡 视觉系 3/4 分支无配方 | 图鉴建了但不可直接用 |

> 这份清单会随进展更新。**不要把"结构完整"误当"已经可用"。**

---

## 许可与隐私

个人审美资产库，默认**私有**。配方与日志中包含个人工作偏好记录。
若源文件涉及第三方版权（杂志扫描、参考图等），已在对应 `assets/` 目录或 `sources` 字段标注。
