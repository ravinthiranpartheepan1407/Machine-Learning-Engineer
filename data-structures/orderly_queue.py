# You are given a string s and an integer k. 
# You can choose one of the first k letters of s and append it at the end of the string..

# Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

# Breakdown:

# 1. Create an input var for getting the string
# 2. Create an inout with int type for accessing the char index.
# 3. Iterate through the string
# 4. Get the char from string using it's index.
# 5. Iterate the chars order until the selected char index ends in -1

strings = input("Enter a string: ")
index = int(input("Enter an index: "))
queue = []

def orderly_queue(strings, index):
    for chars in range(len(strings)):
        queue.append(strings[chars])
    
    get_char = queue[index]
    print(f'The char we want to shift it to last index: {get_char}')

    for elements in range(0,len(queue),1):
        if index < len(queue):
            pick_char = queue.pop(elements)
            print(f'Char added to last index is: {pick_char}')
            queue.append(pick_char)

orderly_queue(strings, index)
print(queue)
