# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty. 
# Words may also contain numbers, for example "Hello world123 567"

# Breakdown:

# 1. Create a list for storing string
# 2. Create a list for regex (Special chars identification)
# 3. Iterate through loop on list1 and if the list contains special chars exclude it it during count
# 4. Return max

import re

list = ["Hello Ravinthiran", "Hello My Friend", "Hello Suren"]
# special_char = re.compile(r'\W\s')
length = []

def find_longest_string(list): # This code block has the time complexity of O(n^2) which is the worst case
    for items in range(len(list)):
        # print(list[items])
        join = list[items].replace(" ","")
        len_string = len(join)

        length.append(len_string)              
        
        # Visualization in key-value pair
        find = {
            'String': join,
            'Length': len_string
        }
        # print("Viuslaization in key-value pair", find)

        # Get key and value; Return max value from the value field aong with it's key
        key = find.get("String")
        value = find.get("Length")
        if value == max(length):
            print(f'The string {key} has max length of {value}')
        else:
            print(None)

def find_long_string(list): # This block has good time complexity of o(n)
    max_len = 0
    string = ""
    for items in list:
        join = items.replace(" ","")
        length = len(join)
        if length > max_len:
            max_len = length
            string = join
    if max_len:
        print(f'This string {string} has a max length of {max_len}')
    else:
        print(" ")
        

find_longest_string(list)
find_long_string(list)