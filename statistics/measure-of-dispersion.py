# Variance = 1/(n-1) * ((value[index] - mean_of_all_values)^2)

# 1/(n-1): Sample Variance (Emprical Quantity: Need to measure because it will show differences per measurement )
# 1/n: Population variance (Theoretical Quantity: We the measurement in advance)

# Variance: 
    # Low variance: Low deispersion and easier to predict because of the data are tightly coupled with the mean value (but only has fewer data)
    # High Variance: High variability / Dispersion and diffcult to predict because the data are not tightly coup0led with mean value (But have more data)
    # In some cases: High variance is desired depend on the use case where more is needed but it also has higher risk(poor predictable results, bias..)
    # By default low variance is desired in most cases...
    # Suitable for: Any distribution (Gaussian, uniform, skew,....)
    # Suitable data types: Numerical (Best suited) and Ordinal(Ordinal has to intepreted carefully)

# Find variance for this values arr [8,0,4,2,-1,7]

# Sqaured difference used to get higher data dispersion but it will also expose to higher scale of outliers
# By Mean Absolute Difference(Rarely used): It will have low data dispersion since we are not squaring it and also, it will have low outliers scale.

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
