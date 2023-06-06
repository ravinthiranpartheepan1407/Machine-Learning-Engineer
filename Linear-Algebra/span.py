# Span: Used to scale / reach different points from a given vectors with the usage of linear combination and that makes a plane
# vectors lies on the same line doesn't form scale or reach any points and doesn't create a plane


# Linear Independence: In a 2D or 3D plane or Hyperplanes any two of vectors should form the remaining vector. 
                       # For ex: it could v2 = x.v1 + y.v3 (or) v1 = x.v2 + y.v3 and so on...

# If it is not possible to match any one of the elements w/o scaled from source vector to target vector then it is linearly independent.
## For ex: v2 = [4,6,7] != 2.[2,3,4] => v2 != x.v1 (Then it is called as Linearly independent)
# If it is possible to match it is called as Linearly Dependent.

# IMPORTANT:
    # If (1-D) both vectors lies on same plane then it is LINEAR DEPENDENCE
    # If (2D) both vectors have different directions then it has LINEAR INDEPENDENCE since we cannot scale and match one scalar vector with another.
    # If there are (3D) vectors then there is a possibility to scale and match with any one of other vectors so it is LINEAR DEPENDENCE.
    # If there are 3D vectors with one vectors scales out of the plane then it is said to have LINEARLY INDEPENDENT.

# Theorem: Max N Independent vectors in R^N
    # Any set of M > N vectors in R^N is dependent. [ M = 8 (Elements) and N = 4 (Total Vectors) ]
    # Any set of M <= N vectors is R^N could be independent. [ M = 4 (Elements) and N = 5 (Total Vectors) ]

# IMPORTANT (FOLLOW THESE STEPS):
    # How to check whether a set is independet?
        # - Check the no.of vectors and comapre with R^N (If there are more numbers than dim then the set will be Dependent)
        # - Check 0's in all elements (If there is a 0 then the whole set is Dependent)
        # - Guess and Test
        # - Matrix rank method
 