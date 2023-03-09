### Space complexity

list = [1,2,3,4,5] #O(1) allocation and var
n = int(input("Enter a number: ")) # allocation and var

def excellent_complexity(): 
    # allocation and var
    if n == 2 and n in list: #O(1): Because the range is not iteartive; # without else (Else added then it will be O(n))
        print("Data Found")   
    #(Alt)
    check_condition = bool(n==2) #O(1): Poor Readbility
    check_in = bool(n in list)  #O(1)
    print(check_in and check_condition) #O(1)
    # else: 
    #     print("data not found!")

def good_complexity(n): # O(n) because its an iterative process
    for i in range(n): 
        print(f'The space complexity will be: O({i}n) so the space complexity will be O(n)')

excellent_complexity() # Function calls O(1) because it takes no params and it return a linear value
good_complexity(n) # Function call O(n) because it takes no.of ops

