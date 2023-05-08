# Fano Factor and Coefficient of Variation(COV): (Normalized measurement for variability and accepts only positive data/values):

# Fano (Use when you want to count the data; If Fano_Factor < 1: lesser variance and Fano_Factor > 1: Higher Variance ) : (variance)^2 / mean
# Cov (use when comparing the variability of datasets with different means such as financial data of a stock in different months): variance / mean

import numpy as np
import matplotlib.pyplot

data = np.arange(start=1, stop=100, dtype=int)

def fano_n_cof(data):
    cal_std = np.var(data)
    cal_mean = np.mean(data)
    print(f'The mean for data: {cal_mean}')
    print(f'The variance for data: {cal_std}')

    cal_fano = np.square(cal_std) / cal_mean
    cal_cov = cal_std / cal_mean
    print(f'The Fano factor for data is: {cal_fano}')
    print(f'The Coefficient of Variation for data is: {cal_mean}')

fano_n_cof(data)


