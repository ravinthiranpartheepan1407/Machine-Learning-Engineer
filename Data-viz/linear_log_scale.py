# Linear Scaling (Mostly Used in Comparisons, trend analysis): Addition(0,10,20,30)
# Logarithmic Scaling: Multiplication (Grows really fast and space between ticks are different) (0,10,100,1000....)
# Log Scaling: Grows by Exponents (10^0,10^1.....)

# Both Logarithmic and Linear are inverse to each other
    # In Linear axis: The Logarithmic grows faster and Linear grows in a straight line
    # In Logarithm axis: The Linear grows faster and Logarithmic grows in a straight line

# Linear(Use this as much as possible for easier understanding): Scaled to big, small and -ve numbers
# Logarithmic (Use only when there is a need to process big differences between data): 
    #Doesn't work with -ve numbers, used in financial data, or really big differences between data

# Problem: Trasnform Linear Y-Axis to Logarithmic Y-Axis
# By default the axes will be in  Linear scaling

import numpy as np
import matplotlib.pyplot as plt

# Shapes of two axis must be same
x_linear_values = np.linspace(start=0, stop=36, num=10)
y_linear_values = np.linspace(start=0, stop=36, num=10)
print(x_linear_values)

def linr_to_log(x_linear_values, y_linear_values):
    convert_to_log = np.exp(y_linear_values)
    print(convert_to_log)
    plt.plot(x_linear_values, convert_to_log)
    plt.title("Linear to Log Scaling on Y-Axis")
    plt.xlabel("Linear Scaling")
    plt.ylabel("Logarithmic Scaling")
    plt.show()

linr_to_log(x_linear_values, y_linear_values)

x_log_values = np.exp(x_linear_values)
y_log_values = np.exp(y_linear_values)

def log_to_linr(x_log_values, y_log_values):
    # Shapes of two axis must be same
    convert_y_linear = np.linspace(start=0, stop=y_log_values, num=10)
    print(convert_y_linear)
    plt.plot(x_log_values, convert_y_linear)
    plt.title("Log to Linear Scaling on Y-Axis")
    plt.xlabel("Log Scaling")
    plt.ylabel("Linear Scaling")
    plt.savefig("./plots/log_to_linear.png")
    plt.show()

log_to_linr(x_log_values, y_log_values)





