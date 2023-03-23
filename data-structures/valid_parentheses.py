# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Breakdown:

# 1. Create a list with parantheses chars
# 2. Create a input var
# 3. If there is a match in parathesis print True else False

parantheses = ['(',')','{','}','[',']']
input_1 = str(input("Enter chracters_1: "))
input_2 = str(input("Enter chracters_2: "))

def valid_parantheses(parantheses, input_1, input_2):
    for chars in range(len(parantheses)): # Complexity of the code is O(1) since we are printing only the values from lists with fixed range.
        print(parantheses[chars])
        if input_1 == parantheses[0] and input_2 == parantheses[1]:
            print(True)
        elif input_1 == parantheses[2] and input_2 == parantheses[3]:
            print(True)
        elif input_1 == parantheses[4] and input_2 == parantheses[5]:
            print(True)
        else: 
            print(False)
        break

valid_parantheses(parantheses, input_1, input_2)