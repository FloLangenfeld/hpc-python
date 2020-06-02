import numpy as np

my_mat = np.full((4, 4), 52.39)

sec_row = my_mat[1]
print(sec_row)

third_column = my_mat[:, 2]
print(third_column)

my_mat[:2, :2] = 0.21
print(my_mat)

chequerboard = np.zeros((8, 8))
chequerboard[::2, ::2] = 1
chequerboard[1::2, 1::2] = 1
print(chequerboard)
