# Assets · 图像资产层

本目录存放**本地落地的图像资产**，解决"审美资产依赖外部 CDN"的结构性风险。
规范见 [[image-assets|图像资产层规范]]。

## 目录结构

```
assets/
├── elements/<维度>/<concept-id>/   # 原子元素示例图（路径镜像 atlas/ 结构）
├── recipes/<recipe-id>/            # 配方产物 + 生成参数快照
└── references/                     # 参考图（品牌/创作者/年代）
```

## 当前状态

* **已建立目录骨架**，尚无图像文件。
* 现有配方 `y2k-warm-dv-idol` 的产物仅有外部 CDN 链接
  （`https://aka.doubaocdn.com/s/LtVVF5U004`），**待本地化**：
  下载后放入 `recipes/y2k-warm-dv-idol/v1-2026-10-12.jpg`，
  并补 `v1-2026-10-12.json` 参数快照。

## 待做 To Do

- [ ] 把 y2k-warm-dv-idol 的 CDN 产物下载本地化
- [ ] 为关键概念页补示例图（优先：尖刺立发、白妆、蕾丝与网纱、Kote-kei 子风格）
- [ ] 视觉系配方产物落地并回填参数快照
- [ ] 补 `assets/index.md` 自动生成脚本（沿用 `tools/build_index.py` 思路）

> 注：本文件为目录说明，**不是**自动生成的资产清单。
> 自动清单将在 `tools/build_index.py` 扩展后产出。
