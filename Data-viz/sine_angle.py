# Opposite:
    # Where the angle meets 90 degree
    # Opposite = hypotenuse * sin(angle)
# Angle:
    # sine(opposite / hypotenuse)
# Adjacent:
    # Adjacent = sqrt(hypotenuse^2 - opposite^2)
# Hypotenuse:
    # Hypotenuse = sqrt(hypotenuse^2 + opposite^2)
    # Opposite to right the 90 degree (Opposite side)

# Breakdown:
# Find Opposite
# Find Hypotenuse
# Find Adjacent
# Find Angle

# Sine of angle (Right Traingle used in the trend analysis, weather analysis, Financial analysis (Loan interest))

# Parameters

import numpy as np 

# angle = int(input("Enter angle value: "))
opposite = int(input("Enter opposite value: "))
hypotenuse = int(input("Enter hypotenuse value: "))

class Angle:
    def angle_find(self, opposite, hypotenuse):
        find = opposite / hypotenuse
        sin = np.sin(find)
        return sin        

class Opposite(Angle):
    def opposite_find(self, hypotenuse):
        find = hypotenuse * np.sin(Angle.angle_find(self, opposite, hypotenuse))
        print(f'The opposite is: {find}')

class Adjacent:
    def adjacent_find(self, opposite, hypotenuse):
        find = np.sqrt((hypotenuse^2) - (opposite^2))
        print(f'The adjacent is: {find}')

class Hypotenuse:
    def hypotenuse_find(self, hypotenuse, opposite):
        find = np.sqrt((hypotenuse^2) + (opposite^2))
        print(f'The hypotenuse is: {find}')


obj_angle = Angle()
obj_opposite = Opposite()
obj_adjacent = Adjacent()
obj_Hypotenuse = Hypotenuse()

print(obj_angle.angle_find(opposite, hypotenuse))
print(obj_opposite.opposite_find(hypotenuse))
print(obj_adjacent.adjacent_find(opposite, hypotenuse))
print(obj_Hypotenuse.hypotenuse_find(hypotenuse, opposite))

