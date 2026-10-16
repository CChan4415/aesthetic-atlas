---
type: Visual Element
title: 监控视角 / CCTV 高角度（Security Camera / CCTV Angle）
description: 走廊尽头、天花板角落的固定高角度监控摄像头视角——画面带 surveillance 感，常与 bounding box、时间码叠层搭配。
tags: [retro-game-cg, camera, cctv, surveillance, high-angle, fixed]
status: draft
generated: { by: agent:deepseek, at: 2026-10-16T20:45:00+08:00 }
sources:
  - id: raw-videos-2026-10
    resource: /raw/videos/
    title: 千禧年低多边形 3D 短片合集
    author: "@鴉鴉的幻覺"
---

# 定义 Definition

**监控视角**指模拟**固定监控摄像头**（CCTV / surveillance camera）的拍摄视角：
- 位置：走廊尽头天花板角落、室外电线杆、商场高处
- 角度：俯视 15–45°
- 镜头：广角、固定（不摇不移）
- 画幅：常带画面畸变（广角桶形畸变）

> **核心心理效果**：监控视角让观众成为"观察者"，被拍摄者不知情——
> 制造窥视感、孤独感、被监视的不安，是 2000s 同人恐怖/悬疑短片的核心镜头。

# 视觉特征 Visual Cues

- **位置高**：相机在画面主体上方 2–4 米
- **俯视**：俯角明显，地面占画面 50%+
- **固定**：镜头不动，主体在画面中走动
- **广角**：走廊、大厅全景尽收
- **畸变**：广角桶形畸变，画面边缘弯曲
- **画质**：常故意做旧（噪点、色差、扫描线），模拟监控摄像头低画质

## Prompt Keywords

`security camera angle, CCTV perspective, surveillance footage, high-angle fixed camera,
corridor end view, ceiling-mounted camera, wide-angle surveillance lens, barrel distortion,
monitoring footage, observed from above, fixed surveillance view, anonymous observation,
top-down corridor shot, 2000s CCTV aesthetic, security cam footage, watched from a distance`

# 适用风格 Applies To

- **必需**：[[retro-game-cg|Retro Game CG]] 的 **CCTV 故障感** 子风格
- **搭配**：[[y2k-retro-future|Retro Future]]（监控是早期互联网美学的一部分）
- **不适用**：[[visual-kei|Visual Kei]]（视觉系要舞台化的主动镜头，不是被动监控）

# 搭配建议 Pairs With

- [[low-poly-3d-render|低多边形 3D 渲染]]——监控画面质感
- [[digital-overlays|监控 bounding box]]——红色矩形框 + ID
- 场景：[[school-corridor-cctv|学校走廊监控]]、[[mall-arcade|商场/游戏厅]]
- 光影：荧光灯顶光（无方向性散射光）
- 情绪：孤独、被观察、不安

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| **俯视（bird's eye / top-down）** | 俯视是 90° 正上方；监控视角是 15–45° 斜俯视 |
| **第三人称游戏视角** | 第三人称跟随主体；监控视角固定不动 |
| **无人机航拍** | 航拍在户外高空、会移动；监控在室内低角度、固定 |

# 生成提示 / 常见失败

- **模型容易把"监控"理解为"画面右下角加时间戳"**：必须明确 `high-angle fixed camera in the corner of the corridor, looking down at the figure`
- **俯角不够**：补充 `looking down from ceiling height, 30 degrees angle`
- **畸变缺失**：广角监控的桶形畸变是重要细节，`wide-angle lens with barrel distortion`
- **画质太清晰**：监控画面应**比实时渲染更脏**——`compressed video, low resolution, slight scanlines`

# 来源 Sources

- [[raw/videos/_source|raw/videos/_source.md]] — @鴉鴉的幻覺 走廊监控视频（典型范例）
