import math

def H(y, nu):
    return (nu**3 + 2*nu**2*y**2 - 8*nu**2*y + 2*nu**2 + nu*y**2 - 4*nu*y + 16*nu + 2*y**2 - 8*y)

def test_threshold_endpoints():
    for y in (0.55,0.7,0.9):
        assert H(y,0) < 0
        assert H(y,y) > 0

def test_private_allocation_is_interior_on_canonical_example():
    E,kappa,nu=0.7,1.0,0.5
    y=E*kappa
    for b in (0.0,0.25,0.5,0.75,1.0):
        x=(y-nu*b)/(kappa*(2-nu*b))
        assert 0 < x < E

def test_nu_mapping():
    rho=math.sqrt(3)-1
    nu=rho/(2-rho*rho)
    assert abs(nu-0.5) < 1e-12
