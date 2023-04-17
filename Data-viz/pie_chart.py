# Pie-Chart can visualize nominal, ordinal and discrete data type
# Conidition on a data for a pie-chart: Total pieces must sum to 1 (or 100%)
# Dont use pie chart if the data didn't sum upto 1 or 100% (Mostly don't use pie chart) 

import numpy as np
import matplotlib.pyplot as plt
sequence = ["Apple", "Banana", "Lemon", "Orange", "Grapes"]
float_values = np.array([10.1,38.1,36.3,7.2,5.0]) 

# Ceil: Output will be in scalar array and used to round up the int close to next value such 1.2 closer value is 2
values = np.ceil(float_values) # Ceil: Absolute Value (-ve gives same point like -1.2 is -1 and +ve gives +1 increment like 1.2 is 2)

plt.pie(values, labels=values)
plt.show()

print(float_values)
print(values)