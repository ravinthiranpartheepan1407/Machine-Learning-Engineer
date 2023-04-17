# Bar plot(shape is not important so we can swap both axis): 

    # Can take categorical on x-axis and interval, ratio or discrete on y-axis

# Histogram (shape is important and can swap only y-axis):

    # Can use only continous data (Upto certain range) on both x-axis and y-axis such as interval type, ratio type or discrete type.

# Histogram Count(Overall Total): Total measure and easy to interpret raw data (sum doesn't require)
# Histogram Proportion(A Chunk): Can analyze a chunk and it will take more efforts to relate to raw data(Sum requires).

## Formula for converting count to proportions: item[index] = item[index] / sum(all items)
## To get probability from proportion use: 100*items[index]/sum(all_items)

import numpy as np
import matplotlib.pyplot as plt

rangeval = int(input("Enter element range: "))
items = np.arange(rangeval).reshape(3,3)
print(items)

for index in range(len(items)):
    count = sum(items[index])
    prop = np.histogram(items[index],bins=rangeval)
    print(len(items[index]))
    # items[index] = 100*items[index]/count # Gives probability from proportions
    prop_1 = items[index]/count
    plt.hist(prop_1)
    plt.show()
    print(prop_1)
