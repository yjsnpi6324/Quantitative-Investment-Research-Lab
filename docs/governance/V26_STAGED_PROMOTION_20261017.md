# 日报多节点治理 V2.6：分批转正与验收门禁（2026-10-17）

范围：TASK-ASTOCK-DAILY / BASIC-PROD-20260825-A 与 TASK-AI-DAILY / AI-PROD-20260825-A；两条谱系独立。本文件只定义治理运行门禁，不修改任何已锁定 FINAL、生产任务提示词、预测值或既有评估。

## 第一批：正式治理基线（PRODUCTION_GATED）
- 完整 Notion Handoff FINAL + Handoff Block 读取、FINAL/REVIEW/SYSTEM-E2E 分类与 PROD-PROMPT-V3/V3.x 版本门禁。
- Canonical Manifest、可稳定规范化时的报告 content_hash；不得将其与 Prediction Hash 混用。
- V3.5+ 新 FORMAL_PREDICTION 原始 Canonical JSON 严格校验、NATIVE Hash 独立重序列化/复算、Target Dates 官方交易日历独立校验、BODY_ALIGNMENT 对照第4/5/6/11段。
- 只读/追加式治理回执、原始 FINAL 不可变；非交易日 REVIEW 不生成 Prediction Hash 或 Evaluation。
- 任何缺失、冲突、未核验或不一致均 fail closed；不得以历史成功替代本轮源与四节点回读。

## 第二批：受控生产（CONTROLLED_PRODUCTION）
- 四核心 Supabase / Notion Registry / GitHub main / Dropbox 幂等扇出：逐节点读后写、写后回读，仅当四节点及身份、正文、Hash/Target Dates（适用时）一致才给 PERSISTENCE_READY。
- Repair/Retry 仅重试失败或缺失节点；不覆盖已 VERIFIED 节点；GitHub 只通过 branch -> PR -> merge -> main readback，不将 PR_PENDING 当完成。
- Evaluation T+1/T+3/T+5 append-only：仅有效原始 Hash、正确交易日、经独立证据核验 Actual、去重及正文对齐全部满足时 FORMAL_CLOSED；否则保持 ACTUAL_UNAVAILABLE / BLOCKED_INVALID_HASH / HASH_MISMATCH_BLOCKED / NOT_DUE / ALREADY_EVALUATED。
- Champion Health Check 只输出可复算的分项指标；未定义完整输入/公式的综合 Health Score 不升级为可信自动决策。
- 异常、证据不齐、接口限流或节点分歧时停止自动晋级并人工复核；禁止静默覆盖或自动补造事实。

## 第三批：测试隔离（SHADOW_ONLY）
- Supabase fresh/replay/完整 db reset 的真实 CLI CI，须全绿并复核权限矩阵后才能解除门禁；不得对生产库执行 reset。
- 历史 MIGRATED Hash provenance 与自动 Backfill：仅 append-only 证据记录，不能伪装 NATIVE 或自动入评；全自动历史修复继续关闭。
- OpenAI Agents adapter：仅已验证的 provider-neutral / offline contract；真实模型、工具、密钥和生产执行必须独立验收，不因离线测试通过而自动启用。
- Bigdata / Firecrawl / Context7 / Vercel / Flourish 等保持各自旁路定位，不替代 FINAL、Actual 或四核心回读。

## 转正退出条件与回退
1. 第一批：每次生产运行仍逐份完成完整性、Hash/Alignment、来源和版本门禁；异常回退为 PERSISTENCE_PARTIAL 或 GOVERNANCE_VERSION_REVIEW。
2. 第二批：至少通过去重重放、单节点失败重试、节点不一致阻断、评估缺 Actual 阻断的可复现实测；此前只视为受控运行，不宣称无人值守自愈。
3. 第三批：Supabase CLI Postgres 17 两段重建和权限检查全绿；Agents adapter 必须另有真实生产兼容/故障证据；历史 provenance 逐案审查，不设自动整体放行。
4. 所有批次不重写 FINAL、不重新预测、不制造保活数据；变更只能走最小 PR 与回读。任何转正仅为运行策略，不构成对历史每条记录的追认。

## 当前证据和已知缺口
- QIRL #47–#56 为多日真实治理归档/回执证据，须逐个核实 main 和四核心才可对单条报告声明 READY。
- gpt-workspace #5 的 runtime contract 与离线 Agents SDK 测试成功；这不是生产 Agent 已上线的证据。
- gpt-workspace #6 已合并，但 GitHub Actions run 38573363368 的 reset-and-grants 失败于 no_default_grants.sql 对 supabase_admin 的默认权限修改；完整 db reset 被跳过。此项保持 SHADOW_ONLY，修复并重新运行后复核。

## 2026-10-22 增量验证：Supabase 本地 CI 解除旧阻断（append-only）

本节追加最新证据，保留上文 2026-10-17 的历史失败描述作为当时快照；不追认任何旧预测、不更改生产数据库或四核心持久化判定。

- `gpt-workspace` [PR #7](https://github.com/yjsnpi6324/gpt-workspace/pull/7) 已于 2026-10-22 合并至 `main`（merge commit `4ccc1dcdcacb81383840d0c583b43af605efce7b`）。变更仅限 `tests/supabase/no_default_grants.sql`：删除本地 Postgres 17 环境中导致 42501 的 `ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin` 测试夹具语句；未修改迁移或生产权限策略。
- [Supabase explicit grants run 38988076494](https://github.com/yjsnpi6324/gpt-workspace/actions/runs/38988076494) 在 PR head `49a5751bad529a8c94f2eeedea27db5744dc4715` 上成功：一次受限迁移重放（含测试默认权限撤销）以及一次完整本地 `supabase db reset --local --no-seed --yes`，两段均实际执行 `tests/supabase/explicit_grants.sql` 并返回成功。该成功发生于 2026-10-17 的 PR CI，在 2026-10-22 合并前。
- [runtime-contract run 38988076582](https://github.com/yjsnpi6324/gpt-workspace/actions/runs/38988076582) 的两项 job 均成功；PR head 的 Vercel status 为 success。此为工程测试证据，不替代生产运行或真实部署验收。
- 当前可判定 `LOCAL_SUPABASE_CI_VERIFIED`：上述本地 Postgres 17 测试夹具原阻断已解除；但不能从本地 CI 推断真实托管项目权限完全相同，也不能据此声明 `SUPABASE_VERIFIED`、`PERSISTENCE_READY` 或四核心扇出已经成功。
- 2026-10-22 连接器只读项目检查返回 `ACTIVE_HEALTHY`，`public` 下 8 张现有表均启用 RLS；这一检查仅证实项目/基础结构可见，不等于逐份报告和四节点内容回读。任何 hosted 权限漂移、真实写后回读、历史 Backfill、Agents 真实 adapter 仍按其各自门禁处理。
- 治理第三批中的「本地 CLI reset/replay/显式权限检查」单项 CI 门禁已有上述成功证据，可记录为已通过本地测试；第三批其他功能及真实生产推广不得因为这次合并自动转正。生产 Task 保留既有 Prompt V3.6、治理 Task 保留 V2.7、插件策略保留 `PLUGIN-POLICY-20261020-R2`，不修改任何 schedule、FINAL、Prediction、Native Hash 或 Champion。
