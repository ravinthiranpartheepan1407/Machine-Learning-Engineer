# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.

dial = input("Enter numbers to dial: ")

def phone_no_combination(dial):
    dial_pad = {
        '1': '_',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    contact = []

    for numbers in dial:
        get_strings = dial_pad.get(numbers)
        contact.append(get_strings)
    print(contact)

    start_index = 0
    end_index = 0
    for items in range(0, len(contact)+1):
        iterate_chars = contact[start_index][end_index] + contact[start_index+1][end_index]
        end_index = end_index + 1
        print(iterate_chars)
        continue
        

phone_no_combination(dial)