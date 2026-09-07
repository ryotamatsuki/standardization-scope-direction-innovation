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

## Initial formalized claims

`SSDI/Core.lean` currently verifies, without `sorry`:

1. `0 < rho < 1` implies `0 < nu(rho) < 1` for `nu = rho/(2-rho^2)`.
2. The closed-form private allocation satisfies the exact two-policy difference identity and is strictly decreasing in scope on its interior domain.
3. The paper's quadratic derivative expression for private common-layer R&D is strictly negative on its interior domain.
4. The coordinated symmetric quadratic allocation satisfies the exact difference identity and is strictly increasing in scope.
5. The threshold polynomial identities `H(y,0)=2y(y-4)` and `H(y,y)=2y(y-2)^2(y+1)`.
6. The endpoint signs used in the selective-standardization proof.
7. The algebraic lower bound `H_nu > 5(y-2)^2`, hence `H_nu>0`, on the frozen region `1/2<y<1` and `0<nu<y`.
8. Positivity of the symmetric-Bertrand welfare multiplier and strict positivity of the Bertrand quantity-control welfare gap for nonzero symmetric quality.

## Not yet formalized

The first Lean layer does **not** yet claim a complete machine proof of the paper. In particular, the following remain analytic-manuscript results pending later formalization:

- global price-continuation uniqueness at every feasible upstream history;
- the full general-technology P2R revealed-preference theorem with arbitrary differentiable, increasing, strictly concave `g` and corner solutions;
- existence and uniqueness of `bar_nu(y)` via continuity/monotonicity;
- the full regulator optimization theorem mapping the sign of `F'(1)` into `b*=1` versus a unique interior optimum;
- the complete subgame-perfect equilibrium construction.

The intended progression is to formalize these in that order, while keeping the active economic theory freeze unchanged.
