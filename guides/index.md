# Guides · Agent 协议

本目录定义 agent 使用本资产库时的行为规范。**接入本库的 agent 应先读本页，再按任务读对应协议。**

## 核心四操作

| 想做什么 | 读哪个协议 |
|---|---|
| 与用户**探索/收敛**新风格 | [[style-exploration\|风格探索协议]] |
| 直接**出图** | [[image-generation\|图片生成规范]] |
| 直接**出视频** | [[video-generation\|视频生成规范]] |
| 用户丢来**书/杂志**要编译 | [[ingestion\|原料编译管道]] |

## 建设与维护

| 想做什么 | 读哪个协议 |
|---|---|
| 新增/修改原子元素、索引、日志 | [[maintenance\|维护规范]] |
| **新建一个风格运动/子风格/家族** | [[new-style-pack\|新建风格包规范]] |
| 写或改**配方**（双表示） | [[recipe-schema\|配方 schema 规范]] |
| 管理**图片资产**绑定与产物 | [[image-assets\|图像资产层规范]] |

## 工具

```bash
python3 tools/validate.py       # 一致性校验（链接/frontmatter/配方引用/命名）
python3 tools/build_index.py    # 重建检索索引 index/compact.md 与 graph.json
```

**铁律**：
1. 改动后**必须**跑 `validate.py`，0 错误才算完成
2. 涉及新增/删除概念页后**必须**跑 `build_index.py` 重建索引
3. 任何写入后**必须**更新对应 `index.md` 与根 `log.md`
