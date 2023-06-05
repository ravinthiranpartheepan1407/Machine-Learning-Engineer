# Hermitian Transpose: Uses complex conjugate for a complex number
# Hermitian Transpose: Keep the real part of complex number as it but it flips the magnitude of imaginary part 
# Complex number: (a + bi)
# Complex conjugate: (a - bi)

# Hermitian Transpose represented as "H" (not T)

# For ex: v= [1 4i, -2i, 4, 7]  the v^H (Hermitian Transpose) = [
#                                                                 1 -4i
#                                                                 2i
#                                                                 4
#                                                                 7
#                                                                ]

## We cannot use normal transpose (v^T w) because it will give complex number as a result and that will make no sense
## Hermitian transpose will result in real numbers that would make more sense to interpret the result

import numpy as np

def hermitian_conjugate():
    print(np.complex(2, 3))   # The first element is always real number and second will be the imaginary part

hermitian_conjugate()