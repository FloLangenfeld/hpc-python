import numpy as np

A = np.random.random(size=(2, 2))
Asym = A + A.T
B = np.random.random(size=(2, 2))
B = B + B.T

C = np.dot(A, B)

D = np.linalign.eigvals(C)
