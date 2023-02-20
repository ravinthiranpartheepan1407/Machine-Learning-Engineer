# Methods: In, Count, Sort, Copy, reverse, range, Join

# In return a boolean value if the element is present in the list or not present in the list
data = ["Hello", "My", "Name", "Is", "Suren"]
check_in = "Hello" in data
print(check_in)

# Count checks how many times a requested element is present in the list
check_count = data.count("Suren")
print(check_count)

# Sort used to sort the element in an alphabetical order; It doesn't return any value
alphabet = ['a', 'z', 'e', 'i', 'h']
alphabet.sort()
print(alphabet)

# Copy used to copy a list; It can return a value
copy_alphabet = alphabet.copy()
print(copy_alphabet)

# Reverse used to order the elements in a list in a reverse order; It doesn't return any value
reverse_alphabet = alphabet.reverse()
print(alphabet)

# Range used to specify a certain range of values; It can return a value
range_numbers = range(100) # Start and Stop Value
print(range_numbers)

# Join used to merge a list of elements with existing elements; It can return a value
alphabet_join = "  ".join(["Hello", "Suren", "!"])
print(alphabet_join)