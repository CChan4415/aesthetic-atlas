---
type: Visual Element
title: 低多边形 3D 渲染（Low-Poly 3D Render）
description: PS1/PS2 世代游戏实时渲染的视觉特征——可见三角面、低分辨率贴图、vertex wobble、简单光照，是 Retro Game CG 风格运动的核心介质。
tags: [retro-game-cg, grade, 3d, lowpoly, ps1, ps2, render]
status: draft
generated: { by: agent:deepseek, at: 2026-10-16T20:40:00+08:00 }
sources:
  - id: raw-videos-2026-10
    resource: /raw/videos/
    title: 千禧年低多边形 3D 短片合集
    author: "@natural water / @鴉鴉的幻覺 / @龙崎日舞"
---

# 定义 Definition

**低多边形 3D 渲染**是第五代（PS1 / N64 / Saturn）与第六代（PS2 / Dreamcast / GameCube）
游戏主机实时渲染的视觉签名。它不是"差劲的 3D"，而是**特定硬件限制下的美学**——
当多边形预算、贴图大小、光照模型、屏幕分辨率都受限时，3D 画面呈现出的独特质感。

> **关键判断**：识别一个画面是否为 Low-Poly 3D，看**头发是否为块状三角面**、
> **皮肤是否为单色或简单渐变**、**贴图是否可见像素**、**手指是否合并**。

# 视觉特征 Visual Cues

- **头发**：块状三角面、片状结构、无单丝细节、可见发片边缘
- **皮肤**：单色或简单渐变、无毛孔/纹理/SSS、可能带 vertex lighting 阴影
- **眼睛与嘴**：贴图绘制（一张位图贴在脸上），而非几何建模
- **手**：常合并为方块手（mittens），手指是简单棱柱
- **服装**：褶皱是雕刻的大形状，无布料模拟
- **贴图**：低分辨率位图（64×64 到 256×256），可见像素、可能有重复贴图接缝
- **边缘**：锯齿明显（无抗锯齿或简单 MSAA）
- **光照**：简单 vertex lighting、固定高光、无软阴影、无环境光遮蔽
- **背景**：低多边形建筑、天空盒可能是手绘位图

## Prompt Keywords

`low-poly 3D render, PS1 graphics, PS2 graphics, 2000s video game render, visible triangle faces,
chunky blocky hair, flat shaded polygons, low-resolution textures, vertex lighting, jagged edges,
no anti-aliasing, 2000s game screenshot, early 3D render, N64 aesthetic, Dreamcast graphics,
texture-mapped face, mitten hands, simple gradient skin, low poly environment, 4:3 frame,
rendered on 2000s game console, retro 3D look`

# 强度分级

| 强度 | 适用 | 表现 |
|---|---|---|
| **轻** | 接近当代 indie 游戏的"风格化低模" | 多边形较多，贴图较精细，有简单 AA；类似《Stray》《Tunic》 |
| **中** | **PS2 世代实时渲染**（推荐默认） | 明显块状头发、贴图可见像素、锯齿；类似《Final Fantasy X》《Kingdom Hearts》 |
| **重** | **PS1 世代实时渲染** | 极低模、vertex wobble 明显、affine texture warping；类似《Final Fantasy VII》《Metal Gear Solid》 |

# 变体 Variants

- **Cel-shaded Low-Poly**：《Jet Set Radio》《Zelda: Wind Waker》式动漫渲染，黑边线 + 平色
- **Pre-rendered FMV**：见 [[ps2-fmv-grade]]——比实时渲染精细，但仍是 2000s CG
- **MMD 同人 CG**：MikuMikuDance 风格，模型更精细但保留低多边形美学

# 适用风格 Applies To

- **必需**：[[retro-game-cg|Retro Game CG]] 所有子风格
- **部分适用**：与 [[y2k-retro-future|Retro Future]] 混搭时（Retro Future 是界面符号，本元素是 3D 渲染）

# 搭配建议 Pairs With

- [[security-camera-cctv|监控视角]]、[[third-person-game-camera|第三人称游戏相机]]
- [[lowpoly-jk-character|低多边形 JK 角色]]——本元素是它的介质基础
- 场景：[[school-corridor-cctv|学校走廊监控]]、[[underground-passage-tiled|地下通道瓷砖]]

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| **当代 indie 低模**（《Stray》） | 那是高模+风格化渲染；本元素是**真正的硬件限制美学** |
| **Voxel / 体素**（《Minecraft》） | Voxel 是立方体；本元素是任意三角面 |
| **像素风** | 像素风是 2D；本元素是 3D |
| **当代写实 3D**（UE5） | 完全相反——必须显式排除 `unreal engine, ray tracing, photorealistic` |

# 生成提示 / 常见失败

> **预判**（待实测验证）：

- **介质锚定句放最前面**：`RENDERED ON A 2000s GAME CONSOLE, low-poly 3D, NOT a modern game engine render`
- **必须显式排除现代 3D 特征**：`unreal engine 5, ray tracing, subsurface scattering, high-poly sculpt,
  octane render, photorealistic, 8k textures, smooth shading`
- **块状头发要写清**：`chunky blocky hair with visible triangle faces`，否则模型会生成光滑丝滑头发
- **贴图画眼睛**：`face texture with painted eyes and mouth`——防止模型建出真实眼球
- **画幅 4:3 用平台参数**（参考 Y2K 教训）

# 来源 Sources

- [[raw/videos/_source|raw/videos/_source.md]] — 4 部 PS1/PS2 风格短片
- 待补充：PS1/PS2 游戏截图对比（《Final Fantasy VII》《Metal Gear Solid》《Kingdom Hearts》）
