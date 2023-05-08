# Mean (Average Value) (Randomly Distributed: Unimodal and Bimodal) is suitable only in Interval and Ratio data type.
# Mean can also used in discrete and ordinal data type but needs to be carefully interpreted
# Mean cannot be used in nominal because it doesn't have a rank or order to process it in numerical type

# Failure cases occurs when the mean is zero duting the distribution.

# Mean(Meu(x)) = n^-1 summation(no. of elements) where n^-1 = 1/n
# Data = [5,7,6,3,4] -> Mean = 5+7+6+3+4/5 = 5

# Median (Middle value used to cut the data (50% lower and 50% higher)): n+1/2 (Middle value of the data)
# Media: Unimodal Distribution
# Suitable for Interval and Ratio
# Median: First Sort the data and Perform Median ops

# Mode(Most Common Value): Most Common Value (Count the no.of unique elements and picks the max count of an unique element)
# Mode: Any distrubution (Unimodal, Bimodal, Multi-modal)
# Mode: Accepts any data type (Numerical data should converted to discrete)
# For ex: [0,1,1,1,1,2,3,2,2,2,3,0]
# Mode = [1,2]

# Mean
import numpy as np

data = [23,45,67,89,13,87,63]

def mean(data):
    mean_total = sum(data) / len(data)
    print(mean_total)

def median(data): # First sort the data and the find the median
    # for values in range(len(data)):
    sorted_data = sorted(data)
    print(sorted_data)
    cut_off = len(sorted_data) / 2
    if type(cut_off) == float:      
        round_val = round(cut_off)
        ceil_val = int(np.ceil(cut_off))
        print(f'The middle order: {sorted_data[round_val-1]}, {sorted_data[ceil_val]}')
        median_val = (sorted_data[round_val-1] + sorted_data[ceil_val]) / 2
        print(f'The median value is: {int(median_val)}')
    else:
        print(data[int(np.ceil(cut_off))-1])
        

# mean(data)
median(data)


