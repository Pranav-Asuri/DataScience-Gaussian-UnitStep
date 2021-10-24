from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(-10,10,0.1)
y = norm.pdf(x)
for i in range(len(x)):
    if x[i]<0:
        y[i]=0

plt.plot(x, y)

plt.show()
