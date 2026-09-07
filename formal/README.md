# Lean formal verification

This directory adds an independent Lean 4 + mathlib verification layer for the active theory freeze `SSDI-THEORY-FREEZE-2026-09-06-v3`.

It is deliberately separate from the Python/SymPy verification stack and from the LaTeX submission build. The Lean code is a verification aid; it does not modify the frozen model or expand the paper's claims.

## Toolchain

- Lean: `v4.32.1`
- mathlib: `v4.32.1`
- project root: `formal/`

Build locally from this directory with:

```bash
lake update
lake exe cache get
lake build
```

## Formalized claims

All current Lean proofs compile without `sorry`.

### `SSDI/Core.lean`

1. `0 < rho < 1` implies `0 < nu(rho) < 1` for `nu = rho/(2-rho^2)`.
2. The closed-form private allocation satisfies the exact two-policy difference identity and is strictly decreasing in scope on its interior domain.
3. The paper's quadratic derivative expression for private common-layer R&D is strictly negative on its interior domain.
4. The coordinated symmetric quadratic allocation satisfies the exact difference identity and is strictly increasing in scope.
5. The threshold polynomial identities `H(y,0)=2y(y-4)` and `H(y,y)=2y(y-2)^2(y+1)`.
6. The endpoint signs used in the selective-standardization proof.
7. The algebraic lower bound `H_nu > 5(y-2)^2`, hence `H_nu>0`, on the frozen region `1/2<y<1` and `0<nu<y`.
8. Positivity of the symmetric-Bertrand welfare multiplier and strict positivity of the Bertrand quantity-control welfare gap for nonzero symmetric quality.

### `SSDI/Threshold.lean`

9. Exact two-point factorization of `H(y,nu2)-H(y,nu1)`.
10. Strict positivity of the secant factor on `0 <= nu1 < nu2 <= y < 1` in the frozen region.
11. Strict monotonicity of `H(y,nu)` in `nu` on `[0,y]`.
12. By continuity and the endpoint signs, existence of a root `bar_nu(y)` strictly inside `(0,y)`.
13. Uniqueness of that root, yielding `exists_unique_threshold_root`.
14. Exact sign classification: `H(y,nu) <= 0` at/below the threshold and `H(y,nu) > 0` above it.

### `SSDI/PolicySigns.lean`

15. Positivity of the paper's `F'(0)` expression.
16. Negativity of the paper's `F''(b)` expression on `b in [0,1]` under the frozen quadratic restrictions.
17. Positivity of the denominator in the complete-scope endpoint expression `F'(1)=-H/[2(2-nu)^3]`.
18. The complete-scope endpoint slope is nonnegative at/below the unique rivalry threshold and strictly negative above it.
19. The corresponding iff characterizations of the endpoint-slope regime.

## Not yet formalized

The current Lean layer does **not** yet claim a complete machine proof of the paper. The main remaining targets are:

- connect the reported `F'`/`F''` expressions to the actual normalized policy objective by formal differentiation, then close the full regulator argmax theorem `b*=1` versus a unique interior optimum;
- global price-continuation uniqueness at every feasible upstream history;
- the full general-technology P2R revealed-preference theorem with arbitrary differentiable, increasing, strictly concave `g` and corner solutions;
- the complete subgame-perfect equilibrium construction.

The next priority is the formal differentiation plus regulator argmax layer, because the threshold existence/uniqueness and policy-sign architecture of P4 are now machine checked.
