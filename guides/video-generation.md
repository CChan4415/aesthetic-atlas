---
type: Guide
title: 视频生成规范
description: 将图片与风格配方组装为视频生成 prompt（运镜/动作/节奏/转场/声音）的规范。
tags: [guide, video-generation, prompt, motion]
status: stable
generated: { by: human:cc, at: 2026-10-12T00:00:00+08:00 }
---

# 视频生成规范

## 1. 首选路径：图生视频（image-to-video）

以已确认的角色定妆照为首帧，最大程度保证主角不换脸。视频 prompt **只描述"动"的部分**，
不重复首帧已有的静态外观。

## 2. Prompt 组装顺序

```
[主体动作/表演 subject action/performance] + [表情变化 expression change]
+ [运镜 camera movement]（方向 + 速度 + 稳定性）
+ [环境动态 environmental motion]（头发/衣物/粒子/光流）
+ [节奏 pacing] + [转场 transitions] + [特效 VFX]
+ [动态质感 motion texture]（动态模糊/丢帧/拖影）
+ [声音提示 audio cue]（如工具支持）+ [整体氛围 mood]
```

词汇取自 [[atlas/motion/index|`atlas/motion/`]]、[[atlas/audio/index|`atlas/audio/`]]；
配方文件 `# Video Prompt` 已预组装。

## 3. 运镜与动作的搭配原则

- **梦幻漂浮**：slow push-in / slow orbit + 轻微手持浮动 + 头发衣物慢飘，慢门拖影。
- **故障高能**：whip zoom / 手持晃动 + 快速动作 + glitch-cut、strobe、datamosh。
- **怀旧 DV**：手持 sway、突然数码变焦 push、偶发丢帧与磁带跟踪条，动作像被抓拍。
- **电影推进**：稳定 dolly/pedestal，浅景深焦点转移，动作克制、留白。
- 一条镜头只安排 **1 个主动作 + 1 个主运镜**，避免模型"动作打架"。

## 4. 参数约定

- 画幅：竖屏 9:16（手机）/ 横屏 16:9 / 电影感 21:9 / DV 原生 4:3。
- 时长：单镜头 5–10 秒；复杂叙事 10–30 秒并拆分镜。
- 系列视频：固定角色参考、配色、质感与运镜语言，形成统一风格签名。

## 5. 分镜与连续性

1. 长视频先写分镜表：镜号 / 时长 / 景别 / 运镜 / 动作 / 转场 / 声音。
2. 相邻镜头保持：同一角色形象、屏幕方向（180° 轴线）、光源方向、配色一致。
3. 转场优先复用画面内元素（遮挡转场、闪光、匹配剪辑），少用生硬硬切堆叠。

## 6. 声音（资产层面）

[[atlas/audio/index|`atlas/audio/`]] 记录音乐风格、BPM、标志性音效（磁带咔哒、拨号上网、快门、
VHS 噪声）。即使生成工具不支持音频，也用于后期配乐选曲与节奏参考。

## 7. 质量检查

- 主角面部是否稳定、无身份漂移；动作是否自然、无多指/肢体粘连；
- 运镜是否符合配方气质；故障/颗粒特效强度是否恰当；首尾帧是否可用。
