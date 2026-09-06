import math
import numpy as np

# Stage 11R independent continuation audit.
# This script reconstructs consumer allocation directly from KKT regimes and
# never calls the manuscript's numerical equilibrium/deviation evaluator.

E = 0.7
KAPPA = 1.0
Y = KAPPA * E
NU = 0.5
RHO = math.sqrt(3.0) - 1.0
A0 = 10.0
THETA = 0.2


def g(r):
    return r - 0.5 * KAPPA * r * r


def qualities(x1, x2, b):
    return (
        A0 + THETA * (g(x1) + b * g(x2) + g(E - x1)),
        A0 + THETA * (g(x2) + b * g(x1) + g(E - x2)),
    )


def candidate_price(Ai, Aj):
    return ((2.0 - RHO * RHO) * Ai - RHO * Aj) / (4.0 - RHO * RHO)


def direct_quantity_i(price_grid, p_j, Ai, Aj):
    """Consumer KKT reconstruction for q_i over a vector of own prices."""
    p_i = np.asarray(price_grid, dtype=float)
    vi = Ai - p_i
    vj = Aj - p_j
    den = 1.0 - RHO * RHO

    q_i_both = (vi - RHO * vj) / den
    q_j_both = (vj - RHO * vi) / den

    q_i = np.zeros_like(p_i)
    both = (q_i_both >= 0.0) & (q_j_both >= 0.0)
    q_i[both] = q_i_both[both]

    # Rival inactive: consumer buys only i if its one-product allocation
    # satisfies rival's complementary-slackness condition.
    qi_only = np.maximum(vi, 0.0)
    rival_inactive = (~both) & (qi_only > 0.0) & (vj - RHO * qi_only <= 1e-12)
    q_i[rival_inactive] = qi_only[rival_inactive]

    # Remaining profiles either leave i inactive or are numerical boundary
    # points. Verify every remaining point satisfies i's inactivity KKT.
    remaining = ~(both | rival_inactive)
    qj_only = max(vj, 0.0)
    inactivity_slack = vi[remaining] - RHO * qj_only
    if np.any(inactivity_slack > 1e-9):
        raise RuntimeError("UNRESOLVED consumer KKT regime")

    return q_i, both, rival_inactive, remaining


def audit_history(b, x1, x2):
    A1, A2 = qualities(x1, x2, b)
    p1 = candidate_price(A1, A2)
    p2 = candidate_price(A2, A1)
    if not (p1 > 0.0 and p2 > 0.0):
        raise AssertionError("candidate price is not positive")

    outcomes = []
    for Ai, Aj, p_i, p_j in ((A1, A2, p1, p2), (A2, A1, p2, p1)):
        # Direct KKT quantity at the candidate profile.
        q_eq, both_eq, _, _ = direct_quantity_i(np.array([p_i]), p_j, Ai, Aj)
        if not bool(both_eq[0]) or not (q_eq[0] > 0.0):
            raise AssertionError("candidate profile is not active-product")
        eq_profit = p_i * q_eq[0]

        # Large finite deviation search: includes p=0 and prices high enough
        # to force the deviator itself inactive, so it exits the regular branch.
        grid = np.linspace(0.0, 2.0 * max(Ai, Aj), 10001)
        qi, both, rival_inactive, own_inactive = direct_quantity_i(grid, p_j, Ai, Aj)
        profits = grid * qi
        best_grid_profit = float(np.max(profits))
        if best_grid_profit > eq_profit + 1e-8:
            raise AssertionError("profitable finite price deviation found")

        # Under condition (R), a nonnegative deviation against the candidate
        # continuation cannot foreclose the rival.
        if np.any(rival_inactive):
            raise AssertionError("foreclosure deviation found under (R)")
        if not np.any(own_inactive):
            raise AssertionError("large-deviation inactive regime not reached")

        outcomes.append((eq_profit, best_grid_profit, int(np.sum(own_inactive))))
    return outcomes


def main():
    A_min = A0 + THETA * E * (1.0 - Y / 2.0)
    A_max = A0 + THETA * E * (2.0 - 3.0 * Y / 4.0)
    R_rhs = 2.0 / (RHO * (3.0 - RHO * RHO))
    assert A_max / A_min < R_rhs
    assert 0.0 < NU < Y < 1.0

    # Adversarial boundary histories plus deterministic random histories.
    histories = [
        (b, x1, x2)
        for b in (0.0, 1.0)
        for x1 in (0.0, E)
        for x2 in (0.0, E)
    ]
    # Explicit asymmetric history used in the Stage-11 report.
    histories.append((1.0, 0.0, E))
    rng = np.random.default_rng(20260906)
    histories.extend(
        (float(rng.random()), float(E * rng.random()), float(E * rng.random()))
        for _ in range(64)
    )

    unresolved = 0
    failures = 0
    for history in histories:
        try:
            audit_history(*history)
        except RuntimeError:
            unresolved += 1
        except AssertionError:
            failures += 1

    assert unresolved == 0, f"UNRESOLVED continuations: {unresolved}"
    assert failures == 0, f"continuation failures: {failures}"

    # Report the explicit adversarial history numerically.
    A1, A2 = qualities(0.0, E, 1.0)
    p1 = candidate_price(A1, A2)
    p2 = candidate_price(A2, A1)
    q1, _, _, _ = direct_quantity_i(np.array([p1]), p2, A1, A2)
    q2, _, _, _ = direct_quantity_i(np.array([p2]), p1, A2, A1)
    print(
        "STAGE11_CONTINUATION_AUDIT: PASS; "
        f"histories={len(histories)}; unresolved=0; failures=0; "
        f"adversarial A=({A1:.6f},{A2:.6f}); "
        f"p*=({p1:.6f},{p2:.6f}); q*=({q1[0]:.6f},{q2[0]:.6f})"
    )


if __name__ == "__main__":
    main()
