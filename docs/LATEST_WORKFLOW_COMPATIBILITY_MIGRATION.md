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
| Stage 9 formal-artifact reproducibility synchronization | **PASS** | `docs/STAGE_09_FINAL_CLOSEOUT.md`; `docs/REPRODUCIBILITY_MANIFEST.json`; merged-main full run `34479910733`; formal run `34479910711` | `REPRODUCIBILITY BASELINE READY` |
| Stage 11 certification-regression recheck | **PASS** | `docs/STAGE_11_CERTIFICATION_REGRESSION_RECHECK.md`; `docs/CERTIFICATION_REGRESSION_LEDGER.json`; qualified run `34482554751` | `GO TO JOURNAL POSITIONING`; no theory rollback |
| Current Journal Requirements Ledger | **PENDING** | — | next required compatibility step before refreshed Stage 14 |
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

Final closeout: `docs/STAGE_09_FINAL_CLOSEOUT.md`.

Stage-9 canonical main merge: `707b9688dfb8afd4624f006795b91f5f2ef83b79`.

Post-merge qualification:

- full reproducibility run `34479910733`: **success**;
- focused formal run `34479910711`: **success**.

The full workflow executes `make all`, including symbolic/numerical verification, Stage-4A and Stage-11 independent equilibrium audits, pytest, deterministic exposition regeneration, manuscript build, pinned Lean build, and formal escape-hatch audit. Stage-9 verdict: `REPRODUCIBILITY BASELINE READY`.

## Stage 11 certification-regression recheck

Canonical record: `docs/STAGE_11_CERTIFICATION_REGRESSION_RECHECK.md`.

Machine-readable regression ledger: `docs/CERTIFICATION_REGRESSION_LEDGER.json`.

Qualified implementation head: `4b11aabb582e5d777c2553d16bb9f2f5ccfad6d4`.

Clean qualification run `34482554751`: **success**.

The recheck explicitly classifies and permanently guards three regression classes:

1. historical P2R hidden-smoothness / general-quantifier inflation — genuine `CERTIFICATION REGRESSION`, repaired by v3/v4 order comparative statics;
2. historical unqualified price-equilibrium uniqueness wording — `CLAIM_SCOPE REGRESSION`, repaired to pure-strategy scope;
3. stale Appendix v3 active-freeze provenance after Stage 9 — `REPRODUCIBILITY PROVENANCE REGRESSION`, repaired to active v4.

Clean Stage-11 evidence:

- Stage-4A: 126 parameter sets, 2,142 histories, 4,284 player-history cases; unresolved `0`; profitable price deviations `0`; alternative pure equilibria `0`;
- Stage-11 continuation audit: 73 histories; unresolved `0`; failures `0`;
- pytest: `22 passed`;
- Lean: 8,664 jobs, success; project escape-hatch audit PASS;
- manuscript, exposition, title-page, citation/reference, package and PDF preflight: PASS.

Unresolved fatal attacks: `0`. Unresolved major attacks: `0`. Unresolved material certification regressions: `0`.

Final Stage-11 verdict: `GO TO JOURNAL POSITIONING`.

Because the already-completed Stage 12 selected IJIO and the Stage-11 recheck found no scientific or result-level novelty change, the migration does not rerun journal ranking.

## Change-control note

The migration adds certification and reproducibility provenance around the unchanged scientific result set. It does not authorize theory changes.

Any substantive defect routes to the earliest affected analytic stage. Any material change to a formalized theorem or encoded hypothesis makes the Formal Verification Certificate stale and requires recertification before refreeze.

## Next compatibility step

`Current Journal Requirements Ledger`.

After that:

`refreshed Stage 14 QA -> new Stage 15 submission freeze`.
