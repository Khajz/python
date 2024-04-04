#Lim (𝐭𝐚𝐧 𝟐𝐱)/𝟕𝐱 = ? 
#x -> 0
#0 noktasında 2/7=0,29
#bu grafik bunu gösteriyor

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-2*(np.pi), 2*(np.pi), 0.3)
y = np.tan(2*x)/(7*x)
plt.plot(x, y)
plt.grid()
plt.show()
