import numpy as np

dxi = 0.1
xi = np.arange(0, np.pi / 2, dxi)
xprimei = (xi[1:] + xi[:-1])/2
integral = np.sum(np.sin(xprimei) * dxi)
print(integral)
