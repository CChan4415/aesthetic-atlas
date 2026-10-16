---
type: index
title: Aesthetic Atlas · 审美图鉴
description: 个人视觉风格资产库（OKF v0.2 知识包），用于沉淀、组合、复用图片与视频创作的审美决策。
okf_version: "0.2"
created: 2026-10-12
---

# Aesthetic Atlas · 审美图鉴

> 个人视觉风格资产库（OKF v0.2 知识包）。用于沉淀、组合、复用图片与视频创作的审美决策，
> 并让接入的 agent 能基于本库与用户**共同探索**风格、**编译**外部书籍杂志、调用**现成风格配方**。

## 1. 这是什么

本库是一个"风格操作系统"，由七层构成：

| 区域 | 角色 | 类比 |
|---|---|---|
| [[atlas/index\|`atlas/`]] | **原子图鉴**：所有视觉元素的精细分类库，可自由组合 | 乐高积木箱 |
| [[recipes/index\|`recipes/`]] | **风格配方**：已锁定的完整风格，开箱即用、可版本维护（Markdown + 机读 YAML） | 预制菜谱 |
| [[references/index\|`references/`]] | **参考资料库**：时代、品牌、创作者、作品、视觉符号 | 图书馆 |
| [[raw/index\|`raw/`]] | **原料区**：未编译的书、杂志、扫描件（pending → compiled） | 收件箱 |
| [[guides/index\|`guides/`]] | **Agent 协议**：探索、生成、编译、维护、建设的行为规范 | 操作手册 |
| [[compact\|`index/`]] | **检索索引**：自动生成的概念清单与关系图（agent 首选入口） | 索引卡 |
| [[assets/index\|`assets/`]] | **图像资产**：本地落地的图片与生成参数快照 | 底片库 |
| `tools/` | **校验与生成工具** | 质检台 |

## 2. 收录的风格

### Visual Kei · 日系视觉系（风格家族，与 Y2K 平级）
* [[visual-kei-kote-kei|Kote-kei 古典系]] — 黑西装、白妆、尖刺立发
* [[visual-kei-angura|Angura 暗黑哥特系]] — 蕾丝束腰、和洋折衷、华美颓废
* [[visual-kei-oshare-kei|Oshare-kei 御洒落系]] — 彩发糖果色、明快甜美
* [[visual-kei-kirakira|Kirakira 华丽系]] — 亮片水钻、极致炫耀

### Y2K · 千禧年风格（约 1997–2006）
* [[y2k-cyber-metal|Cyber Metal]] · [[y2k-sweet-candy|Sweet Candy]] ·
  [[y2k-retro-future|Retro Future]] · [[y2k-grunge-glam|Grunge Glam]]
* [[y2k-cyber-goth|Cyber Goth 赛博哥特]] · [[y2k-mcbling|McBling 奢华浮夸]] ·
  [[y2k-harajuku-shibuya|里原宿/涩谷系]]

## 3. Agent 快速开始

1. **定位已有概念** → 先读 [[compact|`index/compact.md`]]（162 个概念页的紧凑清单），再下钻。
2. **想探索新风格** → 阅读 [[style-exploration|`guides/style-exploration.md`]]，按协议逐维度提问并组装。
3. **想直接出图** → 在 [[recipes/index|`recipes/`]] 选一个配方（读 `.recipe.yml` 结构 + `.md` 的 prompt）。
4. **想直接出视频** → 配方 + [[video-generation|`guides/video-generation.md`]]。
5. **用户丢来一本书/杂志** → 放入 `raw/`，按 [[ingestion|`guides/ingestion.md`]] 编译进 `atlas/`。
6. **新建一个风格** → 按 [[new-style-pack|`guides/new-style-pack.md`]] 的 checklist。
7. **新增/修改后** → 跑 `python3 tools/validate.py`，再跑 `python3 tools/build_index.py`，更新 `index.md` 与 `log.md`。

## 4. 阅读约定

- 每个概念 = 一个 Markdown 文件 = YAML 元数据 + 中文正文；`Prompt Keywords`（英文）可直接喂给图像/视频模型。
- 文件路径即概念 ID；**链接一律用相对路径**（保证换渲染器/换目录可用）。
- `status: draft | stable | deprecated`；信任层级见各文件 `verified` 字段。
- 配方为**双表示**：`.md` 给人读（prompt 文本以此为准），`.recipe.yml` 给 agent 读（结构与引用以此为准）。

## 5. 当前可用配方

| 配方 | 一句话 | 气质 |
|---|---|---|
| [[visual-kei-kote-cold-black\|Visual Kei · Kote-kei 冷黑肖像]] | 黑西装、石膏白妆、尖刺立发、强单点硬光 | 冷、锐利、舞台化 |
| [[y2k-warm-dv-idol\|Y2K · 暖调 DV 千禧偶像]] | 橙粉/古铜/脏金、老 DV、海报卧室 | 暖、怀旧、生活化 |

> 两者构成当前的两极，可用于验证"资产库能否产出气质相反的作品"。
