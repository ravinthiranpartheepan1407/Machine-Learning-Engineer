# In histogram bins size does matter a lot for measuring dispersion

# How to calculate bin: k = ceil(max(x) - min(x)) / h
# Where k = no.of bins and h = width of a bin
# Ceil rounds-up to the next value (For ex: if the value os 2.01 then it will be 3.0)

# How many bins?
    # Struges (Depends on data count: If the data is larger then the bins will also be larger): k = ceil(log2(x)) + 1  # Note: Log always increase
    # Freedman-Diaconis[Common Choice] (Depends on Data count and data spread): h = 2 * IQR/cube_root(n) where IQR = Q1-Q3
        # If IQR gets larger: Larger dispersion || total bin size will also larger || no.of bins will decrease
        # If n gets larger: Bin width gets smaller || that results larger no.of bins
    # Arbitrary: (Intution Based) k = some_value

import numpy as np
import matplotlib.pyplot as plt

def cal_bin_Freedman_Diaconis():
    # Load your data into a NumPy array or generate your data.
    # Compute the IQR of your data using the numpy.percentile() function with arguments (Q1 - some_val and Q3 - some_val : Both sum upto 100)
    # Compute the bin width using the formula 2 * IQR / (n**(1/3)) where n is the number of data points.
    # Compute the number of bins using the formula (max(data) - min(data)) / bin_width.
    # Plot

    data = np.random.gamma(0.6, size=1000)
    iqr = np.percentile(data, 65) - np.percentile(data, 35)
    bin = 2 * iqr / (len(data)**(1/3)) # 1/3 = Cube root
    num_of_bins = (np.ceil(max(data) - min(data))) / bin
    print(num_of_bins)

    plt.hist(num_of_bins, bins=50)
    plt.title("Freedman-Diaconis")
    plt.show()

cal_bin_Freedman_Diaconis()
    