import numpy as np

np.set_printoptions(legacy='1.13')  # This is to comply with HackerRank's output format.

# Read the array from input
A = np.array(input().split(), float)

# Perform and print the floor, ceil, and rint operations
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
