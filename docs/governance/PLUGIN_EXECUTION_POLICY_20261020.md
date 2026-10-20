# 预测任务插件执行规则 — 2026-10-20 R2

Policy ID: `PLUGIN-POLICY-20261020-R2`

适用于两条独立A股生产任务、既有多节点治理与美股三大指数/中国红利低波观察。此文件与20261017能力注册表互补，只收敛调用、审计、替代和故障行为；不追认历史结果、不更换模型、不扩大四核心写权限。修改后的Task提示词必须单独保存并回读；文档合并不等于Task已更新或计划运行已验收。

## 当前检查证据与限度

| 能力 | 2026-10-20管理会话结果 | 验证限度 |
| --- | --- | --- |
| Bigdata market tearsheet | 成功返回FMP来源/时点 | 未在此检查独立验证所有报价；ETF与指数分开 |
| Exa + Firecrawl | 上交所休市公告发现/原文回读成功 | 同一公告是一条来源 |
| Firecrawl论文检索/正文 | 检索成功；已读取arxiv:2608.23808正文片段 | 仅验证检索/片段读取，不代表整库或方法有效 |
| Firecrawl公开模型卡 | Qwen/Qwen3-8B页面HTTP 200 | 不代表Hub连接器或模型推理可用 |
| firecrawl-trends interest_over_time | 两关键词2026-09-01至09-30返回30个日桶 | 相对热度，不是访问量；本次消耗5 credits不构成未来费率承诺 |
| Wolfram | 合成fixture Brier=29/300、Correlation=1 | 不构成实盘统计验收 |
| Context7 / Vercel | Supabase官方文档/既有项目清单可读 | 版本兼容与deployment/runtime未验收 |
| Similarweb直接流量接口 | 403产品权限缺失 | 仅此端点级结论 |
| Firecrawl Similarweb流量通道 | 402额度不足，提示需预留最多110 credits；provider未执行 | 不是可用替代来源；不代表已消耗110 credits |
| Scite / Ahrefs | 订阅门禁 / Ahrefs额度与metrics均Insufficient plan | 已连接不等于有数据权限；用户未购Ahrefs套餐 |
| Hugging Face model_search | 上游tools/list未提供 | 不推断官网或其他端点也不可读 |

这些记录均为管理会话证据；生产推广计数从实际计划运行的可回读回执开始。没有运行证明就不声明生产生效或增益。

## 共同执行规则

【插件联动规则｜PLUGIN-POLICY-20261020-R2】
读取main的docs/governance/PLUGIN_EXECUTION_POLICY_20261020.md并记实际commit/blob；该文补充20261017能力注册表，沿用其转正门禁。读取失败时执行以下自足规则，不宣称已读取。2026-09-19 Notion插件编排基线是历史记录，不能覆盖当前任务版本。插件按本轮具体缺口选择，工作流技能不是独立数据源。
1. 优先现有官方行情/日历/公告证据；Bigdata查金融/宏观/财报/事件候选，Exa补来源缺口，Firecrawl恢复所选原文。重要事实逐条检查时间、口径与独立来源；多个工具返回同公告/转载/同底层数据商，只算一条来源。BASIC聚焦资金风格及衣食住行银行，AI聚焦产业链、业绩/订单与海外映射；跨市场观察始终保留四个主指数口径。
2. 替代路径明确分开：论文问题→Firecrawl research_search_papers，已知ID用research_inspect_paper/research_read_paper，需要引用关系再用research_related_papers；仅摘要可得就标摘要证据，不能伪报Scite支持/反驳分类。模型资料→Exa发现官方模型卡/作者仓库，Firecrawl读公开卡或GitHub读README；只研究资料，不下载或运行模型、不替换Champion。需求热度→Firecrawl先find_tools取firecrawl-trends/trends/interest_over_time当前契约，再按有限关键词/时间窗查询；搜索热度0–100是区间内相对指标，记录地区、搜索类型、完整/partial时间桶，不等同于访问量、App活跃、收入或领先因子，不直接决定正式预测。
3. 先复用截至信息截止已可用、时点与口径一致的公开证据；缓存必须保留来源/发布时间/观察时间，不能借缓存引入未来信息或复用另一条预测身份。非交易日无增量时不反复查收盘/旧政策。每轮新增SHADOW最多1个具体研究问题；核心数据和正文优先完成，辅助检验不延误FINAL/Handoff，不提高正式生产工具预算。
4. 不购买套餐、充值或自动加购；仅用现有授权与额度。Scite订阅门禁、Similarweb流量403、Ahrefs账户/metrics套餐门禁、Firecrawl的Similarweb流量通道额度不足、Hugging Face model_search上游缺失均是已知“端点级”限制。未有真实套餐/权限/工具清单变化前不盲试、不换通道绕过相同门槛；本轮未调用记NOT_INVOKED，另记last_known_status=DEGRADED及skip_reason=PLAN_LOCKED/QUOTA_LOCKED/TOOL_UNAVAILABLE，不能把历史失败算本轮失败。用户已说明未购买Ahrefs套餐。高额度/成本不明查询改选有来源的公开材料，缺口保留N/A；catalog列出能力不等于执行成功。可恢复超时/429/5xx依工具指示最多1次重试；参数错误先读schema，仅在符合用户约束时纠正一次；401/403/付费门禁不循环重试。
5. 每个实际调用记plugin/capability、task_id/production_id/report_id、policy_revision、requested_at及时间依据、input_scope、明确source_uri、published_at/available_at、status、可可靠计算的digest、corroboration、adoption=ACCEPTED/REJECTED/NO_INCREMENT/SHADOW、具体正文用途和原因。请求时刻只能用真实客户端/工具时间；缺失为null/UNAVAILABLE，run_started_at单列，不能拿运行起点替代所有调用时刻。来源必须给可回读URL/ID，不能只写“返回19条链接”。旧时间或digest不可回写修正已锁FINAL。
6. Public Equity Investing用于催化/估值/反证，Data Analytics用于数据质量与已定义统计，Wolfram仅独立SHADOW复算，Flourish仅展示核验结构化数据，Context7/Vercel仅技术校准/现有部署观测；都不对方向投票。邮件/Drive/Slack只在已知项目研究范围有具体需要时最小只读；不发送消息、不扫私人资料。无当前用途的插件不调用。
7. Notion搜索仅作候选发现。优先已核验source URI或对应目录；必须fetch全文并核对Task/Production/Report ID、日期和文种后使用。搜AI返回BASIC、标题近似、目录陈旧或无结果均不能冒充目标报告，记SOURCE_IDENTITY_UNVERIFIED/NOT_FOUND_IN_CHECKED_SCOPE并交治理核查；不据搜索未命中断言从未生成，不跨线替代、不后验重做预测。
第1段/跨市场来源段用紧凑审计表，第8/9/10段列真实采用证据与反证；保持固定正文与Handoff，不新增第13段或Canonical JSON键。管理会话测试仅是带日期的种子，不能当本轮调用或计划运行验收。

## 生产任务

【生产侧观察与职责】
论文、模型卡和Trends替代路径本会话已单次读通，仍未完成本版计划运行验收，新增结果仅SHADOW；同一插件多个能力分别核验。每个新增能力按既有门禁积累至少3次不同真实计划运行，与可复核原基线对照来源一致性、证据增量、时延/可见成本和实际失败降级，未实测失败则UNTESTED，无可比基线不声称改善。只让原有已独立核验的证据路径参加既有研究，不自动调整模型权重/概率/Champion。全部证据审计随首次FINAL锁定送原Notion Mailbox；后续累计/转正/四核心/Evaluation交治理，生产不写其他节点。可选插件不可用不单独阻断日报，核心行情/官方交易日历/必要证据仍按原Data Quality Gate阻断。

## 治理任务

【治理侧闭环】
先完成Mailbox→原始Hash/正文/Target Dates→四核心→到期Evaluation，再观察辅助插件。按task_id+production_id+report_id+policy_revision+capability去重累计，管理测试、人工重跑、相同报告重试不冒充不同计划运行；RUN_ORIGIN无可靠证据则UNVERIFIED。可读取明确且只读的公开证据缓存，禁止跨预测ID复用评估。审计/3轮记录只追加在既有允许的治理回执/Registry兼容字段中，记录source URI和检查时点，不建表、不改schema、不回写FINAL；不能保存则STATE_UNPERSISTED，不声称已累计。按既有对照、来源/失败门禁审查，满足条件才允许证据层升级，不改Champion或正式工具预算。
Data Analytics只从合格FORMAL_CLOSED样本分线/版本/跨度计算定义明确的指标，概率是区间且无点估计/事件编码时不硬算Brier；Wolfram给定相同真实输入作独立复核；样本不足N/A，三次接口成功不等于预测增益。对部署/接口异常才触发Vercel/Context7，项目清单可读不代表runtime健康。
分别核查两线预期Report与已读Mailbox；真实运行已发生而源仍未读到时记录SOURCE_IDENTITY_UNVERIFIED或NOT_FOUND_IN_CHECKED_SCOPE、已查范围、最近有效身份与待重试项，不用另一线或旧REVIEW顶替，不自动补做历史预测。通知仅在实质故障/状态变化/证据增量时出现。

## 跨市场观察

【跨市场侧边界】
只读观察，完整四指数与宏观核验优先；不写A股生产/治理记录，也不创建旁路存储或调度。新Trends/模型/论文证据仅SHADOW，至少3次不同真实计划运行保留可复核来源、一致性/增量/时延与失败证据后才按既有规则评估用途；未实测项UNTESTED，不能宣称提高预测准确率。实际指数、ETF、价格/总收益、本币与时区口径继续独立标明。

## 不变量与验收

- 保留Production IDs、Champion/模型权重、官方交易日历、固定12段、首次FINAL锁定、Native Prediction Hash schema与BODY_ALIGNMENT。
- Task仅改prompt，不改变schedule、timezone、enabled、conversation归属；学习任务不在本次范围。
- 政策字段进入审计，不能新增Canonical JSON字段或后验改已发布Hash。
- 故障状态的历史种子与本轮实际调用分开；optional能力缺失与核心证据缺失分开。
- 配置验收：逐字Task回读，保护段落不变，main文件回读，PR/检查状态可核验。
- 运行验收：后续真实计划运行验证替代路径、审计链接与时间、断路/降级和证据用途；无实测不声称已通过。
