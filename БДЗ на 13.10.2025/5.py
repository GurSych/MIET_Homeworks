import sympy as sp

x = sp.Symbol('x')
f = ((x**2+3)/(x**2+2*x-1))**(3*x+5)
a = sp.limit(f,x,sp.oo)
print(a)