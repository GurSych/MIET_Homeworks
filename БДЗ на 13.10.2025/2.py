import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
f = ((1-x)**3-(1+3*x))/(x**3-x)
a = sp.limit(f,x,0)
print(a)
b = sp.solve_univariate_inequality(sp.Abs(f-a)<.0001,x,relational=False)
c = sp.solve_univariate_inequality(x > 0,x,relational=False)
d = sp.Intersection(b,c)
sp.pprint(d)

x = np.linspace(1,100,1000)
y = ((1-x)**3-(1+3*x))/(x**3-x)
plt.plot(x,y,'.',color='DarkOrchid')
plt.show()