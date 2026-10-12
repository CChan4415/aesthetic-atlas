---
type: Visual Element
title: 高对比戏剧质感（High-Contrast Dramatic Grade）
description: 视觉系的画面质感——深黑压暗、高光锐利、整体去饱和或强偏色，去掉一切生活感。
tags: [visual-kei, grade, contrast, dramatic]
status: stable
generated: { by: agent:deepseek, at: 2026-10-12T10:40:00+08:00 }
---

# 定义 Definition

**高对比戏剧质感**是视觉系影像的后期基调。它的目标不是"好看"，
而是**把画面从现实里拽出来**——让观众立刻感到"这是舞台/这是作品"。

手法上，它与 Y2K 的做旧质感**方向相反**：
- Y2K [[vhs-dv-texture|VHS/DV 质感]] 追求"**像一盘旧录像带**"（噪点、褪色、低清）
- 视觉系高对比质感追求"**像一张戏剧海报**"（干净、锐利、极深黑、去饱和）

两者可以在"日系千禧"主题下混合，但会互相削弱——**选一个作为主导**。

# 视觉特征 Visual Cues

- **极深的黑**：暗部被压到接近纯黑，细节主动牺牲
- **锐利高光**：高光不溢出但边界明确，形成硬朗的明暗切割
- **去饱和**：整体降低饱和度，只保留主题色（如血红、暗金）
- 强阴影：面部与服装上有明确的**硬边阴影**
- 可轻微偏色：冷蓝（冷峻）或暗红（危险）
- 对比度高但**不脏**——保留干净的黑

## Prompt Keywords

`high contrast dramatic grade, deep crushed blacks, sharp crisp highlights, desaturated color
grade, strong chiaroscuro, hard-edged shadows, theatrical poster look, moody dark grading,
clean deep shadows, cinematic high contrast, cool blue tint or deep red tint, graphic lighting`

# 强度分级

| 强度 | 表现 | 适用 |
|---|---|---|
| 轻度 | 对比略强、轻微去饱和 | 需保留面料细节（蕾丝、刺绣）时 |
| 中度 | 明显深黑、硬阴影、明显去饱和 | **推荐默认值** |
| 重度 | 黑场极深、接近剪影、强偏色 | 纯氛围图、剪影构图 |

# 适用风格 Applies To

- 全部视觉系分支（[[visual-kei-kote-kei|Kote-kei]]、[[visual-kei-angura|Angura]]、[[visual-kei-kirakira|Kirakira]]）
- 哥特、暗黑系、以及需要"戏剧感"的 Y2K [[y2k-cyber-goth|Cyber Goth]]

# 搭配建议 Pairs With

- 光影：[[dramatic-single-source|dramatic-single-source]]（强单点光是前提）
- 配色：[[visual-kei-monochrome|visual-kei-monochrome]]
- 妆容：[[white-foundation|白妆]]（白妆 + 高对比 = 面具感最大化）

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| 单纯调高对比度 | 高对比若不做去饱和会显得"艳丽脏"；本质感是**对比 + 去饱和**的组合 |
| HDR | HDR 把暗部细节提亮；本质感**主动压掉暗部细节**，是相反方向 |
| VHS/DV 做旧 | 做旧是加噪点、褪色、低清；本质感是干净的极深黑与锐利 |

# 生成提示 / 常见失败

- 易失败点：模型倾向输出"正常曝光的平衡画面"。需强调 `crushed blacks, deep shadows, high contrast, desaturated`
- 若同时要蕾丝/刺绣等细节，**必须降到轻度**，否则细节会被黑场吃掉
- 与"overly clean digital look"负向词的关系：本质感要**干净但暗**，所以应保留"干净"、去掉"明亮"
- 负向词建议加：`flat lighting, low contrast, washed out, HDR, bright even lighting`

# 来源 Sources

- [视觉系 · 中文维基](https://zh.wikipedia.org/zh-cn/%E8%A6%96%E8%A6%BA%E7%B3%BB)
- [日系视觉 · 百度百科](https://baike.baidu.com/item/%E6%97%A5%E7%B3%BB%E8%A7%86%E8%A7%89)
