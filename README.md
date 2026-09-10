# Standardization Scope and Endogenous Innovation Portfolios

Active canonical theory freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Canonical freeze record: `docs/THEORY_FREEZE.md`  
Historical v3 freeze: `docs/THEORY_FREEZE_v3.md`

Historical production workflow: `ryotamatsuki/research-paper-workflow` v1.3 at `3e4e6a3f76d86058024d06f9710f942e21627386`.

Latest-workflow compatibility authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`.

Latest compatibility gates closed:

- Stage 4A: `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`;
- Stage 7.5A: `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`;
- Formal Verification Gate: `FORMAL VERIFICATION PASS`;
- Stage 8: `THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`;
- Stage 9: `REPRODUCIBILITY BASELINE READY`;
- Stage 11 certification-regression recheck: `GO TO JOURNAL POSITIONING`;
- unresolved fatal/major Stage-11 attacks: `0 / 0`;
- active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`.

The v4 refreeze is certification-only. Scientific delta from v3 is `NONE`: no model primitive, proposition conclusion, threshold, welfare result, or contribution claim changed.

Canonical Stage-9 closeout: `docs/STAGE_09_FINAL_CLOSEOUT.md`.  
Canonical Stage-11 recheck: `docs/STAGE_11_CERTIFICATION_REGRESSION_RECHECK.md`.  
Certification-regression ledger: `docs/CERTIFICATION_REGRESSION_LEDGER.json`.  
Machine-readable reproducibility map: `docs/REPRODUCIBILITY_MANIFEST.json`.

Stage-11 qualified head: `4b11aabb582e5d777c2553d16bb9f2f5ccfad6d4`.  
Clean Stage-11 run: `34482554751` — success.

## Reproducibility

Install the Python packages in `requirements.txt`, a TeX Live environment with `pdflatex`/BibTeX, and `elan`. Then run the complete local-equivalent gate:

```bash
make all
```

`make all` runs:

- `make verify`: symbolic identities, numerical checks, retroactive Stage-4A independent equilibrium-set/globality audit, independent Stage-11 continuation audit, and pytest regressions;
- `make exposition`: deterministic regeneration and validation of `figures/policy_regime_map.pdf`;
- `make paper`: modular LaTeX/BibTeX manuscript build;
- `make formal`: pinned Lean/mathlib dependency resolution and `lake build`;
- `make formal-audit`: fail-closed scan for `sorry`, `admit`, or project-defined `axiom` declarations.

The full GitHub Actions workflow `.github/workflows/verify.yml` executes the same `make all` gate and retains IJIO package QA and PDF/font preflight. The focused `.github/workflows/lean.yml` executes `make formal` and `make formal-audit`.

## Formal verification

Formal source lives under `formal/`.

Pinned environment:

- Lean 4 `v4.32.1` via `formal/lean-toolchain`;
- mathlib exact commit `520045ab14e26149ee970e2e617ca04b09bde5d6` via `formal/lakefile.toml`.

Canonical certificate: `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

The formal layer covers selected proof-critical cores for P1, P2R, P4, the `(R)` price-continuation inequalities, and exact welfare identities. It does **not** claim to formalize the complete consumer KKT correspondence, full SPNE, mixed-strategy price-equilibrium uniqueness, the complete P4 calculus-to-argmax chain, or an unrestricted first-best problem.

## Stage 11 certification regressions

The latest Stage-11 recheck explicitly records three regression classes.

1. Historical P2R generality inflation: the old pointwise optimizer-derivative formulation exceeded the stated differentiable strictly concave function class. Current v4 uses global order comparative statics; strict order is limited to compared interior optima. Corner and differentiable non-`C^2` counterexamples are permanent tests, and `formal/SSDI/Generality.lean` certifies the bounded-domain order core.
2. Historical price-equilibrium wording inflation: the certified uniqueness statement is pure-strategy only. Mixed-strategy uniqueness is not claimed.
3. Stage-9 provenance regression found in the recheck: Appendix verification prose still called v3 active. It has been corrected to active v4 while preserving v3 as the unchanged scientific predecessor.

All three are `CLOSED_PERMANENTLY_GUARDED`; unresolved material certification regressions = `0`.

Clean Stage-11 evidence includes:

- Stage-4A independent audit: 126 parameter sets, 2,142 histories, 4,284 player-history cases; unresolved `0`, profitable deviations `0`, alternative pure equilibria `0`;
- independent continuation audit: 73 histories, unresolved `0`, failures `0`;
- pytest: `22 passed`;
- Lean: 8,664 jobs, success; escape-hatch audit PASS;
- exposition, manuscript, title page, citation/reference kill test, package QA and PDF preflight: PASS.

## Claim traceability

`docs/REPRODUCIBILITY_MANIFEST.json` traces E0/P1/P2R/P3R/P4/P5R-W1 from manuscript source through Stage-4A certification, Stage-7.5A claim scope, bounded Lean formalization, and symbolic/numerical/continuation/counterexample evidence.

The repaired theory scope remains:

- P2R: globally nonincreasing private and globally nondecreasing coordinated common-R&D for differentiable increasing strictly concave `g` on `[0,E]`; strict only when both compared optima are interior; no general pointwise optimizer derivative claim;
- P4: exact selective-standardization threshold is quadratic-specific;
- downstream price uniqueness: global pure-strategy continuation under `(R)` only;
- coordinated symmetric-R&D benchmark: constrained benchmark with decentralized Bertrand pricing, not unrestricted first best.

## Journal positioning and current route

Historical Stage 12 selected the **International Journal of Industrial Organization (IJIO)** as the primary target. The default ladder remains:

`IJIO -> Review of Industrial Organization -> Journal of Industry, Competition and Trade`

with *The Journal of Industrial Economics* as an optional higher-risk stretch. RAND remains excluded by project instruction.

The Stage-11 recheck found no scientific or result-level novelty change requiring Stage 12 to be rerun. The next latest-workflow compatibility step is:

`current Journal Requirements Ledger -> refreshed Stage 14 QA -> new Stage 15 submission freeze`.

Historical Stage 13, Stage 14 and Stage 15 records remain preserved as historical provenance and do not substitute for the refreshed current-chain submission certification.

## Theory change control

Any substantive change to the model, theorem statements, quantifiers, equilibrium concept, benchmark, condition `(R)`, or policy objective must roll back to the earliest affected analytic stage. Any material change to a formally certified theorem or encoded hypothesis also makes the affected Formal Verification Certificate stale until Stage-7.5A formal recertification is completed.
