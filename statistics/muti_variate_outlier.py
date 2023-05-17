# If a point's x-axis length is small and y-axis length is larger then it has low leverage outlier
# If a point's x-axis length and y-axis length is larger then it has higher leverage outlier
# Outlier often called noisy, junks, extreme values..

# Startegy 1: Remove outliers from the data prior analyses
# Strategy 2: If the outlier has an important data point the keep it and reduce the -ve impact of the outliers on the results.

## Remember:
    # Outliers must be investigated and evaluated.
    # Never remove outliers without thought
    # Never ignore outlier (Beacuse it will give information about where the outlier come from)

# Iterative Algorithm:
    # Convert data to z-score
    # If data point exceeds more than the threshold then it is an outlier (If the value arbitrarly set to 3 then value below -3 is also an oulier) 
    # Remove outlier and repeat until all the putliers are gone.

### If the distribution normal or gaussian

#### Then use Z-Score formula: Z[index] = (x[index] - mean) / std(x[index])

### If the distribution is non-gaussain the use modified Z-Score for anlyzing outliers

#### Modified Z-Score Formula: M[index] = 0.675 (x[index] - median(x)) / median(|x[index] - median(x)|) 
    # where MAD = median(|x[index] - median(x)|)
    # Where 0.675 is the values IQR - Q3 range which 75%

## Eucledian Distance: d = sqrt((a(base(x) - b(base(x)))^2 + (a(base(y) - b(base(y)))^2)
# Use when there is a need to calculate distance betwwen two points we can use Eucledian distance formula
# Eucleadian distance is for any arbitrary number of dimensions

# Multivariate Mean: It's just mean of all points in both dimensions (mean of x-axis and mean of y-axis)

## Multivariate Algorithm:

    # Compute data mean
    # Compute distance from each data point to mean
    # Conver distances to z-score


