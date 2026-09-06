import math
import numpy as np


def argmax_grid(objective, E, n=60001):
    xs = np.linspace(0.0, E, n)
    vals = np.array([objective(float(x)) for x in xs])
    return float(xs[int(vals.argmax())])


def test_corner_plateaus_are_allowed_by_global_order_theorem():
    E = 0.7
    nu = 0.5

    def g(r):
        return 10.0 * (1.0 - math.exp(-r / 10.0))

    def private_x(b):
        return argmax_grid(lambda x: (1.0 - nu * b) * g(x) + g(E - x), E)

    def coordinated_x(b):
        return argmax_grid(lambda x: (1.0 + b) * g(x) + g(E - x), E)

    # This technology produces corner plateaus: private effort sticks at zero,
    # while coordinated effort sticks at E over high-scope ranges.
    p20, p40 = private_x(0.2), private_x(0.4)
    s20, s40 = coordinated_x(0.2), coordinated_x(0.4)
    assert p20 < 2e-5 and p40 < 2e-5
    assert abs(s20 - E) < 2e-5 and abs(s40 - E) < 2e-5
    assert p40 <= p20 + 2e-5
    assert s40 + 2e-5 >= s20


def test_ordering_does_not_require_twice_differentiable_technology():
    E = 0.7
    nu = 0.5
    a = 0.35
    eps = 0.2

    # g is differentiable, strictly increasing and strictly concave on [0,E],
    # but is not twice differentiable at r=a because of the |r-a|^(3/2) term.
    def g(r):
        return r - eps * abs(r - a) ** 1.5

    def private_x(b):
        return argmax_grid(lambda x: (1.0 - nu * b) * g(x) + g(E - x), E)

    def coordinated_x(b):
        return argmax_grid(lambda x: (1.0 + b) * g(x) + g(E - x), E)

    bs = [0.0, 0.15, 0.30, 0.45]
    private = [private_x(b) for b in bs]
    coordinated = [coordinated_x(b) for b in bs]

    for left, right in zip(private, private[1:]):
        assert right <= left + 2e-5
    for left, right in zip(coordinated, coordinated[1:]):
        assert right + 2e-5 >= left

    # These grid solutions are interior and display strict order separation.
    assert all(1e-4 < x < E - 1e-4 for x in private)
    assert all(1e-4 < x < E - 1e-4 for x in coordinated)
    for left, right in zip(private, private[1:]):
        assert right < left - 2e-5
    for left, right in zip(coordinated, coordinated[1:]):
        assert right > left + 2e-5
