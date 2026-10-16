---
type: Style Recipe
title: Visual Kei · Kote-kei 冷黑肖像（Cold Black Kote-kei Portrait）
description: 全黑西装、石膏白妆、尖刺立发的经典日系视觉系配方，强单点硬光与高对比质感，含图/视频双 prompt。
tags: [visual-kei, recipe, kote-kei, dark, portrait]
status: stable
generated: { by: agent:deepseek, at: 2026-10-12T10:40:00+08:00 }
version: '1'
---

# 一句话 One-liner

一位性别模糊的日系视觉系表演者，石膏般惨白的脸、上挑的粗黑眼线、
向后硬挺的黑色尖刺立发，穿着修身黑西装与蕾丝细节，站在一束聚光灯下的纯黑空间里——
冷峻、锐利、有压迫感，像一张 2000 年代视觉系乐队的宣传照。

# 适用场景 Use Cases

视觉系人物定妆照；暗黑系音乐视频主角；情绪向短视频封面；
高对比人物海报；**图生视频的首帧**（强光影 + 长发/长下摆，动态余地大）。

# 锁定决策 Locked Decisions（风格签名）

> 以下元素链接到原子图鉴；`locked` 为风格签名，`tunable` 可按项目替换。

| 维度 | 决策 | 状态 |
|---|---|---|
| 风格运动 | [[visual-kei\|Visual Kei 视觉系]] | locked |
| 子风格 | [[visual-kei-kote-kei\|Kote-kei 古典系]] | locked |
| 角色原型 | 性别模糊的日系表演者（androgynous，非特定偶像） | locked |
| 底妆 | [[white-foundation\|石膏白妆]]（瓷白、哑光、可见颈部色差） | locked |
| 眼妆 | [[winged-eyeliner\|上挑粗黑眼线]] + [[smoky-eye-visual-kei\|深色烟熏]] | locked |
| 唇妆 | [[dark-lips\|苍白唇 / 暗色唇]]（取失血感） | locked |
| 发型 | [[spiky-styled-hair\|尖刺立发]]，或 [[eye-covering-bangs\|遮眼刘海]] 长发变体 | locked |
| 服装 | [[black-tailored-suit\|黑色修身西装]]（长下摆），黑衬衫 | locked |
| 材质 | [[leather-and-hardware\|皮革与金属件]] + [[lace-and-tulle\|蕾丝与网纱]] | locked |
| 配饰 | choker、长皮手套、银质金属件 | locked |
| 配色 | [[visual-kei-monochrome\|视觉系·黑白冷调]] | locked |
| 光影 | [[dramatic-single-source\|强单点光]]（侧光或顶光，硬阴影） | locked |
| 场景 | [[dark-stage\|空旷舞台与暗厅]]（纯黑背景 + 聚光灯） | locked |
| 镜头/构图 | 平视、半身或胸像、居中；竖版 3:4 或 2:3 | locked |
| 画面质感 | [[high-contrast-grade\|高对比戏剧质感]]，中度，轻微去饱和 | locked |
| 情绪 | [[cold-futuristic\|冷峻疏离]]，带危险感 | locked |
| 姿态 | 直立、微侧脸、或单手抚发 | tunable |
| 是否遮眼 | 单侧遮眼 / 双眼可见 | tunable |
| 背景具体化 | 纯黑场 / 舞台 / 老旧洋馆 | tunable |
| 是否持乐器 | 空手 / 麦克风 / 吉他 | tunable |

# Image Prompt（EN，已组装）

```
An androgynous Japanese visual kei performer, extreme pale porcelain white foundation with a
mask-like matte finish, visible contrast against the neck, sharp thick black winged eyeliner
dramatically elongated at the outer corners, heavy smudged dark smoky eyeshadow in black and
charcoal, bloodless pale lips, naturally thin arched brows; short black hair styled into
sculptural rigid spikes with heavy styling product, sharply gelled and directional; wearing a
slim-fit black tailored suit with a long coat tail, black high-collar shirt, black leather
harness straps with silver buckles, black lace trim at the cuffs, silver choker, long black
leather gloves; standing upright with a slight three-quarter turn, one hand raised near the
face; in an empty dark space with a single hard spotlight from the side, deep crushed blacks,
harsh hard-edged shadows falling across the face, faint haze in the air; eye-level medium
close-up portrait, centered composition, 3:4 vertical frame; monochromatic black and cold white
palette with silver accents, leather and lace textures, moderate high-contrast dramatic grade
with slight desaturation, cool tones, sharp crisp highlights; cold, distant, dangerous and
theatrical atmosphere, kote-kei visual kei, 2000s J-rock promotional photography
```

# Negative Prompt

```
lowres, bad anatomy, bad hands, extra fingers, deformed, blurry, watermark, text artifacts,
warm tones, sepia, golden tint, yellow cast, natural skin tone, tanned skin, healthy glow,
pink lips, nude natural lips, subtle natural eyeliner, thin minimal makeup, soft natural hair,
flat limp hair, casual hairstyle, soft even lighting, flat lighting, multiple light sources,
studio softbox, bright ambient light, low contrast, washed out, HDR, bright even lighting,
colorful clothing, pastel colors, cheerful expression, smiling broadly, modern 2020s fashion,
smartphones, cluttered background, busy background, crowd
```

# Video Prompt（EN）

```
The performer slowly lifts their gaze to the camera with a cold piercing stare, then with a
sharp deliberate motion whips their head to the side so the spiked hair cuts through the
spotlight; a slow restrained push-in from a static locked-off camera, the single hard
spotlight creating shifting shadows that sweep across the white-painted face as the head
turns, the long suit tail and leather straps swaying slightly with the movement, hair strands
and dust motes drifting through the light beam; extremely slow and deliberate theatrical
pacing, with a long dramatic pause before the head turn, cool desaturated high-contrast grade,
2000s J-rock promotional video mood
```

视频参数建议：3:4 或 9:16，5–8 秒，单镜头，缓慢运镜；
详见 [[video-generation|视频生成规范]]。

# 可调参数 Tunable

- **遮眼**：单侧遮眼（更神秘）或双眼可见（更可读）
- **发型变体**：尖刺立发（最 Kote）或长直发 + 遮眼刘海（更 Angura 邻接）
- **光位**：侧光（塑形最强）/ 顶光（最阴郁）/ 逆光轮廓（黑发分离最佳）
- **背景**：纯黑场（最通用）/ 舞台 / 老旧洋馆（偏 Angura）
- **高对比强度**：中度（推荐）/ 轻度（保留蕾丝细节）/ 重度（接近剪影）
- **画幅**：3:4 / 2:3 / 9:16

# 与其他配方的区别 Differentiation

| 对比 | 差异 |
|---|---|
| [[y2k-warm-dv-idol\|Y2K · 暖调 DV 千禧偶像]] | 那个是**暖调、生活化、怀旧、甜**；本配方是**冷调、舞台化、当下、危险** |
| 一冷一暖、一戏剧一日常，构成本库目前的两极 | 适合验证"风格资产库能否产出气质相反的作品" |

# 产物记录 Outputs

| 日期 | 类型 | 版本 | 路径 | 评价 |
|---|---|---|---|---|
| 2026-10-12 | 静帧 v1（用户即梦生成） | v1 | ![[v1-2026-10-12.png]]（1440×2560） | ✅ **方向达成**，细节待调 |

## 产物评价与诊断 Diagnosis

**v1 成功点**（用户评价：方向对，气质到位）：

| 配方要求 | 实际输出 | 判定 |
|---|---|---|
| 石膏白妆 + 颈部色差 | 惨白面具感明显，颈部可见色差 | ✅ |
| 上挑粗黑眼线 | 锐利、明显拉长上挑 | ✅ |
| 尖刺立发 | 放射状硬挺尖刺，结构感强 | ✅ |
| 黑西装 + 皮革金属件 | 黑西装 + 皮质绑带 + 银扣 + 蕾丝袖口 | ✅ |
| 性别模糊 | 雌雄莫辨，成功 | ✅ |
| 强单点光硬阴影 | 侧光，阴影明确 | ✅ |
| 黑白冷调、去饱和 | 冷调黑白，无暖色污染 | ✅ |

**v1 待改进项**：

| 问题 | 说明 | 修正方向 |
|---|---|---|
| 画幅 9:16 而非 3:4 | prompt 写了 3:4 但被忽略 | 用**平台原生画幅参数**设置，不要只写在 prompt 里 |
| 偏"现代影棚高清" | 皮肤与西装缺材质颗粒 | **本配方不追求年代感**（视觉系是当代戏剧），可接受；要质感可加轻颗粒 |
| 背景成"云雾"而非空旷暗厅 | 生成了烟雾背景 | prompt 明确 `pure black background, empty space, no fog` |
| 举手姿态使手部成焦点 | 手部细节略简化 | 可将"手部是否入画"设为 tunable |

> **重要区分**：本配方**不需要** [[anti-modern-digital|去现代数码感]]。
> Kote-kei 追求"当代戏剧高清"，年代做旧会削弱其锐利感——
> 这是它与 Y2K 配方的**根本分野**，不要盲目套用 Y2K 的修正。

# 版本历史 Version History

- **v1（2026-10-12）**：首次锁定——Kote-kei 冷黑肖像，黑白冷调、尖刺立发、白妆、强单点光。
  用户以即梦 Seedream 5.0 Lite 生成，方向验证通过；待改进项见上方诊断。
