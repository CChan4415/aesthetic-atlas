---
type: Guide
title: 图像资产层规范
description: 本地图像资产的存放、命名、绑定与检索约定，解决"审美资产依赖外部 CDN"的结构性风险。
tags: [guide, assets, images, storage]
status: stable
generated: { by: agent:deepseek, at: 2026-10-12T10:40:00+08:00 }
---

# 图像资产层规范

## 1. 为什么需要这一层

审美资产的核心是"**看见**"。但当前设计里，图片只能以 URL 形式写在配方的产物记录中
（如 `https://aka.doubaocdn.com/s/...`）。这有三个风险：

1. **链接会失效** —— CDN 链接不保证长期存活，届时资产库只剩文字描述
2. **概念无法挂示例图** —— "块状挑染长什么样"无法直观呈现
3. **agent 无法"看图"** —— 只能读文字描述

**因此：所有图片必须落本地。** 外部 URL 仅作补充线索，不作为唯一来源。

## 2. 目录结构

```
assets/
├── elements/<维度>/<concept-id>/     # 原子元素的示例图
│   ├── 001.jpg
│   ├── 002.jpg
│   └── _meta.md                      # 来源、授权、说明
├── recipes/<recipe-id>/              # 配方的产物
│   ├── v1-2026-10-12.jpg
│   └── v1-2026-10-12.json            # 生成参数快照
├── references/                       # 参考图（品牌/创作者/年代）
└── index.md                          # 资产总索引
```

**规则**：`assets/elements/` 下的路径结构**镜像** `atlas/` 的结构。

| atlas 概念页 | 对应资产目录 |
|---|---|
| `atlas/hair/chunky-highlights.md` | `assets/elements/hair/chunky-highlights/` |
| `atlas/makeup/white-foundation.md` | `assets/elements/makeup/white-foundation/` |

## 3. 命名规则

| 类型 | 规则 | 例子 |
|---|---|---|
| 元素示例图 | `NNN.<ext>` 三位序号 | `001.jpg`、`002.png` |
| 配方产物 | `v<版本>-<日期>.<ext>` | `v1-2026-10-12.jpg` |
| 配方参数快照 | 与产物同名 `.json` | `v1-2026-10-12.json` |
| 参考图 | `<来源>-<序号>.<ext>` | `lachapelle-01.jpg` |

- 一律小写、kebab-case、无空格
- 保留原始文件格式；不要为省空间转换格式（避免再压缩损失）

## 4. 在概念页中绑定图片

在概念页正文中使用**相对链接**：

```markdown
# 示例 Examples

`![块状挑染示例](../../assets/elements/hair/chunky-highlights/001.jpg)`
```

**注意**：从 `atlas/hair/x.md` 到 `assets/elements/hair/x/` 需要上溯两级（`../../`）。
路径一律用**相对链接**（不要用 `/` 开头），保证换渲染器/换目录都能用。

## 5. 尺寸与体积约定

| 类型 | 建议长边 | 理由 |
|---|---|---|
| 元素示例图 | ≤ 512 px | 仅作示意，不需要高清 |
| 配方产物 | 保留原尺寸 | 是实际作品，可能要用 |
| 参考图 | ≤ 1024 px | 平衡清晰度与体积 |

- 单文件建议 ≤ 2 MB（配方产物除外）
- 大图可另存缩略图 `001.thumb.jpg` 供快速浏览

## 6. 生成参数快照（配方产物必做）

每个配方产物应配一个同名 `.json`，记录**可复现信息**：

```json
{
  "recipe_id": "visual-kei-kote-cold-black",
  "recipe_version": 1,
  "date": "2026-10-12",
  "model": "<使用的模型/平台>",
  "prompt_snapshot": "<实际提交的完整 prompt>",
  "negative_snapshot": "<实际提交的负向词>",
  "seed": null,
  "aspect_ratio": "3:4",
  "dimensions": "1536x2048",
  "overrides": { "grade_strength": "medium" },
  "rating": null,
  "notes": ""
}
```

**为什么要 snapshot prompt 而不是只存引用**：因为配方会演进。
若只存 `recipe_id`，未来配方改了版本，就无法知道当时到底用了什么。
**快照是产物可追溯性的保证。**

## 7. 与 `_meta.md` 的配合

每个元素资产目录可放 `_meta.md` 记录：

```yaml
---
type: Asset Meta
title: 块状挑染 示例图
source: <来源：自生成 / 网络 / 扫描>
license: <授权状态>
generated: { by: ..., at: ... }
---
```

用途：当资产涉及第三方版权时，明确标注，避免误用。

## 8. 检索索引

`assets/index.md` 由 `tools/build_index.py` 自动生成，列出所有资产与对应概念页。
**它是再生成产物，不要手工编辑**（避免与文件系统不一致）。

## 9. 反例 Not To Do

| 错误做法 | 为什么错 |
|---|---|
| 只在配方里存 CDN URL | 链接失效即资产蒸发 |
| 用 `/` 开头的绝对路径引用图片 | 换渲染器/换目录即断链 |
| 手工维护 `assets/index.md` | 必然与文件系统漂移 |
| 配方产物不存参数快照 | 无法复现，也无法追溯版本 |
| 把示例图存成 4000px 大图 | 库体积膨胀，且没有必要 |
