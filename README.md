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
- active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`.

The v4 refreeze is certification-only. Scientific delta from v3 is `NONE`: no model primitive, proposition conclusion, threshold, welfare result, or contribution claim changed.

Canonical Stage-9 synchronization record: `docs/STAGE_09_V4_FORMAL_REPRODUCIBILITY_SYNC.md`.  
Machine-readable reproducibility map: `docs/REPRODUCIBILITY_MANIFEST.json`.

Qualified Stage-9 implementation head: `fd650e6a3a925e7ae0d24e8981bb38a357a33f09`.  
Clean full reproducibility run: `34478441732` — success.  
Clean focused formal run: `34478441787` — success.

## Reproducibility

Install the Python packages in `requirements.txt`, a TeX Live environment with `pdflatex`/BibTeX, and `elan`. Then run the complete local-equivalent gate:

```bash
make all
```

`make all` is the canonical Stage-9 reproducibility command. It runs:

- `make verify`: symbolic identities, numerical checks, the retroactive Stage-4A independent equilibrium-set/globality audit, the independent Stage-11 continuation audit, and pytest regressions;
- `make exposition`: deterministic regeneration and validation of `figures/policy_regime_map.pdf`;
- `make paper`: modular LaTeX/BibTeX manuscript build;
- `make formal`: pinned Lean/mathlib dependency resolution and `lake build`;
- `make formal-audit`: fail-closed scan for `sorry`, `admit`, or project-defined `axiom` declarations.

Individual targets remain available:

```bash
make verify
make exposition
make paper
make formal
make formal-audit
```

The full GitHub Actions workflow `.github/workflows/verify.yml` installs the required Python/TeX/Lean host tooling and executes the same `make all` gate before retaining the IJIO package QA and PDF/font preflight. The focused `.github/workflows/lean.yml` executes the same `make formal` and `make formal-audit` targets.

## Formal verification

Formal source lives under `formal/`.

Pinned environment:

- Lean 4 `v4.32.1` via `formal/lean-toolchain`;
- mathlib exact commit `520045ab14e26149ee970e2e617ca04b09bde5d6` via `formal/lakefile.toml`.

Canonical certificate:

`theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

The formal layer covers selected proof-critical cores for P1, P2R, P4, the `(R)` price-continuation inequalities, and exact welfare identities. It does **not** claim to formalize the complete consumer KKT correspondence, full SPNE, mixed-strategy price-equilibrium uniqueness, the complete P4 calculus-to-argmax chain, or an unrestricted first-best problem.

`formal/README.md` documents the exact formal target map and model boundary.

## Claim traceability

`docs/REPRODUCIBILITY_MANIFEST.json` traces each headline result E0/P1/P2R/P3R/P4/P5R-W1 from:

1. manuscript source;
2. Stage-4A theorem/equilibrium certificate;
3. Stage-7.5A quantifier/scope decision;
4. Lean artifact where applicable;
5. symbolic, numerical, continuation, or counterexample regression evidence.

This keeps analytic proof maturity separate from bounded formal-proof coverage.

## v3 -> v4 scientific-output invariance

The Stage-8 refreeze changed certification/provenance material only. Comparing pre-refreeze main `3648ac2d4917986f1f09873a30bbd5948fceb8b3` with Stage-8 merge `4c923f9e8e236ea18added57dfefa401f8c406e3` shows no change to `paper/`, `formal/`, the core model verification scripts, bibliography, threshold equation, or figure-generation source.

Stage 9 synchronizes active reproducibility metadata to v4 without changing the scientific output. `docs/EXPOSITION_OUTPUT_MANIFEST.json` explicitly records inheritance from v3 and `scientific_source_delta = NONE`.

The policy-regime figure remains generated from the same quadratic threshold equation and retains the representative values:

- `bar_nu(0.7) = 0.3587285925190902`;
- `bar_nu(0.9) = 0.4755546783510237`.

## Certification records

Stage 4A:

- `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`;
- `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`;
- `scripts/stage4a_independent_equilibrium_set_audit.py`.

Stage 7.5A + Formal Verification:

- `docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md`;
- `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`;
- `formal/`.

Stage 8 certification-only refreeze:

- `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`;
- active `docs/THEORY_FREEZE.md`;
- historical `docs/THEORY_FREEZE_v3.md`.

Stage 9 formal reproducibility synchronization:

- `docs/STAGE_09_V4_FORMAL_REPRODUCIBILITY_SYNC.md`;
- `docs/REPRODUCIBILITY_MANIFEST.json`;
- `docs/EXPOSITION_OUTPUT_MANIFEST.json`;
- `Makefile`;
- `.github/workflows/verify.yml`;
- `.github/workflows/lean.yml`.

## The repaired theory scope

P2R uses order comparative statics. For `b2>b1`, private common-layer R&D is globally nonincreasing and coordinated symmetric common-layer R&D is globally nondecreasing for differentiable increasing strictly concave `g` on `[0,E]`. Strict order is claimed only when both compared optima are interior. No pointwise derivative sign is claimed for arbitrary general `g`.

P4 remains an exact quadratic-baseline result: for each `y in (1/2,1)` there is a unique threshold `bar_nu(y)`, with complete standardization at/below the threshold and a unique interior scope above it within `0<nu<y`.

The downstream-price uniqueness claim is explicitly limited to the global **pure-strategy** continuation certified under condition `(R)`. Mixed-strategy uniqueness is not claimed.

The coordinated symmetric-R&D benchmark keeps decentralized Bertrand pricing and is not an unrestricted first best.

## Journal positioning and historical submission records

Stage 12 selected the **International Journal of Industrial Organization (IJIO)** as the primary target. The operational default ladder remains:

`IJIO -> Review of Industrial Organization -> Journal of Industry, Competition and Trade`

with *The Journal of Industrial Economics* retained as an optional higher-risk stretch. RAND remains excluded by project instruction.

Historical Stage 13 integration, Stage 14 QA, and Stage 15 submission-freeze records are preserved. They predate the latest-workflow certification migration and therefore are not the final latest-workflow submission certification.

With Stage 9 now certified, the remaining compatibility route is:

`Stage 11 certification-regression recheck -> current Journal Requirements Ledger -> refreshed Stage 14 QA -> new Stage 15 submission freeze`.

## Theory change control

Any substantive change to the model, theorem statements, quantifiers, equilibrium concept, benchmark, condition `(R)`, or policy objective must roll back to the earliest affected analytic stage. Any material change to a formally certified theorem or encoded hypothesis also makes the affected Formal Verification Certificate stale until Stage-7.5A formal recertification is completed.
