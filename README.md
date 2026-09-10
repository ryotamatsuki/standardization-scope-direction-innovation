# Standardization Scope and Endogenous Innovation Portfolios

Active canonical theory freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Canonical freeze record: `docs/THEORY_FREEZE.md`  
Historical v3 freeze: `docs/THEORY_FREEZE_v3.md`

Canonical historical production workflow: `ryotamatsuki/research-paper-workflow` v1.3  
Historical workflow release commit: `3e4e6a3f76d86058024d06f9710f942e21627386`

Latest-workflow compatibility authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`.

Retroactive Stage 4A is closed with `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`. Retroactive Stage 7.5A is closed with `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`, and the embedded Formal Verification Gate is closed with `FORMAL VERIFICATION PASS`. Stage 8 has therefore been re-frozen on a certification-only basis as v4. The v4 scientific object is unchanged from v3; the refreeze records the latest-workflow certification inheritance and formal-proof boundary.

The Stage-8 record is `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`. The next compatibility step is Stage 9 formal-artifact reproducibility synchronization.

Stage 11 hostile audit previously reopened Stage 7R only for the general-technology P2R formulation. That defect was repaired and refrozen as v3 without changing the quadratic baseline or Proposition 4. The repeated Stage 11R hostile referee gate returned `GO TO JOURNAL POSITIONING`.

Stage 12 journal positioning selected **International Journal of Industrial Organization (IJIO)** as the primary target. Stage 13 IJIO full-paper integration returned `INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA`. Stage 14 submission QA and the historical Stage 15 submission freeze remain valid historical records under the old production chain, but a refreshed latest-workflow Stage 14/15 pass will occur only after Stage 9 formal synchronization and the certification-regression recheck.

The operational default journal ladder remains `IJIO -> Review of Industrial Organization -> Journal of Industry, Competition and Trade`, with The Journal of Industrial Economics retained as an optional higher-risk stretch. RAND remains excluded by project instruction.

## Reproducibility

Install Python dependencies and run:

```bash
make verify
make exposition
make paper
```

Or run the complete local-equivalent gate:

```bash
make all
```

- `make verify` runs symbolic identities, numerical checks, the retroactive Stage-4A independent equilibrium-set/globality audit, the independent Stage-11 continuation audit, and pytest regression tests.
- `make stage4a` runs the permanent latest-workflow Stage-4A regression audit directly.
- `make exposition` regenerates and validates the policy-regime figure from the unchanged quadratic threshold equation.
- `make paper` depends on `make exposition` and builds `paper/main.pdf` from the modular LaTeX source and bibliography.
- CI additionally runs Stage-14 submission-package QA, PDF/font preflight, title-page build, unresolved-reference kill tests, and submission-artifact assembly.

The formal proof layer is under `formal/`. The pinned environment is Lean 4 `v4.32.1` with mathlib commit `520045ab14e26149ee970e2e617ca04b09bde5d6`. The dedicated workflow `.github/workflows/lean.yml` performs a clean `lake build`, prints axioms for selected certified targets, and fails on project `sorry`, `admit`, or project-defined `axiom` declarations.

## Retroactive Stage 4A certification

The latest-workflow compatibility record is `docs/LATEST_WORKFLOW_COMPATIBILITY_MIGRATION.md`.

Stage-4A artifacts:

- `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`;
- `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`;
- `scripts/stage4a_independent_equilibrium_set_audit.py`.

The audit separates candidate-deviation verification from alternative-equilibrium/multiplicity certification. Under `(R)`, it independently certifies the unique global pure-strategy price continuation, the unique quadratic R&D equilibrium, the P4 policy optimum, zero-demand/zero-profit indifference behavior, welfare identities, and the constrained benchmark taxonomy.

## Retroactive Stage 7.5A + Formal Verification Gate

Canonical Stage-7.5A record:

`docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md`.

Formal certificate:

`theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

Final states:

- `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`;
- `FORMAL VERIFICATION PASS`.

The formal layer covers selected proof-critical cores for P1, P2R, P4, the `(R)` continuation inequalities, and exact welfare identities. It does not claim to formalize the complete consumer KKT correspondence, full SPNE, mixed-strategy price-equilibrium uniqueness, the entire P4 calculus-to-argmax chain, or an unrestricted first-best problem.

Clean evidence includes Lean run `34469130983`, PR-head run `34471931934`, and merged-main run `34472224655`, all successful. The project contains no certified `sorry`, `admit`, or project-specific axiom; the selected theorem dependency reports contain only standard Lean/mathlib foundations.

## Stage 8 certification-only refreeze

Canonical record:

`docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`.

Active freeze:

`SSDI-THEORY-FREEZE-2026-09-10-v4`.

Scientific delta from v3: `NONE`.

The exact v3 freeze is preserved at `docs/THEORY_FREEZE_v3.md`. v4 records the current Stage-4A theorem-certificate register, Stage-7.5A claim-scope register, formal theorem mapping/model boundary, continuation completeness, solver/unresolved ledger, benchmark definitions, counterexample regressions, and current theory-change-control rules required by the latest Stage-8 template.

Historical Stage-9/10 reproducibility metadata is intentionally not relabeled retroactively. Stage 9 must explicitly synchronize those artifacts to v4 and record that the quantitative scientific outputs remain unchanged.

## Stage 7R2 repair

The repaired general-technology result uses order comparative statics only. For `b2>b1`, private common-layer R&D is globally nonincreasing and coordinated symmetric common-layer R&D is globally nondecreasing. If both compared optima are interior, the corresponding order inequalities are strict. No pointwise derivative sign is claimed for arbitrary differentiable increasing strictly concave `g`, and no `g''` assumption is added.

The historical v2 and v3 freezes are preserved in `docs/THEORY_FREEZE_v2.md` and `docs/THEORY_FREEZE_v3.md`. The Stage-7R2 repair record is `docs/STAGE_07R2_P2R_EXACT_MONOTONICITY_REPAIR.md`.

## Stage 11R referee re-gate

The repeated full-manuscript hostile audit is recorded in `docs/STAGE_11R_V3_HOSTILE_REFEREE_REGATE.md`.

Key result:

- no unresolved fatal attack;
- no unresolved major attack;
- P2R v3 repair independently survives;
- P1, P3R, P4, and P5R remain intact;
- welfare formulas and constrained-benchmark interpretation pass;
- independent off-path price-continuation audit passes with zero unresolved histories and zero profitable finite deviations;
- result-level novelty is classified `DISTINCT BUT NARROW`;
- final Stage-11R verdict: `GO TO JOURNAL POSITIONING`.

The independent continuation implementation is `scripts/stage11_independent_continuation_audit.py` and is part of `make verify`.

## Stage 12 journal positioning

The positioning record is `docs/STAGE_12_JOURNAL_POSITIONING.md`.

Verdict: `PRIMARY JOURNAL SELECTED — GO TO INTEGRATION`.

Primary target: **International Journal of Industrial Organization**.

## Stage 13 IJIO integration

The integration record is `docs/STAGE_13_IJIO_FULL_PAPER_INTEGRATION.md`.

Verdict: `INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA`.

Integrated items include IJIO-specific Introduction/literature emphasis, Figure 1 `(R)` qualification, pure-strategy equilibrium wording, standards/innovation evidence, Elsevier-style AI/data declarations, Highlights, cover letter, and submission metadata. No theory change was authorized or introduced by Stage 13.

## Stage 14 IJIO submission QA

The historical QA record is `docs/STAGE_14_IJIO_SUBMISSION_QA.md` with verdict `SUBMISSION QA PASS` under the earlier production chain.

The qualified package source commit was `c5c5f132a051a40339fc3a140c07f91e0920629e`. That package passed symbolic/numerical verification, continuation safety, regression tests, figure regeneration, LaTeX build, bibliography/cross-reference checks, anonymous-manuscript separation, title-page/declarations checks, PDF font preflight, package completeness, and visual inspection.

A fresh Stage-14 pass under the latest workflow will be performed only after Stage 9 formal-artifact reproducibility synchronization and the latest-workflow certification-regression recheck.

## Exposition architecture

The only required quantitative visual remains `figures/policy_regime_map.pdf`, generated by `scripts/generate_exposition_outputs.py`. The P2R repair and certification-only v4 refreeze do not alter Proposition 4, the threshold equation, or the figure. Stage 9 will migrate the active reproducibility metadata to v4 while preserving this scientific identity.

## Theory change control

The active theory is defined by `docs/THEORY_FREEZE.md`. Historical freezes v1, v2, and v3 are preserved. Any subsequent substantive theory change requires a recorded rollback to every affected workflow stage; changes touching formalized theorem statements or encoded assumptions also stale the Formal Verification Certificate until recertified.

Latest-workflow migration route:

`Stage 4A PASS -> Stage 7.5A PASS + FORMAL VERIFICATION PASS -> Stage 8 v4 FROZEN -> Stage 9 formal sync -> Stage 11 certification regression -> refreshed Stage 14/15 compliance`.
