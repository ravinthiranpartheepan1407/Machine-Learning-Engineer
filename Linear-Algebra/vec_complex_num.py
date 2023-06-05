## Cartesian axis (AKA Graph): 2 Dimensional Space
## Complex number: A real number + An imaginary number   -> For ex: (2+3i) 2 -> real and 3i -> Imaginary

# Horizontal axis (-infinte to +Infinite): 1D 
# Vertical Plane (-infinte to + Infinite): 1D -> That makes 2D plane

# Horizontal axis [-x to +x]: Have real number 
# Vertical axis[-y to +y]: Have imaginary numbers

### If a data contains real and imaginary points then it is called complex number
### For ex: data_1 = (7, 14i) -> Where 7 is real num (Lies on Horizontal) AND 14i will be imaginary (Lies on Y (Vertival axis))

# We can also extract two props such as:
    # Length measurement from origin to the points convergence
    # Angle measurement for both magnitude splits

# Dot Product ex 1:
    # x = 2 + 3i
    # y = 7 + 14i
    # z = x + y => z = (2+3i) (7+4i)
        # z = 14 + 8i + 21i + 12i^2   (Where i^2 = -1)
        # So, z = 14 + 8i + 21i - 12


# Dot product with complex numbers: v^T w
    # v = [1 4i, -2i, 4, 7] and w= [ 14, 8i, 21i, 12]
    # Note: v = [1 4i, -2i, 4, 7]       (Where [1 4i] is just a single element not a multi dimension element)
    
    # v^T w = [1 4i, -2i, 4, 7] * [14
#                                  8i
#                                  21i
#                                  12
#                                 ]

    # Vector_Output = [14 56i, 16, 84i, 84] 
    # Scalar_Output = 14 + 16 + 84 + 56i - 84i => 114 - 28 = 86   (Take conjucate for Imaginary Part which is nothing but subtraction)
    # Final result = 86
