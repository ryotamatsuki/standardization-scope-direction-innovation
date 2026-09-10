# Provenance

## Active canonical state

- Freeze ID: `SSDI-THEORY-FREEZE-2026-09-10-v4`
- Freeze date: 2026-09-10
- Freeze record: `docs/THEORY_FREEZE.md`
- Historical freezes: `docs/THEORY_FREEZE_v1.md`, `docs/THEORY_FREEZE_v2.md`, `docs/THEORY_FREEZE_v3.md`
- v4 classification: `CERTIFICATION-ONLY REFREEZE`
- Scientific baseline entering v4: `main@3648ac2d4917986f1f09873a30bbd5948fceb8b3`
- Scientific delta from v3: `NONE`

## Workflow authority

- Repository: `ryotamatsuki/research-paper-workflow`
- Active historical production version: `v1.3`
- Historical release commit: `3e4e6a3f76d86058024d06f9710f942e21627386`
- Latest-workflow compatibility authority: `f48984013898696f010f0437a8cfed6b5b54bdc2`

Earlier workflow references remain historical provenance only. Retroactive compatibility certifications do not rewrite the original stage chronology.

## Stage 9R

- Starting remote `main`: `26d28b84dc3e0649c6c9f40e4fd706e23c0694ed`
- Stage 9R branch: `stage9r-v13-reproducibility-sync`
- Stage 9R merge commit: `ba641614eb191928193f443d46d15d40af08b1d9`
- Verdict: `REPRODUCIBILITY BASELINE READY`

This is historical v1.3 provenance. Its reproducibility metadata predates v4 and will be explicitly synchronized by the next latest-workflow Stage 9 step rather than silently relabeled.

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

The exact v3 freeze is now preserved at `docs/THEORY_FREEZE_v3.md` after the certification-only v4 refreeze.

## Stage 11R repeated hostile referee gate

- Starting remote `main`: `4d221158ed9d1b3375a8a5e970ea9e6f5cd2afcd`
- Branch: `stage11r-v3-hostile-referee-regate`
- Merge commit: `87108448ef5665bcc6d898911aa2179c7aa6a3bb`
- Audit record: `docs/STAGE_11R_V3_HOSTILE_REFEREE_REGATE.md`
- Independent continuation implementation: `scripts/stage11_independent_continuation_audit.py`

The repeated gate independently re-audited novelty, assumptions, P2R, the quadratic policy theorem, welfare, benchmark interpretation, exposition, and the full pure-price continuation over off-path histories. The continuation audit reconstructs consumer KKT allocations directly, includes boundary R&D/scope histories and large finite price deviations, and fails closed on unresolved active sets.

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

## Stage 12 journal positioning

- Starting remote `main`: `87108448ef5665bcc6d898911aa2179c7aa6a3bb`
- Branch: `stage12-journal-positioning`
- Positioning record: `docs/STAGE_12_JOURNAL_POSITIONING.md`
- Final verdict: `PRIMARY JOURNAL SELECTED — GO TO INTEGRATION`
- Primary target: `International Journal of Industrial Organization (IJIO)`
- Operational default ladder: `IJIO -> Review of Industrial Organization -> Journal of Industry, Competition and Trade`
- Optional stretch: `The Journal of Industrial Economics`
- RAND: excluded by explicit project instruction.

No theory change was authorized by Stage 12.

## Stage 13 IJIO full-paper integration

- Starting remote `main`: `10109b3fa528b638a9d652e635cc10099ee1f8f5`
- Branch: `stage13-ijio-integration`
- Merge commit: `25a308c07277614a522164d0b52387b550c93a2e`
- Integration record: `docs/STAGE_13_IJIO_FULL_PAPER_INTEGRATION.md`
- Verdict: `INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA`

Stage 13 sharpened the Introduction and closest-literature boundary for IJIO, added the `(R)` scope qualification to Figure 1, restricted global price-equilibrium wording to pure strategies, integrated bounded standards/innovation evidence, added Elsevier-style AI/data declarations, and prepared Highlights, cover letter, and submission metadata. The theory freeze remained v3.

## Stage 14 IJIO submission QA

- Starting remote `main`: `25a308c07277614a522164d0b52387b550c93a2e`
- Branch: `stage14-submission-qa`
- QA record: `docs/STAGE_14_IJIO_SUBMISSION_QA.md`
- Qualified package source commit: `c5c5f132a051a40339fc3a140c07f91e0920629e`
- Qualified workflow run: `34029839013`
- Qualified artifact ID: `9988256374`
- Artifact ZIP SHA-256: `df90da9f8cf7e8a485702399f542eef2a232d703afcfe5acf7094377e3f47c64`
- Verdict: `SUBMISSION QA PASS`

This remains valid historical submission-QA provenance but is not the final latest-workflow submission certification after the v4 refreeze.

## Historical Stage 15 submission freeze

The historical IJIO submission freeze was completed before the latest-workflow compatibility migration and before formal verification became part of the canonical freeze chain. It remains preserved as historical evidence only. A refreshed Stage 14/15 pass will be required after Stage 9 formal synchronization and the latest certification-regression recheck.

## Retroactive latest-workflow Stage 4A certification

- Scientific baseline when migration opened: `main@9678decb82ea60a6706c9212505bdd73c9915c67`
- Stage-4A merge commit: `5d878738dccd2dbe08066eda5678b1845b2e8a1a`
- Record: `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`
- Theorem certificates: `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`
- Permanent independent audit: `scripts/stage4a_independent_equilibrium_set_audit.py`
- Verdict: `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`

The permanent evaluator records `parameter_sets=126`, `histories=2142`, `player_histories=4284`, and zero unresolved cases, profitable price deviations, alternative pure price equilibria, R&D-corner failures, policy-regime failures, and welfare failures.

## Retroactive latest-workflow Stage 7.5A + Formal Verification Gate

- Starting canonical main: `5d878738dccd2dbe08066eda5678b1845b2e8a1a`
- Branch: `retro-stage075a-formal-verification`
- Merge commit: `3648ac2d4917986f1f09873a30bbd5948fceb8b3`
- Stage record: `docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md`
- Formal certificate: `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`
- Certified Lean source commit: `5078719c57495c510405aa0cd33e621f3a7a2ab0`
- Dedicated clean Lean workflow run: `34469130983` — `success`
- PR-head Lean workflow run: `34471931934` — `success`
- Merged-main Lean workflow run: `34472224655` — `success`
- Merged-main normal verification/package run: `34472224636` — `success`
- Lean: `v4.32.1`
- mathlib exact commit: `520045ab14e26149ee970e2e617ca04b09bde5d6`
- Axiom/escape-hatch status: only `propext`, `Classical.choice`, `Quot.sound`; no project-specific axiom; `PROJECT_LEAN_ESCAPE_HATCH_AUDIT=PASS`
- Stage verdict: `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`
- Formal state: `FORMAL VERIFICATION PASS`

The formal gate certifies selected proof-critical cores rather than the entire economic game. Explicit exclusions include full KKT/SPNE formalization, mixed-strategy price-equilibrium uniqueness, and a complete machine-checked P4 differentiation/argmax chain.

## Latest-workflow Stage 8 certification-only refreeze

- Pre-refreeze canonical main: `3648ac2d4917986f1f09873a30bbd5948fceb8b3`
- Branch: `stage8-certification-only-refreeze`
- Stage record: `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`
- New active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`
- Historical inherited freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`, preserved at `docs/THEORY_FREEZE_v3.md`
- Scientific delta from v3: `NONE`
- Verdict: `THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`

The v4 freeze records all latest Stage-8 mandatory registers: exact proposition quantifiers, parameter/function-class restrictions, welfare/benchmark definitions, Stage-4A certificates, Stage-7.5A claim scope, formal-verification theorem mapping/model boundary/toolchain/axiom status, off-path continuation completeness, active-set/corner handling, solver/unresolved taxonomy, multiplicity/nonexistence scope, independent verification artifacts, and permanent counterexample/regression evidence.

Historical Stage-9/10 metadata remains attached to v3 until the explicit next Stage-9 synchronization; this prevents retroactive falsification of provenance.

Authorized latest-workflow compatibility route:

`Stage 8 v4 FROZEN -> Stage 9 formal-artifact reproducibility synchronization -> Stage 11 certification regression -> refreshed Stage 14/15 compliance`.

Any substantive manuscript/theory change requires rollback to the earliest affected stage. Any change to a formally certified theorem or encoded assumption makes the affected formal certificate stale until recertified.
