---
type: Visual Element
title: PS2 FMV 预渲染质感（PS2 FMV Grade / Pre-rendered CG）
description: PS2 世代游戏预渲染过场动画（FMV / OP / ED）的画面质感——比实时渲染精细但仍保留 2000s CG 的渲染限制痕迹，介于低模与当代 3D 之间。
tags: [retro-game-cg, grade, 3d, ps2, fmv, pre-rendered, 2000s]
status: draft
generated: { by: agent:deepseek, at: 2026-10-16T20:42:00+08:00 }
sources:
  - id: raw-videos-2026-10
    resource: /raw/videos/
    title: 千禧年低多边形 3D 短片合集
    author: "@龙崎日舞"
---

# 定义 Definition

**PS2 FMV Grade** 指 PS2 / Dreamcast / GameCube 世代游戏的**预渲染过场动画**（Full Motion Video）
的画面质感。与实时渲染的 [[low-poly-3d-render|低多边形]] 不同，FMV 是离线渲染的（可用更高多边形、
更精细贴图、更复杂光照），但**仍保留 2000s 早期 CG 的特征**——皮肤过于光滑、光照简单、
色彩饱和偏低、对比柔和、动作略僵硬。

> **核心区别**：Low-Poly 3D Render 是"实时渲染的粗糙感"；PS2 FMV 是"**预渲染的塑料感**"。

# 视觉特征 Visual Cues

- **皮肤**：光滑、无毛孔、轻微塑料感、可能带简单 SSS
- **头发**：仍有片状结构但比实时渲染更细、有简单高光
- **光照**：三点打光、软阴影但无 GI、色彩饱和偏低
- **贴图**：比实时渲染精细（512×512+）但仍是手绘位图
- **背景**：预渲染背景（《最终幻想 7-9》式静态背景 + 实时人物）
- **动作**：略僵硬（手 keyframe，无动作捕捉的自然感）
- **画幅**：常 4:3 或 16:9 信箱

## Prompt Keywords

`PS2 FMV, pre-rendered cutscene, 2000s game cinematic, early 2000s CG, Kingdom Hearts cutscene,
Final Fantasy X FMV, smooth plastic skin, simple three-point lighting, pre-rendered background,
stiff animation, painted texture face, 2000s video game cinematic, offline render, soft shadows,
subtle gradient skin, low saturation, 4:3 letterbox, early CG aesthetic, PlayStation 2 era cutscene`

# 强度分级

| 强度 | 适用 | 表现 |
|---|---|---|
| **轻** | 接近当代独立游戏 CG | 较精细建模，但仍识别得出"2000s" |
| **中** | **PS2 后期 FMV**（推荐默认） | 皮肤光滑塑料感、简单光照、僵硬动作 |
| **重** | **PS1 FMV** / 早期 Dreamcast | 接近实时渲染 + 静态背景混合 |

# 与 Low-Poly 3D Render 的区别

| 维度 | Low-Poly 3D Render | PS2 FMV Grade |
|---|---|---|
| **多边形** | 极低（可见三角面） | 中等（皮肤光滑） |
| **贴图** | 低分辨率（64-256px） | 中等（512px+） |
| **光照** | Vertex lighting | 三点打光、软阴影 |
| **头发** | 块状 | 片状但更细 |
| **皮肤** | 单色/简单渐变 | 光滑塑料感 |
| **用途** | 游戏内实时画面 | 过场动画 / OP / ED |
| **典型代表** | 《FF7》游戏内 | 《FFX》FMV |

# 适用风格 Applies To

- **[[retro-game-cg|Retro Game CG]]** 子风格：**PS2 FMV**、**MMD 小剧场**（MMD 模型更接近 FMV 精度）
- **部分适用**：[[y2k-retro-future|Retro Future]] 中的游戏截图美学

# 搭配建议 Pairs With

- [[lowpoly-jk-character|低多边形 JK 角色]]——本元素是它的"精细版"
- 场景：[[school-cafeteria-3d|学校食堂]]、[[school-corridor-cctv|学校走廊]]
- 光影：[[tv-crt-glow|屏幕辉光]]、[[golden-hour-backlight|黄金时刻逆光]]

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| **当代 3D 动画**（皮克斯、Disney） | 那是电影级渲染，毛孔/毛发/SSS 全开；本元素是 2000s 早期 CG |
| **当代写实游戏**（《最后生还者 2》） | 完全相反——必须显式排除 `photorealistic, motion capture, filmic` |
| **2D 动漫** | 2D 是手绘；本元素是 3D 渲染（即使 cel-shading） |
| **虚拟主播 Live2D** | Live2D 是 2.5D；本元素是真 3D |

# 生成提示 / 常见失败

> **预判**（待实测验证）：

- **介质锚定词**：`rendered as a 2000s PS2 game FMV cutscene, pre-rendered CG, early 2000s game cinematic`
- **塑料感皮肤要写清**：`smooth plastic skin, no pores, slight subsurface scattering`，
  否则模型会输出真实皮肤
- **排除当代 CG**：`photorealistic, movie quality render, pixar style, unreal engine cinematic,
  ray tracing, motion capture animation`
- **画幅**：常用 4:3 信箱，可用平台参数；画面上下可有黑边

# 来源 Sources

- [[raw/videos/_source|raw/videos/_source.md]] — @龙崎日舞 两部视频（食堂、值日）
- 待补充：《Final Fantasy X》《Kingdom Hearts》《.hack》PS2 FMV 截图对比
