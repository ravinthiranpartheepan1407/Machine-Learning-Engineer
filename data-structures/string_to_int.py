# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.

# Breakdown:

# 1. Create a variable for input with the type of string
# 2. Check conditions if there are signed int format. If -vely signed, then the result should be in -ve else by default it's positive if there is no sign
# 3. Remove whitespaces if present
# 4. Iterate thorugh string and convert them into an int.

string_data = [" -42", " -619", "72", "-56", "108"]

def string_to_int(string_data):
    int_data = ""
    for digits in range(0,len(string_data),1):
        string_data[digits].replace(" ","")
        if int(string_data[digits]) < 0:            
            int_data = string_data[digits].replace(" ","")
            print(f'Negative Integer: {int_data}')
        else:
            int_data = string_data[digits].replace(" ","")
            print(f'Positive Integer: {int_data}')

string_to_int(string_data)