---
type: Guide
title: 维护规范
description: 资产库命名、粒度、元数据、索引、日志、生命周期与配方版本规则。
tags: [guide, maintenance, conventions, metadata]
status: stable
generated: { by: human:cc, at: 2026-10-12T00:00:00+08:00 }
---

# 维护规范

## 1. 语言与格式

- 正文中文；每个原子概念必须含 `## Prompt Keywords`（英文词组，逗号分隔，可直接入 prompt）。
- UTF-8、kebab-case 文件名；一个概念一个 `.md`；结构用标题/列表/表格，少用散体长文。

## 2. 粒度规则（何时拆分 / 何时聚合）

**独立成文件**：跨风格复用、有独立搭配逻辑或互斥关系的元素（如"肚链""锡纸烫""VHS 颗粒"）。

**聚合在维度 index 表格**：同一属性的简单枚举变体（如景别、光位、机位角度、单色卡）。

**拆分触发条件**：当某变体被单独引用 ≥2 次、或需要独立的搭配/来源说明时，从聚合表拆为独立文件。

## 3. 概念类型（type）参考

| type | 用途 |
|---|---|
| `Style Movement` / `Style Substyle` | 风格运动 / 子风格 |
| `Visual Element` | 原子视觉元素（发型、妆容、单品、配饰、材质、光影、质感等） |
| `Motion Element` | 视频动态元素（运镜、动作、转场、特效） |
| `Color Palette` | 完整配色方案 |
| `Style Recipe` | 完整风格配方 |
| `Reference` | 品牌/创作者/作品/时代/符号等外部参考 |
| `Raw Source` | raw 原料登记 |
| `Guide` | 协议流程 |

允许自定义新 type；未知 type 按通用概念处理，不得报错。

## 4. 必备 frontmatter 模板

```yaml
---
type: Visual Element
title: 中文名（English Name）
description: 一句话说明
tags: [y2k, <维度>, ...]
status: draft          # draft | stable | deprecated
sources: [...]         # 有外部来源时
generated: { by: human:cc, at: 2026-10-12T00:00:00+08:00 }
---
```

## 5. 原子概念正文标准段落

```
# 定义 Definition
# 视觉特征 Visual Cues（ bullet ）
## Prompt Keywords（英文，必含）
# 适用风格 Applies To（链接）
# 搭配建议 Pairs With（链接）
# 变体 Variants（如有）
# 易混/反例 Not To Confuse（如有）
# 来源 Sources（如有）
```

## 6. 索引与日志

- 每个目录放 `index.md`（无 frontmatter；根 index 例外，可带 `okf_version`），列出本目录概念与一句话描述。
- 新增/修改/废弃概念后，同步更新所在目录 `index.md` 与根 `log.md`（newest first，`YYYY-MM-DD`）。
- 断链可容忍（代表尚未撰写），但应在 log 中记录待补项。

## 7. 生命周期

- `draft` 草稿 → 复核通过转 `stable`；过时转 `deprecated`（保留以维护链接）。
- 时效性内容用 `stale_after`（绝对时间）。
- 用户复核过的内容加 `verified: { by: human:cc, at: ... }`。

## 8. 配方版本

- 配方一旦被实际用于产出，即视为受版本管理；重大改动（主体/配色/质感变更）递增版本号并在配方内
  保留版本历史与对应产物记录；小调整（换道具、换配饰）记为同版本微调。
- 配方内区分 `locked`（风格签名，不可轻易改）与 `tunable`（可按项目替换）。
