# Unsupervised Learning:
    # Compare mean and median distribution
    # Comapre it with dataset conatins large scale data and outliers

import numpy as np
import matplotlib.pyplot as plt

class SmallOutlierData:
    def __init__(self):
        self.value = np.concatenate((np.arange(start=-1000, stop=1000, dtype=float, step=100), np.array([-10000, 10000])))
        print(self.value)

class Visualization(SmallOutlierData):
    def small_outlier_viz(self):
        # get_data = np.log(self.value) #with log scaling
        get_data = self.value
        cal_mean = np.mean(get_data)
        cal_median = np.median(get_data)
        print(f'The mean value is: {cal_mean}')
        print(f'The median value is: {cal_median}')
        print(get_data)
        plt.boxplot(get_data) # Box plot will not accept -ve values
        plt.show()
        
        
data_obj = SmallOutlierData()
Visualization_obj = Visualization()
print(f'The Data Values are: {data_obj.value}')
print(f'Visual Data: {Visualization_obj.value}')
Visualization_obj.small_outlier_viz()
