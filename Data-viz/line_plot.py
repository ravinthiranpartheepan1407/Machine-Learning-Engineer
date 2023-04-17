# Use line plot when: There are many bars (To get fine resolution) and In-Graph comparisons of different categories.

# Don't use bar plot with line plot when the data type is categorical
# Use line plots when the data is resolution is too good and many (If there are more categories then use line instead of bar)

# Sine : Use it for periodicity and oscillation
# Log: Growth or Decay

import numpy as np
import matplotlib.pyplot as plt

department = {
        "IT": "orange",
        "Sales": "blue",
        "HR": "black",
        "Design": "green",
        "Media": "yellow"
}

revenue_range = np.arange(3).reshape(3,1)
it = np.random.normal(loc=revenue_range)
sales = np.random.normal(loc=revenue_range)
hr = np.random.normal(loc=revenue_range)
design = np.random.normal(loc=revenue_range)
media = np.random.normal(loc=revenue_range)

print(it)

def analyze_growth_loss(it, sales, hr, design, media):
        fig, viz = plt.subplots()
        viz.plot(it, color=department['IT'], label="IT")
        viz.plot(sales, color=department['Sales'], label="Sales")
        viz.plot(hr, color=department['HR'], label="HR")
        viz.plot(design, color=department['Design'], label="Design")
        viz.plot(media, color=department['Media'], label="Media")
        viz.set_xlabel("Iterations")
        viz.set_ylabel("Revenue")
        viz.legend()
        viz.set_title("Department Performance")
        viz.grid(True)
        plt.show()

analyze_growth_loss(it, sales, hr, design, media)
