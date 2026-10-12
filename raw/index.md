# Raw · 原料区

未编译的原始材料。把审美书籍、杂志、lookbook、扫描件或文章放入对应子目录并登记，
然后请 agent 按 [[ingestion|原料编译管道]] 编译进 `atlas/`。

## 子目录

- `inbox/` — **未分类暂存区**：还没想好归类的原料先丢这里，agent 编译时自动归位
- `books/` — 书籍（PDF / EPUB / 扫描）
- `magazines/` — 杂志（单期或专题）
- `scans/` — 图片扫描、广告片、lookbook
- `articles/` — 文章、论文、网页存档

> **建议用法**：拿不准放哪就丢 `inbox/`——不需要先想清楚分类，
> agent 在 INGEST 时会判断归属并移动/登记。降低"投喂"的心理成本。

## 使用步骤

1. 原料放入对应子目录，建议 `作者或刊物-年份-标题/` 单独成文件夹。
2. 复制 [[_template-source]] 为该文件夹下 `_source.md`，填写元数据。
3. 告知 agent：「编译 raw/ 下的 XXX」；agent 执行七步管道并把状态改为 `compiled`。

> 原料保持只读；编译产物只写入 `atlas/`，不在 raw 内改写。
