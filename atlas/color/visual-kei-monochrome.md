---
type: Color Palette
title: 视觉系·黑白冷调（Visual Kei Monochrome）
description: 视觉系的骨架配色——纯黑、石膏白、银灰三色构成的高对比冷调，Kote-kei 的标准色板。
tags: [visual-kei, color, palette, monochrome, kote-kei]
status: stable
generated: { by: agent:deepseek, at: 2026-10-12T10:40:00+08:00 }
---

# 定义 Definition

**黑白冷调**是视觉系色彩体系的**地基**——几乎所有分支都在此之上叠加主题色。
它只有三个角色，但对比关系极强：

| 角色 | 色值 | 用途 |
|---|---|---|
| 绝对黑 | `#0A0A0C` | 服装、发色、眼线、阴影（占画面 60–70%） |
| 石膏白 | `#F2F0EC` | 白妆底妆、衬衫、高光（占 10–15%） |
| 银灰 | `#8C8F94` | 金属件、发丝过渡、中间调（占 15–20%） |

关键：**白必须"冷"**（不能偏暖黄），**黑必须"深"**（不能是灰黑），
中间调尽量压缩——高对比是这个色板的全部意义。

# 色卡 Swatches

```
#0A0A0C  绝对黑   Absolute Black   服装主体 / 眼线 / 发色
#16171A  炭黑     Charcoal          层次分离用（比主黑略亮）
#8C8F94  银灰     Silver Grey       金属 / 中间调
#C8CACE  亮银     Bright Silver     金属高光 / 首饰
#F2F0EC  石膏白   Plaster White     白妆 / 衬衫 / 高光
#FFFFFF  纯白     Pure White        镜头高光 / 眼白
```

可选点缀（极少量，≤5%）：`#4A0E1E` 暗血红、`#2A1A3E` 深紫

# Prompt Keywords

`monochromatic black and white palette, stark black and cold white, high contrast monochrome,
pure black clothing with pale white skin, silver grey accents, desaturated cool tones, no warm
colors, austere color scheme, graphic black and white contrast`

# 适用风格 Applies To

- [[visual-kei-kote-kei|Kote-kei]]（标准色板）
- [[visual-kei-angura|Angura]]（作为基底，叠加暗红/暗金）
- [[visual-kei-kirakira|Kirakira]]（作为基底，叠加金属色）
- 与 Y2K [[chrome-cool-palette|chrome-cool-palette]] 的差异：
  chrome-cool 更"未来科技蓝"，本板更"戏剧黑白"

# 搭配建议 Pairs With

- 光影：**强单点硬光**——黑白板依赖硬光产生明确阴影，柔光会让画面变灰
- 质感：[[high-contrast-grade|high-contrast-grade]]、轻颗粒
- 场景：黑背景、空旷舞台、暗色室内

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| 一般黑白摄影 | 一般黑白是"去色"；本板是**主动的三色调设计**，白妆与黑衣是刻意的高对比 |
| 冷淡风 / 极简 | 极简追求"少而干净"；视觉系黑白板上承载大量繁复细节（蕾丝、金属）|
| 暖调黑白 | 若白偏黄、黑偏棕，会失去冷峻感——**必须强调 cool** |

# 生成提示 / 常见失败

- 易失败点：模型会把"黑白"输出成**低对比灰色**。必须强调 `stark, high contrast, pure black, cold white`
- 暖色污染是最常见问题——负向词加 `warm tones, sepia, golden tint, yellow cast`
- 皮肤在黑白板下若被生成成自然肤色，会破坏整体——需与 [[white-foundation|白妆]] 配合描述

# 来源 Sources

- [视觉系 · 中文维基](https://zh.wikipedia.org/zh-cn/%E8%A6%96%E8%A6%BA%E7%B3%BB)
