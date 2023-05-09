# mean = sum of all elements / n
# variance (Dispersion) = (element[index] - mean)^2 / n
# skewness (Dispersion Asymmetry) = (element[index] - mean)^3 / nσ (Where σ is standard deviation: σ = sqrt(variance))
# kurtosis (Tail Fatness) = (element[index] - mean)^4 / (n(σ^2)) (Where σ^2 is variance)

## Skweness
# Right Skew: Positive
# Left Skew: Negative

## Kurtosis
# If data falls off quickly then it has low kurtosis - Normal Distribution
# If data falls off slowly then it has high kurtosis - Extreme values or outliers

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from PIL import Image

def left_skew_data(): # Left Skew: Gamma value should be < 1
    data = np.random.gamma(0.7, size=1000) # Random possibilities of shapes 0.7 with size = 10
    print(data)
    plt.hist(data, bins=50)
    plt.title("Left-Skew Distribution")
    plt.show()
    plt.savefig("../images/left-skew-image.png")


def right_skew_data(): # Right Skew: Gamma value should be > 1
    data = np.random.gamma(2.0, size=1000) # Random possibilities of shapes 2.0 with size = 10
    print(data)
    plt.hist(data, bins=50)
    plt.title("Right Skew Distribution")
    plt.show()
    plt.savefig("../images/right-skew-image.png")

def high_kurtosis():
    data = np.random.gamma(3.5, size=1000)
    plt.hist(data, bins=25)
    plt.title("High Kurtosis")
    plt.show()
    plt.savefig("../images/high-kurtosis.png")


def low_kurtosis():
    data = np.random.gamma(0.6, size=1000)
    plt.hist(data, bins=25)
    plt.title("Low Kurtosis")
    plt.show()
    plt.savefig("../images/low-kurtosis.png")

left_skew_data()
right_skew_data()
high_kurtosis()
low_kurtosis()