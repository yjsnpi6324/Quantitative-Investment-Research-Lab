# Experiment 001A：数据、标签与执行验收协议（待冻结草案）

**结论：执行方案已整理；实验仍是 Planned，未运行、未验证、未晋级。** 本文把数据冻结、可得时点、透明基线、时间顺序验证及最终 OOS 门禁落实到字段、公式与检查表。所有新增数值都是**拟议默认值**，不是仓库已批准参数；数据源、真实日期及责任人未定，因此现在不得标记 `FROZEN`。

- 研究 ID：`EXP-001A`；建议模型身份：`MS-001A-RULE-3STATE-v0.1`，角色 `EXPERIMENT`。
- 本次只读核查日期：2026-10-24；仓库快照：`eba9c474314511b2abb4c001095ecc5151585ed8`。[S0]
- 原任务：[Issue #3][S1]，open，0 条评论；实验 README 为 Planned。[S2]
- 本次范围：协议与来源回执，本地交付；没有下载行情、运行训练/回测、改 GitHub/Notion/Dropbox、改生产任务或提出投资建议。
- 建议合入位置：`research/experiments/market-state-classification/experiment-001a-protocol.md`。本文不是已经合入的文件。

## 1. 已核实约束与真正的缺口

| 核查结果 | 对本实验的约束 / 行动 |
|---|---|
| 实验目录只有 README；没有数据规格、标签、分割或结果文件 | 不能把文档齐备等同于可直接开跑。冻结数据、实现与单测均待完成。[S2] |
| README 初始五类状态；Issue #3 提议 Bull / Neutral / Bear + 单独高波动标记 | 001A 采用较小假设集，五类留给后续实验；不是已确认的经济“真值”。[S1][S2] |
| Method Registry 泛称 Market-state classification 为 Active / Ongoing OOS | 与 001A 的 Planned 不是同一粒度；没有发现可把该行当成 001A 验证证据的链接。新增独立版本记录，保留并显式解释旧行，不自行改其状态。[S3] |
| 必须 PIT、无未来成分、walk-forward、最终 OOS、最简合理基线 | 所有输入按 `available_at <= information_cutoff`；没有 vintage 证明的历史序列不能冒充 PIT。[S2][S4] |
| 生产任务 T+1/T+3/T+5，BASIC 与 AI 独立 | 首轮仅研究 `basic_market` 的一个指数代理目标；不能外推为 AI 板块已验证，也不是现 Champion 对照。[S5][S6] |
| `ProviderMarketDataAdapter` 只是接口边界 | 未发现已绑定历史数据 provider 或实验数据快照；采购/新权限不在本次范围。[S7] |
| `AShareTradingCalendar` 只内置 2026 年休市日，其他年份 fail closed | 历史多年份测试必须先补经过官方核验的日历；严禁以工作日替代交易日。[S8] |
| `rolling_metrics` 的 stability/robustness 是简化分数，非本文定义；DQ gate 也不检查 PIT lineage | 不可直接当成本实验统计验收。新增研究专用指标与时点断言，不修改生产评分含义。[S9][S10][S19] |
| GitHub 存研究逻辑；Dropbox 存大快照；Notion 存操作状态/决策 | 本文只提议路径，不编造资产链接、冻结哈希或审批回执；后续写入需另按授权执行。[S11][S12] |

本次未见实验专用依赖锁、CLI 或测试。后续必须固定 Python、数值库/模型库、OS、随机种子、线程数、依赖 lockfile 与代码 commit；本协议中的操作步骤不是当前仓库已有命令。

## 2. 冻结前必须定案的 7 项

| ID | 拟议默认值（未批准） | 冻结证据 / 未决事项 |
|---|---|---|
| D1 | 沪深300**价格指数**日收盘作为唯一主目标；历史当期成分作为宽度宇宙 | 确认指数 provider ID、币种、价格/总收益口径；是否接受只覆盖该代理而非全 A 股 |
| D2 | 现有授权内 Tier A/B 行情源；官方交易日历；PIT 成分与公司行动 | 明确供应商、许可证、首次可得时间和修订/vintage 能力；缺一项不能冻结完整版本 |
| D3 | 开发集后留 **252 个预测交易日**最终 OOS；优先可信隔离历史期，否则前瞻期 | 不能凭“没在本次打开”声称 untouched；记录历史访问/调参污染审计。无法证明则最终验证从冻结后首个交易日起前瞻运行 |
| D4 | 每交易日 20:00 `Asia/Shanghai` 信息截止；预测在截止后生成 | 验证核心数据届时实际可得。截止前已知不等于今天回取旧数据；不明确的可得时间不能人为填 20:00 |
| D5 | 状态阈值及模型见 §4–6；主 horizon=T+5，T+1/T+3 次要 | 冻结同意该主假设，禁止根据更好看的 horizon 换主指标 |
| D6 | §8 的样本门槛、实质改善量、区块置信区间、非劣容忍度 | 数值是研究设计建议，不是仓库已有政策或保证能通过；需在看最终 OOS 前签字 |
| D7 | 研究负责人、数据审阅人、独立 OOS 保管/验收人 | 姓名/身份、审批时间、权限分离、运行预算、最终截止日及版本签名目前均为 `null` |

不需要先作投资观点选择。最小开跑条件是 D1–D7 有记录、所有必需文件哈希齐全、PIT 与日历测试通过。若 PIT 成分拿不到，可另开“指数-only 降级变体”作为探索，不能悄悄删去宽度后仍声称完成同一 001A。

## 3. 数据冻结与 Manifest

### 3.1 数据表与行级时间语义

每个日期使用交易所真实 session；保留 UTC 时间戳，展示时区为 `Asia/Shanghai`。日频观察粒度：`instrument_id × trading_date × vintage_id`；实验特征粒度：`benchmark_id × trading_date × cutoff`。

| 表 | 最少字段 / 不变量 |
|---|---|
| `calendar` | `session_id, trading_date, exchange, is_open, official_source_uri, source_revision, available_at`；覆盖所有历史/目标日期，跨年未知即 BLOCK |
| `index_daily` | `instrument_id, trading_date, close, currency, return_type, session_close_at, published_at, available_at, retrieved_at, revised_at, vintage_id, source_uri`；收盘正数、无重复/错日 |
| `constituents_pit` | `index_id, security_id, effective_from, effective_to, announced_at, available_at, vintage_id, source_uri`；仅当已公布且已生效才进入 `U_t`；不能回套当前成分 |
| `security_daily` | 稳定证券 ID、交易日、原始收盘、当时可得复权/公司行动、成交/停牌状态、上市/退市日期与其来源；保留后续退市证券 |
| `features` | `feature_asof, information_cutoff, upstream_row_ids, max_input_available_at, feature_version, dq_status, exclusion_reason`；所有输入可得时间不晚于 cutoff |
| `outcomes` | `origin_date, horizon, target_date, realized_return, event_y, actual_available_at, source_uri, vintage_id`；与输入物理/权限隔离，仅训练已成熟样本或指定评价时解封 |

`retrieved_at` 只表示本次抓取，不证明历史可得性。事后更正、新复权因子、新成分都不能覆盖旧 vintage。信息在截止后发布的，当日特征不采纳；宏观/海外/新闻首轮全部排除，避免引入未定义发布时间与跨市场收盘规则。

原始快照逐文件 SHA-256，规范化表另存 hash；Manifest 对固定 UTF-8、字段排序、换行规则的字节求 hash，不自我包含自身哈希。原始 bytes、提取逻辑及 schema 分别校验，不能只给一个 CSV 文件名。

### 3.2 缺失、停牌与质量处理

1. 原始数据不回填未来值、不双向插值；指数缺失、成分身份不明、时间冲突、关键修订无法核验：该日 `BLOCK`。缺失真实结果为 `ACTUAL_UNAVAILABLE`，不是 0 收益/预测失败/成功。
2. 宽度/离散度使用当日实际交易且有完整所需历史的 `V_t ⊆ U_t`。停牌当日不当作“平盘股票”；保留停牌原因、成员数、有效数。历史停牌日只有供应商明确记录的有效估值延续才可用于均线，不能拿未知缺失冒充停牌。
3. 新股历史不足 60 个交易日不进入宽度分母；退市或移出发生前的历史仍保留。公司行动按当时已知的逐日调整收益串接，禁止直接用今天统一后复权序列假装 PIT。
4. 建议要求 `|V_t| >= 200` 且 `|V_t| / |U_t| >= 0.80`；否则整日特征不合格。每天同时报告成员覆盖与排除原因，防止选择性停牌造成隐性幸存者偏差。
5. 必需特征不插补；B0、B1、C 使用相同有效样本，不能各自删掉失败日期。先按日历确定 split，再应用质量 mask，**不得删除坏日后重新把时间轴压缩**。
6. 记录重复、负价/异常跳变、来源冲突、缺失率、修订率、PIT 覆盖、各阶段/状态排除率。严重冲突需排查，不能事后仅删掉对模型不利样本。历史 DQ 的“新鲜度”按当时 cutoff 检查，不按今天减历史日期；原生产 policy 不被修改。[S10]

### 3.3 可实例化的 Manifest 模板

以下为合法 JSON 模板；`null` 不可被当作完成值。参数嵌入表示建议，不表示批准。

```json
{
  "schema_version": "exp001a-manifest-draft-v1",
  "experiment_id": "EXP-001A",
  "status": "DRAFT_NOT_FROZEN",
  "repository_commit": "eba9c474314511b2abb4c001095ecc5151585ed8",
  "protocol_hash": null,
  "execution_code_commit": null,
  "dataset_id": null,
  "freeze_at": null,
  "approved_by": null,
  "information_cutoff": {"timezone": "Asia/Shanghai", "local_time": "20:00:00"},
  "benchmark": {"name_proposed": "CSI300", "provider_id": null, "return_type": "price", "currency": "CNY"},
  "coverage": {"raw_start": null, "raw_end": null, "eligible_start": null, "eligible_end": null},
  "sources": [{"source_id": null, "source_uri": null, "tier": null, "license_reference": null, "vintage_policy": null, "available_at_rule": null}],
  "calendar": {"official_source_uri": null, "covered_years": [], "sha256": null},
  "universe": {"membership_mode": "point_in_time", "membership_asset_id": null, "sha256": null},
  "assets": [{"asset_id": null, "owner_system": "Dropbox", "canonical_path": null, "verified_at": null, "rows": null, "byte_size": null, "sha256": null, "schema_hash": null}],
  "labels": {"version": "rule-3state-draft-v1", "momentum_z_threshold": 0.5, "breadth_bull_min": 0.55, "breadth_bear_max": 0.45, "high_vol_quantile": 0.8, "high_vol_lookback": 252},
  "targets": {"primary_horizon": 5, "secondary_horizons": [1, 3], "event": "price_log_return_gt_zero"},
  "split": {"mode": null, "train_sessions": 756, "validation_sessions": 126, "test_sessions": 126, "step_sessions": 126, "minimum_development_folds": 4, "max_horizon": 5, "pre_eval_information_embargo": 5, "final_oos_sessions": 252, "split_file_sha256": null},
  "oos": {"origin_start": null, "origin_end": null, "last_outcome_date": null, "custodian": null, "access_audit": null, "unseal_at": null},
  "execution": {"python_version": null, "lockfile_sha256": null, "seed": 1, "threads": 1, "config_sha256": null},
  "qa": {"status": "NOT_RUN", "report_sha256": null}
}
```

资产建议目录：`/A股量化研究系统/01_Raw_Data/Snapshots/`；数据包名称遵循 `<dataset>｜asof-<UTC timestamp>｜<vintage>.<ext>`。研究输出放 `02_Research_Artifacts/Quant_Methods/`，大模型二进制按既有资产契约。这里未创建或核验任何该类资产。[S12]

## 4. 特征与操作性状态标签：不把未来写回当下

设 `P_t` 为主指数当日价格收盘，`r_t = ln(P_t / P_{t-1})`，所有窗口为真实交易日；只用至 t 的已可得值。

| 特征 | 固定定义（建议） |
|---|---|
| `z20`, `z60` | `ln(P_t/P_{t-L}) / (sigma20_t * sqrt(L))`，L=20、60 |
| `sigma20` | 最近20个 `r` 的样本标准差（ddof=1），不年化；为0则当日无效 |
| `drawdown60` | `P_t / max(P_{t-59},...,P_t) - 1` |
| `breadth60` | `V_t` 中，PIT 调整后的个股当日价格高于该股过去60日均价的等权占比；相等记不高于 |
| `dispersion1` | 同一 `V_t` 个股当日 PIT 调整收益的横截面样本标准差（ddof=1） |

最终 X 固定为以上6列。量价比、行业集中度、流动性代理留给后续变体；不能看到 OOS 后临时加入。

状态规则（**当前状态**，非未来收益标签）：

```text
if mandatory_data_invalid: state = UNKNOWN, exclude_with_reason
elif z20 >= +0.5 and breadth60 >= 0.55: state = Bull
elif z20 <= -0.5 and breadth60 <= 0.45: state = Bear
else: state = Neutral

q80_t = 80th percentile(sigma20[t-252 : t])  # 不包含 sigma20_t
high_vol_t = (sigma20_t > q80_t)             # 相等为 false
```

分位数算法固定为排序后线性插值；必须有252个既往有效波动值，不能用全样本分位数。由此原始价格预热至少覆盖20个收益窗口再加252个过去波动观察；按公式确定首个有效日，不随 split 重置历史。`UNKNOWN` 是数据状态，不是第四种市场状态。

这些标签只是可复现的工作定义。**不得训练模型复现这套规则后，把高分类准确率称为“识别真实市场状态”或“预测收益能力”。** 首轮状态分类器本身就是透明规则，真正检验的是加上状态后未来预测是否增益。高波动为独立诊断旗标，首轮不把3×2组合拆成6个专家，以免稀释样本。[S1][S2]

## 5. 下游目标与不变量

- `R[t,h] = ln(P[t+h]/P[t])`，h∈{1,3,5}，目标日期只由官方交易日历计算。
- 主事件 `Y[t,h] = 1{R[t,h] > 0}`；恰为0归“非正”，不是任意删除。预测 `p=P(Y=1)` 是点概率；`p > 0.5` 判正，否则判非正，平手固定判非正。
- 此处是截止后对 close-to-future-close **统计事件**的预测；当日收盘价不代表预测发布后能按该价成交，不宣称策略收益。
- `state_t` 和 X 在预测时可得，`Y[t,h]` 仅在未来 t+h 收盘、可靠行情可得后用于训练或评分；`label_available_at <= fit_cutoff` 为硬断言。
- 先锁 `prediction_id, origin_date, cutoff, state, high_vol, p_B0/p_B1/p_C, config_hash, data_snapshot_id, code_commit` 的研究预测字节哈希；actual/outcome 在旁表追加，永不重写预测。
- 现有日报概率区间、主观文字、HIT/PARTIAL/MISS 不转换为本研究事件/点概率，不据其硬算 Brier；缺失原始预测也不重建。[S13][S14]
- 本实验唯一主比较是 **T+5 的 C 对 B1**；T+1/T+3、B0、状态切片均完整报告，但不以其中最漂亮者替代主检验。

## 6. 透明基线与最小候选

| 模型 | 实现规范（拟议） | 意义 |
|---|---|---|
| B0 | 每一训练窗按 horizon 的历史正收益频率，Laplace 平滑 `(n_up+1)/(n+2)`，窗口内所有预测同概率 | 无特征常数概率/多数方向底线 |
| B1（主基线） | 每 horizon 一套 pooled L2 logistic，6列 X；不输入 state、不分状态、不变路由；各列训练窗均值/标准差缩放；单一模型权重恒为1 | 最简 regime-agnostic 基线；固定权重单成员特例，非现生产 ensemble |
| C（候选） | 相同 X、目标、训练样本、缩放、超参数与预测日；训练3个 state 子样本 logistic；`p_C = w_s*p_s + (1-w_s)*p_B1`，`w_s=n_s/(n_s+252)` | 只检验状态条件化是否带来增益 |

拟议锁定：L2、`C=1.0`、包含截距、`class_weight=None`、确定性求解器 `lbfgs`、`tol=1e-6`、`max_iter=2000`、seed=1、单线程；锁定具体库版本后确认其参数语义。标准化只 fit 训练窗，std=0 的列置0并记日志；不使用全样本标准化、无目标驱动特征筛选，无调参网格。

每状态训练样本 `n_s < 126` 或任一 Y 类少于20时，`w_s=0`，明确回退 B1；不把退回 pooled 的结果算作有效状态专家证据。子模型不另 fit scaler，沿用同训练窗 B1 scaler。B1 若缺类、拟合不收敛则 fold BLOCK；C 若本应可训练但不收敛也 BLOCK，不得静默把故障伪装成成功回退。

首轮不做额外概率重校准。若开发集证明需要校准，另登记变体，在训练内单独设时间顺序校准窗，并重做开发验证；不能在 OOS 上 fit Platt/isotonic。开发结果不足时仍应产出失败记录，而非无限尝试至成功。

主结构检查是 `C` 与已有全连续 X 的 B1 对比，避免拿过弱的仅均值 baseline 夸大标签贡献。其他特征消融只能另行登记，不扩充首轮必跑模型。后续如要生产提案，还须补真实 Champion 同任务、同事件/窗口的可比结果；本轮不声称已完成这一步。[S5][S15]

## 7. 时间顺序 walk-forward、purge、embargo 与最终 OOS

### 7.1 先冻结 session 清单，后读结果

`splits.csv` 必须显式列出每行 `session_id,date,fold_id,role,fit_cutoff,target_dates,purge_reason,embargo_reason,dq_status`，不可只写“80/20”。日期来自实际已核验数据与日历；本次没有这些数据，所以以下是**可直接实例化的索引算法，不是假造的冻结日期**。

建议每 fold：训练756、验证126、开发测试126个 session；测试步长126，至少4个不重叠开发测试窗。设 `Hmax=5`，附加信息 embargo `E=5`，总边界间隔 `g=Hmax+E=10`。

以下端点均含首尾，索引是预热结束后的原始交易日历位置，不是删缺失后的行号：

```text
outer_test = [a, a+125]
validation = [a-136, a-11]                 # 126 sessions
inner_train = [a-902, a-147]               # 756 sessions
gap_before_validation = [a-146, a-137]     # 10 sessions
gap_before_outer_test = [a-10, a-1]        # 10 sessions

用 inner_train 训练，产生 validation 预测；仅诊断/开发，不碰 final OOS。
规则/超参数已锁且 QA 通过后，outer_test 前统一重新拟合：
outer_fit_origins = [a-892, a-11]          # 最近882个可用 origin slots
for every model and horizon:
    retain only origins with actual_available_at <= fit_cutoff
    assert target_index(origin, Hmax) < a-E
    assert all feature_input_available_at <= origin_cutoff
生成整个 outer_test 期间的预测，模型参数不在该窗内重拟合。
a_next = a + 126
```

窗口长度指原始日历槽位；DQ 掩码后实际 n 另报。validation 边界同样断言 `target_index(train_origin,5) < validation_start-E`。outer fit 可以纳入此前验证/开发测试里已经成熟的历史样本；永远不纳入当前测试窗或未来信息。特征的后向窗口跨越边界是允许的（真实可观察历史），禁止的是未来目标/fit 统计跨界。

**Purge 与 embargo 分开记账：**

- Purge：训练样本的结果区间 `[origin, target_date]` 若触及或跨过当前评估窗开始，剔除；目标端点恰等于开始也剔除。
- 附加 pre-evaluation information embargo：即使已 purge，还要求所有训练结果结束于评估开始前至少 E 个完整 session。上式合计留下10个预测起点槽位不用于 fit。
- 通常所说评估窗后的 embargo 为 `[test_end+1,test_end+E]` 不进入该 fold 的未来侧训练；本协议每 fold **根本不使用未来侧训练**，因此该项天然满足，不能谎称需随机双向 CV。未来 fold 仅在过去结果成熟并满足自己的边界约束后使用它们。
- 不随机打乱、不 K-fold 时间混排；开发测试窗的表现不是最终独立 OOS。所有尝试和失败版本进 `trials.jsonl`，没有“只报告胜出者”。

索引例（仅说明算法）：a=902 时训练0–755、gap756–765、验证766–891、gap892–901、测试902–1027；随后测试1028–1153、1154–1279、1280–1405。实际日期必须通过已冻结官方日历导出。

### 7.2 最终 untouched OOS

1. 在开发开始前由独立保管人锁定起止日期与252个预测日；最后一个目标实际日期为末个 origin 后第5交易日，不能把未成熟尾部当0或随意裁掉。
2. 历史方案只能取**事先规定的连续末段**，并证明模型/特征/阈值选择没有使用其结果；不得挑选有利牛熊阶段。访问审计不能建立时，历史回测一律称“历史留出/探索”，最终验证改为冻结后首交易日起的252个前瞻预测日。
3. 所有开发评分 origin 也须 `target_index(origin,5) < OOS_start-E`，避免开发集末尾标签读入 OOS 价格。OOS 前10个 origin 槽位不参与最终拟合。使用 OOS 起点前最近882个符合规则的 origin 训练最终 B0/B1/C。
4. 最终 OOS **一次性锁定模型**，整段不 refit、不调标签阈值、不校准、不按中期结果改门槛。滚动特征/过去252日高波动阈值只按已锁公式向前更新，不使用未来数据或 Y。
5. 历史回放由隔离评价程序按日注入截至 cutoff 的 X；前瞻运行按真实时间生成。两者均保存每个预测 hash，再追加对应 actual；研究者不得中途读取聚合 OOS 分数。
6. 全段目标成熟后一次解封，保留访问者/时间/文件哈希。缺失实际仍未齐时记录未完成，不用代替行情；按预注册覆盖门禁出结论。看过结果后的改进是新版本，原 OOS 从此仅为开发证据，需新 untouched 期。
7. 不因未覆盖某状态而事后延长/剪裁以争取通过。按 §8 判 `INCONCLUSIVE / Keep Testing`；若要新一期，先登记新固定时间窗，不覆盖旧失败记录。

## 8. 指标、统计与验收门禁（全部为待批准建议）

### 8.1 统一定义

- 方向准确率 DA：`mean(1{(p>0.5)==Y})`；明确“非正”包含零收益。
- 主概率分数：`Brier = mean((p-Y)^2)`，越低越好；主增益 `delta = Brier_B1 - Brier_C`，正值为改善。
- Balanced accuracy：同一 regime 内 `0.5*(TPR+TNR)`；任一真实类别缺失则 N/A，不填0、不悄悄改成单类别指标。总体与各状态都给 n、正/负类数量。
- 校准：5个固定等宽概率箱 `[0,.2),...,[.8,1]` 的 n、预测均值、实际频率；空箱 N/A。报告 Brier 与可靠性表，不能把 accuracy 当 calibration。
- 稳定性：各开发窗/最终两个连续126日子窗的 delta、DA、BA；state 占比、转移矩阵、切换率、持续期中位数/分位数、high-vol 占比；首尾截断持续期单列。
- 下行集中误差：真实 `Y=0` 时仍预测正的 false-positive rate、Bear/high-vol 中该值与 Brier、最差20个单日概率损失及连续失误段。样本不足明确 N/A。
- 所有模型按完全相同 origin/horizon 做 paired comparison，同时报告原始应有 n、有效 n、缺失 n、回退比例；无样本的指标为 null，不使用现有 helper 的空集0分。[S9]

统计：按连续 session 的**配对 loss difference**作 moving-block bootstrap，block长度20、重抽2000次、seed=1，95% percentile 区间；附 block长度10/40敏感性，保留缺失掩码与日期，不把稀疏缺失后的日期拼成连续日。方向差同样成对重抽。只有 T+5 主检验有确认性地位；其他 horizon/切片不宣称未经多重比较控制的显著性。区块方法只是处理重叠 horizon 与相关性的预设近似，不保证覆盖率或统计功效。

### 8.2 分层 Gate

| Gate | 建议通过条件 | 未满足时 |
|---|---|---|
| G0 完整性 | Manifest 所有必需 null 已补齐；0 个未解决时点/哈希/日历/成员身份严重错误；相同样本/同一目标；重跑预测在规定容差内一致 | BLOCK，禁止看分数后补规范 |
| G1 开发充分性 | ≥4个不重叠测试窗；至少3窗 T+5 delta>0； pooled 开发 delta>0；没有单一窗贡献超过总正向改善的80%；各类失败、回退、缺失完整报告 | Keep Testing / 重开版本，不进入最终解封 |
| G2 OOS 可评价性 | 252个预定预测日中 ≥95% 有共同有效数据；每个 Bull/Neutral/Bear 至少30个配对日且各有≥10个 Y=0/1；high-vol 切片≥30日；两个126日子窗均可评分；状态专家至少在两个状态实际生效 | INCONCLUSIVE，不称通过；稀少类别不算模型失败但不足以证明稳健 |
| G3 主增益 | T+5 `delta >= 0.002`（绝对 Brier）且20日 block 的95%区间下界>0；10/40日 block 敏感性区间下界也均>0，否则视为统计不稳健；两个126日子窗 delta均>=0 | Fail / Keep Testing，不能换主指标或放宽阈值 |
| G4 不伤害 | 总体 `DA_C-DA_B1 >= 0`，该差95%下界>=-0.01；各有足够样本的 state BA差>=-0.03；各state及high-vol Brier恶化不超过0.01；真实Y=0的 false-positive rate恶化不超过0.03 | 记录退化场景，不认为跨状态稳健 |
| G5 可复现与故障解释 | 提供逐日预测/结果、完整配置/快照/版本、最差案例、缺失机制、重跑对齐；没有用事后 revised 数据救结果 | BLOCK 或 Keep Testing |

0.002、1/3个百分点等数值是**待责任人批准的最小实质差异/容忍度**，不是从数据算出的结果。状态支持数/样本量不足时应讨论功效与新窗口，不为追求显著性增加试验次数。所有 gate 只有“待运行”，当前没有任何性能数值。

G0–G5 通过仅表示该版本具备**研究层面提出进一步验证的资格**；仍不能直接标 CHAMPION、改模型权重或用于生产。需另按治理完成当前 Champion 的同任务对照、相关生产适配、成本/执行可行性与正式决策。AI Sector 必须单独验证。[S5][S15]

首轮不构造交易策略，交易成本指标记 `N/A — forecasting-only`。若后续将状态用于交易，须另冻结真实可成交起点、停牌/涨跌停约束、持仓与换手规则、费用/滑点及成本压力梯度；不得用 close-to-close 预测回测自动冒充可交易净收益。[S2]

## 9. 产物、评估记录与注册表衔接

建议目录（均为拟议新文件，不是已存在）：

```text
research/experiments/market-state-classification/
  experiment-001a-protocol.md       # 本协议
  configs/001a-v0.1.yaml            # 待决项批准后唯一运行配置
  manifests/<dataset_id>.json      # 真实资产引用/字节hash，不含大数据
  splits/<run_id>.csv              # 明确日期、各角色与排除原因
  runs/<run_id>/run_manifest.json  # 代码、依赖、硬件、耗时、种子、运行状态
  runs/<run_id>/data_qa.json
  runs/<run_id>/trials.jsonl
  runs/<run_id>/metrics.json
  runs/<run_id>/failure_cases.md
  runs/<run_id>/evaluation.md      # 按现有模板记录 baseline/OOS/decision
  runs/<run_id>/artifact_index.json # 大型逐日预测、actual、模型的资产引用
  runs/<run_id>/registry_decision.md
```

实现建议另放 `src/research/market_state/` 与 `tests/research/`；不要把尚未验证研究代码接进 `run_prediction`、`run_evaluation_closure` 或自动变更生产 registry。

研究预测 schema 应独立且 versioned，保留现有 immutable 思想及 T+1/3/5字段，但不能为实验方便往生产 canonical JSON 加键或强制套日报语义。[S6][S13] 逐日输出至少带 baseline/candidate 同行概率、实际事件、regime、高波动、全部 ID/hash、fit window、outcome availability、missing/fallback reason。

`evaluation.md` 必须写：任务/版本、数据与日期、基线、主次指标、IS/开发/OOS身份、样本与缺失、失败案例、限制、Gate逐项结果、Decision、下一步及资产链接。未运行实际结果=`NOT_RUN`，无样本指标=`null`。遵循现有 experiment/evaluation 模板，不伪填 HIT/PARTIAL/MISS。[S16][S17][S18]

拟议 registry 决策草案：

> `Market-state classification / EXP-001A / v0.1`：研究状态 `planned`，模型角色 `EXPERIMENT`；如后续纳入简化 Method Registry 则单独行 `Testing`，Evidence 指向本协议且明确 **protocol only; no OOS result**。当前 Decision：Keep Testing / Prepare frozen data。不得把既有泛称 Active 行解释为本版本批准；其历史含义待 owner 澄清。真正状态写入/Notion 决策须另行授权与回读验证。

## 10. 后续执行检查表与停止条件

### A. 准备与冻结

- [ ] 审阅 D1–D7；指定数据与 OOS 保管人；分开研究审批与生产权力。
- [ ] 查询现有授权数据可用性，验证历史成员/vintage/许可证，**不新增付费订阅**。
- [ ] 先按官方交易日历导出真实窗口及 t+1/3/5目标日期，修复已知仅2026年覆盖限制。
- [ ] 完成原始快照、schema、数据QA、PIT回放；把修订/时点不明项留在排除清单。
- [ ] 创建配置、split、数据Manifest、依赖锁；核对各文件hash；独立审批后才设 `FROZEN`。
- [ ] 记录 final OOS 的污染审计、隔离权限、解封条件；不能证明隔离就选择前瞻方案。

### B. 实现验收（非真实实验结果）

- [ ] 用合成数据测试标签阈值相等、零收益/零方差、分位数不含当日、缺失与停牌分母、成分变更公告时间。
- [ ] 用可控“未来哨兵”修改 t 之后价格，确认 t 的 X/state/prediction 不变；复权未来事件不能改变旧特征。
- [ ] 验证 purge/embargo 端点、跨年/节假日、t+5未成熟、calendar未知年份 fail closed。
- [ ] 验证全样本 scaler/未来标签注入会触发拒绝；训练ID与OOS ID交集为空。
- [ ] 独立检查 Brier fixture：Y=[1,0], p=[0.8,0.2]，Brier=0.04；空集=null，缺真实类别的BA=null。
- [ ] 检查模型回退、收敛失败、相同日期配对、重跑容差、hash不一致阻断；不把fixture算成实盘证据。

### C. 开发验证与一次解封

- [ ] 只在开发分区运行 B0/B1/C；留存每次尝试、每fold逐日预测、全部失败与复杂度。
- [ ] 先判 G0/G1；失败则停止解封，开新研究版本，而不是换分割争取通过。
- [ ] 锁定最终 config/code/hash；OOS 程序按固定起止日运行，不反馈中期分数。
- [ ] 待最后目标成熟，核验 actual 与来源再一次性解封；计算 G2–G5，原始缺失保留。
- [ ] 写失败分析：状态边界频繁切换、危机转折、低覆盖/停牌、新股/退市、概率过度自信、子模型稀缺、跨年度退化。
- [ ] 形成版本化 Evaluation 与 Registry 决策草案；后续如获授权写入，要回读并核验实际 commit/资产/决策身份。

**停止/转交规则：** 数据/许可/官方日历/PIT证据缺失→停止依赖步骤并给具体缺口；未成熟结果→保持pending；污染或哈希错误→BLOCK并记录；样本/阶段不足→INCONCLUSIVE；OOS不通过→保留失败并 Keep Testing/Retire，不追认旧版本；即使通过，也不改变生产。

## 11. 本次交付验收边界

- 已完成：只读读取 Issue、实验目录、数据治理、registry、生产隔离、资产职责、评估模板/schema、日历/数据adapter/评分实现；据此形成本文与 `experiment_001a_source_receipt.json`。
- 交付前检查：Markdown结构、JSON模板可解析、来源链接与固定commit、窗口长度/端点公式、关键参数一致性；见附带 `experiment_001a_protocol_qa.md`。
- 未完成且不冒充完成：数据冻结、provider核验、历史日历补全、实验代码、训练、开发测试、OOS、资产上传、registry修改、方法晋级。

## 来源（固定仓库快照；Issue 本身不可按 commit 固定）

[S0]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/commit/eba9c474314511b2abb4c001095ecc5151585ed8
[S1]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/issues/3
[S2]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/research/experiments/market-state-classification/README.md
[S3]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/research/method-registry.md
[S4]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/research/DATA_SOURCE_GOVERNANCE.md
[S5]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/research/RESEARCH_INTAKE_CONTRACT.md
[S6]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/config/production_tasks.yaml
[S7]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/src/adapters/market_data.py
[S8]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/src/evaluation/a_share_calendar.py
[S9]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/src/evaluation/metrics.py
[S10]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/config/data_quality_policy.yaml
[S11]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/docs/SYSTEM_OF_RECORDS.md
[S12]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/docs/DROPBOX_ASSET_INDEX_CONTRACT.md
[S13]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/docs/governance/PLUGIN_EXECUTION_POLICY_20261020.md
[S14]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/evaluation/RECOVERY_BASELINE_2026-08-26.md
[S15]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/docs/REGISTRY_GOVERNANCE.md
[S16]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/templates/experiment.md
[S17]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/templates/evaluation.md
[S18]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/evaluation/README.md
[S19]: https://github.com/yjsnpi6324/Quantitative-Investment-Research-Lab/blob/eba9c474314511b2abb4c001095ecc5151585ed8/src/data_quality/gate.py
