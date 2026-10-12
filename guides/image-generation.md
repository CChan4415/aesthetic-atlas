---
type: Guide
title: 图片生成规范
description: 将风格配方或临时选择组装为图像模型 prompt、负向词与参数的规范。
tags: [guide, image-generation, prompt]
status: stable
generated: { by: human:cc, at: 2026-10-12T00:00:00+08:00 }
---

# 图片生成规范

## 1. Prompt 组装顺序

按以下顺序拼接英文描述，**先具体后抽象**，逗号分隔；每类只保留最有信息量的 2–4 个词：

```
[主体 subject] + [表情/姿态 expression/pose] + [发型妆容 hair/makeup]
+ [服装 wardrobe] + [配饰 accessories] + [动作 action]
+ [场景/道具 setting/props] + [构图/景别/镜头 composition/camera/lens]
+ [光影 lighting] + [材质 materials] + [配色 color palette]
+ [画面质感/调色/颗粒 grade/texture/grain] + [情绪 mood] + [风格年代与参考 style era/refs]
```

原子概念文件的 `Prompt Keywords` 段落即为可直接取用的词组；配方文件的 `# Image Prompt` 已预组装。

## 2. 标准模板

```
<archetype>, <face/skin>, <expression>, <hair>, <makeup>, wearing <outfit layers>,
<accessories>, <pose/action>, in <setting> with <props/dressing>,
<shot size>, <camera angle>, <lens>, <composition>,
<lighting>, <materials>, <color palette> tones,
<grade/texture/grain/overlay>, <mood> vibe, Y2K year-2000 aesthetic, <reference anchors>
```

## 3. 负向词库（**两层结构**：内容层 + 介质层）

> ⚠️ **v2 重要修正**：v1 的负向词只有"内容层"，导致 Y2K 配方生成的图**年代道具对、但影像是当代高清**。
> 详见 [[anti-modern-digital|去现代数码感]] 的失败案例。

### 3.1 内容层（画面里有什么）
- 通用：`lowres, bad anatomy, bad hands, extra fingers, deformed, blurry, watermark, text artifacts`
- 保年代感：`smartphones, modern smartphone, wireless earbuds, airpods, LED strip lights, modern furniture, contemporary interior, 2020s fashion, current makeup trends`

### 3.2 介质层（**怎么拍的** —— 做旧风格必需，最容易漏）
```
modern digital photography, contemporary photo, high dynamic range, HDR, DSLR,
sharp modern lens, tack sharp, ultra detailed skin, flawless skin, retouched skin,
denoised, noise reduction, clean shadows, professional studio lighting, softbox,
editorial fashion photography, shallow depth of field, bokeh, cinematic color grade,
modern color grading, 8k, high resolution, CG render, 3d render, digital painting,
airbrushed, plastic skin, waxy skin, overly smooth, clean crisp modern image quality
```

### 3.3 按方向的取舍
| 方向 | 介质层负向词 | 理由 |
|---|---|---|
| **怀旧/年代**（Y2K、胶片、DV）| **必加**（完整介质层）| 模型默认输出当代高清，必须压制 |
| **当代戏剧**（Visual Kei Kote-kei）| **不要加** | 它要的就是锐利高清，加了会削弱 |
| 真人质感 | 追加 `3d render, plastic skin, doll-like` | 避免塑料感 |
| 虚拟人偶方向 | **反向**：不加上述词 | 就是要非人感 |

## 3.4 介质锚定 Medium Anchoring（正向，与负向同等重要）

**只加负向词不够**，必须正向声明**拍摄介质**，模型才会切换到对应的成像模型：

| 目标 | 正向锚定写法 |
|---|---|
| 千禧家用 DV | `SHOT ON A 2000s CONSUMER DV CAMCORDER, low-resolution 4:3 interlaced video frame` |
| VHS 录像带 | `VHS tape transfer, analog video artifacts, soft muddy image` |
| 千禧傻瓜胶片机 | `shot on a 2000s point-and-shoot film camera, 35mm, harsh flash, film grain` |
| 杂志内页扫描 | `scanned from a 2000s magazine page, halftone print texture` |
| 早期 CCD 数码 | `shot on an early 2000s CCD digital camera, harsh direct flash, blown highlights` |

**写法要点**：
1. **放在 prompt 最前面**（模型对前置 token 权重更高）
2. **用独立句子大写强调**，不要埋在逗号串里
3. 明确写 `NOT a modern digital photograph`
4. 质感强度必须**写明**（轻/中/重）——只写 `VHS grain` 时模型取最保守值，几乎不可见

## 4. 画幅与用途

| 比例 | 用途 |
|---|---|
| 1:1 | 头像、杂志封面感、卡片 |
| 4:5 / 3:4 | 小红书/Instagram、竖版封面、人物海报 |
| 9:16 | 手机全屏、竖屏视频首帧 |
| 16:9 | 横屏视频首帧、Banner |
| 4:3 | DV/老电视/千禧家庭照片原生比例（做旧风格首选） |

> ⚠️ **画幅必须用平台原生参数设置，不要只写在 prompt 文字里。**
> 实测（即梦 Seedream 5.0 Lite）：prompt 里写 `4:3` / `3:4` **会被忽略**，输出 9:16。
> 应在生成界面的画幅/比例选项中显式选择，prompt 中的画幅描述仅作辅助。

## 5. 角色一致性（系列图/图生视频）

1. 同一角色固定：面孔描述、发型发色、标志性配饰、肤色；使用同一 seed 或角色参考图。
2. 先出 1 张"定妆照"，用户确认后作为后续所有图/视频的参考图输入。
3. 换装/换场景时只改对应段落，人物段落逐字复用。
4. 视频首帧优先使用已确认的静帧，保证主角不"换脸"。
5. **本库落地优先**：确认的定妆照应存入 `assets/`，不要只留外部链接。

## 6. 质量检查（交付前）

- **介质检查（做旧风格必查）**：这是"当代照片"还是"当年的影像"？颗粒/色偏/锐度是否真的到位？
- **年代道具**是否穿帮（尤其**手机**——最常出现）；
- 手指、配饰、文字是否崩坏；
- 配色是否符合配方 hex 区间；质感强度是否符合约定的"新旧程度"；
- 构图与景别是否达成；**画幅是否与目标一致**；主体是否为画面焦点。

## 7. 失败归档（本库的复利机制）

**每次生成失败都应回填到配方的「产物评价与诊断」段**，并提炼为元素页的「常见失败」。

理由：审美是长尾问题，同一类失败会反复发生。
本库已记录的两个真实案例：
- **Y2K 配方**：年代感完全丢失（介质层缺失）→ 催生 [[anti-modern-digital|去现代数码感]]
- **Visual Kei 配方**：画幅被忽略 → 催生本节的画幅警告

> **不要删除失败记录**。它们是这个资产库区别于"一堆好看图片"的核心价值。
