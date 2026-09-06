# Stage 7R2 — P2R Exact Monotonicity Repair

Date: 2026-09-06

Repository: `ryotamatsuki/standardization-scope-direction-innovation`

Starting main: `2198864d1d762d1d84823ec9083536e12f1530d6`

Workflow authority: `ryotamatsuki/research-paper-workflow` v1.3, release commit `3e4e6a3f76d86058024d06f9710f942e21627386`.

Rollback trigger: Stage 11 hostile referee audit.

## A. Exact diagnosis

The v2 general-technology P2R statement combined only differentiability, monotonicity, and strict concavity of `g` with a pointwise derivative claim `dx^F/db<0<dx^S/db` at interior optima. Its Appendix proof differentiated the FOCs and invoked `g''` although twice differentiability was not assumed. A strictly monotone optimizer can also have a zero derivative at isolated points, so strict order monotonicity does not by itself imply a pointwise strict derivative sign.

This defect does not affect the quadratic baseline, where the explicit formulas are differentiable and the derivative signs are analytically verified.

## B. Repaired theorem

For differentiable, increasing, strictly concave `g` on `[0,E]` and any `b_2>b_1`:

- `x^F(b_2) <= x^F(b_1)` globally;
- `x^S(b_2) >= x^S(b_1)` globally.

If both compared private optima are interior, then `x^F(b_2) < x^F(b_1)`.

If both compared coordinated symmetric optima are interior, then `x^S(b_2) > x^S(b_1)`.

No pointwise derivative sign is claimed for arbitrary general `g`.

## C. Proof architecture

For the private objective,

`f_F(x,b_2)-f_F(x,b_1)=-nu(b_2-b_1)g(x)`,

which is nonincreasing in `x`. Strict concavity gives a unique maximizer, and the revealed-preference/decreasing-differences argument yields the global weak order, including corners.

For the coordinated objective,

`f_S(x,b_2)-f_S(x,b_1)=(b_2-b_1)g(x)`,

which is nondecreasing in `x`, giving the opposite global weak order.

At an interior point, differentiability, monotonicity, and strict concavity imply `g'(x)>0`: if `g'(x_0)=0` at interior `x_0`, concavity and monotonicity force `g` to be constant on a nontrivial interval to the right, contradicting strict concavity. Equality of two interior optima at distinct policy values would then make the two FOCs inconsistent. Hence the order comparisons are strict when both compared optima are interior.

No `g''` is used.

## D. Theory-change record

Old statement: pointwise strict derivative signs at interior optima for arbitrary differentiable increasing strictly concave `g`.

New statement: global weak order comparative statics, with strict order inequalities when both compared optima are interior.

Assumptions: unchanged. No `C^2`, strong-concavity, Inada, or higher-order smoothness assumption is added.

Affected proposition: P2R only.

Unaffected: P1, P3R, P4, P5R, price continuation, welfare formulas, threshold polynomial, canonical numerical example, figure architecture, and contribution boundary.

New active freeze: `SSDI-THEORY-FREEZE-2026-09-06-v3`.

Historical v2: `docs/THEORY_FREEZE_v2.md`.

## E. Bounded Stage-11 clarifications

- Welfare decomposition: the endogenous composition term is zero at `b=0` and strictly negative for `b>0` in the quadratic interior baseline.
- Endogenous total R&D: the relative FOC is stated only for an extension in which common and proprietary effort face the same marginal total-capacity cost, such as `C(x+z)`.
- Literature: Bryan–Lemus (2017) is distinguished specifically on its trade-expansion/entry/research-race channel; Acemoglu–Gancia–Zilibotti (2012) is acknowledged as already containing constrained optimal standardization, so generic second-best restriction is not claimed as novel.

## F. Hostile kill tests

Regression tests include:

1. a highly concave exponential technology producing corner plateaus, confirming that global comparative statics may be weak;
2. a differentiable, strictly increasing, strictly concave technology with an interior non-`C^2` point, confirming that the order theorem does not rely on `g''`;
3. preservation of the quadratic P1 derivative and P4 threshold identities/checkpoints.

## G. Required verification before merge

The repair is not complete until the PR head passes:

- `make verify`;
- `make exposition`;
- citation/cross-reference regressions;
- `make paper`;
- full GitHub Actions CI.

The complete diff must show no accidental change to the quadratic baseline or Proposition 4.

## H. Routing

If all checks pass and the PR is merged:

`REPAIR COMPLETE — RETURN TO STAGE 11 RE-GATE`.

Do not proceed directly to Stage 12.
