# Shallow Copy (View): A new array obj inherits orginal arr obj which means updates made in old arr obj the changes will also happen in new arr obj
# Deep Copy (Copy): It creates a new arr as an isolated arr obj which mean it is independent
# VStack: Merge arr objs in vertical order
# HStack: Merge arr obj in horizonatl order
# Transpose: Inverse of a matrix ( 1/Matrix )

import numpy as np

matrix = np.array([[10,20,30], [40,50,60], [70,80,90],[100,110,120]])
matrix_A = np.array([[100,200,300], [400,500,600], [700,800,900],[1000,1100,1200]]) # 2x3 and 2x3 and 2 objs

# Shallow Copy
shallow_matrix = matrix.view()

# Deep Copy
deep_matrix = matrix.copy()

# Change_Value
matrix[0][0] = 200

print(shallow_matrix)
print(deep_matrix)

# VStack
v_stack = np.vstack((matrix, matrix_A)) # Take two args wraped with tuple
print(v_stack)

# HStack
h_stack = np.hstack((matrix, matrix_A)) #Take two args wraped with tuple
print(h_stack)

# Concatenate
concat_matrix = ((matrix, matrix_A))
print(concat_matrix)

# Transpose
t_matrix = matrix_A.T
print(t_matrix)

