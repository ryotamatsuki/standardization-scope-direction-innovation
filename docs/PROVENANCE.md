# Provenance

## Active canonical state

- Freeze ID: `SSDI-THEORY-FREEZE-2026-09-10-v4`
- Freeze date: 2026-09-10
- Freeze record: `docs/THEORY_FREEZE.md`
- Historical freezes: `docs/THEORY_FREEZE_v1.md`, `docs/THEORY_FREEZE_v2.md`, `docs/THEORY_FREEZE_v3.md`
- v4 classification: `CERTIFICATION-ONLY REFREEZE`
- Scientific baseline entering v4: `main@3648ac2d4917986f1f09873a30bbd5948fceb8b3`
- Stage-8 merge activating v4: `4c923f9e8e236ea18added57dfefa401f8c406e3`
- Scientific delta from v3: `NONE`

## Workflow authority

- Repository: `ryotamatsuki/research-paper-workflow`
- Historical production version: `v1.3`
- Historical release commit: `3e4e6a3f76d86058024d06f9710f942e21627386`
- Latest-workflow compatibility authority: `f48984013898696f010f0437a8cfed6b5b54bdc2`

Historical workflow/stage records remain historical provenance. The latest-workflow migration certifies the unchanged current scientific object without rewriting the chronology under which earlier stages were produced.

## Historical Stage 9R / Stage 10R baseline

Historical Stage 9R:

- starting remote main: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`;
- branch: `stage9r-v13-reproducibility-sync`;
- merge: `ba641614eb191928193f443d46d15d40af08b1d9`;
- verdict: `REPRODUCIBILITY BASELINE READY`.

Historical Stage 10R:

- starting remote main: `b975e42e4cba97ee6aa2cb177efa34df3f1c85d0`;
- merge: `2198864d1d762d1d84823ec9083536e12f1530d6`;
- output architecture: `docs/FIGURE_TABLE_ARCHITECTURE_STAGE10R.md`;
- quantitative-output authority: `docs/EXPOSITION_OUTPUT_MANIFEST.json`.

The only required quantitative output remains the policy-regime map.

## Stage 7R2 P2R repair and historical Stage 11R

The first Stage-11 hostile audit identified one material scope defect in P2R: the then-current wording overclaimed pointwise derivative signs for arbitrary differentiable increasing strictly concave `g` while relying on second-derivative reasoning.

Stage 7R2:

- merge: `4d221158ed9d1b3375a8a5e970ea9e6f5cd2afcd`;
- record: `docs/STAGE_07R2_P2R_EXACT_MONOTONICITY_REPAIR.md`;
- repaired freeze: v3, now preserved at `docs/THEORY_FREEZE_v3.md`.

The repair replaced the general pointwise derivative claim with global order comparative statics and strict order only when both compared optima are interior. P1, P3R, P4 and P5R were unchanged.

Repeated historical Stage 11R:

- merge: `87108448ef5665bcc6d898911aa2179c7aa6a3bb`;
- record: `docs/STAGE_11R_V3_HOSTILE_REFEREE_REGATE.md`;
- independent continuation: `scripts/stage11_independent_continuation_audit.py`;
- unresolved fatal/major attacks: `0`;
- novelty: `DISTINCT BUT NARROW`;
- verdict: `GO TO JOURNAL POSITIONING`.

## Stage 12 / 13 / historical 14 / historical 15

Stage 12 selected the International Journal of Industrial Organization as the primary journal. Record: `docs/STAGE_12_JOURNAL_POSITIONING.md`.

Stage 13 IJIO integration merged at `25a308c07277614a522164d0b52387b550c93a2e`; record: `docs/STAGE_13_IJIO_FULL_PAPER_INTEGRATION.md`.

Historical Stage 14 QA:

- qualified source: `c5c5f132a051a40339fc3a140c07f91e0920629e`;
- workflow run: `34029839013`;
- artifact ID: `9988256374`;
- artifact ZIP SHA-256: `df90da9f8cf7e8a485702399f542eef2a232d703afcfe5acf7094377e3f47c64`;
- verdict: `SUBMISSION QA PASS` under the earlier production chain.

Historical Stage 15 submission freeze remains preserved as historical evidence only because it predates the latest certification/formal-verification migration. A new Stage 14/15 pass is required before submission under the current chain.

## Retroactive latest-workflow Stage 4A

- scientific baseline when migration opened: `main@9678decb82ea60a6706c9212505bdd73c9915c67`;
- merge: `5d878738dccd2dbe08066eda5678b1845b2e8a1a`;
- record: `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`;
- certificates: `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`;
- permanent independent audit: `scripts/stage4a_independent_equilibrium_set_audit.py`;
- verdict: `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`.

The permanent evaluator covers candidate deviations, alternative pure equilibria, and zero-payoff/indifference behavior as separate attacks.

## Retroactive latest-workflow Stage 7.5A + Formal Verification

- starting main: `5d878738dccd2dbe08066eda5678b1845b2e8a1a`;
- branch: `retro-stage075a-formal-verification`;
- merge: `3648ac2d4917986f1f09873a30bbd5948fceb8b3`;
- record: `docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md`;
- formal certificate: `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`;
- certified Lean source commit: `5078719c57495c510405aa0cd33e621f3a7a2ab0`;
- Lean: `v4.32.1`;
- mathlib: `520045ab14e26149ee970e2e617ca04b09bde5d6`;
- clean Lean run: `34469130983` — success;
- PR-head Lean run: `34471931934` — success;
- merged-main Lean run: `34472224655` — success;
- merged-main normal verification run: `34472224636` — success;
- proof escape-hatch audit: PASS;
- Stage 7.5A verdict: `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`;
- formal state: `FORMAL VERIFICATION PASS`.

The formal boundary is selected proof-critical core only. Full KKT/SPNE formalization, mixed-strategy price-equilibrium uniqueness and the complete P4 differentiation-to-argmax chain are explicitly outside Lean.

## Latest-workflow Stage 8 certification-only refreeze

- pre-refreeze main: `3648ac2d4917986f1f09873a30bbd5948fceb8b3`;
- branch: `stage8-certification-only-refreeze`;
- merge: `4c923f9e8e236ea18added57dfefa401f8c406e3`;
- record: `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`;
- active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`;
- inherited v3 freeze: `docs/THEORY_FREEZE_v3.md`;
- scientific delta: `NONE`;
- verdict: `THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`.

A compare from `3648ac2...` to `4c923f9...` changed only certification/provenance material; no scientific source changed.

## Latest-workflow Stage 9 formal-artifact reproducibility synchronization

- Stage-9 implementation branch: `stage9-v4-formal-reproducibility-sync`;
- PR: `#21`;
- Stage-9 merge commit: `707b9688dfb8afd4624f006795b91f5f2ef83b79`;
- final closeout merge: `857c828dadb1b2b3b5d4ee0bf74f1f8a5c936146`;
- synchronization record: `docs/STAGE_09_V4_FORMAL_REPRODUCIBILITY_SYNC.md`;
- final closeout: `docs/STAGE_09_FINAL_CLOSEOUT.md`;
- machine-readable map: `docs/REPRODUCIBILITY_MANIFEST.json`;
- active output manifest: `docs/EXPOSITION_OUTPUT_MANIFEST.json`;
- complete local-equivalent target: `make all`.

Stage 9 integrates formal verification into the ordinary repository reproducibility path. `make all` comprises analytic/computational verification, deterministic exposition generation, manuscript build, pinned Lean build, and formal proof-escape-hatch audit.

Post-merge qualification on the actual Stage-9 main object:

- full reproducibility run `34479910733`: `success`;
- focused formal run `34479910711`: `success`.

Stage-9 verdict: `REPRODUCIBILITY BASELINE READY`; Stage 9 is closed.

## Operational no-content incident before current Stage 11

During Stage-11 setup, a one-line temporary file `TEMP_NOT_USE` was accidentally created on main and immediately deleted. The resulting cleaned main commit was `67caf65aac91f0f5db1a7f445a86714e47266acd`. A compare against the Stage-9 closeout `857c828dadb1b2b3b5d4ee0bf74f1f8a5c936146` reported zero file differences. This is repository-history noise only; there is no content or scientific delta.

## Latest-workflow Stage 11 certification-regression recheck

- starting cleaned main: `67caf65aac91f0f5db1a7f445a86714e47266acd`;
- branch: `stage11-certification-regression-recheck`;
- PR: `#23`;
- qualified implementation head: `4b11aabb582e5d777c2553d16bb9f2f5ccfad6d4`;
- canonical record: `docs/STAGE_11_CERTIFICATION_REGRESSION_RECHECK.md`;
- certification-regression ledger: `docs/CERTIFICATION_REGRESSION_LEDGER.json`;
- P2R historical regression record: `docs/CERTIFICATION_REGRESSION_P2R.md`;
- permanent current regression suite: `tests/test_stage11_certification_regressions.py`.

Clean qualification run `34482554751`: `success`.

Re-executed evidence:

- symbolic verification: PASS;
- numerical verification: PASS; canonical `b*≈0.68775`;
- Stage-4A independent audit: 126 parameter sets, 2,142 histories, 4,284 player-history cases, unresolved `0`, profitable deviations `0`, alternative pure equilibria `0`, R&D-corner failures `0`, policy-regime failures `0`, welfare failures `0`;
- independent Stage-11 continuation audit: 73 histories, unresolved `0`, failures `0`;
- pytest: `22 passed`;
- exposition v4 synchronization: PASS;
- manuscript build: PASS;
- Lean v4.32.1 / pinned mathlib build: 8,664 jobs, success;
- project proof escape-hatch / project-axiom audit: PASS;
- title-page, unresolved citation/reference kill test, package QA and PDF/font preflight: PASS.

Certification-regression classifications:

1. `CR-01 CERTIFICATION REGRESSION` — historical P2R hidden-smoothness/general-quantifier inflation; current status `CLOSED_PERMANENTLY_GUARDED`.
2. `CR-02 CLAIM_SCOPE REGRESSION` — historical unqualified price-equilibrium uniqueness wording; current status `CLOSED_PERMANENTLY_GUARDED`; manuscript scope is pure-strategy only.
3. `CR-03 REPRODUCIBILITY PROVENANCE REGRESSION` — Appendix still called v3 the active freeze after Stage 9; repaired to active v4 and permanently guarded.

The current recheck found no new fatal or major scientific defect. The only new repair was CR-03, affecting Stage-9 provenance/exposition only. It changes no theorem or scientific result.

Fresh adjacent-literature recheck did not identify a result-level collision. Novelty remains `DISTINCT BUT NARROW`.

Unresolved fatal attacks: `0`. Unresolved major attacks: `0`. Unresolved material certification regressions: `0`.

Final Stage-11 verdict:

`GO TO JOURNAL POSITIONING`.

No theory rollback and no Stage-8 refreeze are required.

Because the completed Stage 12 already selected IJIO and the current Stage-11 recheck found no scientific or result-level novelty change requiring repositioning, the next latest-workflow compatibility step is the current Journal Requirements Ledger rather than a redundant Stage-12 rerun.

## Current route

`Stage 11 GO TO JOURNAL POSITIONING -> current Journal Requirements Ledger -> refreshed Stage 14 QA -> new Stage 15 submission freeze`.

Any substantive manuscript/theory change requires rollback to the earliest affected stage. Any material change to a formally certified theorem or encoded assumption makes the affected Formal Verification Certificate stale until recertified.
