---
type: Guide
title: 配方 schema 规范
description: 配方双表示约定（Markdown 给人读 + YAML 给 agent 读）、字段定义与校验规则。
tags: [guide, recipe, schema, machine-readable]
status: stable
generated: { by: agent:deepseek, at: 2026-10-12T10:40:00+08:00 }
---

# 配方 schema 规范

## 1. 为什么需要双表示

配方是本库最重要的复用单元，但它有两种读者，需求相反：

| 读者 | 需要 | 问题 |
|---|---|---|
| **人（你）** | 可读的散文、理由、排版好的 prompt | agent 无法可靠解析 |
| **agent** | 结构化、可校验、引用明确 | 散文需要"理解"，会漏项、会误解 |

**结论：一个配方 = 两个文件，同步维护。**

```
recipes/
├── visual-kei-kote-cold-black.md          ← 人读（权威叙事 + 组装好的 prompt）
├── visual-kei-kote-cold-black.recipe.yml  ← 机读（权威结构 + 引用关系）
```

## 2. 权威性规则（避免双写漂移）

> **prompt 文本以 `.md` 为准；结构与引用关系以 `.yml` 为准。**

- 修改某个原子元素时：**只需改原子概念页**，两个配方文件都不用动（它们只存引用 ID）
- 修改锁定的组合时：两个文件都要改 → **先改 `.yml`（结构），再改 `.md`（散文与 prompt）**
- 校验脚本以 `.yml` 为准检查引用完整性

## 3. 字段定义

```yaml
id:            # 必填，kebab-case，与文件名一致（不含扩展名）
version:       # 必填，整数，实质性改动递增
title_zh:      # 必填
title_en:      # 必填
status:        # draft | stable | deprecated
updated:       # YYYY-MM-DD
movement:      # 风格运动页路径（相对库根）
substyle: []   # 子风格页路径列表

locked:        # 风格签名。改动 = 视为新配方
  <维度>: <概念页路径> 或 [路径列表]
tunable:       # 可按项目替换
  <维度>: [取值列表]

video:         # 视频专用（可选）
  motion:      # 动态元素页路径
  camera: []   # 运镜取值
  duration_sec: [min, max]
  pacing:      # 节奏描述

prompts:       # 指向 .md 中已组装好的 prompt 段落
  image_ref:  "recipes/<id>.md#<段落标题>"
  video_ref:  "recipes/<id>.md#<段落标题>"
  negative_ref: "recipes/<id>.md#<段落标题>"

outputs:       # 产物记录
  - {date, type, version, dimensions, aspect, remote_url, local_path, rating}

taste:         # 主观偏好（本库特有，见 §5）
  affinity:    # 1-5
  confidence:  # low | medium | high
  note:        # 一句话说明
```

## 4. 校验规则

跑 `tools/validate.py` 检查：

1. **引用完整性**：`locked` / `tunable` / `movement` / `substyle` / `video.motion` 中
   所有指向 `atlas/` 的路径必须存在
2. **必填字段**：`id` / `version` / `title_zh` / `movement` / `locked` 必须存在
3. **id 一致**：`id` 必须等于文件名（去掉 `.recipe.yml`）
4. **双表示匹配**：每个 `.recipe.yml` 应有同名 `.md`，反之亦然
5. **prompt 段落存在**：`prompts.*_ref` 指向的段落标题必须在 `.md` 中找到

**校验失败 = 配方不可用**，agent 必须报告而不是猜测。

## 5. taste 字段：本库特有的主观维度

OKF 的 `verified` 表达"定义是否被评审过"，但审美资产还需要表达**"我喜不喜欢"**——
这是企业知识库没有的维度：

- `affinity: 1-5` —— 主观喜好度
- `confidence: low | medium | high` —— **对自身偏好的确定程度**
- `note` —— 一句话理由

**为什么需要 confidence**：审美会变，且常常"说不清"。
`confidence: low` 明确告诉 agent："这里我不确定，可以多给我几个方向试试"——
这让 agent 的探索行为更有依据，而不是假装用户什么都确定。

## 6. Agent 使用流程

1. **选用现有配方**：读 `.recipe.yml` 得到结构 → 按需替换 `tunable` → 从 `.md` 取 prompt
2. **生成新配方**：先确定 `locked`/`tunable` 划分 → 写 `.yml` → 跑校验 → 再写 `.md` 的散文与 prompt
3. **改动现有配方**：
   - 只改 `tunable` 取值 → 不改版本号（视为同版本微调，记入产物）
   - 改 `locked` 任何一项 → **递增 version**，并在 `.md` 版本历史追加说明
4. **跨配方复用**：多个配方引用同一元素页时，改元素页即可全局生效——
   这正是"引用而非复制"的价值。

## 7. 反例 Not To Do

| 错误做法 | 为什么错 |
|---|---|
| 在 `.yml` 里抄一遍完整 prompt | 双写，必然漂移；prompt 只在 `.md` 里 |
| 在 `.md` 里写具体 prompt 却不在 `.yml` 里登记引用 | agent 无法程序化校验"用了哪些元素" |
| 改了 locked 却不递增版本 | 产物无法追溯到具体配方版本 |
| 为了"灵活"把所有维度都设成 tunable | 配方失去签名，等于没有风格 |
