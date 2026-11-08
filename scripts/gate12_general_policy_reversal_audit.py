#!/usr/bin/env python3
"""SSDI independent Gate 2 regression audit (2026-11-08).
Requires numpy, scipy and sympy. Research branch only; not a certified theorem.
"""
from math import exp,log,sqrt
import numpy as np
import sympy as s
from scipy.optimize import brentq,minimize_scalar

g_log=lambda x:log(1+3*x)/3
g_exp=lambda x:(1-exp(-3*x))/3
g_sqrt=lambda x:sqrt(1+x)-1
g_quad=lambda x:x-.35*x*x
tech={"log":g_log,"exp":g_exp,"sqrt":g_sqrt,"quadratic":g_quad}
def xprivate(b,nu,k):
 t=nu*b
 candidates={
  "log":(3-4*t)/(3*(2-t)),
  "exp":(1+log(1-t)/3)/2,
  "sqrt":(2*(1-t)**2-1)/(1+(1-t)**2),
  "quadratic":(.7-t)/(.7*(2-t))
 }
 return min(1,max(0,candidates[k]))
def Q(b,nu,k):
 x=xprivate(b,nu,k)
 return (1+b)*tech[k](x)+tech[k](1-x)

b,n=s.symbols("b n",real=True)
x=(3-4*n*b)/(3*(2-n*b))
logtech=lambda x:s.log(1+3*x)/3
expr=s.simplify((1+b)*logtech(x)+logtech(1-x))
d2=s.factor(s.diff(expr,b,2))
formula=n*(b*b*n**3+3*b*n-2*n-4)/(3*(2-b*n)**2*(1-b*n)**2)
assert s.simplify(d2-formula)==0
slope1=(s.log(5*(1-n)/(2-n))-n*(1+n)/((2-n)*(1-n)))/3
assert s.simplify(s.diff(expr,b).subs(b,1)-slope1)==0
root=brentq(s.lambdify(n,slope1,"numpy"),.01,.749,xtol=1e-14)
assert abs(root-.410410971694386)<1e-12
f2=s.lambdify((b,n),d2,"numpy")
assert all(f2(beta,nu)<0 for nu in [.01,.2,.4,.5,.7,.749] for beta in np.linspace(0,1,201))
nu=.7
opt=minimize_scalar(lambda beta:-Q(beta,nu,"log"),bounds=(0,1),method="bounded",options={"xatol":1e-14})
assert abs(opt.x-.544863935215696)<1e-7
assert Q(opt.x,nu,"log")>Q(0,nu,"log") and Q(opt.x,nu,"log")>Q(1,nu,"log")
rho=brentq(lambda r:r/(2-r*r)-nu,1e-10,1-1e-10)
a,theta=10,.2
ratio=(a+theta*(2*g_log(.5)+g_log(1)))/(a+theta*g_log(1))
cap=2/(rho*(3-rho*rho))
assert ratio<cap
# Global mesh, not single bounded optimization, because corner allocations create flat boundary ranges.
for k in tech:
 for nu in [.9,.99]:
  grid=np.linspace(0,1,2001)
  vals=np.array([Q(float(bb),nu,k) for bb in grid])
  assert 0<int(np.argmax(vals))<len(grid)-1, (k,nu)
  assert Q(0,nu,k)>Q(1,nu,k)
  assert np.max(vals)>Q(0,nu,k)
# g(0)>0 destroys the claimed universal high-rivalry conclusion.
assert Q(1,.99,"log")+30>Q(0,.99,"log")+20
print("PASS: Gate 2 independent symbolic and numerical audit")
print("log threshold nu*:",root)
print("log nu=.7: b*:",opt.x,"Q*:",Q(opt.x,.7,"log"))
print("R bound ratio:",ratio,"R threshold:",cap)
