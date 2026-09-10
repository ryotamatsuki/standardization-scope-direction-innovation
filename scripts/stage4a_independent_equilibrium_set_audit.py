import math
import numpy as np

# Retroactive Stage 4A independent adversarial certification.
# This implementation is deliberately separate from the production symbolic
# and numerical solvers. It reconstructs consumer KKT regimes directly and
# attacks candidate deviations, alternative pure price equilibria, zero-demand
# indifference, R&D globality/corners, policy-regime classification, and welfare.

SEED = 20260910
PARAMETER_DRAWS = 120
RANDOM_HISTORIES_PER_DRAW = 8
PRICE_GRID_SIZE = 4001
TOL = 1e-8


def rho_from_nu(nu):
    return (-1.0 + math.sqrt(1.0 + 8.0 * nu * nu)) / (2.0 * nu)


def g(r, kappa):
    return r - 0.5 * kappa * r * r


def quality_bounds(E, kappa, a, theta):
    y = kappa * E
    amin = a + theta * E * (1.0 - y / 2.0)
    amax = a + theta * E * (2.0 - 3.0 * y / 4.0)
    return amin, amax


def choose_a_for_R(E, kappa, theta, rho):
    y = kappa * E
    cmin = theta * E * (1.0 - y / 2.0)
    cmax = theta * E * (2.0 - 3.0 * y / 4.0)
    rhs = 2.0 / (rho * (3.0 - rho * rho))
    threshold = max(0.0, (cmax - rhs * cmin) / (rhs - 1.0))
    return 1.0 + 1.25 * threshold


def qualities(x1, x2, b, E, kappa, a, theta):
    return (
        a + theta * (g(x1, kappa) + b * g(x2, kappa) + g(E - x1, kappa)),
        a + theta * (g(x2, kappa) + b * g(x1, kappa) + g(E - x2, kappa)),
    )


def candidate_price(Ai, Aj, rho):
    return ((2.0 - rho * rho) * Ai - rho * Aj) / (4.0 - rho * rho)


def direct_quantity_i(price_grid, p_j, Ai, Aj, rho):
    """Direct consumer-KKT reconstruction for firm i over own-price values."""
    p_i = np.asarray(price_grid, dtype=float)
    vi = Ai - p_i
    vj = Aj - p_j
    den = 1.0 - rho * rho

    qi_both = (vi - rho * vj) / den
    qj_both = (vj - rho * vi) / den

    qi = np.zeros_like(p_i)
    both = (qi_both >= -1e-12) & (qj_both >= -1e-12)
    qi[both] = np.maximum(qi_both[both], 0.0)

    qi_only = np.maximum(vi, 0.0)
    rival_inactive = (~both) & (qi_only > 0.0) & (vj - rho * qi_only <= 1e-10)
    qi[rival_inactive] = qi_only[rival_inactive]

    remaining = ~(both | rival_inactive)
    qj_only = max(vj, 0.0)
    if np.any(vi[remaining] - rho * qj_only > 1e-8):
        raise RuntimeError("UNRESOLVED consumer KKT regime")

    return qi, both, rival_inactive, remaining


def x_private(b, E, kappa, nu):
    y = kappa * E
    return (y - nu * b) / (kappa * (2.0 - nu * b))


def private_objective(x, b, E, kappa, nu):
    return (1.0 - nu * b) * g(x, kappa) + g(E - x, kappa)


def x_coordinated(b, E, kappa):
    y = kappa * E
    return (y + b) / (kappa * (2.0 + b))


def H(y, nu):
    return (
        nu**3
        + 2.0 * nu**2 * y**2
        - 8.0 * nu**2 * y
        + 2.0 * nu**2
        + nu * y**2
        - 4.0 * nu * y
        + 16.0 * nu
        + 2.0 * y**2
        - 8.0 * y
    )


def reduced_F(b, y, nu):
    kappa = 1.0
    E = y
    x = x_private(b, E, kappa, nu)
    return (1.0 + b) * g(x, kappa) + g(E - x, kappa)


def threshold_root(y):
    lo, hi = 0.0, y
    flo, fhi = H(y, lo), H(y, hi)
    if not (flo < 0.0 < fhi):
        raise AssertionError("threshold endpoint signs fail")
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if H(y, mid) <= 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def audit_price_history(b, x1, x2, E, kappa, nu, rho, a, theta):
    A1, A2 = qualities(x1, x2, b, E, kappa, a, theta)
    Amin, Amax = quality_bounds(E, kappa, a, theta)
    if not (Amin - TOL <= A1 <= Amax + TOL and Amin - TOL <= A2 <= Amax + TOL):
        raise AssertionError("quality bound violation")

    for Ai, Aj in ((A1, A2), (A2, A1)):
        # D2/D3 prerequisite: any zero-demand action can profitably re-enter
        # because Ai > rho Aj, independently of the rival's nonnegative price.
        if not Ai > rho * Aj:
            raise AssertionError("inactive-product re-entry inequality fails")

        p_i = candidate_price(Ai, Aj, rho)
        p_j = candidate_price(Aj, Ai, rho)
        if not p_i > 0.0:
            raise AssertionError("candidate price is nonpositive")

        qeq, both, _, _ = direct_quantity_i(np.array([p_i]), p_j, Ai, Aj, rho)
        if not bool(both[0]) or not qeq[0] > 0.0:
            raise AssertionError("candidate is not strictly active")
        eq_profit = p_i * qeq[0]

        # D1 global finite-deviation attack across all consumer KKT regimes.
        grid = np.linspace(0.0, 2.0 * max(Ai, Aj), PRICE_GRID_SIZE)
        qi, _, rival_inactive, own_inactive = direct_quantity_i(grid, p_j, Ai, Aj, rho)
        profits = grid * qi
        if float(np.max(profits)) > eq_profit + 2e-5:
            raise AssertionError("profitable finite price deviation")
        if np.any(rival_inactive):
            raise AssertionError("nonnegative foreclosure deviation reachable under (R)")
        if not np.any(own_inactive):
            raise AssertionError("own-inactive regime was not reached")

        # D3 zero-profit indifference stress. Force i inactive, recompute a
        # numerical rival best response, and verify profitable positive re-entry.
        p_high = 2.0 * max(Ai, Aj)
        q_high, _, _, _ = direct_quantity_i(np.array([p_high]), p_j, Ai, Aj, rho)
        if q_high[0] > TOL:
            raise AssertionError("high-price zero-demand trigger not reached")
        rival_grid = np.linspace(0.0, 2.0 * max(Ai, Aj), PRICE_GRID_SIZE)
        qj, _, _, _ = direct_quantity_i(rival_grid, p_high, Aj, Ai, rho)
        jprofits = rival_grid * qj
        p_j_br = float(rival_grid[int(np.argmax(jprofits))])
        reentry_cap = Ai - rho * (Aj - p_j_br)
        if not reentry_cap > 0.0:
            raise AssertionError("zero-demand action could survive as equilibrium")
        p_reenter = 0.5 * reentry_cap
        q_reenter, _, _, _ = direct_quantity_i(np.array([p_reenter]), p_j_br, Ai, Aj, rho)
        if not p_reenter * q_reenter[0] > 0.0:
            raise AssertionError("positive re-entry profit not found")


def audit_parameter_draw(y, nu, theta, rng):
    kappa = 1.0
    E = y
    rho = rho_from_nu(nu)
    a = choose_a_for_R(E, kappa, theta, rho)
    Amin, Amax = quality_bounds(E, kappa, a, theta)
    Rrhs = 2.0 / (rho * (3.0 - rho * rho))
    if not (0.0 < rho < 1.0 and 0.0 < nu < y < 1.0):
        raise AssertionError("parameter-domain failure")
    if not Amax / Amin < Rrhs:
        raise AssertionError("(R) construction failure")

    histories = [
        (0.0, 0.0, 0.0),
        (0.0, 0.0, E),
        (0.0, E, 0.0),
        (0.0, E, E),
        (1.0, 0.0, 0.0),
        (1.0, 0.0, E),
        (1.0, E, 0.0),
        (1.0, E, E),
        (1.0, 0.5 * E, 0.5 * E),
    ]
    histories.extend(
        (float(rng.random()), float(E * rng.random()), float(E * rng.random()))
        for _ in range(RANDOM_HISTORIES_PER_DRAW)
    )
    for hist in histories:
        audit_price_history(*hist, E, kappa, nu, rho, a, theta)

    # R&D globality/corners: exact interior solution versus full [0,E] grid.
    xgrid = np.linspace(0.0, E, 5001)
    for scope in (0.0, 1e-8, 0.25, 0.75, 1.0 - 1e-8, 1.0):
        xp = x_private(scope, E, kappa, nu)
        if not (0.0 < xp < E):
            raise AssertionError("private R&D optimum hit an unreported corner")
        vals = private_objective(xgrid, scope, E, kappa, nu)
        x_num = float(xgrid[int(np.argmax(vals))])
        if abs(x_num - xp) > E / 2000.0:
            raise AssertionError("private R&D global argmax mismatch")

        xs = x_coordinated(scope, E, kappa)
        if not (0.0 < xs < E):
            raise AssertionError("coordinated R&D optimum hit an unreported corner")

    # P4 global policy attack.
    bar = threshold_root(y)
    bgrid = np.linspace(0.0, 1.0, 10001)
    Fvals = np.array([reduced_F(float(bb), y, nu) for bb in bgrid])
    bnum = float(bgrid[int(np.argmax(Fvals))])
    if nu <= bar:
        if abs(bnum - 1.0) > 1e-4:
            raise AssertionError("complete-scope regime mismatch")
    else:
        if not (1e-4 < bnum < 1.0 - 1e-4):
            raise AssertionError("interior-scope regime mismatch")

    # Welfare identity stress at the implied rho.
    A = a + theta * E
    p = A * (1.0 - rho) / (2.0 - rho)
    q = A / ((2.0 - rho) * (1.0 + rho))
    cs_direct = 2.0 * A * q - (1.0 + rho) * q * q - 2.0 * p * q
    cs_formula = A * A / ((2.0 - rho) ** 2 * (1.0 + rho))
    ps_direct = 2.0 * p * q
    ps_formula = 2.0 * A * A * (1.0 - rho) / ((2.0 - rho) ** 2 * (1.0 + rho))
    if not (
        math.isclose(cs_direct, cs_formula, rel_tol=1e-10, abs_tol=1e-8)
        and math.isclose(ps_direct, ps_formula, rel_tol=1e-10, abs_tol=1e-8)
    ):
        raise AssertionError("welfare accounting mismatch")

    return len(histories)


def main():
    rng = np.random.default_rng(SEED)
    total_histories = 0
    total_player_histories = 0

    # Canonical example first.
    h = audit_parameter_draw(0.7, 0.5, 0.2, rng)
    total_histories += h
    total_player_histories += 2 * h

    # Near-boundary and threshold attacks.
    fixed = [
        (0.5001, 0.0001, 0.2),
        (0.5001, 0.4999, 0.2),
        (0.9990, 0.0001, 0.2),
        (0.9990, 0.9980, 0.2),
        (0.7000, 0.358728592519, 0.2),
    ]
    for yy, nn, tt in fixed:
        h = audit_parameter_draw(yy, nn, tt, rng)
        total_histories += h
        total_player_histories += 2 * h

    for _ in range(PARAMETER_DRAWS):
        yy = float(rng.uniform(0.5001, 0.999))
        nn = float(rng.uniform(0.0001, 0.999 * yy))
        tt = float(rng.uniform(0.05, 1.0))
        h = audit_parameter_draw(yy, nn, tt, rng)
        total_histories += h
        total_player_histories += 2 * h

    print(
        "STAGE4A_RETRO_AUDIT: PASS; "
        f"parameter_sets={PARAMETER_DRAWS + 6}; "
        f"histories={total_histories}; player_histories={total_player_histories}; "
        "unresolved=0; profitable_price_deviations=0; "
        "alternative_pure_price_equilibria=0; "
        "rd_corner_failures=0; policy_regime_failures=0; welfare_failures=0"
    )


if __name__ == "__main__":
    main()
