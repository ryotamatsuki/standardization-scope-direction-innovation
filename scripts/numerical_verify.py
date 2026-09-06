import math
import numpy as np

def g(r, kappa): return r - 0.5*kappa*r*r

def x_private(b, E, kappa, nu):
    y = kappa*E
    return (y-nu*b)/(kappa*(2-nu*b))

def quality_component(b, E, kappa, nu):
    x = x_private(b,E,kappa,nu)
    return (1+b)*g(x,kappa) + g(E-x,kappa)

def profit_price(p_i, p_j, A_i, A_j, rho):
    if p_i < 0 or p_j < 0: return -math.inf
    qi = (A_i-p_i-rho*(A_j-p_j))/(1-rho*rho)
    qj = (A_j-p_j-rho*(A_i-p_i))/(1-rho*rho)
    if qi >= 0 and qj >= 0: return p_i*qi
    if qj < 0: return p_i*max(A_i-p_i,0.0)
    return 0.0

E=0.7; kappa=1.0; nu=0.5; rho=math.sqrt(3)-1; a=10.0; theta=0.2
bs=np.linspace(0,1,20001)
vals=np.array([quality_component(b,E,kappa,nu) for b in bs])
b_star=float(bs[int(vals.argmax())])
assert 0.65 < b_star < 0.72
for b in [0.0,0.25,b_star,1.0]:
    x_star=x_private(b,E,kappa,nu)
    xs=np.linspace(0,E,20001)
    obj=(1-nu*b)*np.array([g(x,kappa) for x in xs])+np.array([g(E-x,kappa) for x in xs])
    assert abs(float(xs[int(obj.argmax())])-x_star) < 1e-4
for b in [0.0,b_star,1.0]:
    x=x_private(b,E,kappa,nu)
    A=a+theta*((1+b)*g(x,kappa)+g(E-x,kappa))
    p=A*(1-rho)/(2-rho)
    base=profit_price(p,p,A,A,rho)
    grid=np.linspace(0,1.8*A,30001)
    best=max(profit_price(float(pp),p,A,A,rho) for pp in grid)
    assert best <= base + 2e-5
print(f"NUMERICAL_VERIFY: PASS; canonical b*≈{b_star:.5f}")
