# Standardization Scope and Endogenous Innovation Portfolios

Active canonical theory freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`

Canonical historical production workflow: `ryotamatsuki/research-paper-workflow` v1.3  
Workflow release commit: `3e4e6a3f76d86058024d06f9710f942e21627386`

A latest-workflow compatibility migration is now in progress against `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`. Retroactive Stage 4A has passed with verdict `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`; the record is `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`. This compatibility work does not rewrite the historical v1.3 provenance and does not change the v3 scientific theory freeze. Retroactive Stage 7.5A plus the Formal Verification Gate remains the next migration gate.

Stage 11 hostile audit previously reopened Stage 7R only for the general-technology P2R formulation. That defect was repaired and refrozen as v3 without changing the quadratic baseline or Proposition 4. The repeated Stage 11R hostile referee gate returned `GO TO JOURNAL POSITIONING`.

Stage 12 journal positioning selected **International Journal of Industrial Organization (IJIO)** as the primary target. Stage 13 IJIO full-paper integration returned `INTEGRATED MANUSCRIPT READY FOR SUBMISSION QA`. Stage 14 submission QA is complete under the historical workflow with verdict `SUBMISSION QA PASS`. The operational default ladder remains `IJIO -> Review of Industrial Organization -> Journal of Industry, Competition and Trade`, with The Journal of Industrial Economics retained as an optional higher-risk stretch rather than the default second submission. RAND remains excluded by project instruction.

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

## Retroactive Stage 4A certification

The latest-workflow compatibility record is `docs/LATEST_WORKFLOW_COMPATIBILITY_MIGRATION.md`.

Stage-4A artifacts:

- `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`;
- `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`;
- `scripts/stage4a_independent_equilibrium_set_audit.py`.

The audit separates candidate-deviation verification from alternative-equilibrium/multiplicity certification. Under `(R)`, it independently certifies the unique global pure-strategy price continuation, the unique quadratic R&D equilibrium, the P4 policy optimum, zero-demand/zero-profit indifference behavior, welfare identities, and the constrained benchmark taxonomy. Formalization is classified `FORMALIZATION APPLICABLE`; final proof-assistant statement-fidelity and model-boundary closure is intentionally deferred to retroactive Stage 7.5A as required by the current workflow.

## Stage 7R2 repair

The repaired general-technology result uses order comparative statics only. For `b2>b1`, private common-layer R&D is globally nonincreasing and coordinated symmetric common-layer R&D is globally nondecreasing. If both compared optima are interior, the corresponding order inequalities are strict. No pointwise derivative sign is claimed for arbitrary differentiable increasing strictly concave `g`, and no `g''` assumption is added.

The historical v2 freeze is preserved in `docs/THEORY_FREEZE_v2.md`. The Stage-7R2 repair record is `docs/STAGE_07R2_P2R_EXACT_MONOTONICITY_REPAIR.md`.

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

Integrated items include:

- IJIO-specific Introduction and literature emphasis;
- Figure 1 caption domain clarification (`conditional on (R)`);
- pure-strategy equilibrium wording correction;
- 2026 standards/innovation empirical citation;
- Elsevier-compliant generative-AI declaration and AI-assisted verification disclosure;
- data-availability statement;
- IJIO Highlights;
- cover letter;
- submission metadata;
- live fee/format check.

No theory change was authorized or introduced by Stage 13.

## Stage 14 IJIO submission QA

The QA record is `docs/STAGE_14_IJIO_SUBMISSION_QA.md`.

Historical-workflow verdict: `SUBMISSION QA PASS`.

The qualified package source commit is `c5c5f132a051a40339fc3a140c07f91e0920629e`. Clean CI verifies symbolic identities, numerical checks, continuation safety, regression tests, figure regeneration, LaTeX build, bibliography/cross-references, anonymous-manuscript separation, author title page, declarations, PDF font embedding, package completeness, and artifact generation.

Author metadata and declaration fields are synchronized to the author's prior successful journal submissions. The IJIO article type is fixed to the previously confirmed Editorial Manager label `Research Paper`. The public repository does not store the private street address.

The exact qualified CI artifact was visually inspected page by page. The manuscript is 16 pages; the title page and vector Figure 1 are clean and legible. Stage-14 cosmetic QA removed visible hyperlink boxes and an internal title-page note without changing theory or results.

A fresh Stage-14 pass under the latest workflow will be performed only after the retroactive Stage 7.5A/Formal Verification Gate, certification-only refreeze, and formal reproducibility synchronization are complete.

## Exposition architecture

Workflow v1.3 assigned every headline result a primary exposition vehicle. The only required quantitative visual remains `figures/policy_regime_map.pdf`, generated by `scripts/generate_exposition_outputs.py`. No quantitative table is required. The P2R repair does not alter this figure.

## Theory change control

The active theory is defined by `docs/THEORY_FREEZE.md`. Historical freezes v1 and v2 are preserved. Any subsequent substantive theory change requires a recorded rollback to every affected workflow stage.

Historical submission state remains preserved. Latest-workflow migration route:

`Retroactive Stage 4A PASS -> Retroactive Stage 7.5A + Formal Verification Gate -> certification-only Stage 8 refreeze -> Stage 9 formal sync -> Stage 11 regression recheck -> refreshed Stage 14/15 compliance`.
