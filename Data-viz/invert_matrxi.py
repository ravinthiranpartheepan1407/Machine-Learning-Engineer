# Write a NumPy program to create a 3x3 identity matrix, then invert it and multiply it by itself. The result should be the original identity matrix.

# Breakdown:
# 1. Create a 3x3 Matrix
# 2. Invert the 3x3 Matrix
# 3. Product of Orginal and Inverted matrix
# 4. Make sure the product matrix is eq to orginal matrix

import numpy as np
matrix = np.zeros(9, dtype=int).reshape(3,3)
np.fill_diagonal(matrix[0:], [1,1,1])

invert_matrix = np.invert(matrix)
np.fill_diagonal(invert_matrix[0:], [1,1,1])

product = matrix * invert_matrix
print(product)

# Approach 2:

matrix_A = np.identity(3, dtype=int) # Creates 1 diagonally
invert_matrix_A = np.linalg.inv(matrix_A) # Creates element ^ -1
product_A = np.dot(matrix_A,invert_matrix_A)

print(product_A)