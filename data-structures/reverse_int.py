# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Breakdown:

# 1. Create an input var
# 2. Iterate thorugh input with complexity of O(n)
# 3. Push the last int element [:-1] to the front index [0]

# 1.1 -> input = 123
# 1.2 -> for items in input : --> items = 123
# 1.3 -> set items[::-1] -> items[0]
# 1.4 -> set items[::-2] -> items[1]....items[::-n] -> items[n]
# 1.5 -> return items

input_int = str(input("Enter an Integer: "))

def reverse_int(input_int): #O(n)
    rev_int = ""
    signed_int = ""
    try:
        for digits in range(len(input_int)-1, -1, -1): # Start = 4-1 -> 2, Stop = -1(So, it will iterate from 2,1,0), Step = -1 (Backward step point by one)
            rev_int += input_int[digits] # rev_int = 3, rev_int = 2, rev_int=1
            if int(input_int) < 0:
                signed_int += input_int[digits].replace("-","")
                print(f'-{signed_int}')
            else:
                print(f'{rev_int}')
               
    except:
        raise ValueError("Please enter a integer dude!")

reverse_int(input_int)
  

