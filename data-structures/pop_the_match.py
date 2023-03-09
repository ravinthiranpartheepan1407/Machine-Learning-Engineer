## Clarifications:
# 1. The inputs and expected outputs are clear (Resolved)
# 2. Is there any requirements for time complexity and space complexity?

## Thought Process:

# Good Code:
# 1. Make the time and space complexity to be in the form of O(n) || O(1)
# 2. Iterate through list_1 and use if-else to check for duplicates in list_2; This case will avoid nested loops for iterating over multiple lists and also to avoid O(n^2).
# 3. Implement if-else -> O(1) and check the condition for the matching letters to matched list and not_matched to the respective list itself.

# Bad Code:
# 1. Implementing nested loop is not a good complexity for this case since we want to get the results in good complexity: O(n) || O(1)

## Goals:
# 1. Make it readable
# 2. O(n) || O(1) -> Time and Space complexity


list_1 = ['a','b','r','e','c'] # Time Complexity: O(1) and Space Complexity: O(1)
list_2 = ['z','a','c','h','g','i'] # Time Complexity: O(1) and Space Complexity: O(1)

match = [] # Time Complexity: O(1) and Space Complexity: O(1)

def merge_list(list_1, list_2): # Time Complexity: O(m,n) and Space Complexity: O(1)
    for elements in list_1: # Time Complexity: O(n) and Space Complexity: O(n)
        if elements in list_2: # Time Complexity: O(1) and Space Complexity: O(1)
            list_1.remove(elements) # Time Complexity: O(1) and Space Complexity: O(1)
            list_2.remove(elements) # Time Complexity: O(1) and Space Complexity: O(1)
            match.append(elements) # Time Complexity: O(1) and Space Complexity: O(1)
            print(f'The unmatched elements: {list_1 + list_2} and The matched elements are: {match}')   
            print("-------------------------List View---------------------------")
            print(f'{list_1 + list_2}, {match}')         
        else:
            print("There is no match")

merge_list(list_1, list_2)
print("The time complexity is: O(n) and Space complexity is O(n)")
