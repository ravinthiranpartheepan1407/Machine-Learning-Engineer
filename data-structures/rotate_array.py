# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Breakdown:

# 1. Create a list with type of int
# 2. Iterate through the loop or without loop with complexity of O(n)
# 3. Set key value = userdefined (3)
# 3. Get the last 3 items using [::-1] and push it to the rotated_list

key = int(input("Enter a key to rotate: "))
lists = [1,2,3,4,5,6,7]

def rotated_array(key, lists): #O(n) because it has n no.of items in the list
    get_last = lists[:]
    last_items = lists[:-key]
    remove_duplicates = list(set(get_last) - set(last_items))
    print(remove_duplicates)
    print("The rotated array is: ", remove_duplicates+last_items)       
    
  
rotated_array(key, lists)


