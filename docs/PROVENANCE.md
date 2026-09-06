# Provenance

## Active canonical state

- Freeze ID: `SSDI-THEORY-FREEZE-2026-09-06-v3`
- Freeze date: 2026-09-06
- Freeze record: `docs/THEORY_FREEZE.md`
- Historical freezes: `docs/THEORY_FREEZE_v1.md`, `docs/THEORY_FREEZE_v2.md`
- Stage 7.5R authorization commit: `7c7f19094c0151f350e0b256152c34da6ba9f851`

## Workflow authority

- Repository: `ryotamatsuki/research-paper-workflow`
- Active version: `v1.3`
- Release commit: `3e4e6a3f76d86058024d06f9710f942e21627386`

Earlier workflow references remain historical provenance only.

## Stage 9R

- Starting remote `main`: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`
- Stage 9R branch: `stage9r-v13-reproducibility-sync`
- Stage 9R merge commit: `ba641614eb191928193f443d46d15d40af08b1d9`
- Verdict: `REPRODUCIBILITY BASELINE READY`

## Pre-Stage-10R JET/GEB architecture gate

- Active gate record: `docs/TOP_JOURNAL_FIT_GATE_JET_GEB_2026-09-06.md`
- Verdict: `KEEP SSDI v2 — NO JET/GEB THEORY ROLLBACK — PROCEED TO STAGE 10R`
- RAND was explicitly excluded from the active comparison.
- The gate remains historical positioning input; it does not override the later Stage-11-triggered P2R repair.

## Stage 10R

- Starting remote `main`: `b975e42e4cba97ee6aa2cb177efa34df3f1c85d0`
- Branch: `stage10r-v2-manuscript-sync`
- Merge commit: `2198864d1d762d1d84823ec9083536e12f1530d6`
- Manuscript title: *Standardization Scope and Endogenous Innovation Portfolios*
- Figure/Table Architecture record: `docs/FIGURE_TABLE_ARCHITECTURE_STAGE10R.md`
- Quantitative-output authority: `docs/EXPOSITION_OUTPUT_MANIFEST.json`
- Required quantitative outputs: one verified policy-regime figure; no quantitative tables.

Stage 10R synchronized the manuscript to the then-active v2 freeze and removed the earlier first-best, generic-C2, asymmetric-benchmark, and endogenous-total-R&D overclaims.

## Stage 11 hostile audit and Stage 7R2 rollback

The first Stage 11 hostile audit accepted the quadratic baseline, global price continuation, welfare formulas, Proposition 4 threshold theorem, Figure 1, and the core result-level novelty boundary. It identified one material theory-scope defect in P2R: v2 stated pointwise strict derivative signs at interior optima for arbitrary differentiable increasing strictly concave `g`, while the proof invoked `g''` without assuming twice differentiability.

Routing: `REOPEN STAGE 7R` for this defect only.

## Stage 7R2 exact-monotonicity repair

- Starting remote `main`: `2198864d1d762d1d84823ec9083536e12f1530d6`
- Branch: `stage7r2-p2r-exact-monotonicity-repair`
- Merge commit: `4d221158ed9d1b3375a8a5e970ea9e6f5cd2afcd`
- Repair record: `docs/STAGE_07R2_P2R_EXACT_MONOTONICITY_REPAIR.md`
- Active freeze after repair: `SSDI-THEORY-FREEZE-2026-09-06-v3`

The repair:

1. preserves all model primitives and quadratic formulas;
2. preserves P1, P3R, P4, and P5R unchanged;
3. replaces the general-technology derivative claim by global order comparative statics;
4. proves strict ordering across two policy values when both compared optima are interior;
5. uses no `g''` and adds no smoothness assumption;
6. preserves v2 as historical and creates active freeze v3;
7. synchronizes manuscript, exposition metadata, tests, and verification provenance;
8. incorporates bounded Stage-11 clarifications on the welfare decomposition, endogenous-total-R&D relative FOC, and closest-literature boundary.

## Stage 11R repeated hostile referee gate

- Starting remote `main`: `4d221158ed9d1b3375a8a5e970ea9e6f5cd2afcd`
- Branch: `stage11r-v3-hostile-referee-regate`
- Merge commit: `87108448ef5665bcc6d898911aa2179c7aa6a3bb`
- Audit record: `docs/STAGE_11R_V3_HOSTILE_REFEREE_REGATE.md`
- Independent continuation implementation: `scripts/stage11_independent_continuation_audit.py`
- Active theory remains v3; no new theory change is authorized.

The repeated gate independently re-audits novelty, assumptions, P2R, the quadratic policy theorem, welfare, benchmark interpretation, exposition, and the full pure-price continuation over off-path histories. The continuation audit reconstructs consumer KKT allocations directly, includes boundary R&D/scope histories and large finite price deviations, and fails closed on unresolved active sets.

Stage-11R classification:

- P2R v3 repair: `PASS`;
- P1/P3R/P4/P5R: `PASS`;
- welfare and no-first-best discipline: `PASS`;
- independent pure-price continuation: `PASS`;
- unresolved continuation count: `0`;
- result-level novelty: `DISTINCT BUT NARROW`;
- unresolved fatal attacks: `0`;
- unresolved major attacks: `0`;
- final verdict: `GO TO JOURNAL POSITIONING`.

Minor carry-forward items are limited to copy/positioning: clarify pure-strategy uniqueness wording, optionally mention `(R)` in the figure caption, and consider adjacent 2026 empirical standards/innovation evidence during journal-specific integration. None changes the frozen theory.

## Stage 12 journal positioning

- Starting remote `main`: `87108448ef5665bcc6d898911aa2179c7aa6a3bb`
- Branch: `stage12-journal-positioning`
- Positioning record: `docs/STAGE_12_JOURNAL_POSITIONING.md`
- Final verdict: `PRIMARY JOURNAL SELECTED — GO TO INTEGRATION`
- Primary target: `International Journal of Industrial Organization (IJIO)`
- Operational default ladder: `IJIO -> Review of Industrial Organization -> Journal of Industry, Competition and Trade`
- Optional stretch: `The Journal of Industrial Economics`
- RAND: excluded by explicit project instruction.

Current web evidence used at Stage 12 shows that IJIO explicitly covers theoretical and empirical industrial organization, technological change and regulation, and has recently published work on innovation incentives in technical standards and standard-setting/innovation. JIE is retained only as a higher-risk stretch because the surviving contribution is narrow and the exact policy theorem is quadratic-specific. RIO is the strongest fallback because recent issues continue to publish self-contained IO theory on innovation, spillovers, differentiation, and policy.

No theory change is authorized by Stage 12. Journal selection follows the surviving Stage-11 result set.

Authorized forward route after successful CI and merge:

`Stage 12 complete -> Stage 13 IJIO integration`.

Stage 13 may make claim-preserving journal-specific presentation, disclosure, figure-caption, literature, metadata, and cover-letter changes, but may not change the frozen theory without formal rollback.
