# Stage 9 — v4 Formal-Artifact Reproducibility Synchronization

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Latest-workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`, template `templates/STAGE_09_REPRODUCIBILITY_SETUP.md`.

Historical production workflow remains `v1.3@3e4e6a3f76d86058024d06f9710f942e21627386` for provenance; this Stage 9 is a latest-workflow compatibility synchronization and does not rewrite historical stages.

## 1. Work-start remote state

- Starting remote `main`: `4c923f9e8e236ea18added57dfefa401f8c406e3`.
- Open PRs at work start: none.
- Stage-9 branch: `stage9-v4-formal-reproducibility-sync`.
- Stage-8 record: `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`.
- Active freeze record: `docs/THEORY_FREEZE.md`.
- Historical v3 freeze: `docs/THEORY_FREEZE_v3.md`.

No historical branch or commit was reset or overwritten.

## 2. Stage objective

Synchronize the complete reproducibility chain to the certification-only v4 freeze and make the Stage-7.5A formal-verification layer a first-class reproducible artifact alongside the analytic manuscript, symbolic/numerical checks, independent equilibrium audits, regression tests, and deterministic exposition output.

This stage may change tooling, metadata, tests, CI and documentation only. It does not authorize a theory or manuscript-result change.

## 3. v3 -> v4 scientific-invariance check

The Stage-8 refreeze compared the pre-refreeze scientific baseline `3648ac2d4917986f1f09873a30bbd5948fceb8b3` with the Stage-8 merge `4c923f9e8e236ea18added57dfefa401f8c406e3`.

GitHub compare shows only seven changed paths/classes associated with certification/provenance:

- `README.md`;
- `docs/LATEST_WORKFLOW_COMPATIBILITY_MIGRATION.md`;
- `docs/PROVENANCE.md`;
- `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`;
- `docs/THEORY_FREEZE.md`;
- `docs/THEORY_FREEZE_v3.md`;
- `tests/test_stage9r_metadata.py`.

No `paper/`, `formal/`, core symbolic/numerical verifier, Stage-4A/Stage-11 independent evaluator, bibliography, threshold equation, or figure-generation source changed at the refreeze.

Scientific-invariance verdict:

`PASS — SCIENTIFIC SOURCE DELTA FROM v3 TO v4 = NONE`.

The Stage-9 metadata migration therefore does not manufacture a new numerical output. It rebinds the existing verified scientific object to the v4 certification lineage.

## 4. Repository structure

The reproducibility-relevant scaffold is:

```text
.github/workflows/
  verify.yml
  lean.yml
Makefile
requirements.txt
README.md

docs/
  THEORY_FREEZE.md
  THEORY_FREEZE_v1.md
  THEORY_FREEZE_v2.md
  THEORY_FREEZE_v3.md
  STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md
  STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md
  STAGE_08_CERTIFICATION_ONLY_REFREEZE.md
  STAGE_09_V4_FORMAL_REPRODUCIBILITY_SYNC.md
  REPRODUCIBILITY_MANIFEST.json
  EXPOSITION_OUTPUT_MANIFEST.json
  PROVENANCE.md
  LATEST_WORKFLOW_COMPATIBILITY_MIGRATION.md

paper/
  main.tex
  sections/
references/
  references.bib

formal/
  lean-toolchain
  lakefile.toml
  SSDI.lean
  SSDI/
    Core.lean
    Generality.lean
    Continuation.lean
    Threshold.lean
    PolicySigns.lean
    PolicyObjective.lean
    WelfareIdentities.lean
    Assurance.lean

theorem_certificates/
  STAGE4A_RETROACTIVE_CERTIFICATES.md
  STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md

scripts/
  symbolic_verify.py
  numerical_verify.py
  stage4a_independent_equilibrium_set_audit.py
  stage11_independent_continuation_audit.py
  generate_exposition_outputs.py
  stage14_package_qa.py

tests/
  test_freeze_regressions.py
  test_p2r_order_monotonicity.py
  test_stage9r_metadata.py

figures/
tables/
submission/
```

## 5. Build system

The root `Makefile` is now the canonical local-equivalent build interface.

Targets:

- `make symbolic` — SymPy/analytic identity checks;
- `make numerical` — numerical equilibrium/policy checks;
- `make stage4a` — permanent independent equilibrium-set/globality audit;
- `make continuation` — independent Stage-11 direct-KKT continuation audit;
- `make test` — pytest regression suite;
- `make verify` — symbolic + numerical + Stage 4A + continuation + regression tests;
- `make exposition` — deterministic policy-regime figure regeneration and metadata validation;
- `make paper` — complete LaTeX/BibTeX manuscript build;
- `make formal` — pinned Lean/mathlib dependency resolution, version/provenance output and `lake build`;
- `make formal-audit` — fail-closed `sorry` / `admit` / project-defined `axiom` scan;
- `make all` — complete Stage-9 local reproducibility gate: verification + exposition + manuscript + formal build + formal audit.

This removes the previous split in which Lean could only be reproduced through a separate workflow recipe.

## 6. Analytic/computational verification

The v4 reproducibility chain retains all previously certified evidence rather than replacing it with formal verification:

- `scripts/symbolic_verify.py` checks the quadratic closed forms, policy curvature/endpoints, threshold identities, price/profit identities and welfare-relevant algebra;
- `scripts/numerical_verify.py` checks the canonical policy example, private R&D global maximization and unilateral price deviations;
- `scripts/stage4a_independent_equilibrium_set_audit.py` performs the independent D1/D2/D3 equilibrium-set/globality audit and fails closed on unresolved KKT allocation states;
- `scripts/stage11_independent_continuation_audit.py` independently reconstructs price continuation over off-path histories;
- `tests/test_p2r_order_monotonicity.py` permanently retains the counterexamples/stress cases that killed the old pointwise general-`g` derivative formulation;
- `tests/test_stage9r_metadata.py` now fails if v4 metadata, theorem-certificate paths, formal pins, pure-strategy scope, or reproducibility-manifest traceability regress.

## 7. Formal verification reproducibility

Canonical certificate:

`theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

Formal state:

`FORMAL VERIFICATION PASS`.

Pinned environment:

- Lean `v4.32.1` via `formal/lean-toolchain`;
- mathlib exact commit `520045ab14e26149ee970e2e617ca04b09bde5d6` via `formal/lakefile.toml`.

The `formal/README.md` is synchronized to v4 and now points to the actual canonical certificate path. This repairs the pre-Stage-9 documentation defect in which it still named v3 as active and pointed to nonexistent `formal/FORMAL_VERIFICATION_CERTIFICATE.md`.

Formal scope remains exactly the Stage-7.5A certificate boundary: selected proof-critical core only. Full consumer KKT/SPNE formalization, mixed-strategy equilibrium uniqueness, and the complete P4 differentiation-to-argmax chain are not relabeled as machine certified.

## 8. Headline-claim traceability

`docs/REPRODUCIBILITY_MANIFEST.json` is the canonical machine-readable traceability map. For E0, P1, P2R, P3R, P4 and P5R/W1 it records:

1. manuscript source path(s);
2. Stage-4A theorem certificate;
3. Stage-7.5A quantifier/scope certification;
4. Lean artifact where applicable and exact formal boundary;
5. symbolic/numerical/counterexample regression artifact(s).

This preserves the distinction between analytic theorem maturity and bounded formal-proof coverage.

## 9. Figure/table pipeline

`docs/EXPOSITION_OUTPUT_MANIFEST.json` is now synchronized to active freeze v4 while explicitly recording inheritance from v3 and `scientific_source_delta = NONE`.

The only required quantitative visual remains:

`figures/policy_regime_map.pdf`.

Generator:

`scripts/generate_exposition_outputs.py`.

The generator validates v4 metadata, the inherited v3 scientific freeze, both workflow provenance layers, the no-scientific-change flag, and the same representative threshold values:

- `bar_nu(0.7) = 0.3587285925190902`;
- `bar_nu(0.9) = 0.4755546783510237`.

No quantitative table is required.

## 10. Environment/dependencies

Python-side CI uses Python 3.12 and `requirements.txt` (`sympy`, `pytest`, `numpy`, plus the repository's recorded plotting dependency if required by the file).

Manuscript/exposition CI installs TeX Live LaTeX base/recommended/extra, BibTeX-extra and Poppler tools.

Formal CI installs `elan`; the repository pins the Lean toolchain and mathlib revision internally.

No external data download is required for the economic verification, formal proofs, figure, or manuscript.

## 11. CI architecture

`.github/workflows/verify.yml` now installs all required Python/TeX/Lean host tooling and executes `make all`. It then retains the journal-package QA, unresolved-citation/reference kill test, PDF/font preflight and artifact upload.

`.github/workflows/lean.yml` remains a focused formal-verification workflow but now calls the same `make formal` and `make formal-audit` targets. It also triggers when the active freeze, formal certificate, reproducibility manifest or shared Makefile changes, preventing a stale formal-assurance path after metadata/certification changes.

Qualified Stage-9 run IDs and exact implementation commit will be recorded after the clean PR run completes.

## 12. Provenance locations

- active theory: `docs/THEORY_FREEZE.md`;
- Stage 4A: `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md` and `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`;
- Stage 7.5A/formal: `docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md` and `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`;
- Stage 8: `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`;
- current reproducibility map: `docs/REPRODUCIBILITY_MANIFEST.json`;
- quantitative outputs: `docs/EXPOSITION_OUTPUT_MANIFEST.json`;
- chronology: `docs/PROVENANCE.md` and `docs/LATEST_WORKFLOW_COMPATIBILITY_MIGRATION.md`.

## 13. Remaining blockers

At implementation time, the only remaining Stage-9 blocker is clean CI qualification of the exact synchronization head. If the full `make all` or focused formal workflow fails, Stage 9 remains open and the failure must be repaired without altering v4 theory.

## 14. Downstream contract

Because this is a retroactive synchronization of an already-written manuscript, a new Stage-10 manuscript-construction cycle is not required absent a content defect. The latest-workflow migration route after a successful Stage-9 baseline is:

`Stage 9 REPRODUCIBILITY BASELINE READY -> Stage 11 certification-regression recheck -> current Journal Requirements Ledger -> refreshed Stage 14 QA -> new Stage 15 submission freeze`.

Stage 11 must explicitly test whether any prior later-stage defect reveals a regression in the newly reconstructed Stage-4A/7.5A certification chain. It may not silently broaden the v4 claim scope.

## 15. Provisional verdict

`AWAITING CLEAN CI QUALIFICATION`.

Final Stage-9 verdict will be one of the canonical Stage-9 outcomes after the exact branch head is certified.
