import numpy as np

arr = np.random.rand(8, 8)
print(arr)
x1, x2 = np.split(arr, 2)
print(x1, x2)
new_arr = np.concatenate((x1, x2))
print(new_arr)
y = np.split(arr, 2, axis=1)
print(y)
new_new_arr = np.concatenate(y, axis=1)
print(new_new_arr)
