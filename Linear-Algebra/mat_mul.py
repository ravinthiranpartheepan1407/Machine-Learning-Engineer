# Matrix Multiplication is different from Vector Multiplication
    #   - Vec Mul: Both inner product dim has to be same Mat_A = dim(5 x 1) and Mat_B = dim(5 x 1) 
    #   - Mat_A Mat_B => Mat_A ^ T . Mat_B = dim(1 x 5) dim(5 x 1) => Result dim = (1,1)    -> Vector Mul is possible because inner products match

    #   - Mat Mul: # M x N and N x K = M x K (Result): 
        #   - Both N are inner product and M, K are outer product
        #   - Both N should have same dim then only mat mul is possible

# Standard Matrix Mul: It's not commutative.
#                      AB -> A left-multiplies B  (or) A pre-multiplies B
# Can also written as, AB -> B right-multiplies A (or) B post-multiplies A 


# Eg_1: Matrix_A = (5,2) and Matrix_B = (2, 7) => Both inner products(2, 2) are SAME so the mat mul is POSSIBLE. So, the Result dim = (5,7)
# Eg_2: Matrix_A = (7,2) and Matrix_B = (7, 2) => Both inner products (2, 7) are DIFFERENT so the mat mul is NOT POSSIBLE.
# Eg_3: Matrix_A = (7,2)^T and Matrix_B = (7, 2) => Taking transpose on Matrix_A so the inner products will be (7, 7) are SAME so the mat mul is POSSIBLE. So, the Result dim = (2,2)


