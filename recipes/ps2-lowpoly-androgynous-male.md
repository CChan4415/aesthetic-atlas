---
type: Style Recipe
title: PS2 低多边形 · 雌雄莫辨少年（PS2 Low-Poly Androgynous Male）
description: 2000s PS2 游戏渲染风格的低多边形少年角色通用配方——遮眼刘海、休闲街头穿搭，场景可调（厨房/街道/铁馆），含图/视频双 prompt。
tags: [retro-game-cg, recipe, lowpoly, male, androgynous, ps2, 3d]
status: draft
generated: { by: agent:deepseek, at: 2026-10-17T01:00:00+08:00 }
version: '1'
---

# 一句话 One-liner

一位低多边形 3D 风格的日系少年，瘦削体型、遮眼刘海、柔和近中性的面部，
穿宽松帽衫与工装裤，在 2000s 日式小厨房 / 街道 / 老式铁馆之间穿行——
画面像一台 PS2 游戏的实时渲染截图，安静、内敛、微压抑。

# 适用场景 Use Cases

Retro Game CG 风格的男性向图/视频；日常系短片主角；机车/健身/晨起等生活切片；
**图生视频的首帧**（低模风格延续到视频）。

# 锁定决策 Locked Decisions（风格签名）

| 维度 | 决策 | 状态 |
|---|---|---|
| 风格运动 | [[retro-game-cg\|Retro Game CG · 复古游戏 CG]] | locked |
| 角色原型 | [[androgynous-male-youth\|雌雄莫辨少年]]（瘦削、遮眼刘海、柔和面部但男性体型） | locked |
| 渲染介质 | [[low-poly-3d-render\|低多边形 3D 渲染]]（中度：PS2 世代实时渲染） | locked |
| 服装 | 休闲街头：宽松帽衫/T恤 + 工装裤/牛仔裤 + 厚底运动鞋 | locked |
| 发型 | [[eye-covering-bangs\|遮眼刘海]]（块状三角面低模变体） | locked |
| 配色 | 低饱和灰绿/青蓝/暗黄，整体偏冷 | locked |
| 画面质感 | 低多边形 + 低分辨率贴图 + vertex wobble（视频） + 锯齿 | locked |
| 情绪 | 孤独、内敛、晨起、微压抑 | locked |
| 场景 | [[japanese-kitchen-2000s\|日式小厨房]] / [[old-school-gym-iron\|老式铁馆]] / [[underground-passage-tiled\|地下通道]] 等 | tunable |
| 镜头 | [[third-person-game-camera\|第三人称游戏视角]] / [[security-camera-cctv\|监控视角]] / 平视中景 | tunable |
| 机车 | 2000s 日系街车类别（圆灯、单缸、机械感），具体型号不限 | tunable |
| 画幅 | 4:3（图片）；4:3 上下黑边（视频） | locked |
| 叠层 | 无 / 双语字幕 / bounding box | tunable |

# Image Prompt（EN，已组装 · v1 · 厨房场景）

> **介质前置**：渲染介质锚定词必须放最前（见 [[anti-modern-digital|去现代数码感]] 渲染介质章节）。

```
RENDERED ON A 2000s PS2 GAME CONSOLE — this is a low-poly 3D real-time game render,
NOT a modern photorealistic 3D image. Visible triangle faces in hair, texture-mapped face
with painted eyes and mouth, simple gradient skin without pores, chunky low-poly hair pieces,
jagged polygon edges, low-resolution textures, vertex lighting, no anti-aliasing,
640x480 render resolution, 2000s video game aesthetic.

A low-poly androgynous teenage boy with a slim delicate build, male body frame with narrow
shoulders and flat chest, shoulder-length dark hair with chunky triangle bangs covering one
eye, soft feminine facial features, texture-mapped face with painted dark eyes and small
mouth; wearing a loose grey hoodie over a white t-shirt, dark cargo pants, chunky sneakers;
standing at a narrow wooden counter in a small 2000s Japanese apartment kitchen, two-burner
gas stove with a frying pan, small white fridge, rice cooker, stacked bowls, morning light
through a small window, hanging hand towel, cluttered but cozy.

Eye-level medium shot, slightly off-center composition, 4:3 frame; cool desaturated
grey-green palette with warm morning light accents; melancholic quiet morning mood,
slice-of-life 2000s Japanese game atmosphere.
```

# Negative Prompt（v1 · 两层结构）

**内容层**（年代穿帮）+ **渲染介质层**（现代 3D 特征）：

```
lowres, bad anatomy, bad hands, extra fingers, deformed, watermark, text artifacts,
smartphones, LED screens, modern appliances, induction cooktop, stainless steel kitchen,
minimalist interior, smart fridge, 2020s fashion, modern gym, glass walls, treadmill row,
chrome machines, fitness chain, mirror wall,
photorealistic, real human, live action, unreal engine 5, ray tracing, octane render,
high-poly sculpt, subsurface scattering, realistic hair strands, detailed skin pores,
smooth shading, 8k textures, filmic color grading, cinematic lighting, pixar style,
disney style, sharp 4k render, glossy reflective skin, detailed iris, realistic eyeballs,
overly masculine, muscular body, beard, adult man
```

# Video Prompts（EN · v1 · 4 镜头分镜）

> 短片叙事感，4 镜头各 2–3 秒，后期剪辑拼接。首帧用厨房静帧图。

**镜头 1 · 早餐（厨房）**
```
The low-poly boy cracks an egg into the frying pan with one hand, casual practiced motion,
vertex wobble jitter on his outline, steam rising as simple white sprite particles,
camera locked static at eye level, 15 fps with slight frame skips, 2000s PS2 game render,
quiet morning atmosphere
```

**镜头 2 · 门口（拿头盔推车）**
```
He pulls on his sneakers at the genkan entrance, helmet tucked under one arm, grabs keys
from a small shelf, stands up and pushes the door open; fixed camera from inside the
apartment looking toward the door, morning light floods in as the door opens, low frame
rate, slight scanlines, PS2 real-time render quality
```

**镜头 3 · 骑行（第三人称跟随）**
```
Third-person game camera follows behind him riding a 2000s Japanese standard motorcycle
(round headlight, single cylinder, vintage street bike), helmet now on, riding through
empty early-morning residential streets; camera smooth follow with slight lag, low-poly
buildings and utility poles passing by, cool morning light, vertex wobble on distant
geometry, PS2-era racing game feel
```

**镜头 4a/4b · 铁馆撸铁（快切）**
```
4a: He lies on a flat bench in an old-school iron gym, pressing two dumbbells upward,
metal plate dumbbell rack behind him, bare concrete walls with small taped notices,
harsh overhead fluorescent light, fixed low-angle shot from the side
4b: Cut to barbell squat from a fixed front camera, he lowers and rises with control,
chalk dust particles in the air, sweat sheen as simple specular highlights, dim basement
gym atmosphere, 2000s game render
```

视频参数建议：4:3 上下黑边（伪宽屏），8–15 秒成片，15 fps 低帧率，后期配乐。

# 可调参数 Tunable

- **场景**：厨房（默认首图）/ 地下通道 / 铁馆 / 街道
- **镜头**：平视中景（默认）/ 第三人称跟随 / 监控视角
- **服装**：帽衫（默认）/ T恤 / 机车夹克
- **叠层**：无（默认）/ 双语字幕 / bounding box
- **多边形强度**：中（PS2，默认）/ 轻 / 重（PS1）
- **机车镜头**：骑行（默认）/ 推车（更稳）

# 与其他配方的区别 Differentiation

| 对比 | 差异 |
|---|---|
| [[ps2-lowpoly-jk-slice-of-life\|PS2 低多边形 JK 校园日常]] | 那是**少女 + 校园**；本配方是**少年 + 生活场景**（厨房/机车/铁馆） |
| [[y2k-warm-dv-idol\|Y2K · 暖调 DV 千禧偶像]] | 真人摄影 vs 3D 渲染 |
| [[visual-kei-kote-cold-black\|Kote-kei 冷黑肖像]] | 舞台戏剧 vs 日常切片 |

# 产物记录 Outputs

| 日期 | 类型 | 版本 | 路径 | 评价 |
|---|---|---|---|---|
| 2026-10-17 | 静帧（即梦 2K） | v1 | ![[v1-2026-10-17-jimeng-2k-a.png]] | ❌ **失败**：介质太现代（皮肤渐变/软阴影/无噪点/电饭煲 LCD 穿帮） |
| 2026-10-17 | 静帧（即梦 2K） | v1 | ![[v1-2026-10-17-jimeng-2k-b.png]] | ❌ **失败**：同上 |
| 2026-10-17 | 静帧（即梦 1.5K） | v1.5 | ![[v1.5-2026-10-17-jimeng-1.5k.png]] | ⚠️ **部分达标**：头发/布局/配色正确；皮肤仍渐变、光照仍柔和、无介质噪点 |

## 产物评价与诊断 Diagnosis

**v1/v1.5 核心问题**：模型把 prompt 理解为"**低模风格的现代动漫 CG**"，而不是"真正的 PS2 实时渲染"。

| 配方要求 | v1 (2K) | v1.5 (1.5K) | 目标 |
|---|---|---|---|
| 皮肤：平涂 | ❌ 渐变 + 红晕 | ❌ 仍有渐变 | 平涂单色 |
| 眼睛：贴图画 | ❌ 详细瞳孔 | ⚠️ 简化但有高光 | 简单点眼 |
| 贴图：像素化 | ❌ 清晰 | ⚠️ 略模糊 | 64×64 像素 |
| 光照：硬阴影 | ❌ 柔 AO | ⚠️ 改善但仍有 AO | vertex lighting |
| 介质噪点 | ❌ 无 | ❌ 无 | 扫描线 + 噪点 |
| 头发：块状 | ⚠️ 块状但有 shading | ✅ 明确块状 | 块状三角面 |
| 服装/场景 | ✅ | ✅ | — |

**根因**：
1. "PS2"被当代认知污染（当代玩家认识的 PS2 多是高清重制版）
2. "low-poly"被理解为"风格化"，只影响头发不影响皮肤/光照
3. 2K 分辨率把 prompt 里的 `640x480 render resolution` 冲掉
4. 负向词漏了 `ambient occlusion, soft shadows`（现代渲染的隐形签名）

**v2 修正方向**（详见 [[low-poly-3d-render|低多边形 3D 渲染]] 实测失败案例）：
介质锚定升级为 `1998 PS1 on CRT TV`、显式平涂皮肤、显式硬阴影、显式介质噪点、平台选最低分辨率档。

**平台限制**：即梦最低 1K，对真正的 PS1 低模感仍然太高。**用户考虑转向千问或 ComfyUI + PS1 LoRA**。

# 版本历史 Version History

- **v1（2026-10-17）**：首次锁定（draft）——用户指定"男生、少年感、厨房早餐→机车→铁馆"视频方向；
  图片先行验证，视频 4 镜头分镜。
- **v1.5（2026-10-17）**：即梦分辨率降到 1.5K，头发/布局/配色达标；皮肤/光照/噪点仍偏现代。
  用户决定转向千问或 ComfyUI 平台。
