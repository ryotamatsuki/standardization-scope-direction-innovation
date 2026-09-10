# Latest-workflow compatibility migration

Date opened: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Historical production workflow preserved for provenance: `ryotamatsuki/research-paper-workflow` v1.3 at `3e4e6a3f76d86058024d06f9710f942e21627386`.

Latest workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`.

Active canonical theory freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`. The exact v3 freeze is preserved in `docs/THEORY_FREEZE_v3.md`. Historical stage records are not rewritten.

## Migration ledger

| Latest-workflow obligation | Status | Artifact / evidence | Consequence |
|---|---|---|---|
| Retroactive Stage 4A independent mathematical adversarial certification | **PASS** | `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`; `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`; permanent independent evaluator | no Stage-4 rollback |
| Candidate-deviation vs alternative-equilibrium separation | **PASS** | Stage-4A D1/D2 register | pure-price uniqueness not inferred from candidate optimality alone |
| Indifference / zero-payoff trigger audit | **PASS** | Stage-4A D3 register; direct KKT evaluator | inactive/zero-profit pure equilibria excluded |
| Retroactive Stage 7.5A quantifier/scope certification | **PASS** | `docs/STAGE_075A_RETROACTIVE_GENERALITY_QUANTIFIER_FORMAL_VERIFICATION.md` | claim scope closed |
| Formal Verification Gate | **FORMAL VERIFICATION PASS** | `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`; pinned Lean source/toolchain | formal pre-freeze obligation closed |
| Certification-only Stage 8 refreeze | **PASS** | `docs/STAGE_08_CERTIFICATION_ONLY_REFREEZE.md`; active v4 freeze | scientific delta from v3 = none |
| Stage 9 formal-artifact reproducibility synchronization | **PASS** | `docs/STAGE_09_V4_FORMAL_REPRODUCIBILITY_SYNC.md`; `docs/REPRODUCIBILITY_MANIFEST.json`; full run `34478441732`; formal run `34478441787` | `REPRODUCIBILITY BASELINE READY` |
| Stage 11 certification-regression recheck | **PENDING** | — | next required scientific gate |
| Current Journal Requirements Ledger | **PENDING** | — | required before refreshed Stage 14 |
| Refreshed Stage 14 / new Stage 15 submission freeze | **PENDING** | — | required before current-chain submission freeze |

## Stage 4A result

Verdict: `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`.

The permanent evaluator distinguishes candidate-deviation certification, alternative-equilibrium/multiplicity certification, and zero-payoff/indifference attacks and is part of `make verify`.

## Stage 7.5A + Formal Verification result

Stage verdict: `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`.

Formal state: `FORMAL VERIFICATION PASS`.

The selected Lean core covers P1 algebra/order, P2R decreasing/increasing-differences order logic on `[0,E]`, P4 threshold/sign architecture and policy-objective algebraic fidelity, selected `(R)` continuation inequalities, and exact welfare identities. Lean is pinned to v4.32.1 and mathlib commit `520045ab14e26149ee970e2e617ca04b09bde5d6`.

Full KKT/SPNE formalization, mixed-strategy price-equilibrium uniqueness, and the complete P4 calculus/argmax derivation remain explicitly outside Lean.

## Stage 8 certification-only refreeze

Verdict: `THEORY FROZEN — GO TO REPRODUCIBILITY SETUP`.

Active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`.

Scientific delta from v3: `NONE`.

The v4 freeze adds the latest certification/formal registers without altering the scientific result set.

## Stage 9 formal-artifact reproducibility synchronization

Starting remote main: `4c923f9e8e236ea18added57dfefa401f8c406e3`.

Open PRs at work start: none.

Branch: `stage9-v4-formal-reproducibility-sync`.

PR: `#21`.

Qualified implementation head: `fd650e6a3a925e7ae0d24e8981bb38a357a33f09`.

Clean qualification:

- full reproducibility workflow run `34478441732`: **success**;
- focused formal workflow run `34478441787`: **success**.

The full workflow executes `make all`, which now includes symbolic/numerical verification, Stage-4A and Stage-11 independent equilibrium audits, pytest, deterministic exposition regeneration, manuscript build, pinned Lean build, and formal escape-hatch audit. It then retains IJIO package QA and PDF/font preflight.

Stage-9 artifacts:

- `docs/STAGE_09_V4_FORMAL_REPRODUCIBILITY_SYNC.md`;
- `docs/REPRODUCIBILITY_MANIFEST.json`;
- v4-synchronized `docs/EXPOSITION_OUTPUT_MANIFEST.json`;
- v4-synchronized `formal/README.md`;
- root Makefile `make all` / `make formal` / `make formal-audit`;
- full and focused CI workflows using the same Makefile targets;
- strengthened Stage-9 metadata/traceability regressions.

The Stage-8 v3->v4 compare shows no change to paper/formal/core scientific generation sources. Stage 9 therefore rebinds the verified output to v4 without changing the underlying threshold, figure, theorem, or welfare result.

A documentation defect was repaired: `formal/README.md` had still named v3 as active and pointed to nonexistent `formal/FORMAL_VERIFICATION_CERTIFICATE.md`; it now names v4 and the actual certificate `theorem_certificates/STAGE075A_FORMAL_VERIFICATION_CERTIFICATE.md`.

Stage-9 verdict: `REPRODUCIBILITY BASELINE READY`.

## Change-control note

The migration adds certification and reproducibility provenance around the unchanged scientific result set. It does not authorize theory changes.

Any substantive defect routes to the earliest affected analytic stage. Any material change to a formalized theorem or encoded hypothesis makes the Formal Verification Certificate stale and requires recertification before refreeze.

## Next compatibility gate

`Stage 11 — certification-regression recheck`.

After a PASS there, the route is:

`current Journal Requirements Ledger -> refreshed Stage 14 QA -> new Stage 15 submission freeze`.
