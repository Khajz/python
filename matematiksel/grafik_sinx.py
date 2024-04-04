import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-2*(np.pi), 2*(np.pi), 0.3)
y = np.sin(x)/x
plt.plot(x, y)
plt.grid()
plt.show()
