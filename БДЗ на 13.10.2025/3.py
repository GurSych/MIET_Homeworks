import sympy as sp

x = sp.Symbol('x')
f = (x**2+x**3)/((1+6*x)**(1/3)-1-2*x)
a = sp.limit(f,x,0)
print(a)