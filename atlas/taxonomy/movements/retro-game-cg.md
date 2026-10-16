---
type: Style Movement
title: 复古游戏 CG（Retro Game CG · PS1/PS2-era Low-Poly 3D）
description: 1997–2006 年 PS1/PS2 世代游戏画面风格的 3D 渲染美学——低多边形、低分辨率贴图、vertex wobble、固定视角，延伸至同人 CG 与虚拟主播圈。
tags: [retro-game-cg, movement, ps1, ps2, lowpoly, 2000s, 3d]
status: draft
generated: { by: agent:deepseek, at: 2026-10-16T20:35:00+08:00 }
sources:
  - id: raw-videos-2026-10
    resource: /raw/videos/
    title: 千禧年低多边形 3D 短片合集（4 部）
    author: "@natural water / @鴉鴉的幻覺 / @龙崎日舞"
---

# 定义 Definition

**Retro Game CG** 指**以 1997–2006 年第五代（PS1 / N64 / Saturn）与第六代（PS2 / Dreamcast / GameCube / Xbox）
游戏主机的实时渲染或预渲染画面**为审美参照的当代 3D 创作风格。其核心不是"还原游戏内容"，而是
**还原那一代硬件的渲染限制本身**——低多边形、低分辨率贴图、vertex wobble、affine texture warping、
固定低分辨率输出、固定相机视角。

> **它与"现代 3D"的根本区别**：现代 3D（虚幻 5、Unity HDRP）追求照片级真实；Retro Game CG 追求
> **"硬件不足时的妥协感"**——你能看到三角面、能看到贴图模糊、能看到模型边缘的锯齿。

# 时代背景 Context

- **硬件**：PS1 (1994)、N64 (1996)、Dreamcast (1998)、PS2 (2000)、GameCube (2001)。
- **限制**：多边形预算 1k–100k/帧、贴图 64×64 到 256×256、无 vertex shader、固定管线、
  软件或早期硬件抗锯齿（基本没有）、Z-buffer 精度低。
- **延伸文化**：2000s 中后期 Nico Nico Douga / YouTube 上的 MMD（MikuMikuDance）与同人 CG 小剧场、
  早期虚拟主播、PS2 游戏 OP/ED、《Kanon》《Air》等galgame 预渲染背景。

# 视觉语法 Visual Grammar（7 条）

1. **低多边形是结构，不是缺陷**：人物头发是"块状三角面"，手指可能是合并的"方块手"，
   面部靠贴图绘画而非几何细分。**不要试图用 prompt 让模型"修正"这些"错误"**——它们是风格本身。
2. **贴图分辨率低**：纹理可见像素颗粒，墙面/衣服图案是手绘或简单重复的位图。
3. **Vertex Wobble（顶点抖动）**：PS1 没有浮点精度，顶点在屏幕空间会"跳"。静帧不可见，视频里是关键。
4. **Affine Texture Warping（仿射贴图扭曲）**：透视不正确的贴图拉伸，在地面/墙面特写时明显。
5. **固定相机或有限运镜**：早期 3D 游戏常用固定视角（《生化危机》《最终幻想 7-9》），
   即使是当代同人 CG 也常模仿这一点。
6. **简单光照**：vertex lighting 为主，没有 SSAO / GI / 软阴影；高光常用 specular 贴图假做。
7. **画幅与分辨率**：4:3 (320×240 到 640×480) 是 PS1 标配；PS2 可到 4:3 480p。当代同人 CG 也常 4:3 输出。

# 与库内其他风格运动的区别

| 维度 | Retro Game CG（本运动） | [[y2k\|Y2K]] | [[visual-kei\|Visual Kei]] |
|---|---|---|---|
| **介质** | **3D 渲染**（实时或预渲染） | 摄影（DV / 胶片 / 数码） | 摄影（舞台 / 影棚） |
| **人物** | 低模 3D 角色 / 动漫 3D / 虚拟偶像 | 真人偶像 / 辣妹 / 名流 | 真人表演者（视觉系乐队） |
| **典型场景** | 学校走廊、地下通道、教室、游戏内城市 | 卧室、商场、街头、派对 | 舞台、暗厅、洋馆 |
| **质感** | 低模、低分辨率贴图、vertex wobble | VHS / DV 噪点、闪光灯 | 高对比戏剧光、锐利高清 |
| **画幅** | 4:3（或当代 9:16 短视频） | 4:3 / 3:4 / 9:16 | 3:4 / 9:16 |
| **情绪** | 孤独、青春、怀旧、微压抑、暧昧 | 怀旧微苦、俏皮元气 | 冷峻疏离、危险 |
| **介质锚定词** | `rendered on PS1/PS2, low-poly 3D, low-resolution textures` | `shot on 2000s DV camcorder` | （不需要介质锚定） |

> **关键判断**：判断是否属于本运动，看**介质是否为 3D 渲染**而不是看服装道具。
> 一个穿 JK 制服的真人 DV 短片属于 Y2K 子风格；同样的 JK 制服但低多边形 3D 渲染则属于本运动。

# 子风格 Substyles

| 子风格 | 一句话 | 状态 |
|---|---|---|
| **Low-Poly JK Slice-of-Life** | 校园日常、JK 制服、低多边形、压抑青春 | ⏳ 待建（首批配方目标） |
| **PS1 Horror** | 《寂静岭》《Rule of Rose》式恐怖 | 待建 |
| **MMD 小剧场** | Nico Nico 同人 MMD 风格（更精致的动漫 3D） | 待建 |
| **PS2 FMV** | 预渲染 OP/ED，比实时渲染更精细但仍是 2000s CG | 待建 |

> 当前仅锁定 **Low-Poly JK Slice-of-Life** 作为首个配方方向（基于 raw/videos/ 4 个原料）。
> 其他子风格待后续原料到位再建。

# 核心视觉母题 Motifs

低多边形头发（块状三角面）、贴图绘制的眼睛与嘴、方块手、单色或简单渐变皮肤、
瓷砖墙、水泥地面、荧光灯、CRT 屏幕、海报墙、走廊尽头、教室桌椅、
监控 bounding box、双语字幕条、`*斜体标语`、录制时间码。

# 适用维度 Navigation

- **介质/质感**：[[atlas/grade/index|grade/]]——核心维度，含 `low-poly-3d-render`、`ps2-fmv-grade`
- **镜头**：[[atlas/camera/index|camera/]]——`security-camera-cctv`、`third-person-game-camera`
- **场景**：[[atlas/setting/index|setting/]]——学校走廊、地下通道、食堂、教室
- **人物**：[[atlas/subject/index|subject/]]——`lowpoly-jk-character`
- **动态**：[[atlas/motion/index|motion/]]——手持微晃、跟拍、缓推（不用 datamosh/glitch 等数字破坏）

## Prompt Keywords

`low-poly 3D, PS1 aesthetic, PS2 aesthetic, 2000s game graphics, retro game render,
visible triangle edges, vertex wobble, affine texture warping, low-resolution textures,
fixed camera angle, vertex lighting, jagged edges, 4:3 frame, early 3D render,
N64 graphics, Dreamcast era, 2000s video game screenshot, pre-rendered FMV, MMD style,
cel-shaded 3D anime, low-poly JK character, slice-of-life 3D, melancholic school setting`

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| **当代 3D 渲染**（Blender / UE5） | 那些追求"看不出是 CG"；本运动追求"一看就是 PS1/PS2" |
| **像素风 / 8-bit** | 像素风是 2D 精灵；本运动是 3D 多边形 |
| ** vaporwave / 蒸汽波** | 蒸汽波是 80s/90s 商业艺术 + 早期互联网；本运动是 3D 游戏渲染 |
| **Retro Future**（Y2K 子风格） | Retro Future 是**界面与符号**（Win98、低多边形 UI）；本运动是**完整 3D 场景** |
| **动漫插画** | 动漫插画是 2D 绘画；本运动是 3D 渲染（即使 cel-shading 也是 3D） |

# 生成提示 / 常见失败

> **本节待积累实战经验。以下为基于规则推导的预判**：

- **介质锚定词必须放最前**：`Rendered on a 2000s game console, low-poly 3D...`
  （参考 [[anti-modern-digital|去现代数码感]] 的"介质前置"原则，本运动**同样需要**）
- **负向词两层**：内容层（现代物品）+ **渲染介质层**（`photorealistic, unreal engine 5, ray tracing, octane render, subsurface scattering, high-poly, 8k textures`）
- **现代模型会试图"修正"低模**：模型默认输出高模光滑 3D，必须显式压制
  `smooth shading, subsurface skin, realistic hair strands, detailed textures`
- **4:3 画幅用平台参数**设置（不要只写在 prompt 里——参考 Y2K 配方教训）

# 参考资料 References

- [[raw/videos/_source|raw/videos/_source.md]] — 4 部原始参考视频（@natural water / @鴉鴉的幻覺 / @龙崎日舞）
- [[late-1990s-early-2000s|时代：1990s 末–2000s 初]]
- PS1 / PS2 世代游戏截图与 FMV（待补充到 `references/works/`）

# 子风格可用元素 Substyle Elements

> 编译产物按子风格归组登记。

## Low-Poly JK Slice-of-Life 可用

- 待编译后填入（首批原子元素预计：grade/camera/subject/setting 各 2–3 个）
