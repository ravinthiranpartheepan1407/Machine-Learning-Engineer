import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

plot_names = ["./plots/barplot.png", "./plots/lineplot.png"]

data_1 = np.array([[10,20,30,40],[50,80,120,150]])
x_axis = plt.xlabel("Index_0")
y_axis  = plt.ylabel("Index_1")
bar_viz = plt.bar(data_1[0], data_1[1])
line_viz = plt.plot(data_1[0], data_1[1])
error_viz = plt.errorbar(data_1[0], data_1[1], np.mean(data_1[0]), np.mean(data_1[1]))

plt.savefig(plot_names[0])
plt.savefig(plot_names[1])
plt.savefig("./plots/error_viz.png")

for images in range(len(plot_names)):
    with Image.open(plot_names[images]) as open_plots:
        open_plots.show()

print(data_1)
print(data_1.ndim)
print(data_1.shape)
print(data_1.dtype)
print(data_1[0])