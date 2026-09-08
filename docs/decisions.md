# Decisions

Why each choice was made. Add an entry when the decision is taken, not later.

## 2026-09-08 — Repository created from project-template

Started from `opticient/project-template` rather than from scratch, so the lint,
type, hook, CI and branch rules are identical to every other project.

Ports 5434 and 6381 for Postgres and Redis, avoiding the work stack on 5440/6379
and the personal shared stack on 5433/6380.

No dataset or model chosen yet. The scaffold is deliberately empty so the
workflow can be verified before any logic exists.
