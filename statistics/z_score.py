# GIGO (Garbage-In and Garbage-Out): If the data is noisy then the result will also be noisy / poor
# Z-Transofrm: z[index] = variance without square / standarad deviation
# Z-Trasnform: z[index] = x[index] - Mean / standard deviation

# Z-Transofrm: Shift and Strecth the distribution but doesn't change the shape

# Z-Transform Assumptions: Mean and std are valid descriptions of the distribution's central tendency and dispersion


## Z-Transofrm: Used for measuring the data from different categories in a fair way by using mean, and std to measure the spread of score

# For ex: if persons A, B, and C are throwwing a ball where A stands closer to the target and B stands half the distance away from the target and 
# C stands far away from  the target. So obviously A will more than B and C because he is closer to the target so it's not fair to tell how hits more.
# That's where z-score comes in by relatively comparing the peoples distance and their score and use std to get highest person's index.


# Always use ddof (Delta Degress of Freedom):
    # If ddof set to 0 then it is calculating std of population data
    # if ddof is set to 1 then it is calculating std of sample data

