from time import time

input_1 = int(input("Enter a number: ")) #O(1)

input_1_append = [] #O(1)
input_2_append = [] #O(1)

input_2_list = ['a','b','c','b','d','m','n','n'] #O(1)

def main(input_1): 
    timer_1 = time()
    for i in range(input_1): #O(m)
        input_1_append.append(i)
    
    for j in input_2_list: #O(n)
        if input_2_list.count(j) < 2: #O(p)
            input_2_append.append(j)
    timer_2 = time()
    print(f'The time taken for executing the ops is {timer_2 - timer_1}')
    print("The Big-O Complexity is O(m) for 1st for loop, O(n) for 2nd for loop, and O(p) for If condition")
    print(f'The complexity for second loop is O(n*p)')

main(input_1)

print("The input_1 data is:",  input_1_append) #O(1)
print("The input_2 data is:",  input_2_append) #O(1)


print(f'The complexity for first for loop is O(m)')
print(f'The complexity for second for loop is O(n*p)')
print(f'The overall complexity is O(m+(n*p))')
