# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit.
# Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

# For example, the saying and conversion for digit string "3322251":

# Breakdown:

# 1. Create a input var with type of int
# 2. Create dict with key of int(1..9) and values as (one..nine)
# 3. Iterate through the input and count int
# 4. For ex: if the input us 1211
    # 4.1 value[0] = 1 (one) + value[1] = 2 (two) -> one two -> 12
    # 4.2 value[2] = 1 (one) + value[3] = 1 (one) -> one one -> 11
    # 4.3 final -> "12" + "11" -> 1211

input_int = input("Enter a value: ")
say = []

def count_n_say(input_int):
    val_dict = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    for nums in range(len(input_int)):
        if input_int[nums] in val_dict:
            get_val = val_dict.get(input_int[nums])
            say.append(get_val)
            count_say = say.count(get_val)
            print(f"There are {count_say} {get_val}'s")
            find_max_count = max(val_dict.fromkeys(input_int[nums]))
            if count_say > 1:
                result_append = str(count_say) + str(find_max_count)
                print(result_append)

            

count_n_say(input_int)