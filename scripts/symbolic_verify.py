import sympy as sp

b, y, nu, kappa = sp.symbols("b y nu kappa", positive=True)
rho, Ai, Aj = sp.symbols("rho Ai Aj", positive=True)

E = y/kappa
x = (y - nu*b)/(kappa*(2-nu*b))
g = lambda r: r - kappa*r**2/2

assert sp.simplify((1-nu*b)*(1-kappa*x) - (1-kappa*(E-x))) == 0

xb = sp.factor(sp.diff(x,b))
assert sp.simplify(xb + nu*(2-y)/(kappa*(2-nu*b)**2)) == 0

xs = (y+b)/(kappa*(2+b))
assert sp.simplify((1+b)*(1-kappa*xs) - (1-kappa*(E-xs))) == 0
assert sp.simplify(sp.diff(xs,b) - (2-y)/(kappa*(2+b)**2)) == 0

F = sp.simplify(kappa*((1+b)*g(x) + g(E-x)))
Fpp_expected = -nu*(y-2)**2*(2*b*nu**2+b*nu+2*nu+4)/(2-b*nu)**4
assert sp.simplify(sp.diff(F,b,2) - Fpp_expected) == 0

Fp0_expected = y*(4-y)/8
assert sp.simplify(sp.diff(F,b).subs(b,0) - Fp0_expected) == 0

H = (
    nu**3 + 2*nu**2*y**2 - 8*nu**2*y + 2*nu**2
    + nu*y**2 - 4*nu*y + 16*nu + 2*y**2 - 8*y
)
Fp1 = sp.factor(sp.diff(F,b).subs(b,1))
assert sp.simplify(Fp1 - H/(2*(nu-2)**3)) == 0
assert sp.factor(H.subs(nu,y)) == 2*y*(y-2)**2*(y+1)
assert sp.factor(H.subs(nu,0)) == 2*y*(y-4)

p_i = ((2-rho**2)*Ai-rho*Aj)/(4-rho**2)
p_j = ((2-rho**2)*Aj-rho*Ai)/(4-rho**2)
assert sp.simplify(2*p_i-rho*p_j-(Ai-rho*Aj)) == 0

profit = p_i**2/(1-rho**2)
profit_expected = (((2-rho**2)*Ai-rho*Aj)**2)/((4-rho**2)**2*(1-rho**2))
assert sp.simplify(profit-profit_expected) == 0

print("SYMBOLIC_VERIFY: PASS")
