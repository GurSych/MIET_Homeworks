import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,1000)
y = 1/(np.exp(x**2-1))
plt.plot(x,y,'.',color='DarkOrchid')
plt.show()