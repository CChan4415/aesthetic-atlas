---
type: Guide
title: 风格探索协议
description: Agent 基于资产库与用户共同探索、收敛并沉淀视觉风格的对话流程。
tags: [guide, protocol, exploration, workflow]
status: stable
generated: { by: human:cc, at: 2026-10-12T00:00:00+08:00 }
---

# 风格探索协议

目标：当用户"说不清楚想要什么"时，agent 通过**结构化提问 + 快速视觉试错**，把模糊审美收敛为
一个可复用的 [[recipes/index|Style Recipe]]。全程中文交流，选项一次给 2–4 个。

## 1. 四种入口模式

先判断用户从哪里出发：

| 模式 | 触发信号 | 起点 |
|---|---|---|
| **情绪优先 mood-first** | "想要某种感觉/氛围" | [[atlas/mood/index\|`atlas/mood/`]] → 反查风格与配色 |
| **参考优先 reference-first** | 给出明星/电影/MV/品牌/图片 | [[references/index\|`references/`]] → 拆解其视觉要素 |
| **配方改良 recipe-modify** | "在某配方基础上改" | 复制对应 recipe，只改指定维度 |
| **惊喜随机 surprise-me** | "随便来/给我惊喜" | 随机抽取子风格 + 元素组合，允许跨子风格混搭 |

## 2. 提问规则（硬约束）

1. 每轮最多 **4 个问题**，每个问题 2–4 个选项；可多选的明确标注"可多选"。
2. 选项文案 = 用户能直接理解的画面描述，**不要**出现内部术语或工具名。
3. 一次只推进一个维度；存在上下游关系时先问上游（如先定子风格，再定配色）。
4. 用户已明确表达的维度**不要重复问**；把已确认项在提问前简要复述。
5. 信息足够时停止提问，直接生成测试图——不要把决策成本全部丢给用户。
6. 拿不准但可逆的细节，agent 自行给默认值并在交付时注明"可调"。

## 3. 标准探索流程（决策树）

```
Step 0  入口模式判断（情绪 / 参考 / 改良 / 随机）
Step 1  风格运动 → 子风格        atlas/taxonomy/movements/
Step 2  主体类型与角色原型        atlas/subject/
Step 3  发型 → 妆容              atlas/hair/  atlas/makeup/
Step 4  服装 → 鞋履 → 配饰       atlas/wardrobe/  atlas/accessories/
Step 5  场景 → 道具 → 装饰       atlas/setting/
Step 6  配色方案                 atlas/color/
Step 7  材质 → 光影 → 镜头构图   atlas/material/ lighting/ camera/
Step 8  画面质感/后期            atlas/grade/
        （若用于视频）Step 9 运镜 → 动作 → 节奏 → 转场/特效  atlas/motion/
Step 10 组装草稿配方 → 生成测试图
Step 11 按反馈迭代（见 §4）→ 用户确认
Step 12 沉淀为正式 recipe（见 §5），更新 index 与 log
```

允许跳步：用户不关心的维度用子风格默认值填充，并在配方中标注 `default`。

## 4. 试错—批评闭环

1. 一次生成 1 张测试图（用户要求对比时可生成 2–3 张方向稿）。
2. 交付时主动引导批评：**主体 / 配色 / 穿搭 / 场景 / 质感 / 氛围**六个维度逐一确认。
3. 用户反馈要落到具体维度的具体元素上，只改该元素，其余锁定不动（保持角色一致性）。
4. 同一修改失败两次 → 换思路（换参考、换材质、换镜头），而不是反复微调同一描述。
5. 记录"用户不喜欢什么"同样有价值，写入用户偏好画像（§6）。

## 5. 沉淀为配方

用户确认后：

1. 复制 [`/raw` 之外的] 配方模板（见 `/recipes/index.md`），命名风格：`<movement>-<vibe>-<subject>`，kebab-case。
2. 把每个决策链接到对应 `atlas/` 原子概念；区分 `locked`（锁定）与 `tunable`（可调）。
3. 按 [[image-generation|图片生成规范]] 与 [[video-generation|视频生成规范]] 写好双 prompt。
4. 登记测试产物路径、日期与用户评价；`status: stable`。
5. 更新 [[recipes/index|`recipes/index.md`]] 与根 [[log|`log.md`]]。

## 6. 用户偏好画像

跨会话持续记录（使用长期记忆工具），至少包含：

- 常用/排斥的子风格、配色、材质、质感、运镜、节奏；
- 人物形象偏好（人种、肤色、妆容浓度、表情）；
- 画面"新旧程度"偏好（全新渲染 vs 重度做旧）；
- 已确认配方清单与评分；
- 语言与交付格式偏好。

探索时优先复用画像中的已知偏好，偏离时先说明理由。
