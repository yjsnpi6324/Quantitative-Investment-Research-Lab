# Experiment 001A 协议交付 QA

日期：2026-10-24。范围仅为协议静态一致性和小型索引/指标 fixture；不是数据或模型验证。

## 通过项目

- PASS：Markdown code fences paired
- PASS：Exactly one manifest JSON block
- PASS：Manifest remains DRAFT_NOT_FROZEN with no fake data/hash/approval
- PASS：All source references resolve
- PASS：All file/commit links pinned; issue explicitly unpinned
- PASS：Source receipt commit agrees
- PASS：Every cited file has inspected blob receipt
- PASS：fold 902: lengths 756/126/126/882
- PASS：fold 902: training outcomes clear validation embargo
- PASS：fold 902: final fit outcomes clear test embargo
- PASS：fold 902: no current test in fit
- PASS：fold 1028: lengths 756/126/126/882
- PASS：fold 1028: training outcomes clear validation embargo
- PASS：fold 1028: final fit outcomes clear test embargo
- PASS：fold 1028: no current test in fit
- PASS：fold 1154: lengths 756/126/126/882
- PASS：fold 1154: training outcomes clear validation embargo
- PASS：fold 1154: final fit outcomes clear test embargo
- PASS：fold 1154: no current test in fit
- PASS：fold 1280: lengths 756/126/126/882
- PASS：fold 1280: training outcomes clear validation embargo
- PASS：fold 1280: final fit outcomes clear test embargo
- PASS：fold 1280: no current test in fit
- PASS：Four dev windows avoid final OOS outcome leakage
- PASS：OOS has 252 origin slots, 5-session mature tail
- PASS：Synthetic Brier fixture = 0.04
- PASS：No duplicate section numbering

## 人工复核与保留限制

- 状态使用当时可得特征；未来收益只用作下游标签。
- 基线与候选同目标、日期、X与缩放，唯一区别是状态条件化；常数基线仅作诊断。
- 新参数全部标为建议；最终日期、provider、PIT证据、审批者、数据hash未伪填。
- 置信区间敏感性检查使用区间，而非随block长度不变的原始点估计。
- 已去除未定义的强制特征消融，首轮仅 B0/B1/C。
- 未运行行情下载、训练、回测、Bootstrap、真实OOS或任何外部写入。
- 日历历史覆盖、数据源/vintage、依赖锁与实验实现仍是开跑前缺口。

## 文件完整性

- `experiment_001a_execution_protocol_zh.md`：SHA-256 `4de2ed434adb4108127cd23e88661095c8fedd1f1e48735a9e3d46c92529532c`，33796 bytes。
- `experiment_001a_source_receipt.json`：SHA-256 `88e02ac9845a0ab1b3598f4f25e118abb780281de146901be93d820faaa0c804`，7299 bytes。
