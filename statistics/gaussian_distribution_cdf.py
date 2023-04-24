# Measured upto a certain variable
# The total probability should be less than or equal to given input.

# Using Reman computation to normalize the distribution to 1.

import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt

def gaaussian_dist_CDF():
    data = np.linspace(start=-5,stop=5,num=100)
    gauss_dist_CDF = sp.norm.cdf(data)
    
    # We don't ned reman compute or probabilistic analysis to normalize this distribution because it is normalized
    reman_compute = sum(gauss_dist_CDF) * np.diff(data[:2])  # Sum(distribution) * Diff(data[:2])
    print(reman_compute)
    
    print(gauss_dist_CDF)
    plt.plot(gauss_dist_CDF)
    plt.xlabel("Start and Stop")
    plt.ylabel("Distribution Frequency")
    plt.title("Gaussian Distribution using CDF")
    plt.legend("Distribution")
    plt.show()

gaaussian_dist_CDF()
