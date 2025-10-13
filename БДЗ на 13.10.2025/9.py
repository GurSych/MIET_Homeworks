import sympy as sp

x = sp.Symbol('x')
f = sp.sin(sp.sqrt(x**2+1))-sp.sin(sp.sqrt(x**2-1))
a = sp.limit(f,x,sp.oo)
print(a)