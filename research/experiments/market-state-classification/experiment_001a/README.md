# Experiment 001A：开跑前预检（DRAFT / BLOCKED）

此目录只做研究证据完整性检查，不训练、回测、调度或接入生产。当前不具备真实开跑条件；任何合成测试通过都不代表数据、审批或策略表现真实可用。

## 已知协议与原件阻塞

已读取 [issue #3](https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/issues/3)（无评论）及上级 README。001A 使用 Bull / Neutral / Bear，加独立 high-vol 标记；当日状态仅使用当时已知信息。T+5 主检验，T+1/T+3 次要。B0/B1/C、阈值、walk-forward 和最终 OOS 均未批准或冻结。这些约束来自 issue 与本任务指令，不冒充已交付协议全文。

用户指定的 `Experiment_001A_Protocol_2026-10-24.zip`，Library ID `libfile_6b86c7eebd3c81918bd440d8d1ce7ab5`，预期含 `experiment_001a_execution_protocol_zh.md`、source receipt、QA。2026-10-24 在本执行环境使用当前 Library skill 的 resolved-reference materialization 流程：prepare 成功，官方 helper 下载失败；重新 prepare 后有界重试一次，同样失败。两次错误均为 `library file transfer failed: download failed`，工具没有给出更细原因。没有取得可读 ZIP，没有验证其内部文件、source receipt 或所谓 27 项 QA，没有计算原件 Hash。未猜测下载地址、改环境或绕过限制。此处没有复制或重建协议原文。

后续必须取得原件、核对身份及 Hash、阅读正文和 QA，再将协议及回执放入研究证据目录并完成差异审查。当前 `protocol` / `source_receipt` / `protocol_qa` 保持 null。该附件获取是失败，不是待审批或成功但结果不确定。

## 数据入口与日历盘点

核查基线：`eba9c47`，2026-10-24。仓库与父目录未找到 `AGENTS.md`；`.agents/skills` 没有可读技能文件。遵循 `CONTRIBUTING.md`、研究数据治理与用户隔离约束。

| 已有入口/证据 | 实际能确认的范围 | 仍缺条件 |
| --- | --- | --- |
| `src/adapters/market_data.py` | `provider.snapshot`、`actual_for_prediction` 接口边界 | 无具体 provider 实现、授权回执、真实历史训练快照 |
| `research/DATA_SOURCE_GOVERNANCE.md` | 官方来源优先、许可/PIT/修订/生存偏差要求 | 来源类别或供应商举例不是账户数据授权 |
| `docs/governance/PLUGIN_EXECUTION_POLICY_20261020.md` | 历史管理会话中 Bigdata/FMP 单次报价与 Exa/Firecrawl 官方公告读取记录 | 非当前实测；不证明 A 股完整历史、成分股 vintage 或可批量训练权利 |
| `docs/SYSTEM_OF_RECORDS.md`、`docs/DROPBOX_ASSET_INDEX_CONTRACT.md` | Dropbox 是大文件/PIT 快照资产归属，GitHub 是研究代码与协议归属 | 无本实验可回读、已验 Hash 的资产索引与完整数据集 |
| `src/evaluation/a_share_calendar.py` | 静态休市表仅 2026；引用 SSE/SZSE 官方入口 | 未包含 2016–2025 官方原文与逐日快照，2026 也缺本实验可验 Hash 的原文归档 |

已有日历引用仅作为研究来源线索保留：[SSE 休市安排](https://www.sse.com.cn/disclosure/dealinstruc/closed/)、[SZSE 日历](https://www.szse.cn/English/services/trading/calendar/)。本任务没有把目录页当成逐年历史证据，也没有用工作日补造交易日。未调用生产数据库、registry 或调度器验证数据入口。

草案示例数据区间为 2016-01-01 至 2026-09-30，日历至 2026-10-30；这是可替换 DRAFT，不是协议已批准范围。对该示例范围，2016–2025 所有年份均缺完整历史官方证据；2016–2026 的研究快照、授权和 PIT 证据均未交付。warm-up、窗口、阈值、成本口径与最终 OOS 日期待协议核对，不默认已满足。若未来需要共享适配器扩展，应另开依赖任务；本 PR 不改 `src/evaluation` 或共享日历。

## 运行

在仓库根目录使用普通 Python 3.10+（不使用 `-O`）：

```sh
python3 research/experiments/market-state-classification/experiment_001a/preflight.py \
  research/experiments/market-state-classification/experiment_001a/config.draft.json \
  research/experiments/market-state-classification/experiment_001a/manifest.template.json
python3 -m unittest discover -s tests -v
```

预检 JSON 输出 `ready` / `blocked`、逐项 blockers、scope、execution_allowed。blocked 返回码 2；ready 返回码 0。当前模板预期 7 类 blocker：PROTOCOL、PARAMETERS、PROVIDER、CALENDAR、SNAPSHOT_PIT、OOS、FREEZE。`--fixture` 只接受 synthetic 快照且始终 `execution_allowed=false`；默认只接受 real。该工具不执行实验；研究 ready 也不是生产准入或方法晋升。

## 最小 Manifest 契约

将 template 复制到独立研究证据目录，引用其下真实文件；不要提交有许可限制的原始大数据。每个证据引用是 `{"path":"relative/file.json","sha256":"<64 lowercase hex>"}`。预检读取实际非空字节重算 SHA-256，拒绝不存在、Hash 不符、绝对路径或越界 symlink。JSON 不允许用注释或占位 Hash 冒充证据。

- `protocol`、`source_receipt`、`protocol_qa`：原件文本/文件；`protocol_review` 绑定三者 Hash，证明人工完成阅读与一致性核对。
- `provider.name` 与 `provider.authorization`：授权 JSON 包含 provider、research_use_allowed=true、source_uri、license_scope、带时区 verified_at。保留已有合法授权，不生成凭据。
- `calendar`：JSON 数组，每个自然日一条 `{date, is_open}`，完整覆盖 data_start 到 calendar_end；包含休市日，拒绝重复/缺失日期，不自行推导工作日。
- `calendar_sources`：每年每所 SSE/SZSE 的 `{year, exchange, url, artifact}`，artifact 引用官方原文归档；`calendar_review` 绑定逐日表及所有原文 Hash。审核者须核实公告覆盖、临时停市和日期转换；域名验证不等于公告真实性验证。
- `snapshot`：按交易日一条宽表 JSON `{date, as_of, available_at, features}`，features 必须匹配配置、值为有限数；as_of 和 available_at 必须带时区，available_at 不晚于 as_of，as_of 对应上海当日。预检拒绝额外未来收益/标签字段、缺失交易日和重复日期。该宽表是最小研究输入契约，不是原始成分股数据库。
- `snapshot_kind` 为 real；`snapshot_receipt` 包含 kind、provider、snapshot_sha256、source_uri、retrieved_at 和 raw_artifact 引用。原始数据、来源回执和派生快照需要同审，不允许仅改 synthetic 字符串当真实数据。
- `pit_review` 绑定 snapshot、config、receipt 的 Hash，并记录非空 vintages、revisions、survivorship、constituents、corporate_actions、feature_lineage 审核说明。available_at 是整行所有输入的最晚可用时点；聚合/财务数据修订、历史成分和回溯复权风险由 lineage 审核负责。列名检查不能自行证明公式没有使用未来数据。
- `parameter_approval` 绑定当前配置**文件字节**和协议 Hash。配置必须 APPROVED，且保留固定状态/horizon 约束；改变任何字节会使旧批准失效。B0/B1/C 的精确公式和阈值必须在批准前人工核对，不能只改 status。
- `walk_forward` 为 `{train:[start,end], validation:[start,end]}` 数组，`oos` 为 `[start,end]`，日期均为实际开市日；每折训练末端与验证之间、验证末端与 OOS 之间留足严格 T+5 标签 purge，验证窗口有序且不重叠，OOS 末端另需五个真实交易日。B0/B1/C 共用这些窗口和目标，拟合/标准化仅限训练折；此处没有训练实现。
- `oos_isolation` 绑定配置和快照 Hash；记录 untouched=true、sealed_at、first_model_selection_at，以及 access_control、audit_log 两个实际文件引用。封存须早于首次模型选择；审核者核对权限/访问日志，预检不读取 OOS 结果，也不替代访问控制系统。
- `freeze_review` 最后绑定配置、协议/回执/QA/复核、日历/复核、快照/来源回执/PIT、参数批准、OOS 证明和 provider 授权 Hash。修改上游文件必须重新审查；不存在凭证时保持 null。

所有 review JSON 均需 `decision=approved`、reviewer、带时区 reviewed_at、精确 bindings（实现及合成 fixture 给出完整示例）。Hash 提供完整性，不是数字签名或授权认证；审核身份、来源真伪及证据实质需要已有治理流程核实。本工具防缺失/不一致，不声称能识别刻意伪造的整套证据。合成测试中的审核者、原文、ACL 和授权均醒目标记 SYNTHETIC，临时生成后删除，不作为真实冻结凭证提交。

## 验收与后续

本次 27 个新增测试 + 8 个原有检查共 35 个通过，含缺 provider/授权、历史官方日历、真实快照/原始字节、非法/不符 Hash、PIT、未批准参数、OOS 审计/封存/purge、未来字段及 CLI 退出码。当前草案仍 blocked，无实际训练、回测成绩或 frozen 状态。

继续条件：恢复原件读取并对齐协议；确定合法 provider 与完整历史 raw/PIT 快照；补全覆盖期每年 SSE/SZSE 原始官方证据；批准精确参数/窗口与隔离措施；取得真实可审计冻结凭证。之后重跑预检，再独立安排研究运行。不得把本预检 PR 当成方法晋升、合并或部署授权。
