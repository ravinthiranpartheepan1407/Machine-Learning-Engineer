# MIN_MAX SCALING: USED TO SCALE ANY ARBITRARY VALUES UPTO 0 TO 1 (Unity-Normed Data Scale)
# Y-Axis: Contains Arbitrary Values

# Formula: X[index] = x [index]- min(x) / max(x) - min(x)

# When to use Z-Score and Min-Max Scaling?
    # - Both Z-Score and Min-Max scaling are used for normalizing the data and used to compares values from different data and scales the values between 0 to 1
    # - But Z-Score scales the mean to 0 and std to 1; Also used to identify the outliers
    # - Min-Max Scaling scales the data min to 0 and max to 1; Less sensitive to outliers but it emphazie the relative diff btw values


# If data range is important: use this first formula "a + (x - min(x)) / (max(x) - min(x)) * (b - a)" when the data needs to be scaled for some specific range (i.e, -10 to 10)
# If relative vals are important but data range is not: use this second formula "(x - min(x)) / (max(x) - min(x))" when the data needs to be scaled between 0 to 1.
    # The second formula is a common approach in data analysis and machine learning, where the range of the data is not important, but the relative differences between the values are.
