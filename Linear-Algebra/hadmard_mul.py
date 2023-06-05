# Harmand Multipliation: Element wise multiplication.

# np.multiply: Element wise multiplication
# np.dot: Matrix multiplication or dot product

import numpy as np
import matplotlib.pyplot as plt
def harmand_mul():
    element_1 = np.array([7,14,21])
    element_2 = np.array([10,20,30])
    result = np.multiply(element_1, element_2)
    print(result)

harmand_mul()


# Dot product: V^T W [row x column] (No matter how much dim are there the result will be in scalar type (1x1))
# Outer Product: V W^T [column x row] (Dims are based on VxW)

def outer_product():
    element_1 = np.array([7,14,21])
    element_2 = np.array([10,20,30])

    # Way 1: Using np.outer()
    result = np.outer(element_1, element_2)
    print(result)

    # Way 2: Using for-loop
    result_2 = np.ones((len(element_1), len(element_2)))
    print(f'The dimension is: {result_2.shape}')

    for valuesA in range(0, len(element_1)): # Hold 0 until it finishes the second loop to the range 0,1,2 and then it set 1st loop range val as 1....
        for valuesB in range(0, len(element_2)):
            result_2[valuesA][valuesB] = element_1[valuesA] * element_2[valuesB]

    print(result_2)

outer_product()


def cross_product():
    # A x B = C 
    # Cross product: Always result in 3D Vector and Have 3D shape (3 x 3)
    element_1 = np.array([7,14,21])
    element_2 = np.array([10,20,30])    
    # Way 1: Using np.cross
    cross_prod = np.cross(element_1, element_2)
    print(f'The cross product 1 is: {cross_prod}')
    # Way 2: Using manual method
    cross_prod_2 = [
        [element_1[1] * element_1[2] - element_2[1]*element_2[2]], # Index 0 -> [1][2]
        [element_1[0] * element_1[1] - element_2[0] * element_2[1]], # Index 1 -> [0][2]
        [element_1[0] * element_1[1] - element_2[0] * element_2[1]] #Index 2 -> [0][1]
    ]
    print(f'The cross product 2 is: {cross_prod_2}')
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot([element_1[1] * element_1[2] - element_2[1]*element_2[2]], [element_1[0] * element_1[1] - element_2[0] * element_2[1]], [element_1[0] * element_1[1] - element_2[0] * element_2[1]])
    # ax.plot([element_1[0] * element_1[1] - element_2[0] * element_2[1]])
    # ax.plot( [element_1[0] * element_1[1] - element_2[0] * element_2[1]])
    plt.show()


cross_product()

