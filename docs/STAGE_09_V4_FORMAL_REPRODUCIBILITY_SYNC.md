# Stage 9 — v4 Formal-Artifact Reproducibility Synchronization

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Latest-workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`, template `templates/STAGE_09_REPRODUCIBILITY_SETUP.md`.

Historical production workflow remains `v1.3@3e4e6a3f76d86058024d06f9710f942e21627386` for provenance. This Stage 9 is a latest-workflow synchronization and does not rewrite historical stages.

## 1. Work-start remote state

- Starting remote `main`: `4c923f9e8e236ea18added57dfefa401f8c406e3`.
- Open PRs at work start: none.
- Stage-9 branch: `stage9-v4-formal-reproducibility-sync`.
- Stage-8 record: `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`.
- Active freeze record: `docs/THEORY_FREEZE.md`.
- Historical v3 freeze: `docs/THEORY_FREEZE_v3.md`.

No concurrent PR was overwritten and no historical branch/commit was reset.

## 2. Objective and theory boundary

The objective is to make manuscript, theorem certificates, symbolic/numerical checks, independent equilibrium audits, counterexample regressions, deterministic exposition output, and Lean formal verification reproducible under the active v4 freeze.

Allowed changes were limited to tooling, metadata, tests, CI and documentation. No model primitive, theorem conclusion, policy threshold, welfare result, or contribution claim was changed.

## 3. v3 -> v4 scientific-invariance certification

Comparison baseline: `3648ac2d4917986f1f09873a30bbd5948fceb8b3`.

Stage-8 merge: `4c923f9e8e236ea18added57dfefa401f8c406e3`.

The Stage-8 compare changed only:

- `README.md`;
- `docs/LATEST_WORKFLOW_COMPATIBILITY_MIGRATION.md`;
- `docs/PROVENANCE.md`;
- `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`;
- `docs/THEORY_FREEZE.md`;
- `docs/THEORY_FREEZE_v3.md`;
- `tests/test_stage9r_metadata.py`.

No `paper/`, `formal/`, core symbolic/numerical verifier, independent equilibrium evaluator, bibliography, threshold equation, or figure-generation source changed in the certification-only refreeze.

Verdict:

`PASS — SCIENTIFIC SOURCE DELTA FROM v3 TO v4 = NONE`.

## 4. Repository / artifact scaffold

The reproducibility chain retains:

- `paper/` modular LaTeX manuscript;
- `references/references.bib`;
- `scripts/` symbolic, numerical, Stage-4A, continuation, exposition and package checks;
- `tests/` theorem-scope/counterexample/metadata regressions;
- `theorem_certificates/` Stage-4A and Stage-7.5A formal certificates;
- `formal/` Lean source, toolchain and library pin;
- `docs/REPRODUCIBILITY_MANIFEST.json` machine-readable traceability map;
- `docs/EXPOSITION_OUTPUT_MANIFEST.json` quantitative-output authority;
- `.github/workflows/verify.yml` and `.github/workflows/lean.yml` clean CI;
- root `Makefile` as the local-equivalent interface.

## 5. Canonical build system

The complete local-equivalent gate is now:

```text
make all
```

It expands to:

- `make verify` — symbolic + numerical + Stage-4A independent equilibrium-set audit + Stage-11 direct-KKT continuation audit + pytest;
- `make exposition` — deterministic policy-regime figure regeneration;
- `make paper` — LaTeX/BibTeX manuscript build;
- `make formal` — pinned Lean/mathlib resolution and `lake build`;
- `make formal-audit` — fail-closed `sorry` / `admit` / project-defined `axiom` audit.

The focused targets remain individually callable.

## 6. Verification and regression artifacts

Analytic/computational evidence retained:

- `scripts/symbolic_verify.py`;
- `scripts/numerical_verify.py`;
- `scripts/stage4a_independent_equilibrium_set_audit.py`;
- `scripts/stage11_independent_continuation_audit.py`;
- `tests/test_freeze_regressions.py`;
- `tests/test_p2r_order_monotonicity.py`;
- `tests/test_stage9r_metadata.py`.

The old P2R counterexample/stress tests remain permanent. No certification-supporting counterexample regression was dropped.

## 7. Formal verification reproducibility

Canonical certificate:

`theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

Formal state:

`FORMAL VERIFICATION PASS`.

Pinned environment:

- Lean `v4.32.1` via `formal/lean-toolchain`;
- mathlib exact commit `520045ab14e26149ee970e2e617ca04b09bde5d6` via `formal/lakefile.toml`.

`formal/README.md` is synchronized to active v4 and points to the actual canonical certificate. This Stage corrected a documentation defect in which it still named v3 and referred to nonexistent `formal/FORMAL_VERIFICATION_CERTIFICATE.md`.

The formal boundary remains unchanged: selected proof-critical core only. Full consumer KKT/SPNE formalization, mixed-strategy equilibrium uniqueness, and the complete P4 differentiation-to-argmax chain are not claimed as Lean-certified.

## 8. Headline-theorem traceability

`docs/REPRODUCIBILITY_MANIFEST.json` traces E0, P1, P2R, P3R, P4, and P5R/W1 through:

1. paper statement;
2. Stage-4A theorem/equilibrium certificate;
3. Stage-7.5A quantifier/scope decision;
4. Lean artifact where applicable;
5. symbolic/numerical/continuation/counterexample regression evidence.

Analytic proof maturity and formal-proof coverage remain separate fields; no bounded formal result is promoted to full-model formalization.

## 9. Figure/table pipeline

`docs/EXPOSITION_OUTPUT_MANIFEST.json` is synchronized to v4 while recording v3 scientific inheritance and `scientific_source_delta = NONE`.

The only required quantitative output remains `figures/policy_regime_map.pdf`, generated by `scripts/generate_exposition_outputs.py` from the unchanged P4 threshold polynomial.

Representative regenerated checks remain:

- `bar_nu(0.7) = 0.3587285925190902`;
- `bar_nu(0.9) = 0.4755546783510237`.

No quantitative table is required.

## 10. Environment

- Python: CI uses 3.12;
- Python dependencies: `requirements.txt` (`sympy`, `pytest`, `numpy`, `matplotlib` with bounded versions);
- manuscript: TeX Live LaTeX base/recommended/extra, BibTeX-extra;
- PDF preflight: Poppler utilities;
- formal layer: `elan`, with Lean/mathlib pinned inside `formal/`.

No external data download is required for the current economic verification, figure, formal proof or manuscript.

## 11. Clean CI qualification

Qualified implementation head:

`fd650e6a3a925e7ae0d24e8981bb38a357a33f09`.

PR: `#21`.

Full reproducibility workflow:

- run `34478441732`;
- conclusion: `success`;
- `make all`: PASS;
- title-page build: PASS;
- unresolved citation/reference kill test: PASS;
- Stage-14 package QA: PASS;
- PDF/font preflight: PASS;
- submission-artifact assembly: PASS.

Focused formal workflow:

- run `34478441787`;
- conclusion: `success`;
- pinned Lean build: PASS;
- project proof escape-hatch / axiom audit: PASS.

The final record/status commits after this qualified implementation are documentation/metadata closure only and are re-run through CI before merge.

## 12. Provenance locations

- active theory: `docs/THEORY_FREEZE.md`;
- Stage 4A: `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`, `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`;
- Stage 7.5A/formal: `docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md`, `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`;
- Stage 8: `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`;
- Stage 9: this record and `docs/REPRODUCIBILITY_MANIFEST.json`;
- quantitative output: `docs/EXPOSITION_OUTPUT_MANIFEST.json`;
- chronology: `docs/PROVENANCE.md`, `docs/LATEST_WORKFLOW_COMPATIBILITY_MIGRATION.md`.

## 13. Remaining blockers

None at the Stage-9 reproducibility-infrastructure level.

There is no need to reopen Stage 10 manuscript construction merely because this was a retroactive reproducibility migration. Any later substantive defect still routes to the earliest affected analytic stage.

## 14. Exact downstream contract

The existing manuscript may be carried forward only against:

- active freeze v4;
- Stage-7.5A maximum defensible claim wording;
- Stage-4A pure-strategy/globality certificates;
- explicit formal-verification model boundary;
- reproducibility manifest and permanent regression suite.

The next required gate is a **Stage 11 certification-regression recheck**, specifically checking whether defects historically found downstream reveal a missing regression/certification obligation in the reconstructed Stage-4A/7.5A chain.

After that:

`current Journal Requirements Ledger -> refreshed Stage 14 QA -> new Stage 15 submission freeze`.

## 15. Final verdict

`REPRODUCIBILITY BASELINE READY`.
