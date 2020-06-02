import numpy as np

random_arr = np.random.random(size=1000)
mean = np.mean(random_arr)
standard_deviation = np.std(random_arr)
print(mean, standard_deviation)

other_arr = np.random.normal(size=1000)
mean = np.mean(other_arr)
standard_deviation = np.std(other_arr)
print(mean, standard_deviation)
