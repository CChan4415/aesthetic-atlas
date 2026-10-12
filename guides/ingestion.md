---
type: Guide
title: 原料编译管道
description: 将 raw/ 中的审美书籍、杂志、扫描件、文章编译为 atlas/ 结构化概念的流程。
tags: [guide, ingestion, pipeline, raw, compile]
status: stable
generated: { by: human:cc, at: 2026-10-12T00:00:00+08:00 }
---

# 原料编译管道（raw → atlas）

类似 LLM wiki 的编译机制：原始材料进 `raw/`，经本管道"编译"为图鉴中的原子概念。
原则：**原料只读、产物结构化、全程可追溯**。

## 1. 目录与登记

```
raw/
├── inbox/        # 【暂存区】未分类原料，agent 编译时判断归属
├── books/        # 书籍（PDF/EPUB/扫描）
├── magazines/    # 杂志（单期或专题）
├── scans/        # 图片扫描、lookbook、广告片
├── articles/     # 文章、论文、博客、网页存档
└── _template-source.md
```

每批原料：

1. 放入对应子目录（建议 `作者或刊物-年份-标题/` 单独成文件夹）。
   **拿不准放哪就丢 `inbox/`** —— 不需要先想清楚分类。
2. 复制 [[_template-source|`_template-source.md`]] 为 `_source.md`，填写元数据与 `status: pending`。

### Step 0：inbox 归位（若原料来自 `inbox/`）

INGEST 开始时先检查 `raw/inbox/`，对每份原料：

1. **判断类型**：书籍 → `books/`；杂志 → `magazines/`；图片/lookbook → `scans/`；文章/网页 → `articles/`
2. **移动到目标目录**（可保留原名或按 `作者或刊物-年份-标题/` 重命名）
3. **建 `_source.md`**：按模板填写元数据，`source_status: pending`
4. **在 raw/index.md 登记**
5. 继续执行下方七步管道

> 移动而非复制——`inbox/` 是暂存区，处理完应为空。
> 若无法判断类型，默认归入 `articles/` 并在 log 中标注待确认。

## 2. 编译七步

1. **读取 Read**：解析文本；扫描件/图片先 OCR；长文档分页读完，不跳页。
2. **盘点 Inventory**：列出材料覆盖的维度（人物/发型/妆容/服装/配饰/场景/配色/材质/光影/镜头/质感/动态/情绪）。
3. **提取 Extract**：每个有独立复用价值的元素 → 候选原子概念，记录：中文名、英文名、定义、
   视觉特征、英文 prompt 关键词、所属风格/年代、原文页码或图号。
4. **去重 Dedupe**：与 `atlas/` 现有概念比对（同名、近义、同物异名）。
5. **合并 Merge**：
   - 已存在 → 补充信息与新关键词，追加 `sources`，不新建文件；
   - 仅变体差异 → 写入该概念的 `# 变体` 段落；
   - 确为新概念 → 按 [[maintenance|维护规范]] 新建文件。
6. **链接 Link**：建立与风格运动、子风格、配色、搭配元素、参考资料的双向链接。
7. **收尾 Close**：更新各级 `index.md`、根 `log.md`；把 `_source.md` 状态改为 `compiled`，
   并列出本次新增/更新的概念清单。

## 3. 来源与可信度（OKF frontmatter）

每个编译产物在 frontmatter 记录：

```yaml
sources:
  - id: <stable-id>
    resource: /raw/magazines/<folder>/<file>
    title: <原始标题>
    author: <作者/刊物>
    last_modified: <ISO-8601>
generated: { by: <agent/version>, at: <ISO-8601> }
verified: { by: human:cc, at: <用户复核后填写> }
```

未经用户复核的内容 `verified` 留空（unverified）；关键事实优先采用原书原文，避免主观演绎。

## 4. 冲突处理

- 多来源说法不一致 → 在概念正文 `# 争议` 并列各方表述并各自标注来源，不强行统一。
- 图片与文字冲突 → 以原始图片证据为准，文字作辅助，并注明。
- 无法确认的信息 → 标注"待补充"，不编造。

## 5. 批量编译检查清单

- [ ] 原料已登记且状态正确
- [ ] 长文档已完整读取（含图注、版权页、目录）
- [ ] 每个新概念符合 frontmatter 规范且含英文关键词
- [ ] 已去重/合并，无重复概念
- [ ] 双向链接、各级 index、根 log 已更新
- [ ] `_source.md` 标记 compiled 并附产物清单
