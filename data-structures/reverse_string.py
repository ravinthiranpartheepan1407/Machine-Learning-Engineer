# Use array for all string related questions because strings are nothing but an array of characters

# Breakdown:
# 1. Create a list / array to store reversed string
# 2. Set input with input [::-1] get last element and push it into the array as the first element.
# For ex: Last element [d] -> reverse_string = [d] and the next last element as n -> reverse_string = [dn]

string = str(input("Enter a string: ")) # Hello my friend

def reverse_string(string): # O(1)
    try:
        reverse_string = []
        string = string[::-1] 
        reverse_string.append(string)
        return reverse_string                      
    except:
        raise ValueError("Please Enter a string dude!")

def reverse_string_arr(string): #O(n)
    try:
        reverse_string = []
        for i in string:
            i = string[::-1]
            reverse_string.append(i)
            return i            
    except:
        raise ValueError("Enter a string dude!")


def reverse_string_linear(string):
    print(string[::-1]) # O(1)

print(f'Reverse string with O(n): {reverse_string_arr(string)}')
print(f'Reverse Strings with O(1): {reverse_string(string)}')
reverse_string_linear(string)
