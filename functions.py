values = input("Enter character to check duplicates: ")
def check_duplicate(values):
    duplicates = []
    unique = []
    for value in values:
        if values.count(value) <= 1:
            unique.append(value)
    print("Unique Items: ", unique)

    for val in values:
        if values.count(val) > 1:
            if val not in duplicates:
                duplicates.append(val)
    print("Duplicate Items: ", duplicates)

check_duplicate(values)