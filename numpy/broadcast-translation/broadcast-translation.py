import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('points_circle.dat')
plt.plot(data[:,0], data[:,1], 'o')

new_data = data + np.array([2.1, 1.1])
plt.plot(new_data[:,0], new_data[:,1], 'x')

plt.show()
