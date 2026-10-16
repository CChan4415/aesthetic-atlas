---
type: Style Recipe
title: Y2K · 暖调 DV 千禧偶像（Warm DV Millennium Idol）
description: 橙粉/古铜/脏金暖调、老DV与杂志质感的亚洲偶像少女配方，含图/视频双prompt。
tags: [y2k, recipe, warm, idol, dv]
status: stable
generated: { by: human:cc, at: 2026-10-12T00:00:00+08:00 }
version: '1'
---

# 一句话 One-liner

一位 2000 年代亚洲偶像感少女，在贴满海报的暖光卧室里，金属吊带叠穿薄开衫、低腰裤与闪亮配饰，  
画面像一台老 DV 拍下的千禧杂志内页——橙粉、古铜与脏金色调，亲密、怀旧、甜而有分寸。

# 适用场景 Use Cases

人物向短视频主角定妆照；怀旧 MV 风、千禧杂志写真、情绪向 vlog 封面；后续图生视频的首帧。

# 锁定决策 Locked Decisions（风格签名）

> 以下元素链接到原子图鉴；`locked` 为风格签名，`tunable` 可按项目替换。

| 维度 | 决策 | 状态 |
|---|---|---|
| 子风格 | [[y2k-sweet-candy\|Sweet Candy 千禧甜酷]] + 暖调做旧 | locked |
| 角色原型 | [[asian-millennium-idol\|亚洲千禧偶像]] | locked |
| 肤色 | [[face-and-skin\|蜜色健康 / 蜜桃水光]] | locked |
| 表情 | [[expressions\|抓拍说笑 / 回眸]] | tunable |
| 姿态 | [[poses\|坐床沿 / 单手叉腰]] | tunable |
| 发型 | [[face-framing-highlights\|脸际高光碎发]] + [[chunky-highlights\|块状挑染]]，中长发、蓬松光泽 | locked |
| 眼妆 | [[frosted-eyeshadow\|暖金霜状眼影]] | locked |
| 腮红 | [[sunburnt-blush\|晒伤暖橘腮红]] | locked |
| 唇妆 | [[glossy-lips\|镜面蜜桃唇彩]] | locked |
| 眉形 | [[thin-arched-brows\|自然微挑眉]]（不过度细） | locked |
| 内搭 | [[metallic-cami\|古铜/脏金金属吊带]] | locked |
| 层叠 | [[sheer-cardigan\|暖棕薄开衫]]，松垮披搭 | locked |
| 下装 | [[low-rise-jeans\|低腰做旧牛仔裤]] | locked |
| 鞋履 | [[platform-sandals\|厚底凉鞋]] | tunable |
| 首饰 | [[choker\|choker]] + [[belly-chain\|肚链]] + [[rhinestone-jewelry-set\|水钻叠戴]] | locked |
| 包/眼镜 | [[mini-bag\|迷你包]]、[[wrap-sunglasses\|包裹式墨镜]]（可手持/戴头顶） | tunable |
| 身体装饰 | [[body-glitter\|锁骨身体亮片]] | locked |
| 场景 | [[poster-bedroom\|海报卧室]] | locked |
| 道具/装饰 | [[desktop-crt\|台式 CRT]]、[[plushies\|毛绒玩具]]、[[band-posters\|海报墙]]、[[lava-lamp\|熔岩灯]]、[[flip-phone\|翻盖手机]] | tunable |
| 配色 | [[warm-dv-bronze-palette\|暖调 DV 古铜脏金]] | locked |
| 材质 | [[gold-lame\|金葱]]、[[sequins-beading\|亮片水钻]]、[[denim-wash\|牛仔]] | locked |
| 光影 | [[warm-tungsten\|暖色钨丝台灯]] 为主，可混 [[direct-flash\|闪光灯]] | locked |
| 镜头/构图 | 平视、半身或膝上中景、居中或三分；4:3 DV 画幅 | locked |
| 画面质感 | [[vhs-dv-texture\|VHS/DV 质感 轻–中度]] + [[magazine-flash-grade\|千禧杂志调色]] + 轻微 [[lens-flare-haze\|光晕]] | locked |
| 情绪 | [[nostalgic-bittersweet\|怀旧微苦]]，带俏皮 | locked |

# Image Prompt（EN，已组装 · v2）

> **v2 结构性改动**：v1 把质感写在 prompt 末尾一处，被前面 200 词淹没，导致模型输出  
> 当代高清数码照片（见 [[anti-modern-digital|去现代数码感]] 的失败案例记录）。  
> v2 改为**介质前置 + 三段式**结构。

```
SHOT ON A 2000s CONSUMER DV CAMCORDER — this is a low-resolution 4:3 interlaced video frame
captured off a home camcorder, NOT a modern digital photograph. Visible analog tape grain and
soft scanlines, chroma aberration with RGB color fringing, warm orange color cast, blown-out
highlights and lifted milky blacks, noticeably soft focus with compression blockiness, slight
halation around bright lights. Deep 2000s amateur home-video look.

An early-2000s East Asian idol girl, honey-beige peachy skin with visible powder foundation
texture (not airbrushed), soft candid expression with a slight smile, medium-length voluminous
hair with face-framing wispy highlights and subtle chunky honey highlights, warm gold frosted
eyeshadow, sunburnt coral blush across the nose, glossy peach lips; wearing a bronze / dirty-gold
metallic camisole layered under a slouchy warm-brown sheer knit cardigan, low-rise faded jeans,
rhinestone choker and layered crystal necklaces, gold belly chain, body glitter on the collarbones,
long decorated acrylic nails, a mini bag and wrap-around sunglasses in hand; sitting on the bed in
a cozy early-2000s teenage bedroom, walls covered in band and idol posters and magazine clippings,
CRT desktop computer, plush toys, lava lamp, fairy lights, a flip phone on the bed (NO modern
smartphone).

Harsh on-camera direct flash, slightly overexposed, warm tungsten lamp glow from the side,
eye-level medium shot, centered composition, 4:3 frame, warm bronze / peach / dirty-gold palette,
gold lame and sequin sparkle, early-2000s magazine editorial grade, nostalgic bittersweet Y2K vibe
```

**关键差异**（对照 v1）：

| 改动         | v1                   | v2                                                   |
| ---------- | -------------------- | ---------------------------------------------------- |
| 介质声明       | 无                    | **开头独立大写句**，明确"DV 摄像机拍摄的录像帧"                         |
| 质感位置       | 末尾                   | **最前面**（模型对前置 token 权重更高）                            |
| 隐含"不是现代照片" | 无                    | 显式写入 `NOT a modern digital photograph`               |
| 皮肤质感       | `dewy skin`（易生成磨皮）   | `visible powder foundation texture (not airbrushed)` |
| 打光         | `touch of flash`（太弱） | `Harsh on-camera direct flash, slightly overexposed` |
| 手机穿帮       | 负向词里有，仍出现            | 正向补 `(NO modern smartphone)`                         |

# Negative Prompt（v2 · 两层结构）

**内容层**（年代道具穿帮）+ **介质层**（现代摄影特征）——v1 只有内容层，这是失败主因。

```
lowres, bad anatomy, bad hands, extra fingers, deformed, blurry, watermark, text artifacts,
modern objects, smartphones, modern smartphone, wireless earbuds, airpods, LED strip lights,
modern furniture, contemporary interior, 2020s fashion, current makeup trends,
modern digital photography, contemporary photo, high dynamic range, HDR, DSLR,
sharp modern lens, tack sharp, ultra detailed skin, flawless skin, retouched skin,
denoised, noise reduction, clean shadows, professional studio lighting, softbox,
editorial fashion photography, shallow depth of field, bokeh, cinematic color grade,
modern color grading, 8k, high resolution, CG render, 3d render, digital painting,
airbrushed, plastic skin, waxy skin, overly smooth, cold blue-white color grade,
clean crisp modern image quality
```

# Video Prompt（EN，备用；本次不生成）

```
The girl lifts her gaze to the camera with a natural candid laugh, then flips her hair and looks
back over her shoulder; subtle handheld camcorder sway with a very slow push-in, gentle breeze
moving her face-framing strands and the sheer cardigan, glowing dust and glitter motes floating in
the warm lamp light, reflections gliding across her metallic cami and rhinestones; slow dreamy
pacing, occasional VHS tracking bar and dropped frames, soft frame-blend ghosting, warm nostalgic
Y2K home-movie feel
```

视频参数建议：4:3 或 9:16，5–8 秒；详见 [[video-generation|视频生成规范]]。

# 可调参数 Tunable

表情与姿态、鞋履、具体道具、墨镜是否佩戴、DV 颗粒强度（轻/中/重）、画幅（4:3 / 3:4 / 9:16）。

# 产物记录 Outputs

| 日期         | 类型            | 版本 | 路径                                                                        | 评价                         |
| ---------- | ------------- | -- | ------------------------------------------------------------------------- | -------------------------- |
| 2026-10-12 | 静帧 v1         | v1 | \![[v1-2026-10-12.png]]（另存 CDN：<https://aka.doubaocdn.com/s/LtVVF5U004> ） | ⚠️ **偏现代**，年代感不足           |
| 2026-10-12 | 静帧 v1（用户即梦生成） | v1 | \![[v1-2026-10-12-jimeng.png]]（1440×2560）                                 | ❌ **失败**：无复古质感、画幅错误、出现现代手机 |

## 产物评价与诊断 Diagnosis

**v1 的问题**（两版均存在，用户明确指出"太现实了，没有 2000s 复古质感"）：

| 配方要求             | 实际输出            | 判定      |
| ---------------- | --------------- | ------- |
| VHS/DV 质感、扫描线、色差 | 干净锐利的现代数码照片     | ❌ 质感层丢失 |
| 4:3 或 3:4 画幅     | 9:16（1440×2560） | ❌ 画幅被忽略 |
| 闪光灯直打 / 暖钨丝台灯    | 柔和影棚光           | ❌ 光质被替换 |
| 暖调古铜脏金、轻微过曝      | 现代调色、中灰         | ❌ 调色丢失  |
| 无现代物品            | 床上出现现代智能手机      | ❌ 年代穿帮  |

**根因**（详见 [[anti-modern-digital|去现代数码感]]）：

1. 质感只写在 prompt 末尾一处，被主体描述淹没
2. 负向词只排除**内容层**（现代物品），未排除**介质层**（HDR/DSLR/磨皮/降噪）
3. 未声明**拍摄介质**（没有 "shot on 2000s DV camcorder"）
4. 画幅只写在 prompt 文字里，**未用平台原生画幅参数**设置

**v2 修正**：介质前置 + 三段式结构 + 两层负向词 + 平台参数设置画幅（见上方 Image Prompt）。

> **教训**：年代感 ≠ 道具年代感。**介质层（怎么拍的）比内容层（拍了什么）更难控制，且必须显式压制。**

# 版本历史 Version History

- **v1（2026-10-12）**：首次锁定——暖调 DV 亚洲偶像、混搭层叠、海报卧室。
- **v2（2026-10-12）**：**修复现代感问题**——介质前置、强化质感描述、负向词分内容层+介质层、  
  明确打光强度、正向补充"无现代手机"。新增 [[anti-modern-digital|去现代数码感]] 元素页。
