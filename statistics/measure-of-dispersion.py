# Variance = 1/(n-1) * ((value[index] - mean_of_all_values)^2)

# Variance:
    # Suitable for: Any distribution (Gaussian, uniform, skew,....)
    # Suitable data types: Numerical (Best suited) and Ordinal(Ordinal has to intepreted carefully)

# Find variance for this values arr [8,0,4,2,-1,7]

import numpy as np

data = [8,0,4,2,-1,7]
def measure_of_dispersion(data):
    for values in range(len(data)):
        print(data[values])
        cal_mean = sum(data) / len(data)
        print(f'The mean is: {cal_mean}')
        cal_sqr_diff = np.square(data[values] - cal_mean)
        print(f'The squared difference is: {cal_sqr_diff}')
        cal_variance = cal_sqr_diff / (len(data)-1)
        print(f'The variance is: {cal_variance}')

measure_of_dispersion(data)
