# Numpy: Used for statistical ops, math ops, scientific ops, I/O ops...
# Numpy: Fixed in size
    # - ndarry: Array init and it used vectorization to iterate through element by element
    # - Vectorization: Does not create a copy of an element; Makes the loop run faster, It uses C over python
    # - ndarrays: Are fixed and same data type
    # n can be 1-D, 2-D or upto n-D

    # An array in numpy can be created using tupes ((some data)) or using list ([some data])

    # Observed values: Given Input
    # Codes: Points that are close to observed values
    
    # Broadcasting: Both ndarray should have same shape or one of them should be equal to 1 (Scalar)

    # Broadcasting: Used to fabricate the arrays in the same shape
    # Broadcasting: Should consider shape is eauwl to highest shape of the input (For ex: a=[1,2,3] b = [[3,6,9], [12,15,18], [21,24,27]) The shape is (1x3) and the dim is 3.
    # Smaller array broadcast across largest array

    # ndim: can be calculated as 
        # (Taken it as an example: We have a bigger box and inside we have smaller boxes then it is 2-D)
        # For 3-D, we have a box and there is another (Medium sized) box inside the bigger box and inside the medium box we have smalle box

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

element_A = np.ndarray((40,50,60,70))
element_B = np.ndarray([40,50,60,70])

ndim_A = np.array([[[1,2,3], [4,5,6]], [[7,8,9],[10,11,12]], [[15,16,17], [18,19,20]]])
ndim_b = np.array([[10,20,30,40],[50,80,120,150]]) # Insert by row

float_A = np.arange(36.0).reshape(6,6)
float_B = ([1.5])

multiply = float_A * float_B
print(f'The float_A matrix is: {float_A}')
print(f'The multiplied matrix is: {multiply}')
print(f'The shape of multiplied is: {multiply.shape} and ndim is: {multiply.ndim}')

# print(f'The shape of ndim_b is: {ndim_b.shape}')
# print(f'The ndim of element_A is: {element_A.ndim} and element_B is: {element_B.ndim}')
# print(f'The shape of ndim_A is: {ndim_A.shape}')
# print(f'The size of ndim_A is: {ndim_A.size}') # totla elements in the array

shape_scalar = ([1]) # Scalar
shape_a = np.arange(25).reshape(5,5)
shape_b = np.arange(25).reshape(5,5) # Array

add = shape_a * shape_b

# add_viz = plt.plot(add)
# plt.savefig("./plots/add_viz.png")

# with Image.open("./plots/add_viz.png", mode="r") as viz_open:
#     viz_open.show()

# print(f'The shape_b matrix is: {shape_b}')
# print(f'The dimension is: {add.ndim}')
# print(f'The shape is: {add.shape}')
# print(f'The dtype is: {add.dtype}')
# print(f'The shape of add is: {add.itemsize}')