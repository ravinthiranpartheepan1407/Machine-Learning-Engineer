# Violin Plot: Plot histogram on y-axis and mirrors another axis

import numpy as np
import matplotlib.pyplot as plt

def violin_plot():
    data = np.random.gamma(2.5, size=1000)
    plt.violinplot(data)
    plt.show()

def histogram_plot():
    data = np.random.gamma(2.5, size=1000)
    plt.hist(data,bins=50)
    plt.show()

violin_plot()
histogram_plot()