---
type: Style Recipe
title: PS2 低多边形 JK 校园日常（PS2 Low-Poly JK Slice-of-Life）
description: 2000s PS1/PS2 游戏渲染风格的低多边形 JK 校园日常——块状头发、贴图五官、走廊/食堂/地下通道场景，含图/视频双 prompt。
tags: [retro-game-cg, recipe, lowpoly, jk, ps2, slice-of-life, 3d]
status: draft
generated: { by: agent:deepseek, at: 2026-10-16T21:00:00+08:00 }
version: '1'
sources:
  - id: raw-videos-2026-10
    resource: /raw/videos/
    title: 千禧年低多边形 3D 短片合集
    author: "@natural water / @鴉鴉的幻覺 / @龙崎日舞"
---

# 一句话 One-liner

一位低多边形 3D 风格的 JK 少女，块状三角面头发、贴图绘制的眼睛、穿着 JK 制服
（米色开衫 + 格子裙），在学校走廊 / 食堂 / 地下通道中行走或独自停留——画面像一台
PS2 游戏的实时渲染截图，孤独、青春、微压抑。

# 适用场景 Use Cases

千禧年 3D 复古短片主角定妆；校园日常系 MV / 短片；同人 CG 插图；
虚拟主播切片封面；**图生视频的首帧**（低模风格延续到视频）。

# 锁定决策 Locked Decisions（风格签名）

| 维度 | 决策 | 状态 |
|---|---|---|
| 风格运动 | [[retro-game-cg\|Retro Game CG · 复古游戏 CG]] | locked |
| 子风格 | Low-Poly JK Slice-of-Life（校园日常） | locked |
| 角色原型 | [[lowpoly-jk-character\|低多边形 JK 角色]] | locked |
| 渲染介质 | [[low-poly-3d-render\|低多边形 3D 渲染]]（中度：PS2 世代实时渲染） | locked |
| 服装 | JK 制服（白衬衫 + 米色开衫 + 黑蝴蝶结 + 格子百褶裙 + 及膝袜 + 乐福鞋） | locked |
| 发型 | 长直发（遮眼刘海）或双麻花辫，块状三角面 | locked |
| 配色 | 低饱和灰绿/青蓝/暗黄，整体偏冷 | locked |
| 镜头 | [[security-camera-cctv\|监控视角]]（高角度固定）或 [[third-person-game-camera\|第三人称游戏视角]]（背后跟随） | locked |
| 场景 | [[school-corridor-cctv\|学校走廊]] / [[underground-passage-tiled\|地下通道]] / [[school-cafeteria-3d\|学校食堂]] | locked |
| 光影 | 荧光灯冷白光 / 暖色钨丝灯 / 午后阳光斜射 | locked |
| 画面质感 | 低多边形 + 低分辨率贴图 + vertex wobble（视频） + 锯齿 | locked |
| 叠层 | [[digital-overlays\|监控 bounding box + 双语字幕]]（可选） | tunable |
| 情绪 | 孤独、青春、怀旧、微压抑 | locked |
| 表情 | 凝视 / 沉默 / 微低头（不笑） | tunable |
| 姿态 | 行走 / 站立 / 独自用餐 | tunable |

# Image Prompt（EN，已组装 · v1）

> **介质前置**（参考 [[anti-modern-digital\|去现代数码感]] 的"渲染介质"章节）：
> 渲染介质锚定词必须放最前，否则模型会默认输出"当代写实 3D"。

```
RENDERED ON A 2000s PS2 GAME CONSOLE — this is a low-poly 3D real-time game render,
NOT a modern photorealistic 3D image. Visible triangle faces in hair, texture-mapped face
with painted eyes and mouth, simple gradient skin without pores, chunky low-poly hair pieces,
mitten-like blocky hands, jagged polygon edges, low-resolution textures, vertex lighting,
jagged edges without anti-aliasing, 640x480 render resolution, 2000s video game aesthetic.

A low-poly JK girl character with long straight black hair covering one eye (blocky triangle
bangs), texture-mapped face with painted dark eyes and small mouth, simple smooth skin;
wearing a Japanese high school uniform: white shirt, beige knit cardigan, black bow tie,
plaid pleated skirt, knee-high white socks, brown loafers; standing alone in a long empty
school corridor, white tiled walls, fluorescent ceiling lights casting cold white light,
a few band posters and notices taped to the walls, concrete floor with slight reflections.

Surveillance camera angle from ceiling corner, 30-degree downward view, wide-angle lens with
slight barrel distortion, character in the lower third of frame walking away, fixed camera
position; cool desaturated color palette with hints of beige and grey-green; melancholic,
lonely, slice-of-life mood, 2000s Japanese school atmosphere, after-school silence.
```

# Negative Prompt（v1 · 两层结构）

**内容层**（年代穿帮）+ **渲染介质层**（现代 3D 特征）——这是渲染介质版的两层负向词，
对应 [[anti-modern-digital\|去现代数码感]] 的摄影介质版。

```
lowres, bad anatomy, bad hands, extra fingers, deformed, watermark, text artifacts,
modern objects, smartphones, modern furniture, 2020s fashion, LED screens,
photorealistic, real human, live action, unreal engine 5, ray tracing, octane render,
high-poly sculpt, subsurface scattering, realistic hair strands, detailed skin pores,
smooth shading, 8k textures, motion capture, filmic color grading, cinematic lighting,
modern 3D render, pixar style, disney style, contemporary game graphics, sharp 4k render,
glossy reflective skin, detailed iris, realistic eyeballs, individual finger geometry
```

# Video Prompt（EN · v1）

```
The JK girl walks slowly down the corridor, her blocky triangle hair swaying slightly with
each step, vertex wobble causing subtle jitter in her outline, the fluorescent light above
flickering once as she passes under it; fixed surveillance camera holds the shot, she moves
from the center to the lower right corner of frame, her shadow stretching long on the
concrete floor; low frame rate (15 fps) with slight frame skips, slight scanlines and
compression artifacts visible, 2000s game render quality, melancholic pacing, no music
sync, ambient silence feeling, duration 8 seconds, 4:3 frame
```

视频参数建议：4:3 或 9:16，5–10 秒，固定监控视角或缓推；详见 [[video-generation\|视频生成规范]]。

# 可调参数 Tunable

- **场景**：走廊（默认）/ 食堂 / 地下通道 / 教室
- **镜头**：监控高角度（默认）/ 第三人称跟随 / 正面特写
- **发型**：长直发遮眼（默认）/ 双麻花辫 / 中长卷发
- **叠层**：bounding box + 双语字幕 / 仅双语字幕 / 无叠层
- **画幅**：4:3（推荐）/ 9:16（短视频平台）
- **多边形强度**：轻（接近 indie 低模）/ 中（PS2，默认）/ 重（PS1）

# 与其他配方的区别 Differentiation

| 对比 | 差异 |
|---|---|
| [[y2k-warm-dv-idol\|Y2K · 暖调 DV 千禧偶像]] | 那是**真人摄影 + DV 介质**；本配方是 **3D 渲染 + PS2 介质** |
| [[visual-kei-kote-cold-black\|Visual Kei · Kote-kei 冷黑肖像]] | 那是**舞台肖像 + 当代高清**；本配方是**校园日常 + 低模渲染** |
| 三个配方构成"写真 / 舞台 / 游戏"三种介质 | 对应"偶像 / 表演者 / 虚拟角色"三种主体 |

# 产物记录 Outputs

| 日期 | 类型 | 版本 | 路径 | 评价 |
|---|---|---|---|---|
| 2026-10-17 | 静帧（即梦 2K） | v1 | ![[v1-2026-10-17-jimeng-2k-a.png]] | ❌ **失败**：介质偏现代（皮肤渐变/软阴影/无噪点） |
| 2026-10-17 | 静帧（即梦 2K） | v1 | ![[v1-2026-10-17-jimeng-2k-b.png]] | ❌ **失败**：同上 |

## 产物评价与诊断 Diagnosis

两张图走廊+JK 构图正确，但**介质被模型翻译成了"低模风格的现代动漫 CG"**——
头发有块状趋势但皮肤/光照/贴图全是现代渲染。详见 [[ps2-lowpoly-androgynous-male#产物评价与诊断|少年配方的诊断]]（同日同根因）。

# 版本历史 Version History

- **v1（2026-10-16）**：首次锁定——基于 raw/videos/ 4 部参考视频编译。
  介质锚定词参考 [[anti-modern-digital|去现代数码感]] 的"渲染介质"章节（PS2 实时渲染）。
- **v1 实测失败（2026-10-17）**：即梦 2K 出图 2 张全部偏现代。详见 [[low-poly-3d-render]] 的实测失败案例。
  修正方向：v2 改 `PS1 1998 + CRT TV` 锚定 + 显式平涂 + 显式硬光照 + 显式介质噪点，平台选最低分辨率档。
