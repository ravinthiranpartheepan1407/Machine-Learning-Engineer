# Create finite float points with radom value spaces using arange
# Create the equal spaces in the finite floating points by using linspaces

import numpy as np

def fp_linspace():
    precision_1 = np.arange(0, 10, 0.5).reshape(4,5) # Cannot create equal spaces fixed size between start and stop with arange
    print(precision_1)
    precision_2 = np.linspace(0,40,6) # Can create equal spaces between start and stop with fixed sixe
    print(f'The precision 2 is: {precision_2}')

fp_linspace()