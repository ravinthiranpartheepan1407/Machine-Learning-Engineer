# QQ (Quntile-Quntile Plots): USed a diagnostic toll to determine the data are roughly or normally distributed.

# When Calculating Theoretical Quartile use value only btw 0 to 1 and always use normal distribution.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def basic_qq_plot(): # Use PPF (Percentil Point Function (Inverse of CDF))
    data = np.random.normal(100, size=1000) # Choosing Distrubtion and Passing parameters
    calculate_theoretical_ppf = stats.norm.ppf(q=(np.linspace(0.1,0.99,num=len(data)))) # Calculating Theoretical Quartile (q: quartile)
    sort_ppf = np.sort(calculate_theoretical_ppf) # Sorting calculate dtheoretical ppf data
    plt.plot(sort_ppf)
    plt.plot(calculate_theoretical_ppf)
    plt.show()

basic_qq_plot()



