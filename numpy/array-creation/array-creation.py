#!/env/bin/python

import numpy as np

# Start from a Python list containing both integers and floating point values, and construct then a NumPy array from the list.
my_list = [1, 3.2, 4]
my_array = np.array(my_list)

# Generate a 1D NumPy array containing all numbers from -2.0 to 2.0 with a spacing of 0.2. Use optional start and step arguments of the np.arange() function.
my_1D_arr = np.arange(-2, 2, 0.2)

# Generate another 1D NumPy array containing 11 equally spaced values between 0.5 and 1.5.
my_other_1D_arr = np.linspace(0.5, 1.5, 11)

# Take some Python string and construct from it NumPy array consisting of single characters (a character array).
my_string_arr = np.array('my_string_arr')

print(my_array, my_1D_arr, my_other_1D_arr, my_string_arr)
