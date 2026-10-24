# Experiment 001A：证据检查脚手架（DRAFT / BLOCKED）

**本工具不是开跑批准器。任何输入、审批字符串或 fixture 模式都不能得到 `execution_allowed=true`。** 它只检查部分文件完整性和字段关系，不训练、回测、调度、改 registry 或接入生产。证据检查通过不等于科学有效或可以运行。

## 已交付协议与本次修补

完整[待冻结协议](../experiment-001a-protocol.md)已按建议研究路径原样纳入，原始[来源回执](protocol_evidence/experiment_001a_source_receipt.json)与[交付 QA](protocol_evidence/experiment_001a_protocol_qa.md)一并保留。文件来自本任务已有的本地交付原件；先前执行环境的 Library 下载失败并未被改写为成功。原件中的“本次只读”“未合入”等是原交付时点的范围记录，不是本 PR 当前状态。

| 原件 | SHA-256 |
| --- | --- |
| 协议（原名 `experiment_001a_execution_protocol_zh.md`） | `4de2ed434adb4108127cd23e88661095c8fedd1f1e48735a9e3d46c92529532c` |
| source receipt | `88e02ac9845a0ab1b3598f4f25e118abb780281de146901be93d820faaa0c804` |
| protocol QA | `869502a0fe0bba311833b8564a0f8263740542fdfdcf4e03cf006da056ad0d0c` |

前两项与原始 QA 记录的 Hash 一致。QA 仅针对协议静态一致性及小型合成示例，不是数据、模型或 OOS 验证。所有参数仍是建议，D1–D7 未批准，真实日期保持 null；模板不伪造审批、freeze 或数据引用。构建独立 Manifest 证据包时须把三个原件复制到该 Manifest 目录内并按实际字节引用，不能以 `../` 绕过路径隔离。

旧脚手架把合成回执改标 real 后可能返回研究 ready；空/任意特征、一天窗口和占位模型也可能通过。此次固定六列 schema，并令**所有真实模式始终 BLOCKED**，把未实现科学门禁单列；补齐 JSON 或重算 Hash 不能解除。日历来源 URL/year/exchange/artifact 引用现在同时绑定日历审核与 freeze，不再只绑定原文字节 Hash。

## 协议对齐与未实现门禁

`config.draft.json` 只是协议摘要，不是已验证的可执行规格；完整公式以协议为准。`*_proposed` 字段不是已实现的检查。

| 协议要求（未批准建议） | 实际范围 / 尚缺 |
| --- | --- |
| 六列 `z20,z60,sigma20,drawdown60,breadth60,dispersion1`；Bull/Neutral/Bear；独立 high-vol | 校验固定列名/顺序、有限数、部分时间关系；未实现原始数据→特征/状态公式、20:00 上海 cutoff、逐输入 lineage、未来哨兵与 PIT 回放 |
| B0：每 horizon 训练窗正收益频率，Laplace `(n_up+1)/(n+2)` | 无模型实现 |
| B1：同六列 X 的 pooled L2 logistic，训练窗 scaler、无 state 输入 | 无 scaler、拟合、收敛与复现检查 |
| C：状态 logistic，`w_s=n_s/(n_s+252)` 向 B1 收缩；稀疏状态回退 | 无模型、状态支持数、回退与失败检查 |
| 训练756/验证126/开发测试126；≥4不重叠开发测试窗；H5+E5；最终252日 OOS | 仅旧 train/validation 输入的基本 T+5 排序检查；**未验证开发测试角色、窗口长度、5日附加 embargo、标签成熟或最终882槽位拟合**。一天窗口可通过部分证据检查，但不代表协议通过 |
| D1–D7、合法真实数据、PIT 成分/vintage、历史日历、独立 OOS 保管 | 文件/Hash/review 字符串不能验证身份、来源真伪、许可证或 untouched；需要真实凭证和既有治理复核 |
| 依赖锁、可复现执行、G0–G5、失败记录和一次解封 | 未实现/未运行，无表现成绩、不晋级、不生产 |

上述缺口在每份报告的 `execution_blockers` 中列出；解除需要后续单独实现和复核，没有配置开关可绕过。

## 数据入口与真实缺口

核查基线 `eba9c47`，修补基于 `d3a96b9`。完整仓库树未发现 AGENTS.md 或 .agents/skills；遵循 CONTRIBUTING.md 与研究数据治理。

- `src/adapters/market_data.py` 只是 provider 边界；本实验授权、真实 raw/PIT 快照和可回读资产索引未交付。
- 共享 A-share 日历静态休市表仅2026。多年份官方原文、逐日研究日历及 Hash 仍缺；实际范围未冻结，不以工作日伪造交易日。
- [SSE 休市安排](https://www.sse.com.cn/disclosure/dealinstruc/closed/)和[SZSE 日历](https://www.szse.cn/English/services/trading/calendar/)只是线索，目录页不是逐年完整证据。
- GitHub 保存协议/代码；受限大型原始数据遵循现有 Dropbox 资产契约。供应商类别、历史报价或文档提及不证明已有完整训练许可。
- 本 PR 不改 src/evaluation、共享日历、生产 writer、数据库、调度器或 Method Registry。

## 运行与返回语义

仓库根目录使用普通 Python 3.10+（不使用 `-O`）：

```sh
python3 research/experiments/market-state-classification/experiment_001a/preflight.py \
  research/experiments/market-state-classification/experiment_001a/config.draft.json \
  research/experiments/market-state-classification/experiment_001a/manifest.template.json
python3 -m unittest discover -s tests -v
```

- 始终返回 `readiness=evidence_checks_only`、`execution_allowed=false` 和 `execution_blockers`，不再返回 ready。
- 默认研究模式始终 `status=blocked`、退出码2，即使 `evidence_checks_passed=true`。blockers 包括证据错误及未实现门禁。
- `--fixture` 只接受 synthetic；部分合同检查成功则 `status=evidence_checks_passed`、退出码0，失败则 blocked/2。退出码0只给合成测试使用，不授予执行资格。
- 未填模板有7类证据错误（PROTOCOL/PARAMETERS/PROVIDER/CALENDAR/SNAPSHOT_PIT/OOS/FREEZE）加5类执行 blocker。优化 Python 和坏 JSON 也拒绝执行。

## 最小证据合同（不是完整科学验收）

引用格式为 `{"path":"relative/file.json","sha256":"<64 lowercase hex>"}`，文件必须在 Manifest 目录内。重算非空文件字节 Hash，拒绝缺失、Hash 不符、绝对路径和越界 symlink。不要提交受许可限制的大数据或占位 Hash。

- protocol/source_receipt/protocol_qa 为原件；protocol_review 精确绑定三者 Hash。复制原件不产生审批。
- provider 授权核对名称、research_use_allowed、source_uri、license_scope、verified_at 等基本字段。
- calendar 每自然日一条 `{date,is_open}`，完整覆盖 data_start 至 calendar_end；每年 SSE/SZSE 原文由 calendar_sources 引用。官方域名只是语法检查。
- `calendar_review.bindings` 为 `{calendar:<sha>,sources:[{year,exchange,url,artifact:{path,sha256}},...]}`，顺序与 Manifest 一致；`freeze_review.bindings.calendar_sources` 绑定同一完整列表。修改元数据同样令旧审核失效。
- snapshot 宽表为 `{date,as_of,available_at,features}`：固定六列有限数、时区、上海同日、available_at≤as_of、无重复/缺失 session。**列名不能证明没有未来收益，整行 available_at 不能替代逐输入 PIT。**
- snapshot_receipt 记录 kind/provider/snapshot_sha256/source_uri/retrieved_at/raw_artifact；pit_review 绑定 snapshot/config/receipt Hash 与各项 PIT 审核说明。synthetic 改成 real 也不获准执行。
- parameter_approval 绑定 config 文件字节及协议 Hash；APPROVED 字符串与非空 B0/B1/C 描述不是模型验证。没有真实批准时保持 DRAFT/null。
- walk_forward 旧输入仅 `{train:[start,end],validation:[start,end]}`，oos 为 `[start,end]`；只做基本 T+5 purge/排序/尾部日历检查，不具备完整协议 split schema。
- oos_isolation 绑定 config/snapshot Hash，检查封存时间、untouched、access_control/audit_log 文件，不替代权限控制或污染审计。
- freeze_review 绑定 config、protocol/source_receipt/protocol_qa/protocol_review、calendar/calendar_review、snapshot/snapshot_receipt/pit_review、parameter_approval/oos_isolation、provider authorization Hash，以及完整 calendar_sources 列表。

所有 review 需要 decision/reviewer/带时区 reviewed_at/精确 bindings。**Hash 是完整性，不是签名或身份认证。** 一整套自洽合成/伪造文件可能通过部分检查，但仍拒绝执行。测试回执均标 SYNTHETIC，临时生成后删除，不作为真实审批提交。

## 验证与后续

本分支全部44个本地单测通过（研究36 + 原有8），包括合成改标 real、空/任意/重复特征、占位模型、一天窗口、官方 URL/年份/交易所变更和 CLI 退出码；原始协议/receipt/QA 字节 Hash 也锁定测试。测试证明脚手架行为，不证明模型/研究设计通过。

另将本次研究改动与已更新 main `e2d1457` 的精确 source/test/ledger 字节在独立本地目录组合，58项测试全部通过（研究36 + 评估22）；未将 main 合入本分支，也未改生产代码。

下一步仍是 D1–D7、合法数据/历史日历/PIT/OOS 保管证据，以及完整特征、模型、split、评估门禁的独立实现和验收；不能只填满 Manifest 就开跑。研究仍 Planned / NOT_RUN、指标 null，无 frozen 状态；本 PR 不授权合并、部署或晋升。
