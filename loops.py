# items is a variable and data is an iterable varibale
# Item will iterate all the elements present in the data variable

data = input("Enter your input")
set = {"hello", "hi"}
for items in data:
    for next in set:
        print(data, next)

# Iterators can be a list, set, tuples, dict, string.
iterate_string = {"Hello"}
iterate_tupe = (1, 2, 3, 4)
iterate_list = [1, 4, 7, 10]
iterate_dict = {'data': 'User', 'pass': 'Password'}
iterate_set = {10, 20, 30, 40}

for item in iterate_string:
    for key, value in iterate_dict.items():
        for iter in iterate_set:
            print(item, key, value, iter)