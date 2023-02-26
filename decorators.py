# In this decorator examples we pass function as a parameter.
# Then we wrap the passed func parameter in another function
# We use decorator using @ symbol to access the method
# once we init the decorator we create another func to pass it as an argument to the parameter

# How it works?
# add_food(sambhar)

def add_food(func):
    def warp_menu():
        func()
    return warp_menu()

@add_food
def sambhar():
    print("Sambhar is available")

string_generator = str(input("Enter the string: "))
added_string = []

def add_string(func):
    def append_string(string_generator):
        func(string_generator)
    return append_string(string_generator)

#add_string(enter_string(string_generator))

@add_string
def enter_string(data):
    print(data)
    added_string.append(string_generator)
    print("The added strings are: ", added_string)

enter_string(string_generator)
