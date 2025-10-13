import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
y = 1/(np.exp(x**2-1))
x_r = 1
a1 = sp.limit(y,x,x_r,'-')
a2 = sp.limit(y,x,x_r,'+')
print(f"Является устранимой точкой разрыва при {x_r}:","да" if a1==a2 else "нет")
x_r = -1
a1 = sp.limit(y,x,x_r,'-')
a2 = sp.limit(y,x,x_r,'+')
print(f"Является устранимой точкой разрыва при {x_r}:","да" if a1==a2 else "нет")

x = np.linspace(-10,10,1000)
y = 1/(np.exp(x**2-1))
plt.plot(x,y,'.',color='DarkOrchid')
plt.show()