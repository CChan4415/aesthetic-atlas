---
type: Visual Element
title: 第三人称游戏视角（Third-Person Game Camera）
description: 跟随主体背后或越肩的 3D 游戏视角——镜头随主体移动，观众看到主体后脑勺与前方场景，是 PS1/PS2 游戏与同人 CG 的默认运镜。
tags: [retro-game-cg, camera, third-person, follow-cam, over-shoulder, game]
status: draft
generated: { by: agent:deepseek, at: 2026-10-16T20:47:00+08:00 }
sources:
  - id: raw-videos-2026-10
    resource: /raw/videos/
    title: 千禧年低多边形 3D 短片合集
    author: "@natural water / @龙崎日舞"
---

# 定义 Definition

**第三人称游戏视角**指 3D 游戏的默认镜头：**主体在画面下半部分**（看到后脑勺、肩、背），
**镜头从主体后上方跟随**。这是 PS1/PS2 时代 3D 动作/冒险/角色扮演游戏的标配视角
（《古墓丽影》《最终幻想 X》《王国之心》《生化危机 4》越肩视角）。

> **核心识别特征**：能看到主体的后脑勺 / 肩 / 背，而不是正脸。
> 这制造"你是玩家 / 你是跟随者"的代入感。

# 视觉特征 Visual Cues

- **主体位置**：画面下半部分（约 1/3 到 1/2 高度）
- **视角方向**：主体背对镜头，看向前方场景
- **相机位置**：主体后上方 1–3 米，俯角 5–15°
- **运镜**：跟随主体平滑移动（"follow cam"），可能有少量延迟（lag）制造重量感
- **变体**：越肩视角（over-shoulder）——相机几乎贴在主体肩后，前方场景占主画面

## Prompt Keywords

`third-person game camera, follow cam, behind-the-back view, over-shoulder shot, video game camera,
character seen from behind, camera follows the protagonist, 2000s video game perspective,
PS2 third-person view, adventure game camera, player perspective, camera tracking the character,
over-the-shoulder framing, game engine camera, follow behind, third-person adventure`

# 适用风格 Applies To

- **必需**：[[retro-game-cg|Retro Game CG]] 所有"角色在游戏世界中移动"的场景
- **部分适用**：[[y2k-retro-future|Retro Future]] 中的"游戏录屏"美学
- **不适用**：[[visual-kei|Visual Kei]]（视觉系要正面或三分面肖像）、[[y2k-sweet-candy|Sweet Candy]]（偶像写真要正面）

# 搭配建议 Pairs With

- [[low-poly-3d-render|低多边形 3D 渲染]]——本视角的介质基础
- [[lowpoly-jk-character|低多边形 JK 角色]]——典型主体
- 场景：[[underground-passage-tiled|地下通道]]、[[school-corridor-cctv|学校走廊]]、[[mall-arcade|商场]]
- 动态：[[walk-toward|走向镜头]]的反向——**远离镜头**；[[dolly-tracking|跟拍平移]]

# 易混 / 反例 Not To Confuse

| 容易混淆 | 区别 |
|---|---|
| **背后远景** | 远景主体很小；本视角主体占画面 1/3，明显看到背部细节 |
| **第一人称视角** | 第一人称看不到自己；本视角看到主体后脑勺 |
| **监控视角** | 监控固定不动；本视角跟随主体 |
| **电影越肩镜头** | 电影越肩用于对话，相机在肩上；游戏越肩更低、更远 |

# 变体 Variants

- **越肩视角（Over-Shoulder）**：相机紧贴主体肩后，前方场景占主画面（《生化危机 4》《Gears of War》）
- **远景第三人称**：主体在画面 1/4 处，场景为主（《Shadow of the Colossus》）
- **固定第三人称**：相机不动，主体在画面中移动（早期《生化危机》）——介于监控与跟随之间

# 生成提示 / 常见失败

- **模型容易输出正面**：必须明确 `character seen from behind, back of head visible, no face`
- **跟随感不足**：补充 `camera follows the character, slight camera lag, smooth tracking shot`
- **主体位置太中央**：游戏视角主体常偏下或偏侧，`character in lower third of frame`

# 来源 Sources

- [[raw/videos/_source|raw/videos/_source.md]] — @natural water 地下通道视频（前景背影 + 背景正面双人构图）
