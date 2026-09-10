# Stage 4A — Retroactive Independent Mathematical Adversarial Certification

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Scientific baseline audited: `main@9678decb82ea60a6706c9212505bdd73c9915c67`

Active theory freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`

Latest workflow authority: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`

Canonical template applied: `templates/STAGE_04A_MATH_RED_TEAM.md`

Checklists applied:

- `checklists/THEOREM_CERTIFICATION_CHECKLIST.md`
- applicability portion of `checklists/FORMAL_VERIFICATION_CHECKLIST.md`
- equilibrium-continuation requirements inherited from the current pipeline.

This is a retroactive compatibility certification. It tests the present v3 theory against the current Stage-4A gate without pretending that Stage 4A existed in the historical v1.3 sequence. No scientific primitive, theorem, parameter restriction, welfare claim, or manuscript conclusion is changed here.

## 1. Executive adversarial verdict

`GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`

No false equilibrium claim, omitted pure-strategy price equilibrium, profitable boundary deviation, R&D corner equilibrium, policy multiplicity, welfare-accounting error, or benchmark-label error was found within the paper's stated scope.

The most important new closure is the explicit separation of:

1. D1 candidate-deviation certification; and
2. D2 alternative-equilibrium / multiplicity certification.

The price result is not certified unique merely because the displayed candidate survives deviations. The alternative pure-equilibrium class is exhausted separately.

Formal verification is classified `FORMALIZATION APPLICABLE`; implementation/fidelity closure remains a Stage-7.5A obligation under the latest workflow.

## 2. Independent reconstruction summary

### 2.1 Feasible quality bounds

For `g(r)=r-kappa r^2/2` with `y=kappa E<1`, `g` is increasing on `[0,E]`. The own two-layer contribution

`g(x_i)+g(E-x_i)`

is minimized at an endpoint and maximized at `E/2`, giving respectively

`E(1-y/2)` and `E(1-y/4)`.

The rival-transfer term is between `0` and `g(E)=E(1-y/2)`. Therefore every feasible quality lies in the frozen interval

`A_min=a+theta E(1-y/2)`

through

`A_max=a+theta E(2-3y/4)`.

This independently validates the bounds used in `(R)`.

### 2.2 Pure price equilibrium

For any feasible quality pair, `(R)` implies both

`A_i/A_j < 2/[rho(3-rho^2)]`

and

`A_i/A_j > rho(3-rho^2)/2 > rho`.

The lower inequality excludes any pure equilibrium with an inactive product: for every `p_j>=0`,

`A_i-rho(A_j-p_j) >= A_i-rho A_j>0`,

so an inactive firm has a strictly profitable sufficiently small positive-price re-entry.

Thus every pure equilibrium must have both products active and positive prices. The active-region profit is strictly concave in own price and the two FOCs have determinant `4-rho^2>0`, so there is exactly one active candidate:

`p_i^*=[(2-rho^2)A_i-rho A_j]/(4-rho^2)`.

Candidate globality is then checked separately. Against `p_j^*`, rival foreclosure requires a nonnegative price no larger than

`A_i-(A_j-p_j^*)/rho`.

That threshold is negative exactly under the upper ratio inequality in `(R)`. Hence no nonnegative foreclosure deviation exists. High-price deviations yield zero profit; all remaining positive-profit deviations are inside the strictly concave active region. The candidate is therefore the unique global pure-strategy Nash equilibrium at every feasible upstream history.

### 2.3 R&D subgame

Because the price-equilibrium profit bracket is positive under `(R)`, maximizing profit is equivalent to maximizing its positive linear quality index. The `x_i`-dependent terms reduce exactly to

`(1-nu b)g(x_i)+g(E-x_i)`.

The objective is strictly concave, its derivative at `0` is `y-nu b>0`, and its derivative at `E` is negative. Thus the best response is uniquely interior. It is independent of `x_j`, so no asymmetric or boundary R&D equilibrium exists. The unique solution is

`x^F(b)=(y-nu b)/[kappa(2-nu b)]`.

### 2.4 Policy theorem

The reduced quadratic policy objective satisfies `F''(b)<0` on the full interval. Together with `F'(0)>0`, the sign of `F'(1)` completely determines whether the unique maximizer is the endpoint `1` or a unique interior point. The threshold polynomial has opposite endpoint signs and is strictly increasing in `nu`, establishing a unique `bar_nu(y)`.

### 2.5 Welfare and benchmark reconstruction

Consumer surplus, producer surplus, total surplus, and the efficient-quantity gap were reconstructed directly from utility, symmetric Bertrand price, and symmetric quantity. The coordinated R&D exercise retains decentralized Bertrand pricing and symmetric R&D; it is therefore correctly labeled a constrained benchmark rather than first best.

## 3. Headline theorem-certificate table

Detailed certificates are preserved in `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`.

| Claim | Globality / scope | D1 deviation | D2 multiplicity | D3 indifference | Independent reconstruction | State |
|---|---|---|---|---|---|---|
| E0 price continuation | every feasible upstream history; pure strategies; conditional on `(R)` | PASS | PASS — unique pure equilibrium | PASS | direct consumer KKT + analytic exhaustion | PASS |
| E1/P1 private R&D | all `b in [0,1]`, quadratic frozen region | PASS | PASS — unique | N/A | endpoint derivatives + strict concavity + grid attack | PASS |
| P2R general wedge | differentiable increasing strictly concave `g`; weak global order, strict if both optima interior | PASS | PASS for unique one-dimensional optimizers | N/A | revealed preference + nonquadratic tests | PASS |
| P3R fixed symmetric allocation | all fixed symmetric `bar{x}`; strict for `bar{x}>0` | PASS | N/A | N/A | direct quality/welfare derivative | PASS |
| P4 selective scope | all `1/2<y<1`, `0<nu<y`; quadratic only; conditional on `(R)` | PASS | PASS — unique policy optimum | N/A | independent curvature/threshold reconstruction + grid attack | PASS |
| P5R/W1 coordinated benchmark / welfare | frozen quadratic symmetric benchmark | PASS | PASS for scope optimum | N/A | direct utility/welfare reconstruction | PASS |

No certificate contains a material `NOT TESTED` field for the claim actually made.

## 4. Candidate-deviation audit (D1)

### Price stage

The permanent independent evaluator is `scripts/stage4a_independent_equilibrium_set_audit.py`.

It reconstructs consumer KKT regimes directly. It does not call `scripts/numerical_verify.py`, `scripts/symbolic_verify.py`, or the manuscript's price-profit routine. For each audited player-history it searches from `p_i=0` to a price large enough to make the deviator inactive and treats any unclassified KKT regime as `UNRESOLVED` and a hard failure.

The local pre-commit execution produced:

`STAGE4A_RETRO_AUDIT: PASS; parameter_sets=126; histories=2142; player_histories=4284; unresolved=0; profitable_price_deviations=0; alternative_pure_price_equilibria=0; rd_corner_failures=0; policy_regime_failures=0; welfare_failures=0`

This run includes the canonical parameterization, near-domain-boundary values, a threshold-neighborhood case, all scope/R&D corners for each parameter set, and deterministic random feasible histories.

### R&D stage

Strict concavity plus endpoint derivative signs supplies analytic globality. The independent script additionally checks the closed-form private optimum against dense full-interval maximization at `b=0`, `b=1`, near those endpoints, and interior scopes.

### Policy stage

Strict concavity supplies analytic globality. The independent script separately maximizes the reduced objective over the full policy interval for complete-scope and interior-threshold regimes.

## 5. Alternative-equilibrium / multiplicity audit (D2)

### Price equilibrium set

Status: `UNIQUE` in pure strategies under `(R)`.

The audit deliberately does not infer uniqueness from a no-profitable-deviation check. Instead:

1. inactive-product pure equilibria are excluded by profitable re-entry from `A_i>rho A_j`;
2. active zero-price equilibria are excluded because a small positive price yields positive profit while activity is preserved locally;
3. therefore every pure equilibrium is interior in the active-active price regime;
4. the two active FOCs have exactly one solution;
5. that solution passes the separate global-deviation audit.

Thus there is no second pure equilibrium on a boundary, tie set, zero-demand set, or alternative active branch.

### R&D equilibrium set

Status: `UNIQUE` in the quadratic baseline. Each firm has one global best response and it is independent of the rival's R&D choice.

### Policy optimum set

Status: `UNIQUE`. Strict concavity excludes policy multiplicity, including at the threshold where `F'(1)=0` but `F'(b)>0` for every `b<1`.

## 6. Indifference / zero-payoff trigger audit (D3)

The relevant trigger is the continuum of high prices giving a firm zero demand and zero profit.

Analytically, no such action can belong to equilibrium because `A_i>rho A_j` implies profitable re-entry for every nonnegative rival price. Numerically, the new independent script forces own inactivity, recomputes the rival's best response from direct KKT demand, and then verifies a strictly profitable positive-price re-entry.

No other equilibrium-relevant payoff-indifference set was identified in the frozen R&D or policy problems because their relevant objectives are strictly concave or strictly monotone as stated.

## 7. Equilibrium-selection / refinement audit

No equilibrium selection device is needed for the certified pure-strategy path.

The paper does not use:

- a no-loss price restriction;
- a price floor;
- weak-dominance deletion;
- an imposed tie-break;
- a selected member of a multiple pure-equilibrium set.

Condition `(R)` is a primitive sufficient global-continuation parameter restriction, not an equilibrium refinement. It restricts the admissible parameter region; it does not delete equilibria from an otherwise maintained parameter point.

## 8. Global boundary / regime audit

Explicitly attacked classes:

- `b=0`, `b=1`, and near-policy boundaries;
- `x_i=0`, `x_i=E`, symmetric and asymmetric R&D corners;
- active-active consumer allocation;
- one-product-active allocation;
- both-products-inactive / zero-demand behavior;
- own-price inactivity under large deviations;
- attempted rival foreclosure;
- zero-price behavior;
- near `y=1/2`, near `y=1`, near `nu=0`, and near `nu=y`;
- the `H=0` policy-threshold neighborhood.

No previously omitted regime supporting a paper claim was found.

## 9. Continuation audit

The current Stage-4A script and the pre-existing clean-room Stage-11 continuation evaluator are logically separate from the production numerical verifier.

Pre-existing Stage-11 independent evidence:

- 73 upstream histories;
- 146 player-history price-deviation problems;
- 10,001 nonnegative deviation prices per player-history;
- `UNRESOLVED=0`;
- numerical failures `=0`;
- profitable finite deviations `=0`;
- pure boundary-equilibrium counterexamples `=0`.

Retroactive Stage 4A therefore records continuation completeness as `PASS` for the pure-strategy SPNE actually used by the paper.

## 10. Counterexample search design and results

Analytic attacks were performed before relying on grids:

- derive exact feasible quality extrema;
- derive the ratio inequalities implied by `(R)`;
- prove inactive-product re-entry;
- prove unique active-price FOC solution;
- derive the exact foreclosure threshold sign;
- prove R&D endpoint derivative signs and strict concavity;
- prove policy strict concavity and threshold monotonicity;
- reconstruct welfare identities from utility.

Numerical attacks then targeted boundaries, near-boundaries, asymmetric histories, zero-demand regimes, the policy threshold, and random admissible parameter/history draws.

No new counterexample was found.

Historical counterexample/regression evidence remains important: the earlier pointwise general-`g` derivative formulation was too strong and was replaced by P2R's order theorem. `tests/test_p2r_order_monotonicity.py` permanently checks a corner-plateau case and a differentiable strictly concave technology that is not twice differentiable at an interior point.

## 11. Welfare-selection and benchmark-definition audit

Because the certified pure price equilibrium is unique under `(R)`, the paper's symmetric welfare calculations do not hide a pure-equilibrium selection problem.

Benchmark labels pass:

- `P3R`: fixed symmetric-allocation benchmark;
- `P5R`: coordinated symmetric-R&D benchmark with decentralized Bertrand pricing;
- unrestricted first best: explicitly not claimed.

The exact positive Bertrand quantity-control welfare gap confirms that P5R is not an unconstrained first-best problem.

## 12. Evidence ledger

| Claim | Attack actually performed | Evidence/artifact | Result | Surviving limitation |
|---|---|---|---|---|
| E0 global price continuation | KKT reconstruction, finite deviations, inactive-equilibrium elimination, foreclosure inequality, active-FOC uniqueness | `scripts/stage4a_independent_equilibrium_set_audit.py`; `scripts/stage11_independent_continuation_audit.py`; Appendix | PASS | pure strategies only |
| E1/P1 | full `[0,E]` best-response audit, endpoints, strict concavity, asymmetric-equilibrium check | new Stage-4A script; theorem certificate | PASS | quadratic closed form |
| P2R | decreasing/increasing-differences proof; corner and non-C2 stress technologies | Appendix; `tests/test_p2r_order_monotonicity.py` | PASS | no general pointwise derivative; no general policy theorem |
| P3R | direct fixed-allocation quality and welfare derivative | theorem certificate; welfare section | PASS | symmetric fixed allocation only |
| P4 | exact curvature/endpoints/threshold proof; near-boundary and random full-policy-grid attacks | new Stage-4A script; symbolic cross-check; theorem certificate | PASS | quadratic policy theorem; conditional on `(R)` |
| P5R/W1 | direct utility accounting, quantity-control gap, coordinated-envelope sign | new Stage-4A script; theorem certificate; welfare section | PASS | constrained symmetric benchmark |

## 13. Formal-verification applicability and preliminary target map

Final Stage-4A applicability decision:

`FORMALIZATION APPLICABLE`

The proof-critical target map is preserved in `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`. Highest-value targets are P4 threshold/curvature/sign logic, P1 closed-form and derivative signs, P2R order identities/quantifier boundary, welfare identities, and the algebraic inequalities supporting the global price continuation.

The repository's later Lean layer already implements substantial parts of this map, but this Stage-4A decision deliberately does not call that a formal-verification PASS. Under the current workflow, statement fidelity, axiom/placeholder audit, model-boundary certificate, clean-build provenance, and the final formalization scope must be closed at retroactive Stage 7.5A.

## 14. Permanent regression artifacts

Created now:

- `scripts/stage4a_independent_equilibrium_set_audit.py`;
- `make stage4a` target;
- `make verify` now includes `stage4a`, so ordinary verification fails if the retroactive Stage-4A adversarial checks regress;
- `theorem_certificates/STAGE4A_RETROACTIVE_CERTIFICATES.md`.

Pre-existing regression assets retained:

- `scripts/stage11_independent_continuation_audit.py`;
- `tests/test_p2r_order_monotonicity.py`;
- existing symbolic/numerical verification and freeze regression tests.

## 15. Blocker / rollback decision

No Stage-4 mathematical correctness blocker was found. Therefore no rollback to Stage 4 or Stage 5 is triggered.

This pass does **not** by itself make the entire project latest-workflow compliant. The next retroactive gate remains Stage 7.5A, where theorem quantifiers, equilibrium-set wording, benchmark language, and the Formal Verification Gate must be closed against the final v3 theorem set.

## 16. Canonical verdict and routing

Canonical Stage-4A verdict:

`GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`

Historical routing would be `Stage 4A -> Stage 6 Novelty Re-Kill`.

For this already-developed paper, the compatibility-migration route is:

`Retroactive Stage 4A PASS -> Retroactive Stage 7.5A + Formal Verification Gate`.
