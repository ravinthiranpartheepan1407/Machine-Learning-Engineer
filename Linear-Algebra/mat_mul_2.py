### Layer Perspective: Building product matrix one layer at a time.
    # Left Matrix: Comprising Columns and Right Matrix: Comprising Rows
    # It has product scalar value because it has on column worth info and a scaled layer of it's column info by applying distributive technique
        # We compute outer product: V W^T (Column x Row)
        # For ex: A = [         
        #              0 1
        #              2 3
        #             ]

        #         B = [         
        #              a b
        #              c d
        #             ]

        # Compute (A B^T) = [0a 0b
        #                    2a 2b
        #                   ] + [1c 1d
        #                        3c 3d
        #                       ]

        # Result (Element wise addition AKA Spectral theorem of Matrix) = [0a+1c 0b+1d
        #                                   2a+3c 2b+3d
        #                                  ]



### Column Perspective(Dot product and POV from row matrix): 
    # For ex: Mat([row(0, 1) row(2, 3)]) Mat([row(a b), row(c,d)] = [a[column(0, 2)] + c[column(1, 3)]] [b[column(0, 2)] + d[column(1, 3)]]



# NOTE( In statistics and regression analysis): Left matrix is called as design matrix: Contains set of regressors (Simplified model of data)
# NOTE( In statistics and regression analysis): Right matrix is called as vectors: Contains co-efficients


### Row perspective (Same as row but opposite; POV from from matrix):
    # For ex: Mat([row(0, 1) row(2, 3)]) Mat([row(a b), row(c,d)] = [0[row(a, b)] + 1[row(c, d)]] [2[row(a, b)] + 3[row(c, d)]]



### In summary:
    # Element: Normal mat dot product
    # Layer(V W^T): Elment wise dot prod by considering respective nodes from column matrix + rows from row matrix (For ex: [mat_1(node_0) * mat_2(node_0) + mat_1(node_0) * mat_2(node_1)])
    # Column: POV from row matrix and Dot product
    # Row: POV from column matrix and Dot product