# Shape should equal to possible sqaure or possible multiplicatios eg: 100 = 10x10, 20 = 4x5
# The higher dim of the observed values will considered as final ndim

import numpy as np

range_val = int(input("Enter a range: "))
rows = int(input("Enter row shape: "))
columns = int(input("Enter column shape: "))

def create_4D_matrix(range_val, rows, columns):
    matrix_A = np.arange(range_val).reshape(rows,columns)
    matrix_B = np.ones((rows,columns), dtype=float)
    matrix_C = np.zeros((rows,columns), dtype=int)
    matrix_D = np.array([[[1.5]]])

    ops = np.array((matrix_A+matrix_B)-matrix_C+matrix_D) # Output of ndim is 3 Because it has [layer_3[layer_2[layer_1]]]

    for values in range(len(ops)):
        if (ops[values] > 1.0).all(): # If you use .any() the atleast one element should be greater than 1.0 then it is true
            print(f'The filtered values are: {ops[values]}') # All value should be greater than 1.0 then it is true

    print(f'The output is: {ops}')
    print(f'The ops ndim is: {ops.ndim}')

    print(f'shape of matrix_A: {matrix_A.shape} | shape of matrix_B is: {matrix_B.shape} | shape of matrix_C is: {matrix_C.shape} | shape of matrix_D is: {matrix_D.shape}')
    print(f'ndim of matrix_A: {matrix_A.ndim} | ndim of matrix_B is: {matrix_B.ndim} | ndim of matrix_C is: {matrix_C.ndim} | ndim of matrix_D is: {matrix_D.ndim}')
    print(f'size of matrix_A: {matrix_A.size} | size of matrix_B is: {matrix_B.size} | size of matrix_C is: {matrix_C.size} | size of matrix_D is: {matrix_D.size}')

create_4D_matrix(range_val, rows, columns)


