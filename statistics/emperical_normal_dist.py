# Normally Distributed:
    # Strech (Variance)
    # Shift (Mean)
    # Range (Values)

import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt

value = int(input("Enter a value: "))
stretch = int(input("Enter Strech (Variance) value: "))
shift = int(input("Enter Shift (Mean) value: "))

def normally_dist(stretch, shift):
    data = np.random.randn(value)
    # for values in range(len(data)):
        # dist = stretch * data[values] + shift
    dist = stretch * data + shift
    print(dist)
    plt.hist(x=dist, bins=25)
    plt.show()
    print(f'The mean is: {np.mean(dist)}')
    print(f'The Variance is: {np.var(dist)}')

normally_dist(stretch, shift)