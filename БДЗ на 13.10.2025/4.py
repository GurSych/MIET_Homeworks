import sympy as sp

x = sp.Symbol('x')
f = (x-sp.sin(5*x))/(x+sp.sin(8*x))
a = sp.limit(f,x,0)
print(a)