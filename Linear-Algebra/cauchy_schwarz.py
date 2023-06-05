# Cauchy-Schwarz inequality states that for any two vectors a and b in an inner product space, 
    # the absolute value of their dot product is less than or equal to the product of their magnitudes
# Cauchy-Schwarz: |a^Tb| <= |a| |b|

import numpy as np
import matplotlib.pyplot as plt
def cauchy_schwarz(): # Formula: abs(vec_1*vec_2) <= 
    # |a^Tb| = |a| |b| cos(angle[base(ab)])
    vec_1 = np.array([23,-14,7])
    vec_2 = np.array([14,-0.7,21])
    # angle = np.arccos(np.dot(vec_1, vec_2) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))) but we are not calculating angle
    dot_prod = np.dot(vec_1, vec_2)
    magnitude_vec1 = np.linalg.norm(vec_1) # Uses length of vector via geometry formula: || v ||  = sqrt((v1)^2 + (v2)^2)
    print(magnitude_vec1)
    magnitude_vec2 = np.linalg.norm(vec_2)
    if abs(dot_prod) <= magnitude_vec1 * magnitude_vec2:
        print(f'The cauchy-Schwarz condition met')
    else:
        print("Didn't met cauchy-schwarz condition")

cauchy_schwarz()
                    