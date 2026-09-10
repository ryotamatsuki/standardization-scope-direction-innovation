# Stage 11 — Certification-Regression Recheck

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Latest-workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`, especially `templates/STAGE_11_REFEREE_GATE.md`.

Inherited target journal: *International Journal of Industrial Organization* (IJIO).

Qualified implementation head: `4b11aabb582e5d777c2553d16bb9f2f5ccfad6d4`.

Clean qualification run: `34482554751` — `success`.

Artifact: `stage14-submission-package`, ID `10154460327`, ZIP SHA-256 `86e560788d433f485b63fa09fea6cdce59cb1427d7bd356ca535062ed7b7f7ed`.

## 1. Executive referee-gate verdict

`GO TO JOURNAL POSITIONING`

No current fatal or major theory defect was identified. No theory rollback is required.

The recheck converts the historical P2R failure into an explicit certification-regression record and permanently guards the repaired theorem scope. It also found one current minor reproducibility-provenance regression: the Appendix still called v3 the active freeze after Stage 9 had synchronized the project to v4. That sentence was repaired to v4 and regression-tested. No model primitive, theorem conclusion, equilibrium, policy threshold, welfare result, benchmark, or formal theorem changed.

Because Stage 12 already selected IJIO and the current scientific object is unchanged from the surviving v3/v4 contribution, no new journal-ranking exercise is required. Operational routing proceeds directly to a current Journal Requirements Ledger.

## 2. Referee A — novelty / mechanism regression report

### A1. Contribution inflation attack

Result: `PASS`.

The contribution remains the same narrow mechanism: regulator-selected standardization scope changes transferability of common innovation; with fixed R&D capacity, firms reallocate toward proprietary innovation as the competitive penalty on transferable common R&D rises; in the quadratic baseline this endogenous composition response creates an exact rivalry threshold between complete and selective standardization.

The paper does not claim novelty for scarce-resource allocation, underappropriation, standards/innovation trade-offs, or second-best policy in themselves.

### A2. Fresh adjacent-literature collision check

A targeted 2026 search re-opened the closest current neighborhood, including Bergeaud, Schmidt, and Zago (2026) on standards, competition and firm innovation; Bonani (2026) on the IEEE patent-policy change and innovation incentives; and Llanes (2024) on innovation incentives in technical standards.

These papers strengthen the relevance of competition-dependent innovation responses to standards but do not absorb the paper's result-level object: regulator-chosen continuous standardization scope -> fixed common/proprietary R&D portfolio reallocation -> exact complete/selective scope threshold.

Novelty verdict remains:

`DISTINCT BUT NARROW`.

No Stage-6 novelty rollback is triggered.

## 3. Referee B — assumptions / mathematics / globality

### B1. Historical P2R quantifier regression

Result: `PASS — HISTORICAL CERTIFICATION REGRESSION CLOSED`.

The old v2 statement used pointwise optimizer-derivative language for arbitrary differentiable increasing strictly concave `g`, while the proof path implicitly required second-derivative reasoning. The current v4 theorem instead states global order comparative statics, with strict order only when both compared optima are interior.

The hostile recheck preserves two nonbaseline tests in `tests/test_p2r_order_monotonicity.py`: a corner-plateau technology and a differentiable strictly concave technology that is not `C^2` at an interior point. The current order theorem survives both. `formal/SSDI/Generality.lean` separately certifies the bounded-domain decreasing/increasing-differences order core.

### B2. Candidate deviation versus equilibrium-set characterization

Result: `PASS`.

The clean Stage-4A evaluator re-ran D1 candidate deviations, D2 alternative pure equilibria, and D3 zero-demand/zero-profit behavior as distinct tests:

`STAGE4A_RETRO_AUDIT: PASS; parameter_sets=126; histories=2142; player_histories=4284; unresolved=0; profitable_price_deviations=0; alternative_pure_price_equilibria=0; rd_corner_failures=0; policy_regime_failures=0; welfare_failures=0`.

Uniqueness is therefore not inferred merely from survival of the displayed candidate.

### B3. Global / SPNE wording

Result: `PASS`.

The manuscript consistently limits downstream uniqueness to pure strategies: `unique pure-strategy Bertrand equilibrium`, `unique active-product pure-strategy price equilibrium`, and `unique global pure-strategy Nash equilibrium`. Mixed-strategy uniqueness is not claimed.

### B4. Solver failure handling

Result: `PASS`.

The independent evaluators fail closed on unresolved consumer/KKT classifications. Clean CI returned `unresolved=0`; no `None`, NaN, failed active set, or nonconvergence is silently interpreted as evidence against a deviation.

## 4. Referee C — welfare / institution / benchmark

### C1. Welfare-selection robustness

Result: `PASS`.

Under `(R)`, the certified pure price continuation is unique. Hence the welfare path has no pure-equilibrium selection degree of freedom. The paper does not claim selection-invariant welfare over possible mixed equilibria.

### C2. Welfare accounting

Result: `PASS`.

Exact `CS`, `PS`, `W`, efficient quantity, and the Bertrand welfare gap survive analytic, regression, and Lean checks. The clean formal build completed all `8664` jobs successfully.

### C3. Benchmark terminology

Result: `PASS`.

The coordinated benchmark lets the regulator choose scope and a common symmetric R&D composition while Bertrand pricing remains decentralized and R&D remains on the symmetric diagonal. The manuscript explicitly states that this is not an unconstrained first best.

### C4. Institutional overclaim

Result: `PASS`.

`b` remains a reduced-form standardization-scope/transferability instrument. No specific legal disclosure fraction, licensing rule, or SSO procedure is claimed to be literally represented.

## 5. Referee D — exposition / claim scope

### D1. Quadratic policy-theorem inflation

Result: `PASS`.

P4 explicitly remains quadratic-specific. The general P2R theorem is not used to assert a general-technology selective-standardization threshold.

### D2. Historical equilibrium-wording regression

Status: `CLOSED_PERMANENTLY_GUARDED`.

The Stage-4A equilibrium-set certificate and Stage-7.5A claim-scope ledger now require pure-strategy wording; `tests/test_stage11_certification_regressions.py` prevents silent re-expansion.

### D3. Current stale-freeze provenance finding

Severity: `MINOR — REPRODUCIBILITY PROVENANCE REGRESSION`.

The Appendix computational-verification note still identified `SSDI-THEORY-FREEZE-2026-09-06-v3` as active after Stage 9 had synchronized reproducibility to v4.

Repair: it now identifies `SSDI-THEORY-FREEZE-2026-09-10-v4` as the active certification-only freeze and describes v3 as the unchanged inherited scientific object.

Earliest affected stage: Stage 9 metadata/exposition only.

Theory/formal rollback: none.

Permanent guard: `tests/test_stage11_certification_regressions.py`.

## 6. Candidate-deviation re-audit

Result: `PASS`.

The clean run challenged price candidates with nonnegative deviations across 126 parameter sets, 2,142 upstream histories, and 4,284 player-history cases. Profitable price deviations: `0`; unresolved consumer/KKT cases: `0`.

## 7. Alternative-equilibrium / multiplicity re-audit

Result: `PASS` within the paper's pure-strategy scope.

Analytic exhaustion remains: `(R)` implies profitable re-entry from inactivity; therefore every pure equilibrium is active with positive prices; active-region own-profit is strictly concave; the two FOCs have one solution; and the separate global-deviation audit validates it. The clean independent search found `alternative_pure_price_equilibria=0`.

## 8. Indifference / zero-payoff re-audit

Result: `PASS`.

High prices can create zero demand and zero profit, but under `(R)` such actions cannot support a pure equilibrium because `A_i>rho A_j` permits a profitable sufficiently small positive-price re-entry. The independent D3 audit found no counterexample.

## 9. Selection / refinement provenance and symmetry audit

Result: `PASS`.

No weak-dominance deletion, no-loss restriction, asymmetric tie-break, price floor, or ex post refinement selects a preferred equilibrium. `(R)` is a symmetric primitive parameter restriction, not a selection rule applied after multiplicity is observed.

## 10. Independent equilibrium / continuation re-audit

Result: `PASS`.

The clean-room continuation implementation reconstructs direct consumer KKT allocation and does not call the production price-profit evaluator. Current clean run:

`STAGE11_CONTINUATION_AUDIT: PASS; histories=73; unresolved=0; failures=0`.

It deliberately enters deviator-inactive regimes at high finite prices and fails closed on unresolved active sets.

## 11. Welfare-selection regression audit

Result: `PASS`.

No multiple certified pure price equilibria exist under `(R)`. Mixed-strategy selection-free welfare is outside the claim set. The welfare comparison therefore does not rely on an undisclosed pure-equilibrium selection.

## 12. Independent quantifier / function-class re-audit

Result: `PASS`.

The nonbaseline corner and non-`C^2` technologies attack the exact historical P2R failure mode. Current P2R survives as an order theorem. The general proof contains no `g''`; P4 remains quadratic-specific. Clean pytest reports `22 passed`.

## 13. Solver-failure / unresolved-continuation ledger

| Metric | Clean result |
|---|---:|
| Stage-4A parameter sets | 126 |
| upstream histories | 2,142 |
| player-history cases | 4,284 |
| unresolved Stage-4A cases | 0 |
| profitable price deviations | 0 |
| alternative pure price equilibria | 0 |
| R&D-corner failures | 0 |
| policy-regime failures | 0 |
| welfare failures | 0 |
| independent Stage-11 continuation histories | 73 |
| continuation unresolved | 0 |
| continuation failures | 0 |
| pytest | 22 passed |
| Lean build | 8,664 jobs, success |
| project Lean escape-hatch audit | PASS |

No positive failure/unresolved count remains.

## 14. Evidence ledger for material PASS states

| Claim | Attack actually performed | Evidence | Surviving limitation |
|---|---|---|---|
| P2R generality | corner technology + differentiable non-`C^2` technology + bounded-domain formal order logic | `test_p2r_order_monotonicity.py`; `Generality.lean`; Stage-7.5A ledger | no general pointwise optimizer derivative; no generic P4 |
| price candidate globality | large finite deviations + direct KKT reconstruction | Stage-4A + Stage-11 independent scripts | pure strategies only |
| price equilibrium uniqueness | separate inactive/boundary/alternative-equilibrium attack | Stage-4A D2 certificate | mixed uniqueness not certified |
| zero-profit indifference | inactive-action variation + profitable re-entry | Stage-4A D3 | pure strategies only |
| P4 threshold | curvature/endpoints/threshold algebra + formal sign core | symbolic verifier; `Threshold.lean`; `PolicySigns.lean`; `PolicyObjective.lean` | quadratic baseline |
| welfare / benchmark | direct welfare identities + choice-set reconstruction | welfare section; `WelfareIdentities.lean` | constrained symmetric benchmark |
| formal assurance | statement fidelity + pinned build + escape-hatch audit | Stage-7.5A certificate; clean `make all` | selected proof-critical core, not full game |

## 15. Certification-regression ledger

Canonical machine-readable ledger: `docs/CERTIFICATION_REGRESSION_LEDGER.json`.

- `CR-01` — P2R hidden-smoothness / quantifier inflation: `CLOSED_PERMANENTLY_GUARDED`.
- `CR-02` — unqualified price-equilibrium uniqueness wording: `CLOSED_PERMANENTLY_GUARDED`.
- `CR-03` — stale v3 active-freeze Appendix sentence after Stage 9: `CLOSED_PERMANENTLY_GUARDED`.

Unresolved material certification regressions: `0`.

## 16. Consolidated severity table

| Attack | Severity if present | Final state |
|---|---|---|
| P2R hidden smoothness / derivative overclaim | fatal to stated theorem | CLOSED / guarded |
| candidate invalidity | fatal | PASS |
| additional pure price equilibrium | fatal to uniqueness | PASS |
| unresolved continuation | major/fatal | PASS |
| mixed-strategy uniqueness inflation | major scope issue | CLOSED / not claimed |
| P4 functional-form inflation | major | PASS / quadratic only |
| welfare-accounting error | fatal | PASS |
| first-best mislabeling | major | PASS |
| stale v3 Appendix provenance | minor | REPAIRED / guarded |
| result-level novelty collision | major | SURVIVED — DISTINCT BUT NARROW |

## 17. Required fixes and earliest affected stage

Only one current repair was required:

- stale Appendix freeze provenance -> Stage 9 metadata/exposition repair -> completed and regression-tested.

No model, theorem, threshold, welfare, equilibrium-concept, or formal-theorem repair is required.

## 18. Theory-change implications

`NO THEORY CHANGE`.

The active freeze remains `SSDI-THEORY-FREEZE-2026-09-10-v4`. No Stage-8 refreeze is required.

## 19. Resolved versus unresolved attacks

Resolved:

- historical P2R quantifier regression;
- pure-strategy claim-scope regression;
- first-best benchmark terminology;
- formal-verification boundary;
- stale Appendix v3 provenance;
- candidate-deviation, alternative-equilibrium, zero-profit-indifference, continuation, welfare and function-class re-audits.

Unresolved material attacks: `NONE`.

Clean qualification details:

- head: `4b11aabb582e5d777c2553d16bb9f2f5ccfad6d4`;
- run: `34482554751`;
- conclusion: `success`;
- symbolic verification: PASS;
- numerical verification: PASS, canonical `b*≈0.68775`;
- Stage-4A independent audit: PASS;
- Stage-11 continuation audit: PASS;
- pytest: `22 passed`;
- exposition v4 synchronization: PASS;
- manuscript build: PASS;
- Lean 4.32.1 / mathlib `520045ab14e26149ee970e2e617ca04b09bde5d6`: build success;
- `PROJECT_LEAN_ESCAPE_HATCH_AUDIT=PASS`;
- title-page / citation-reference / package / PDF preflight: PASS.

## 20. Verdict and downstream contract

Final canonical Stage-11 verdict:

`GO TO JOURNAL POSITIONING`

Stage 11 is scientifically clear to proceed.

Stage 12 has already selected IJIO and no new scientific or result-level novelty defect changes that positioning. Therefore the next compatibility step is not to rerun Stage 12; it is:

`current Journal Requirements Ledger -> refreshed Stage 14 QA -> new Stage 15 submission freeze`.

Any future substantive theorem or model change must still roll back to the earliest affected analytic stage, and any change touching a formally certified theorem or assumption invalidates the affected Formal Verification Certificate until recertified.