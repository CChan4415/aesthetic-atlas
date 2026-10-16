---
type: Visual Element
title: 学校走廊监控视角（School Corridor CCTV）
description: 2000s 学校走廊的低多边形 3D 场景——荧光灯、瓷砖墙、储物柜、尽头门，常配监控摄像头视角与 bounding box 叠层。
tags: [retro-game-cg, setting, school, corridor, cctv, 3d]
status: draft
generated: { by: agent:deepseek, at: 2026-10-16T20:53:00+08:00 }
sources:
  - id: raw-videos-2026-10
    resource: /raw/videos/
    title: 千禧年低多边形 3D 短片合集
    author: "@鴉鴉的幻覺"
---

# 定义 Definition

**学校走廊监控视角**是 2000s 同人 CG 与低多边形游戏中的经典场景：
- 长长的学校走廊（光线昏暗、尽头有门）
- 天花板的荧光灯（闪烁或部分损坏）
- 两侧瓷砖墙或储物柜
- 视角是监控摄像头（高角度、固定、俯视）

> **核心氛围**：**压抑的青春**——学校是日常，但监控视角把它变成"被观察的囚笼"。

# 视觉特征 Visual Cues

- **走廊**：狭长、尽头有门或窗、地面是水泥或瓷砖
- **墙面**：白色或浅色瓷砖、可能有公告栏、消防栓、污渍
- **天花**：裸露管线 + 长条形荧光灯（一盏或多盏）
- **光线**：荧光灯冷白光、整体偏暗、可能有局部更暗的区域
- **道具**：墙边消防栓、灭火器、垃圾桶、公告栏、储物柜
- **叠层**：bounding box、时间码、REC 标识（配合监控视角）

## Prompt Keywords

`school corridor, long empty hallway, ceiling fluorescent lights, tiled walls, lockers,
fire extinguisher on wall, bulletin board, end of corridor door, dim lighting, cool white light,
2000s school interior, low-poly corridor, surveillance camera view, CCTV hallway, melancholic school,
empty school hallway, after-school atmosphere, Japanese school corridor, liminal space`

# 适用风格 Applies To

- **必需**：[[retro-game-cg|Retro Game CG]] 的 Low-Poly JK Slice-of-Life、CCTV 故障感
- **部分适用**：[[y2k|Y2K]] 中的校园场景（但那是真人摄影，介质不同）

# 搭配建议 Pairs With

- 介质：[[low-poly-3d-render|低多边形 3D 渲染]]
- 镜头：[[security-camera-cctv|监控视角]]（**锁定搭配**）
- 主体：[[lowpoly-jk-character|低多边形 JK 角色]]
- 叠层：[[digital-overlays|监控 bounding box、双语字幕]]
- 光影：荧光灯顶光（无方向性）
- 情绪：孤独、压抑、被观察

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| **当代学校电影场景** | 那是真人摄影、光线温暖；本元素是 3D 渲染、光线冷硬 |
| **恐怖游戏场景**（《寂静岭》） | 恐怖游戏有更多腐败/血迹；本元素是日常但压抑 |
| **Liminal Space 照片** | Liminal Space 是真实照片；本元素是 3D 渲染 |

# 生成提示 / 常见失败

- **走廊不够狭长**：`long empty corridor, perspective converging to a distant door`
- **光线太亮**：监控场景应**偏暗**，`dim fluorescent lighting, some lights flickering or off`
- **墙面太干净**：`slightly stained tiles, worn walls, aged school building`
- **缺少监控感**：必须搭配 [[security-camera-cctv|监控视角]] 与 bounding box 叠层

# 来源 Sources

- [[raw/videos/_source|raw/videos/_source.md]] — @鴉鴉的幻覺 走廊监控视频（典型范例）
