# For ex: I gave input value as 10
# O(n): Iteratives
# O(1): assignments

### Note: Drop constants and Drop Non-Dominants to reduce the complexity

from time import time

input = int(input("Enter a number: ")) #O(1)
numbers = [] #O(1)

def main(input):
    timer_1 = time() #O(1)
    for i in range(input): # O(n)
        print(f'Complexity O({i}n)') #O(1)
        numbers.append(i) #O(n)
    
    print(numbers[:1])

    first_half = input/2 #O(1)
    print(first_half) #O(1)
    timer_2 = time() #O(1)
    print(f'Time took to complete the ops is {timer_2-timer_1}') #O(1)

main(input) #O(1)

### Note: Drop constant reduce the complexity
print("Total no.of O(n) is 10 and no.of O(1) is 9 (Constant)")

print("The final complexity is O(n)")


                