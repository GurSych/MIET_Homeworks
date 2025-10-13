import sympy as sp

x = sp.Symbol('x')
f = ((sp.pi/2)-x)*sp.tan(x)
a = sp.limit(f,x,sp.pi/2)
print(a)