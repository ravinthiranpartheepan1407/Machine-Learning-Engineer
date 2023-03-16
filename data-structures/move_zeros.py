# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the 
# non-zero elements.

# Categories: With a copy of an array and without a copy

# Breakdown:

# 1. Create a list with type of int
# 2. Iterate through the list with complexity of O(n)
# 3. If there are any 0s then move it to the [::-1] last index
# 4. Insert the non-elements before the last indexes.

from time import time

nums = [0,1,0,3,12]
copy = []
zeros = []
def move_zeros(nums): # Without copy of an array
    start = time()
    for items in range(0, len(nums)): # O(n) time complexity
        if nums[items] == 0:
            zeros.append(nums[items]) 
            print(zeros)         
        elif nums[items] != 0:
            copy.append(nums[items])
            print(copy)
        else:
            return None
    end = time()
    print(f'Time taken to complete this process: {end-start}')
    
move_zeros(nums)
print(f'The final elements are: {copy+zeros}')
