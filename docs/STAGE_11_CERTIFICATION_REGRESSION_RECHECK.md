# Stage 11 — Certification-Regression Recheck

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Latest-workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`, especially `templates/STAGE_11_REFEREE_GATE.md`.

Current target journal inherited from the already-completed historical Stage 12: *International Journal of Industrial Organization* (IJIO).

## 1. Executive referee-gate verdict

Provisional pending clean CI:

`GO TO JOURNAL POSITIONING — SUBJECT TO CLEAN REGRESSION CI`

No current fatal or major theory defect has been identified. One historical genuine certification regression (P2R function-class/quantifier inflation) remains correctly repaired and is now recorded explicitly. One new minor reproducibility-provenance regression was found in the Appendix: the computational-verification note still called v3 the active freeze after the Stage-9 v4 synchronization. That wording has been repaired to v4 and is protected by a regression test. It does not alter any theorem, model primitive, equilibrium, threshold, welfare statement, or formal theorem.

The final Stage-11 verdict will be fixed only after the exact PR head passes the canonical `make all` reproducibility path, thereby re-running the independent equilibrium-set, continuation, nonbaseline-function, manuscript, and Lean gates.

## 2. Referee A — novelty / mechanism regression report

### A1. Did certification migration inflate the contribution?

Attack: compare the current v4 claim scope to the historical Stage-11 v3 surviving contribution.

Result: `PASS`.

The contribution remains the same narrow mechanism: regulator-selected standardization scope changes transferability of common innovation; firms reallocate a fixed R&D portfolio toward proprietary innovation as the private competitive penalty rises; this endogenous composition response can overturn complete standardization above an exact rivalry threshold in the quadratic baseline.

The current manuscript does not re-label scarce-resource allocation, underappropriation, generic standards/innovation trade-offs, or second-best policy as new in themselves.

### A2. Fresh adjacent-literature collision check

A targeted 2026 search re-opened the most relevant current neighborhood. Two especially close recent papers are:

- Bergeaud, Schmidt, and Zago (2026), “Patents that Match your Standards: Firm-level Evidence on Competition, Innovation and Growth,” *Journal of Financial Economics*;
- Bonani (2026), “Standard-setting and the incentives to innovate: Evidence from the IEEE patent policy update,” *International Journal of Industrial Organization*.

These strengthen the empirical relevance of competition-dependent innovation responses to standards but do not provide the paper's regulator-chosen continuous scope -> fixed common/proprietary R&D portfolio -> exact complete/selective scope threshold result. Llanes (2024) remains the closest technical-standards innovation-incentive theory reference, with a different standards-formation/licensing/complementary-technology mechanism.

Result-level novelty verdict remains:

`DISTINCT BUT NARROW`.

No Stage-6 novelty rollback is triggered.

## 3. Referee B — assumptions / mathematics / globality

### B1. Historical P2R quantifier regression

Attack: deliberately reintroduce the class of function that defeated the old implicit-`C^2` logic.

Evidence:

- `docs/CERTIFICATION_REGRESSION_P2R.md`;
- `tests/test_p2r_order_monotonicity.py`;
- `formal/SSDI/Generality.lean`;
- Stage-7.5A claim-scope ledger.

The test suite contains both a strictly concave corner-plateau technology and a differentiable strictly concave technology that is not twice differentiable at an interior point. The current order theorem survives; the old pointwise-derivative formulation is not stated.

Current status: `PASS — HISTORICAL CERTIFICATION REGRESSION CLOSED`.

### B2. Candidate deviation versus equilibrium-set characterization

Attack: do not infer price-equilibrium uniqueness from candidate optimality. Re-run the distinct D1/D2/D3 paths.

Evidence:

- `scripts/stage4a_independent_equilibrium_set_audit.py`;
- `scripts/stage11_independent_continuation_audit.py`;
- `docs/STAGE_04A_RETROACTIVE_MATH_ADVERSARIAL_CERTIFICATION.md`.

The Stage-4A evaluator separately checks candidate deviations, alternative pure equilibria, and zero-demand/zero-profit indifference behavior. The Stage-11 continuation evaluator reconstructs consumer KKT allocations independently of the production numerical verifier.

Expected regression condition: any unresolved KKT regime, profitable deviation, alternative pure equilibrium, or boundary-equilibrium counterexample fails `make verify`.

Current status: `PASS SUBJECT TO CLEAN CI RE-RUN`.

### B3. Global/SPNE wording

Attack: search for drift from certified pure-strategy scope to unqualified uniqueness.

Result: `PASS`.

The Model states `unique pure-strategy Bertrand equilibrium`; the Equilibrium section states `unique active-product pure-strategy price equilibrium`; the Appendix states `unique global pure-strategy Nash equilibrium`. Mixed-strategy uniqueness is not claimed.

### B4. Solver failure handling

Attack: inspect whether `None`, NaN, invalid active sets, exceptions, or nonconvergence can be treated as an unprofitable deviation.

Result: `PASS` by inherited implementation design. Both independent continuation paths fail closed on unresolved consumer/KKT classification. Clean CI must reconfirm zero unresolved cases.

## 4. Referee C — welfare / institution / benchmark

### C1. Welfare-selection robustness

The relevant pure-strategy continuation is certified unique under `(R)`, so the current welfare path has no pure-equilibrium selection degree of freedom. The paper does not claim selection invariance over possible mixed equilibria.

Result: `PASS`.

### C2. Welfare accounting

Exact symmetric `CS`, `PS`, `W`, efficient quantity, and Bertrand welfare-gap identities are preserved analytically and in `formal/SSDI/WelfareIdentities.lean`.

Result: `PASS SUBJECT TO CLEAN FORMAL BUILD`.

### C3. Benchmark terminology

Attack: reconstruct the coordinated benchmark's choice set.

The regulator chooses scope and a common symmetric R&D composition; differentiated Bertrand pricing remains decentralized; R&D remains restricted to the symmetric diagonal. The manuscript explicitly states that this is not an unconstrained first best.

Result: `PASS`.

### C4. Institution-specific overclaim

The variable `b` remains a reduced-form scope/transferability object. The model does not claim to reproduce a specific legal disclosure fraction, licensing rule, or SSO procedure.

Result: `PASS`.

## 5. Referee D — journal / exposition / claim scope

### D1. Quadratic policy theorem inflation

Attack: check whether P4 has become a generic arbitrary-`g` selective-standardization theorem.

Result: `PASS`. The manuscript states that P4's global uniqueness and threshold characterization are quadratic-baseline claims only.

### D2. Historical equilibrium wording regression

Historical issue: unqualified uniqueness language could be read as mixed-strategy uniqueness.

Current defense: Stage-7.5A narrowed manuscript wording to pure strategies and `tests/test_stage11_certification_regressions.py` now prevents reintroduction.

Status: `CLOSED_PERMANENTLY_GUARDED`.

### D3. New stale-freeze provenance finding

Finding: Appendix computational-verification prose still named `SSDI-THEORY-FREEZE-2026-09-06-v3` as the active frozen theory after Stage 9 had migrated active reproducibility metadata to v4.

Severity: `MINOR — REPRODUCIBILITY PROVENANCE REGRESSION`.

Repair: Appendix now names `SSDI-THEORY-FREEZE-2026-09-10-v4` and expressly describes v3 as the unchanged inherited scientific object.

Earliest affected stage: Stage 9 metadata/exposition only.

Theory/formal rollback: none.

Permanent guard: `tests/test_stage11_certification_regressions.py`.

## 6. Candidate-deviation re-audit

Required attack: at every audited upstream history, challenge the certified candidate with nonnegative price deviations including deviations large enough to force inactivity.

Artifact: `scripts/stage4a_independent_equilibrium_set_audit.py` and `scripts/stage11_independent_continuation_audit.py`.

The exact current-branch counts will be accepted only from clean CI. Historical certified counts were zero profitable deviations and zero unresolved continuations.

## 7. Alternative-equilibrium / multiplicity re-audit

Required attack: independently search inactive-product, zero-price, boundary, and alternative active pure equilibria rather than equating no-profitable-deviation with uniqueness.

Analytic exhaustion remains:

1. `(R)` implies `A_i > rho A_j`, so an inactive firm can profitably re-enter;
2. any pure equilibrium therefore has both products active and positive prices;
3. active-region profit is strictly concave in own price;
4. the two FOCs have a nonsingular linear system and hence one active candidate;
5. separate global-deviation verification certifies that candidate.

Artifact: Stage-4A independent equilibrium-set audit.

Status: `PASS SUBJECT TO CLEAN CI RE-RUN`.

## 8. Indifference / zero-payoff re-audit

Relevant indifference set: sufficiently high own prices can generate zero demand and zero profit.

Attack: vary own price in the zero-demand region, recompute opponent response/consumer regime, and test profitable positive-price re-entry.

Result: such zero-profit actions cannot support a pure equilibrium under `(R)` because `A_i > rho A_j` leaves a profitable sufficiently small positive-price re-entry.

Status: `PASS SUBJECT TO CLEAN CI RE-RUN`.

## 9. Selection / refinement provenance and symmetry audit

No weak-dominance deletion, no-loss restriction, asymmetric tie-break, price floor, or ex post refinement selects the preferred equilibrium. Condition `(R)` is a symmetric primitive parameter restriction used to guarantee global pure-strategy continuation; it is not an equilibrium-selection device applied after observing multiplicity.

Status: `PASS`.

## 10. Independent equilibrium / continuation re-audit

The clean-room continuation implementation reconstructs direct consumer KKT allocation and does not call the production price-profit evaluator. It deliberately enters deviator-inactive regimes at large finite prices and fails closed on unresolved active sets.

Status: `PASS SUBJECT TO CLEAN CI RE-RUN`.

## 11. Welfare-selection regression audit

No multiple certified pure price equilibria exist under `(R)`, and the paper's policy/welfare claims use the certified pure path. Therefore no alternative pure-equilibrium selection profile exists to reverse the current welfare ranking. Mixed-strategy selection-free welfare is not claimed.

Status: `PASS`.

## 12. Independent quantifier / function-class re-audit

The adversarial nonbaseline-function tests target precisely the historical failure mode:

- corners can flatten optimizer movement, blocking globally strict claims;
- differentiability + strict concavity does not supply a globally usable `g''`;
- current decreasing-/increasing-differences order comparative statics survive.

P4 remains quadratic-specific and is not inferred from P2R.

Status: `PASS SUBJECT TO CLEAN PYTEST + LEAN RE-RUN`.

## 13. Solver-failure / unresolved-continuation ledger

The final clean-CI counts will be inserted at closeout. The required fail-closed categories are:

- solved player/history deviation cases;
- profitable deviations;
- alternative pure equilibria;
- unresolved KKT/consumer states;
- numerical failures;
- R&D-corner failures;
- policy-regime failures;
- welfare failures.

Any positive unresolved/failure count blocks a Stage-11 GO.

## 14. Evidence ledger for material PASS states

| Claim | Attack actually performed | Evidence | Surviving limitation |
|---|---|---|---|
| P2R generality | corner technology + differentiable non-`C^2` technology + bounded-domain formal order logic | `test_p2r_order_monotonicity.py`; `Generality.lean`; Stage-7.5A ledger | no general pointwise optimizer derivative; no generic P4 |
| price candidate globality | large finite deviation / direct KKT reconstruction | Stage-4A + Stage-11 independent scripts | pure strategies only |
| price equilibrium uniqueness | separate inactive/boundary/alternative-equilibrium attack | Stage-4A D2 certificate | mixed uniqueness not certified |
| zero-profit indifference | inactive-action variation + profitable re-entry | Stage-4A D3 / direct KKT | pure strategies only |
| P4 threshold | exact curvature/endpoints/threshold algebra + formal sign core | symbolic verifier; `Threshold.lean`; `PolicySigns.lean`; `PolicyObjective.lean` | quadratic baseline |
| welfare / benchmark | direct welfare identities + planner-choice-set reconstruction | welfare section; `WelfareIdentities.lean` | coordinated symmetric benchmark is constrained |
| formal assurance | statement-fidelity map + pinned build + escape-hatch audit | Stage-7.5A certificate; `make formal`; `make formal-audit` | selected proof-critical core, not full game |

## 15. Certification-regression ledger

Canonical machine-readable ledger: `docs/CERTIFICATION_REGRESSION_LEDGER.json`.

### CR-01 — P2R function-class / quantifier inflation

Class: `CERTIFICATION REGRESSION`.

Historical status: discovered at Stage 11, correctly rolled back to Stage 7R2.

Modern gate that should have caught it: Stage 7.5A.

Current status: `CLOSED_PERMANENTLY_GUARDED`.

### CR-02 — pure-strategy uniqueness wording

Class: `CLAIM_SCOPE REGRESSION`.

Modern gates: Stage 4A equilibrium-set certificate + Stage 7.5A claim-scope ledger.

Current status: `CLOSED_PERMANENTLY_GUARDED`.

### CR-03 — stale v3 active-freeze sentence after Stage 9

Class: `REPRODUCIBILITY PROVENANCE REGRESSION`.

Earliest affected stage: Stage 9 metadata/exposition.

Current status: `REPAIRED`; no scientific rollback.

## 16. Consolidated severity table

| Attack | Severity | Current state |
|---|---|---|
| historical P2R hidden-smoothness/derivative overclaim | fatal if reintroduced | CLOSED / permanently guarded |
| candidate validity | fatal if failed | PASS subject to clean rerun |
| additional pure price equilibrium | fatal to uniqueness | PASS subject to clean rerun |
| unresolved continuation | major/fatal to global path | PASS subject to clean rerun |
| mixed-strategy uniqueness inflation | major claim-scope issue | CLOSED / not claimed |
| P4 functional-form inflation | major if present | PASS / quadratic-only wording |
| welfare-accounting error | fatal if present | PASS subject to formal rerun |
| first-best mislabeling | major if present | PASS |
| stale v3 Appendix provenance | minor | REPAIRED |
| result-level novelty collision | major if found | SURVIVED — DISTINCT BUT NARROW |

## 17. Required fixes and earliest affected stage

Required current fix found by this recheck:

- update stale Appendix freeze provenance from active v3 to active v4; earliest affected stage = Stage 9 metadata/exposition; completed on this branch.

No model, theorem, threshold, welfare, equilibrium-concept, or formal-theorem change is required.

## 18. Theory-change implications

`NO THEORY CHANGE`.

The active freeze remains `SSDI-THEORY-FREEZE-2026-09-10-v4`. No Stage-8 refreeze is required unless clean CI uncovers a substantive failure.

## 19. Resolved versus unresolved attacks

Resolved before clean CI:

- P2R quantifier regression;
- pure-strategy claim-scope regression;
- first-best benchmark terminology;
- formal-verification boundary;
- stale Appendix v3 provenance.

Unresolved only in the procedural sense:

- exact current branch must pass clean `make all`, including independent Stage-4A/Stage-11 equilibrium attacks, pytest, manuscript build, Lean build, and formal escape-hatch audit.

## 20. Verdict and downstream contract

Provisional verdict:

`GO TO JOURNAL POSITIONING — SUBJECT TO CLEAN REGRESSION CI`.

Because Stage 12 already selected IJIO and there is no scientific delta from the surviving v3/v4 contribution, a fresh journal-ranking exercise is unnecessary if the final Stage-11 recheck passes. The compatibility route is then:

`Stage 11 PASS -> current Journal Requirements Ledger -> refreshed Stage 14 QA -> new Stage 15 submission freeze`.

The final record will replace the provisional language with the canonical Stage-11 verdict only after exact-head CI qualification.