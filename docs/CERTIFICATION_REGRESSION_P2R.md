# Certification Regression Record — P2R General-Technology Scope

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Active freeze: `SSDI-THEORY-FREEZE-2026-09-10-v4`

Latest-workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`.

## 1. Regression classification

`CERTIFICATION REGRESSION — HISTORICAL, REPAIRED, PERMANENTLY GUARDED`

The historical v2 version of Proposition 2R stated pointwise strict derivative signs for the optimal private and coordinated common-R&D choices for an arbitrary differentiable, increasing, strictly concave technology `g`.

The proof path used second-derivative reasoning even though the stated function class did not assume `C^2` smoothness. The defect was discovered only at the later historical Stage-11 hostile review and caused rollback to Stage 7R2.

The mathematical mechanism survived, but the theorem scope did not. The corrected v3/v4 statement is an order-comparative-statics theorem:

- for `b2>b1`, `xF(b2) <= xF(b1)` globally;
- for `b2>b1`, `xS(b2) >= xS(b1)` globally;
- strict order is claimed only when both compared optima are interior;
- no pointwise optimizer derivative `dx/db` is claimed for arbitrary differentiable strictly concave `g`.

## 2. Why this is a certification regression

The defect should have been caught before theory freeze by the modern Stage-7.5A generality/quantifier gate.

| Field | Record |
|---|---|
| Missed defect | pointwise derivative claim exceeded the stated differentiability class |
| Historical checkpoint that passed it | pre-v1.3 theory/generalization route before the first Stage-11 hostile audit |
| Canonical obligation that should have caught it | Stage 7.5A function-class / quantifier certification |
| Missing attack | admissible differentiable-but-not-`C^2` technology and optimizer-differentiability challenge |
| Missing artifact | explicit claim-scope ledger plus nonbaseline function counterexample/regression test |
| Discovery point | historical Stage 11 |
| Earliest rollback point then required | Stage 7R / generality theorem construction |
| Repair | replace pointwise derivative theorem by global order comparative statics; strict only for compared interior optima |
| Current freeze containing repair | `SSDI-THEORY-FREEZE-2026-09-10-v4` |
| Permanent guards | Stage-7.5A ledger, `formal/SSDI/Generality.lean`, `tests/test_p2r_order_monotonicity.py`, Stage-11 regression tests |

## 3. Re-executed hostile attack

The recheck does not merely inspect the corrected prose. It reuses two adversarial technologies in `tests/test_p2r_order_monotonicity.py`:

1. a concave technology producing corner plateaus, demonstrating why globally strict optimizer movement cannot be asserted at corners;
2. a differentiable strictly concave technology with a non-`C^2` interior point, demonstrating that the current function class must not rely on a globally available `g''`.

For both technologies the current weak order theorem survives, and in the interior case the strict two-policy ordering survives. This is precisely the maximum scope certified in Stage 7.5A.

## 4. Current analytic and formal defenses

Current manuscript defense:

- the general theorem is stated as order comparative statics;
- the manuscript expressly declines a pointwise `dxF/db` or `dxS/db` sign for arbitrary `g`;
- P4's exact policy theorem is explicitly quadratic-specific.

Current formal defense:

- `formal/SSDI/Generality.lean` formalizes the decreasing-/increasing-differences order logic on the actual bounded R&D domain `[0,E]`;
- the Stage-7.5A Formal Verification Certificate records the model boundary and does not promote the formal core into a full arbitrary-technology policy theorem;
- `make formal-audit` blocks project proof escape hatches.

Current numerical/counterexample defense:

- `tests/test_p2r_order_monotonicity.py` contains both corner and non-`C^2` stress technologies;
- the tests are called by `make verify`, which is part of the Stage-9 canonical `make all` reproducibility gate.

## 5. Fail-closed regression condition

The project must fail certification if any future revision does any of the following without a new proof and recertification:

- restores a general-`g` pointwise optimizer derivative sign;
- restores globally strict movement including corners;
- introduces `g''` into the general P2R proof while retaining only differentiability of `g`;
- promotes P4's quadratic policy threshold to an arbitrary-concave-technology theorem;
- removes the corner/non-`C^2` stress regressions;
- changes the formal statement or encoded assumptions without recertifying Stage 7.5A Formal Verification.

## 6. Workflow lesson

The reusable failure pattern is:

`correct economic direction + smooth baseline algebra -> unjustified optimizer derivative/general quantifier`.

The modern workflow blocks this by requiring the sequence:

`exact function class -> adversarial nonbaseline function -> corner/boundary attack -> maximum defensible quantifier -> formal statement fidelity -> permanent regression test`.

A late Stage-11 discovery of the same class must again be labeled `CERTIFICATION REGRESSION` and rolled back to Stage 7.5A or earlier rather than patched only in exposition.

## 7. Current status

`CLOSED — CURRENT v4 CLAIM SURVIVES RECHECK`

No theory change is required by the current Stage-11 recheck.