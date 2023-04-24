# Gaussian Distribution or Normal or Bell curve Distribution:  f(x) = (1/σ√(2π)) * e^(-(x-μ)²/(2σ²))
    # PDF: f(x) = 1/(b-a)
    # Rules: Considers highest at mean

    # μ -  Mean = all_elements / len(all_elements) || Mean = (10 + 15 + 20 + 25 + 30) / 5 = 20
    # σ - Standard Deviation = sqrt of variance || SQRT(50)
    # σ² - Variance = sqaured difference of all_element and mean  || Variance = ((10 - 20)^2 + (15 - 20)^2 + (20 - 20)^2 + (25 - 20)^2 + (30 - 20)^2) / 5 = 50

    # Shape: Bell Shaped and Symmetrical
    # Range of value: Can take ay range of value
    # Probability Density:  Consider Highest at mean and decreases symmentrically on both sides
    # Variability: Uses S.D as parameter to describe the spread of the data
    # Occurence: Used mode natural phenomena

# Uniform Distribution: CDF: F(X) = (x-a)/(b-a) and PDF: f(x) = 1/(b-a)
    # Shape: No peaks
    # Range of Values: Can only take specific range of values
    # Probability Density: Constant across the range of values
    # Variability: Uses a parameter for range to describe the width of distribution
    # Occurence: Used to model situtations where outcomes are equally same.

    # Rules: Uniform accepts only equal occurences
        # When high == low, then low will be returned
        # High limit may be included in the returned value as low + (high-low) * random_sample()
        # When high < low, then it is undefined because of inequality


import numpy as np
import matplotlib.pyplot as plt

data_1 = np.arange(25, dtype="float").reshape(5,5)
data_2 = np.arange(25, dtype="float").reshape(5,5)

float_value = np.arange(25, dtype=float).reshape(5,5)

sin_conversion = np.sin(data_1)
uniform_distribution = np.random.uniform(0,100,50) # Returns: ndarray or scalar # low: low boundary, high: Upper boundary value <= 1.0 (Default value)
gaussian_distribution = np.random.normal(loc=float_value, scale=1.5) # loc: Mean, scale: Spread of distribution # Returns: ndarray or scalar
print(uniform_distribution)
print(gaussian_distribution)

uniform_viz = plt.boxplot(uniform_distribution)
plt.savefig("./plots/uniform_distribution.png")
plt.show()

gaussian_viz = plt.boxplot(gaussian_distribution)
plt.savefig("./plots/gaussian_distribution.png")
plt.show()

data_viz = plt.boxplot(sin_conversion)
plt.savefig("./plots/unsupervised_learning.png")
plt.show()
