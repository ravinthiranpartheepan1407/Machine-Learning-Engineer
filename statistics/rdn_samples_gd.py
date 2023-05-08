# Write a Python program to generate a random sample from a Gaussian distribution with a given mean and standard deviation.

# Breakdown:

# 1. Import Numpy, Matplotlib, and Scipy
# 2. Create a function that holds the logic to create sample from numpy.rand, mean and standard deviation
# 3. Find the mean and std using the np.mean() and np.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

data_seed = int(input("Enter a stop value: "))

def rand_samples_gauss_dist(data_seed): # f(x) = (1/σ√(2π)) * exp(-((x-μ)/σ)^2/2)
    data = np.linspace(start=-5,stop=5,num=data_seed)
    
    # Using Formula
    find_std = 
    find_mean = 
    find_center_bin = 
    

    # Without using Formula
    gauss_dist = sp.norm.pdf(data)
    fnd_mean = np.mean(gauss_dist)
    fnd_std = np.std(gauss_dist)
    print(gauss_dist)
    print(f'The mean is: {fnd_mean}')
    print(f'The Standard Deviation is: {fnd_std}')
    # plt.hist(x=gauss_dist,bins=25)
    plt.plot(gauss_dist)
    plt.xlabel("Start and Stop")
    plt.ylabel("DIstribution")
    plt.title("Generate a random sample from a Gaussian distribution with a given mean and standard deviation.")
    plt.show()

rand_samples_gauss_dist(data_seed)
