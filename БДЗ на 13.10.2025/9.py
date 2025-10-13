import sympy as sp

x = sp.Symbol('x')
f = sp.sin((x**2+1)**(1/2))-sp.sin((x**2-1)**(1/2))
a = sp.limit(f,x,sp.oo)
print(a)