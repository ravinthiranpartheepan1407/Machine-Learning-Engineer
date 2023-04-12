# Box Plot: Used to illustrate data distribution and ouliers
    # Data Distributions (Coloured Region): Variations in data
    # Outliers (*): Unusual large amount of data and can be illustrated as * or some shapes
    # Quartiles: Segements of the variations (Q1, Q2 - variations and median, Q-3, Data Max, Min)
    # Data max (Highest Value) and Data min (Lowest Value)
    # Median of whole data variation

# Note: Data with lower Interquartile range (IQR) is said to have higher data

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

matrix = np.arange(42).reshape(7,6)
sin_conversion = np.sin(matrix)
box_plot = plt.boxplot(sin_conversion)
plt.savefig("./plots/box_plots.png")

with Image.open("./plots/box_plots.png") as box_viz:
    box_viz.show()
