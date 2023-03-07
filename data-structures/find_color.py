# To calculate : Measure the number of ops to perform

# No. of ops == No.of Elements (For ex: 4 items in list then there's gonna be 4 ops) -> Linear Operation

# All Linear Ops have O(n) -> n can be anything / arbitrary; No.of inputs

# O(n) -> Big O depends on no.of inputs

# O(n): Iteratives

from time import time
color_input = input("Enter Color Name: ")
color_list = ["Red", "Blue", "Green", "Yellow"]
def findColor(color_input):
    timer1 = time()
    for i in color_list:
        if color_input == i:
            print(f'Found color: {i}')
            break
        else:
            print("Color not found! Try again!")
    timer2 = time()
    print(f'The time took to complete the process: {timer2-timer1} ms')
    print("This programm has linear ops so the Big-O complexity is O(n)")

findColor(color_input)