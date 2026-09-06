# Historical Canonical Theory Freeze — v1

Freeze ID: `SSDI-THEORY-FREEZE-2026-09-06-v1`

Status: **SUPERSEDED by `SSDI-THEORY-FREEZE-2026-09-06-v2` after the post-Stage-10 hostile audit and Stage 7R/7.5R repair.**

This file preserves the original v1 freeze verbatim for auditability. It is not the active theory specification.

## Frozen game

1. Regulator chooses `b in [0,1]`.
2. Firms choose `x_i in [0,E]`, with `z_i = E-x_i`.
3. Firms choose `p_i >= 0`.

Innovation technology:
`g(r) = r - kappa*r^2/2`.

Quality:
`A_i = a + theta [ g(x_i) + b g(x_j) + g(E-x_i) ]`.

Consumers:
`U = A_1 q_1 + A_2 q_2 - (q_1^2+q_2^2)/2 - rho q_1 q_2`.

Definitions:
`y = kappa E`,
`nu = rho/(2-rho^2)`.

Main region:
`1/2 < y < 1`,
`0 < nu < y`,
plus the all-history price regularity condition recorded in Stage 8.

## Original headline result

For fixed positive common R&D, and under the first best, complete standardization is optimal. With decentralized endogenous R&D allocation, there is a threshold `bar_nu(y)` such that sufficiently strong rivalry yields a unique interior standardization scope.

## Supersession note

The post-Stage-10 hostile audit established that the phrase `under the first best` was not supported by the solved benchmark, which retained decentralized Bertrand pricing and imposed symmetric R&D control. It also found over-broad general-technology and robustness claims. Those defects were repaired in Stage 7R and Stage 7.5R. The baseline quadratic game and selective-standardization theorem survived.

No downstream work may use this v1 file as the active freeze after the v2 freeze is issued.
