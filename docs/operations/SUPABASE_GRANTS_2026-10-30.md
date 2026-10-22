# Supabase explicit-grant audit — 2026-10-03

The 2026-10-30 change affects newly created public tables, including historical
migrations replayed into a fresh preview branch or reset database. Existing tables
retain their grants. The [Supabase announcement](https://github.com/orgs/supabase/discussions/45329)
confirms the deadline and the distinction between GRANTs and RLS.

## Findings

Neither this repository nor `gpt-workspace` contained SQL migration files on any
fetched branch. The connected project `maxbwlhkgxnniclontig` has five applied
migrations, with two table-creation entries that have no explicit GRANTs:

| Historical migration | Affected public tables |
| --- | --- |
| 20260903132922_initialize_ai_agent_data_hub_v1 | tasks, prompt_versions, task_runs, task_results, memories, artifacts |
| 20260903133213_add_integration_node_topology | integration_nodes, integration_events |

All eight online tables have legacy CRUD/extra grants for anon, authenticated and
service_role, RLS enabled, and no client policies. All three roles have public
schema USAGE. There are no public sequences. The source explicitly keeps these
tables private until an authenticated application/API layer is configured.

The source also relies on the hosted ensure_rls event trigger. Its direct revoke
of `rls_auto_enable()` fails if the hosted helper is absent in a fresh database.

## Repair and ownership

The [runtime repository](https://github.com/yjsnpi6324/gpt-workspace) owns the
migration files, consistent with `docs/REPOSITORY_MAP.md`. Its independent branch
`fix/supabase-explicit-grants-20261030` ([PR #6](https://github.com/yjsnpi6324/gpt-workspace/pull/6)) recovers the five existing migration
versions; only the two table-creation sources change. In each creation migration:

- RLS is enabled explicitly on each created table.
- PUBLIC, anon, authenticated and service_role table privileges are cleared,
  followed by SELECT, INSERT, UPDATE, DELETE for service_role only.
- No client policy is added. Client access remains closed.
- The pre-existing helper-function revoke runs only when the helper exists.

The existing production ACLs and online migration history are unchanged.
Already-applied versions will be skipped; these amendments fix new/replayed
databases. No migration-history repair, production reset or automatic-grant
workaround is needed. Existing preview databases also need deliberate replay or
a forward patch; editing an applied historical file alone does not update them.

## Validation and limits

Read-only live metadata queries confirmed eight tables, RLS on all eight, no
policies/sequences and five applied migration versions. Security advisors reported
eight informational RLS-without-policy notices, matching the private backend intent
([advisor explanation](https://supabase.com/docs/guides/database/database-linter?lint=0008_rls_enabled_no_policy)).
The project returned no preview branches, so there was no hosted branch to test.

Eight isolated Postgres scenarios passed, including missing-GRANT negative
controls, fresh preview-equivalent replay, legacy defaults, missing/present hosted
helper, client denials, backend DML and two public-schema rebuilds. The fallback
engine was PGlite/Postgres 18.3 with pgvector; this is not a hosted-preview or
Supabase CLI reset result. A dedicated runtime-repository workflow performs actual
Supabase CLI 2.119.0/Postgres 17 reset checks.

Detailed permission differences, source fingerprints and executable SQL checks
live in `gpt-workspace/docs/SUPABASE_MIGRATIONS.md`. Runtime test evidence is kept
there; this research repository holds the audit and ownership reference.

## Final-notice recheck — 2026-10-22

The final reminder received on 2026-10-20 explicitly includes new projects,
preview branches and `supabase db reset`. Rechecked research main
`7f4d1c3715f60eaa42ac34f303220178a8647512` and runtime main
`4ccc1dcdcacb81383840d0c583b43af605efce7b` against the live project.

- Research main and all seven other fetched branches contain no migration SQL.
  The runtime repository remains the migration owner; no duplicate SQL is needed.
- All five runtime migrations were read back. The two creation files listed above
  explicitly enable RLS, revoke PUBLIC/client/backend table privileges, and grant
  only service-role CRUD in the same migration. The other three create no tables.
  The hosted-helper revoke is conditional. No missing table grant was found in
  the current runtime main sources.
- [Runtime PR #6](https://github.com/yjsnpi6324/gpt-workspace/pull/6) was merged on
  October 14. [PR #7](https://github.com/yjsnpi6324/gpt-workspace/pull/7), merged on
  October 22, fixes the disposable fixture's 42501 error by revoking defaults only
  for its actual creator, `postgres`, rather than `supabase_admin`.
- [Main CI run 39709770838](https://github.com/yjsnpi6324/gpt-workspace/actions/runs/39709770838),
  at the runtime main SHA above, completed successfully on October 22 at 10:11
  Beijing time. Both "Replay with automatic grants removed" and "Full db reset
  and repeat permission checks" passed with CLI 2.119.0/Postgres 17. The checked
  SQL asserts 192 role/privilege combinations, RLS, schema USAGE, UUID/FK behavior,
  service-role DML, 16 client SELECT denials and RLS after temporary SELECT grants.

| Role | Existing production (read-only recheck) | Fresh/replayed database |
| --- | --- | --- |
| anon / authenticated | Legacy CRUD plus extra ACLs; RLS enabled, no policies | All table privileges explicitly revoked; no client policies |
| service_role | Legacy CRUD plus extra ACLs; BYPASSRLS | Explicit SELECT, INSERT, UPDATE, DELETE only |

Live metadata still shows exactly eight public tables, five applied historical
versions, zero policies and zero public sequences; all three roles have schema
USAGE. Historical online statement text still lacks GRANTs in the two creation
versions. That is retained history, not the source used for fresh replay; no
history repair or production reapplication was performed. Security advisors
returned only the eight informational RLS-without-policy notices described above.

The live project again returned no hosted preview branches. Fresh replay and
local full reset are verified by the main CI run; hosted preview remains untested.
Any existing preview with applied versions would need recreation from repaired
main sources or a separately reviewed forward patch. This recheck changes only
this audit document; live schema, ACLs, data and migration history are unchanged.
