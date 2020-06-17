import numpy as np

# Create a new random value matrix between 1-20 of size 20
print('Original matrix:')
matrix = np.random.uniform(low=1, high=20, size=20)
print(matrix)
print('\n')

# Reshape matrix to 4 X 5
print('Reshaped matrix:')
matrix = matrix.reshape(4, 5)
print(matrix)
print('\n')

