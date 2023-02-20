# Enum will take a iterable objects and index the objects

for characters in enumerate("Ravi"):
    print(characters)

for index, value in enumerate("Suren"):
    print(index, value)

for i, j in enumerate({'data': 'user', 'pass': 'password'}):
    print(i,j)

for k, l in enumerate(list(range(100))):
    if l == 50:
        print("Index of 50 is:", l)