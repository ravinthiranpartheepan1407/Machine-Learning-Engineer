# Gaussian Distribution: PDF was used to measure the likelihood of an element over a contionous range of value.

# Here in this example: 

import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt

range_val = int(input("Enter a value: "))
shape_A = int(input("Enter Shape A Value: "))
shape_B = int(input("Enter Shape B Value: "))

normalize_distriibution = []
probability = ""

def gaussian_dist(range_val, shape_A, shape_B):
    # data_alt = np.arange(range_val).reshape(shape_A, shape_B)
    data = np.linspace(start=shape_A, stop=shape_B, num=range_val)
    gauss_dist = sp.norm.pdf(data) # f(x) = (1/σ√(2π)) * exp(-((x-μ)/σ)^2/2)
    # X = data, μ = Mean(data), σ = Standard Deviation: sqroot(variance(data))

    for values in range(len(gauss_dist)):
        calc_prob = gauss_dist[values] / sum(gauss_dist)
        print(f'THe probability is: {calc_prob}')
        probability = sum(gauss_dist) / sum(gauss_dist)
        normalize_distriibution.append(calc_prob)

    print(f'Overall probability is: {probability}')
    print(gauss_dist)
    plt.plot(normalize_distriibution)
    plt.xlabel("Start and Stop Values")
    plt.ylabel("Distribution Range")
    plt.legend("Gaussian Distribution")
    plt.show()

gaussian_dist(range_val, shape_A, shape_B)

