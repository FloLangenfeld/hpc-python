import numpy as np

data = np.loadtxt('xy-coordinates.dat')
data = data[:, 1] + 2.5
np.savetxt('new-xy-coordinates.dat', data)
