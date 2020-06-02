import numpy as np
import math
import matplotlib.pyplot as plt

dxi = 0.1
xi = np.arange(0, math.pi / 2, 0.1)
fxi = np.sin(xi)
derivative = (fxi[2:] - fxi[:-2]) / (2 * dxi)
cosine = np.cos(xi)
print(derivative)
print(cosine)

f_ref = np.cos(xi[1:-1])
print("Mean squared difference:")
print(np.sqrt(np.sum((derivative - f_ref)**2)))
plt.plot(xi[1:-1], derivative, label="sin'")
plt.plot(xi[1:-1], f_ref, label="cos")
plt.legend()
plt.show()
