# Retroactive Stage 4A theorem certificates

Date: 2026-09-10

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Scientific baseline audited: `main@9678decb82ea60a6706c9212505bdd73c9915c67`

Active theory freeze audited: `SSDI-THEORY-FREEZE-2026-09-06-v3`

Latest workflow authority used for this retroactive certification: `ryotamatsuki/research-paper-workflow@f48984013898696f010f0437a8cfed6b5b54bdc2`.

This file applies the current `checklists/THEOREM_CERTIFICATION_CHECKLIST.md` and Stage-4A requirements to the already-developed v3 scientific object. It is a certification migration artifact. It does not claim that these certificates existed chronologically before Stage 6 in the historical workflow, and it does not modify the frozen theory.

## Common domains and independent evidence

Baseline domain:

- `E>0`, `kappa>0`, `y=kappa E`, `1/2<y<1`;
- `0<rho<1`, `nu=rho/(2-rho^2)`, `0<nu<y`;
- `b in [0,1]`, `x_i in [0,E]`, `p_i>=0`;
- all-history continuation condition `(R)`: `A_max/A_min < 2/[rho(3-rho^2)]`.

Independent evidence used:

- direct consumer-KKT evaluator and full-price-deviation attack: `scripts/stage4a_independent_equilibrium_set_audit.py`;
- separately written downstream continuation evaluator: `scripts/stage11_independent_continuation_audit.py`;
- analytic appendix reconstruction: `paper/sections/appendix.tex`;
- symbolic cross-check only, not counted as independent certification: `scripts/symbolic_verify.py`;
- nonquadratic/corner counterexample stress for P2R: `tests/test_p2r_order_monotonicity.py`.

The Stage-4A independent audit is fail-closed: unresolved consumer KKT regimes raise an error rather than being interpreted as unprofitable deviations.

---

## Certificate E0 — unique global pure-strategy price continuation

### Exact claim

For every feasible upstream history `(b,x_1,x_2) in [0,1] x [0,E]^2` satisfying the frozen parameter restrictions and `(R)`, the downstream price game on `p_i>=0` has a unique global **pure-strategy** Nash equilibrium

`p_i^*=[(2-rho^2)A_i-rho A_j]/(4-rho^2)`,

with both products strictly active.

No claim is made here about nondegenerate mixed-strategy price equilibria.

### Quantifiers and assumptions

Universal over every feasible upstream history. The claim is conditional on `(R)` and on the quadratic frozen quality bounds used to define `A_min,A_max`.

### Independent reconstruction

1. Since every feasible `A_i,A_j` lies in `[A_min,A_max]`, `(R)` implies
   `A_i/A_j > rho(3-rho^2)/2 > rho`.
2. Therefore an inactive product cannot be part of a pure equilibrium. If firm `i` has zero demand at any rival price `p_j>=0`, then
   `A_i-rho(A_j-p_j) >= A_i-rho A_j>0`,
   so a sufficiently small positive price yields strictly positive demand and profit. This eliminates one-active, zero-demand, and both-inactive pure equilibria, including the zero-profit indifference set.
3. Any pure equilibrium therefore has both products active and both prices strictly positive. In the active region each firm's profit is a strictly concave quadratic in its own price. The two necessary FOCs form a nonsingular linear system because `4-rho^2>0`, yielding the displayed candidate uniquely.
4. Candidate globality is separate from uniqueness of the active FOC solution. Holding `p_j=p_j^*`, foreclosure of `j` would require
   `p_i <= A_i-(A_j-p_j^*)/rho`.
   The right-hand side is negative iff `A_i/A_j < 2/[rho(3-rho^2)]`, which follows from `(R)`. Hence no feasible nonnegative deviation can enter a foreclosure regime. A sufficiently high price makes the deviator inactive and earns zero, below the positive candidate profit. All remaining positive-profit deviations stay in the active region, where strict concavity makes `p_i^*` the unique best response.

### D1 candidate-deviation audit

`PASS`.

The new independent Stage-4A script searches nonnegative own prices from zero through a range that forces own inactivity, reconstructing demand directly from consumer KKT regimes. It also checks that no rival-foreclosure regime is reachable under `(R)`.

### D2 alternative-equilibrium / multiplicity audit

`PASS — UNIQUE PURE-STRATEGY EQUILIBRIUM`.

This is not inferred from D1. The separate argument above eliminates every equilibrium containing an inactive product, eliminates zero-price active equilibria, and then uses the unique solution to the two active-region FOCs to exhaust the remaining pure equilibrium class.

### D3 indifference / zero-payoff trigger

`PASS`.

High-price actions producing zero demand and zero profit form a payoff-indifference set, but none can occur in equilibrium because `A_i>rho A_j` guarantees profitable positive-price re-entry for every nonnegative rival price. The Stage-4A script explicitly forces a player into zero demand, recomputes the rival best response, and verifies profitable re-entry.

### Selection/refinement

`NOT APPLICABLE`. No tie-break, no-loss rule, dominance refinement, price floor, or equilibrium-selection rule is used to obtain the pure equilibrium.

### Boundary/regime status

`PASS`. Active-active, one-active, both-inactive, own-inactive deviations, rival-foreclosure deviations, zero price, and price-grid upper tails are covered analytically and/or by the direct KKT evaluator.

### Continuation completeness

`PASS` for the pure-strategy SPNE used by the paper. Existing Stage-11 independent audit: 73 histories, 146 player-history deviation problems, zero unresolved continuations, zero numerical failures, zero profitable deviations.

### Evidence maturity

`PROVED`; independent numerical attack is supplementary.

### Known limitation

The paper and certificate establish uniqueness in pure strategies. They do not claim absence of all possible mixed-strategy equilibria.

### Final certificate state

`PASS`.

---

## Certificate E1/P1 — private R&D equilibrium and reallocation

### Exact claim

Given any scope `b in [0,1]`, the frozen quadratic R&D subgame has the unique equilibrium

`x_1=x_2=x^F(b)=(y-nu b)/[kappa(2-nu b)]`,

which is interior under `0<nu<y<1`, and

`dx^F/db=-nu(2-y)/[kappa(2-nu b)^2]<0`.

### Quantifiers and assumptions

Universal over `b in [0,1]` under the frozen quadratic technology and parameter domain. The reduction to the R&D objective uses the positive pure-price continuation certified in E0.

### Independent reconstruction

Under E0 equilibrium profit is proportional to the square of

`(2-rho^2)A_i-rho A_j`.

The bracket is positive for every feasible history under `(R)`, so maximizing profit is equivalent to maximizing the bracket rather than its square. The terms depending on `x_i`, after division by `2-rho^2`, are exactly

`(1-nu b)g(x_i)+g(E-x_i)`.

The rival's `x_j` is absent from the best-response objective. With quadratic `g`, the second derivative is

`-kappa(2-nu b)<0`.

At `x=0`, the derivative is `y-nu b>y-nu>0`; at `x=E`, it is `(1-nu b)(1-y)-1<0`. Thus the unique global best response is interior. Because it is independent of `x_j`, the joint R&D equilibrium is uniquely symmetric. Solving the FOC yields the displayed `x^F`; direct differentiation yields the displayed negative derivative.

### D1 candidate-deviation audit

`PASS`. Strict concavity plus opposite endpoint derivative signs proves the candidate is the unique global best response on the full interval `[0,E]`. The Stage-4A script independently compares the closed form with dense full-interval maximization including `b=0`, `b=1`, and near-boundary scopes.

### D2 alternative-equilibrium / multiplicity audit

`PASS — UNIQUE`. Each firm's best response is unique and does not depend on the rival's R&D allocation; no asymmetric or boundary R&D equilibrium remains.

### D3 indifference trigger

`NOT APPLICABLE`. Strict concavity gives a unique R&D maximizer; no payoff-equivalent best-response set exists in the frozen baseline.

### Selection/refinement

`NOT APPLICABLE`.

### Evidence maturity

`PROVED`.

### Known limitation

The closed form and strict derivative are quadratic-baseline results. The general-technology result is separately certified as P2R.

### Final certificate state

`PASS`.

---

## Certificate P2R — general-technology directional private/coordinated wedge

### Exact claim

Let `g` be differentiable, increasing, and strictly concave on `[0,E]`. For every `b_2>b_1`,

- `x^F(b_2)<=x^F(b_1)`;
- `x^S(b_2)>=x^S(b_1)`.

If both compared private optima are interior, the first inequality is strict. If both compared coordinated optima are interior, the second inequality is strict. No pointwise derivative sign in `b` is claimed for arbitrary `g`.

### Quantifiers and assumptions

Universal over the stated function class and over pairs `b_2>b_1`. Weak order includes corners. Strict order is conditional on both compared optima being interior.

### Independent reconstruction

For the private problem,

`f_F(x,b_2)-f_F(x,b_1)=-nu(b_2-b_1)g(x)`,

which is nonincreasing in `x`; for the coordinated problem,

`f_S(x,b_2)-f_S(x,b_1)=(b_2-b_1)g(x)`,

which is nondecreasing. Strict concavity gives unique maximizers, so the standard revealed-preference contradiction gives the global weak order without a `g''` assumption. If two compared interior optima were equal, their two FOCs would imply respectively `nu(b_2-b_1)g'(x)=0` or `(b_2-b_1)g'(x)=0`. Differentiability + weak monotonicity + strict concavity imply `g'(x)>0` at an interior point, giving the strict order.

### D1 / D2 status

`PASS` for the one-dimensional private and coordinated optimization problems: each objective is strictly concave, hence its maximizer is unique. This proposition is a comparative-static statement about those unique maximizers, not a new claim of price-game uniqueness.

### Boundary/corner audit

`PASS`. The proof is order-theoretic and explicitly includes corner optima. `tests/test_p2r_order_monotonicity.py` challenges the theorem with a corner-plateau case and with a differentiable strictly concave technology that is not twice differentiable at an interior point.

### Counterexample search

`PASS`. No admissible counterexample was found to the weak order or interior strict-order theorem. The earlier, stronger pointwise-derivative claim was already withdrawn and preserved as a certification regression in the v3 history.

### Evidence maturity

`PROVED AFTER REPAIR`.

### Known limitation

This certificate does not elevate the quadratic P4 policy theorem to a general-technology theorem.

### Final certificate state

`PASS`.

---

## Certificate P3R — fixed symmetric-allocation benchmark

### Exact claim

For any fixed symmetric common-R&D allocation `x_1=x_2=bar{x}>0`, welfare is strictly increasing in `b` and the unique policy optimum is `b=1`. If `bar{x}=0`, welfare is independent of `b`.

### Quantifiers and assumptions

Universal over fixed symmetric `bar{x} in [0,E]` under the frozen quadratic baseline and symmetric Bertrand continuation. No asymmetric fixed-allocation claim is made.

### Reconstruction

`A^FIX(b)=a+theta[(1+b)g(bar{x})+g(E-bar{x})]`.

For `bar{x}>0`, `g(bar{x})>0` because `0<bar{x}<=E` and `y<1`, so `dA^FIX/db=theta g(bar{x})>0`. Symmetric welfare is `W=K(rho)A^2` with `K(rho)>0` and `A>0`, so welfare is strictly increasing. At `bar{x}=0`, `g(0)=0`, so scope drops out.

### D1 / D2 / selection

`PASS / NOT APPLICABLE` as a one-dimensional regulator problem with a monotone objective. No equilibrium-selection assumption is used beyond the already certified unique pure price continuation.

### Benchmark-definition audit

`PASS`. This is explicitly a fixed symmetric-allocation benchmark, not a first-best claim.

### Evidence maturity

`PROVED`.

### Final certificate state

`PASS`.

---

## Certificate P4 — selective standardization threshold

### Exact claim

For each `y in (1/2,1)` there is a unique `bar_nu(y) in (0,y)` satisfying `H(y,bar_nu(y))=0`. In the frozen quadratic region:

- if `nu<=bar_nu(y)`, the unique policy optimum is `b*=1`;
- if `bar_nu(y)<nu<y`, the unique policy optimum satisfies `0<b*<1`.

Equivalently, a unique interior policy occurs iff `nu>bar_nu(y)` within the frozen region.

### Quantifiers and assumptions

Universal over `y in (1/2,1)` and `nu in (0,y)`, conditional on `(R)` for the downstream equilibrium continuation. Quadratic-baseline only.

### Independent reconstruction

The reduced quality objective satisfies

`F''(b)=-nu(2-y)^2(2b nu^2+b nu+2nu+4)/(2-b nu)^4<0`

on `[0,1]`, so it is strictly concave. Also

`F'(0)=y(4-y)/8>0`,

and

`F'(1)=-H(y,nu)/[2(2-nu)^3]`.

Threshold existence and uniqueness follow from

`H(y,0)=2y(y-4)<0`,

`H(y,y)=2y(y-2)^2(y+1)>0`,

and, for `0<nu<y<1`,

`H_nu=3nu^2+4nu(y^2-4y+1)+y^2-4y+16 > 5(y-2)^2>0`.

If `H<=0`, then `F'(1)>=0`; strict concavity implies `F'(b)>F'(1)>=0` for every `b<1`, so the unique maximizer is `b=1`. If `H>0`, then `F'(1)<0<F'(0)` and strict concavity gives exactly one interior root of `F'`, which is the unique global maximizer.

### D1 candidate-deviation audit

`PASS`. Strict concavity certifies globality over the complete policy interval; the Stage-4A script independently maximizes `F` on a dense grid for the canonical case, near-domain-boundary cases, the threshold neighborhood, and deterministic random admissible parameter sets.

### D2 alternative optimum / multiplicity audit

`PASS — UNIQUE`. Strict concavity excludes a second policy maximizer. At the threshold itself `F'(1)=0` but `F'(b)>0` for every `b<1`, so there is no endpoint/interior multiplicity.

### Boundary audit

`PASS`. `b=0` is excluded by `F'(0)>0`; `b=1` is handled by the sign of `F'(1)`; near-threshold and near-domain-boundary values are included in the permanent numerical attack.

### Evidence maturity

`PROVED`; numerical stress is supplementary.

### Known limitation

No general-technology policy concavity/uniqueness theorem is certified.

### Final certificate state

`PASS`.

---

## Certificate P5R/W1 — coordinated symmetric-R&D benchmark and welfare accounting

### Exact claims

1. With the regulator choosing scope `b` and symmetric R&D composition `x`, while Bertrand pricing remains decentralized, the optimal scope is `b^COORD=1`.
2. At symmetric Bertrand quality `A`,
   `CS=A^2/[(2-rho)^2(1+rho)]`,
   `PS=2A^2(1-rho)/[(2-rho)^2(1+rho)]`, and
   `W=A^2(3-2rho)/[(2-rho)^2(1+rho)]`.
3. The efficient-quantity benchmark exceeds decentralized-Bertrand welfare by
   `A^2(1-rho)^2/[(2-rho)^2(1+rho)]>0`.

### Reconstruction

The symmetric coordinated R&D problem is strictly concave and has quadratic solution

`x^S(b)=(y+b)/[kappa(2+b)]`,

which is strictly positive. Along the optimized symmetric R&D choice, the envelope derivative of welfare with respect to scope is `W_A theta g(x^S(b))>0`; hence the unique scope optimum is `b=1`.

For the welfare identities, direct substitution of the symmetric Bertrand price and quantity into consumer utility minus expenditure and producer revenue reproduces the three displayed formulas. Direct optimization of total gross surplus over symmetric quantities gives `q^EFF=A/(1+rho)` and the positive Bertrand quantity-control gap.

### D1 / D2 / selection

`PASS` for the constrained coordinated policy problem. Strict positivity of the envelope derivative excludes alternative scope optima. The price continuation used in welfare is the unique pure continuation certified in E0.

### Welfare-selection robustness

`PASS` for the paper's stated pure-strategy equilibrium concept; there is no pure equilibrium-selection multiplicity under `(R)`.

### Benchmark-definition audit

`PASS`. The manuscript expressly labels P5R a constrained benchmark with decentralized Bertrand pricing and symmetric R&D. It expressly denies that this is an unconstrained first best.

### Evidence maturity

`PROVED`.

### Known limitation

No unrestricted planner problem and no asymmetric coordinated-R&D benchmark is certified.

### Final certificate state

`PASS`.

---

## Cross-certificate equilibrium-selection and indifference conclusion

- Pure price equilibrium set under `(R)`: `UNIQUE`.
- R&D equilibrium set in the quadratic baseline: `UNIQUE`.
- Policy optimum in P4: `UNIQUE` in both complete-scope and interior regimes.
- No auxiliary selection/refinement condition is used.
- Zero-demand/zero-profit price indifference is explicitly triggered and cannot support equilibrium because every inactive product can profitably re-enter.
- No welfare result in the paper depends on choosing among multiple certified pure equilibria.

## Preliminary formal-verification applicability decision

`FORMALIZATION APPLICABLE`.

Stage 4A does not use proof-assistant compilation as a substitute for the independent attacks above. The preliminary high-value target map carried to Stage 7.5A is:

| Claim | Proof-critical formalization target | Main component intentionally outside initial target | Assurance gain |
|---|---|---|---|
| E0 | parameter/ratio inequalities supporting positive candidate prices and exclusion of nonnegative foreclosure | full consumer KKT equilibrium correspondence and mixed strategies | strengthen global-continuation algebra |
| P1 | closed-form R&D FOC identity, interiority inequalities, derivative sign | economic derivation of the profit-to-linear-index reduction | certify comparative-static algebra |
| P2R | two-policy difference identities and order implications where tractable | complete arbitrary-function optimizer correspondence unless economical to encode | protect quantifier/generality repair |
| P4 | `F'`, `F''`, endpoint signs, `H` monotonicity, threshold existence/uniqueness, endpoint-slope regime | full regulator argmax theorem unless differentiation/objective linkage is encoded | highest-value threshold certification |
| W1/P5R | welfare identities, positive welfare multiplier, Bertrand gap | unrestricted planner problem, which the paper does not claim | protect benchmark taxonomy and welfare algebra |

The repository now contains later Lean work covering substantial portions of this target map, but under the latest workflow the final `FORMAL VERIFICATION PASS` decision remains a Stage-7.5A obligation and is not granted by this Stage-4A certificate.

## Overall certificate verdict

Every current headline mathematical claim has an evidence-bearing certificate with no material `NOT TESTED` correctness field for its stated scope.

`GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`
