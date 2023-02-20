# Walrus can be created with := syntax
# It is used to assign values to a variable in terms of long expression and should be covered with ()

a = ['s','u','r','e','n']
# if ((n := len(a)) < 3):
#     print(f"Length of a is: {n}")
if ((b := a[-1]) == 'n'):
    a.append("b")
    print(f"The splitted letter is: {b}")
print(a)
