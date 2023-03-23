# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Breakdown:

# 1. Create an int typed input var
# 2. Implement a loop to perform iterative process
# 3. Create an empty list for appending the iterated results

parantheses_value = int(input("Enter a value: "))

generated_parantheses = []

def gen_parantheses(parantheses_value): # Linear time complexity O(n) because of indefinite input range and appending range
    for _ in range(parantheses_value):
        generate = "()"
        generated_parantheses.append(generate)

gen_parantheses(parantheses_value)
print(generated_parantheses)