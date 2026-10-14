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
