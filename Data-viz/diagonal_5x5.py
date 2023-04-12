# Write a NumPy program to create a 5x5 matrix with values 1, 2, 3, 4 just below the diagonal and 0 elsewhere.

# Breakdown:

# 1. Create a 5x5 numpy array
# 2. Create values in a list
# 3. Iterate through 5x5 and increment rows and columsn by 1
# 4. print the result

import numpy as np
#ufunc
diag_5x5 = np.zeros(25, dtype=int).reshape(5,5)
np.fill_diagonal(diag_5x5[1:], [1,2,3,4])
print(diag_5x5)

# matrix = []

# def diagnoal_5x5_matrix(diag_5x5, value):
#     for values in range(len(diag_5x5)):
#         for rows in range(0, len(diag_5x5)):
#             for columns in range(1, len(diag_5x5)):
#                 if rows == columns:
#                     print(diag_5x5[rows][columns])
#                     diag_5x5[rows][columns] = value[0:]
#                     continue
#                 else:
#                     print(0)
#                     matrix.append(diag_5x5[rows][columns])
#                     break

        

# diagnoal_5x5_matrix(diag_5x5, value)
# print(matrix)