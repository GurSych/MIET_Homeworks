import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

n = sp.Symbol('n')
f = (3*(n**3)-1)/(5*(n**3)+(n**4)-6)
a = sp.limit(f,n,sp.oo)
print(a)
b = sp.solve_univariate_inequality(sp.Abs(f-a)<.0001,n,relational=False)
c = sp.solve_univariate_inequality(n > 0,n,relational=False)
d = sp.Intersection(b,c)
sp.pprint(d)
print(3/.0001)

n = np.linspace(1,100,1000)
y = (3*(n**3)-1)/(5*(n**3)+(n**4)-6)
plt.plot(n,y,'.',color='DarkOrchid')
plt.show()