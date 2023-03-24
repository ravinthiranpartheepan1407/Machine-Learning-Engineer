# Given the head of a singly linked list, 
# return true if it is a palindrome or false otherwise.

# Breakdown:

# 1. Create a list
# 2. Iterate through the list with the complexity of O(n)
# 3. Iterate from the backwards using the range step = -1
# 4. Compare the list and backward list
# 5. If it match print True else False

numbers = [1,2,2,1]
backward_num = []
def palindrome_linked_list(numbers):
    backward = -len(numbers)-1
    for values in range(-1, backward, -1):
        backward_num.append(numbers[values])
        if numbers == backward_num:
            print("It's a palindrome")
            print(f'The input: {numbers} and the palindrome is: {backward_num}')
            break
        else:
            print("It's not a palindrome")
        
    

palindrome_linked_list(numbers)