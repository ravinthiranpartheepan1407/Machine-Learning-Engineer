some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicates:
            duplicates.append(i)
    
print(duplicates)

duplicate = ['a','b','c','b','d','m','n','n']
unique = []
for i  in duplicate:
    if duplicate.count(i) <= 1:
        unique.append(i)
print(unique)
