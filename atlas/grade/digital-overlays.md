---
type: Visual Element
title: 后期叠层（Digital Overlays）
description: 时间码、REC 标识、贴纸、边框、UI 元素、星形闪光、监控 bounding box、双语字幕等后期图形叠层。
tags: [y2k, retro-game-cg, grade, overlay, graphics, cctv, subtitle]
status: stable
generated: { by: human:cc, at: 2026-10-12T00:00:00+08:00 }
---

# 枚举

| 中文 | EN Keyword | 适用 |
|---|---|---|
| 时间码/REC | `camcorder timestamp, REC indicator, blinking battery` | Y2K / DV |
| 贴纸 | `Y2K stickers, butterfly / heart / star graphics` | Y2K Sweet Candy |
| 边框 | `rounded frame, polaroid border, CRT bezel` | Y2K / 拍立得 |
| UI/界面 | `retro UI pop-ups, windows, dialog boxes` | Retro Future |
| 闪光星芒 | `sparkle starbursts, lens stars` | Y2K / Kirakira |
| **监控 bounding box** | `red bounding box overlay, object detection rectangle, tracking ID label, surveillance HUD` | Retro Game CG / CCTV |
| **双语字幕条** | `bilingual subtitles, English subtitle with Chinese below, hardcoded subtitles, fan-sub style` | Retro Game CG 短片 |
| **斜体标语** | `*italic action line, *scene description, fanfiction-style caption, roleplay stage direction` | Retro Game CG / 同人短片 |
| **作者水印** | `watermark with @username, bottom-center attribution, social media watermark` | 同人 CG / 短视频 |

## Prompt Keywords

`Y2K digital overlays, camcorder timestamp, playful stickers and frames, retro UI elements,
sparkle graphics, early-2000s on-screen decoration, red bounding box overlay, surveillance HUD,
object detection rectangle, bilingual subtitles, *italic action line, roleplay caption,
hardcoded fan-sub, watermark with @username`

# 监控 bounding box（Retro Game CG 子类）

> 源自 2000s 游戏引擎 debug 视角与同期 CCTV 监控界面的混合美学。
> 在 @鴉鴉的幻覺 的走廊监控视频中典型：**红色矩形框 + 编号 ID + 跟踪线**，
> 把人物框起来，像 AI 在标记目标。

**视觉特征**：
- 红色或绿色矩形框，框住人物或物体
- 框上方标数字 ID（如 `7758258-011`）
- 可能带连线（指向画面中央或标签）
- 字体是简单等宽字体（终端感）

**Prompt 关键词**：
`red bounding box overlay, object detection rectangle with tracking ID, surveillance HUD element,
digital wireframe box around figure, debug view, 2000s CCTV interface, numbered target marker`

**搭配**：[[security-camera-cctv|监控视角]]、[[low-poly-3d-render|低多边形 3D]]

# 双语字幕条（Retro Game CG 子类）

> 同人短片与虚拟主播圈的标志——英文台词在上、中文翻译在下（或反向），
> 字号小、带描边、底部居中。也常用 `*斜体` 表示场景描述或动作提示（类似剧本舞台指示）。

**视觉特征**：
- 底部居中，英文在上中文在下
- 白色字体 + 黑色描边（或反之），确保任何背景下可读
- 字号小，占画面高度 3-5%
- 斜体行表动作：`*No running in the hallways`、`*禁止在走廊内奔跑`

**Prompt 关键词**：
`bilingual subtitles, English on top Chinese below, hardcoded fan-sub, small white text with black outline,
*italic action line, stage direction caption, roleplay subtitle, fan translation overlay`

**搭配**：[[ps2-fmv-grade|PS2 FMV]]、[[lowpoly-jk-character|低多边形 JK 角色]]

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| **现代 TikTok 字幕** | 那是动态大字、居中跳字；本元素是静态底部小字 |
| **电影字幕** | 电影字幕更精致、无描边；本元素是同人/小剧场风 |
| **HUD 游戏界面** | HUD 是血条/小地图等功能元素；bounding box 是监控/调试视角 |

# 生成提示 / 常见失败

- **bounding box 容易被模型忽略**：可在 prompt 里强调 `red bounding box drawn around the figure, with tracking ID number above`
- **双语字幕容易只出英文**：明确写 `English subtitle on top, Chinese subtitle below` 或反之
- **水印是签名不是装饰**：`@username watermark at bottom center`——AI 会自己编一个，可能不是真账号

# 来源 Sources

- [[raw/videos/_source|raw/videos/_source.md]] — @鴉鴉的幻覺 走廊监控视频（bounding box + 双语字幕）
