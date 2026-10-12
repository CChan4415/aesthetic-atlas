# Recipes · 风格配方

已锁定、开箱即用的完整风格。每个配方含图片与视频双 prompt、可调参数、产物记录与版本历史。

**每个配方有两个文件**：
- `<id>.md` —— 人读：叙事、锁定决策表、组装好的 prompt
- `<id>.recipe.yml` —— 机读：结构化引用，agent 用于校验与组装

规范见 [[recipe-schema|配方 schema 规范]]。

## 可用配方

### Visual Kei 系列

* [[visual-kei-kote-cold-black]] — **Visual Kei · Kote-kei 冷黑肖像**：
  全黑西装、石膏白妆、尖刺立发，强单点硬光与高对比质感，性别模糊表演者（v1）
  * 机读：`visual-kei-kote-cold-black.recipe.yml`

### Y2K 系列

* [[y2k-warm-dv-idol]] — **Y2K · 暖调 DV 千禧偶像**：
  橙粉/古铜/脏金，老 DV 与千禧杂志质感，亚洲偶像少女，混搭层叠穿搭，海报卧室（v1，首个落地配方）
  * 机读：`y2k-warm-dv-idol.recipe.yml`

> 两个配方构成本库当前的两极：**一暖一冷、一生活化一舞台化、一怀旧一当下**。

## 规划中 Planned

按 [[new-style-pack|新建风格包规范]] 的同结构补充：

- **视觉系**：angura-gothic-rose（暗黑哥特玫瑰）、oshare-candy-rock（御洒落糖果摇滚）
- **Y2K**：cyber-chrome-hero、pastel-pink-princess、lofi-crt-world、grunge-riot、mcbling-socialite

## 新增配方的步骤

1. 确定 `locked`（风格签名）与 `tunable`（可替换维度）的划分
2. 写 `<id>.recipe.yml`（先结构）
3. 跑 `python3 tools/validate.py` 校验引用完整性
4. 写 `<id>.md`（散文 + 组装好的 image/video prompt）
5. 更新本 index.md 与根 `log.md`
