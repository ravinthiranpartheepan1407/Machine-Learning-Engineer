# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Breakdown:

# 1. Create list_1 and list_2 with some multiple same value in the type of int
# 2. Megre list_1 and list_2
# 3. Iterate through merged_list and check for duplicates with the complexity of O(n)
# 4. If any element count us > 1 then push it to duplicate list.

list_1 = [1,1,1,3,3,4,3,2,4,2]
list_2 = [1,2,3,1,7]

duplicate_items = []
unique_items = []

def linked_list_duplicate(list_1, list_2):
    try:
        linked_list = list_1 + list_2
        # print(linked_list)
        for items in linked_list:
            if linked_list.count(items) > 1:
                duplicate_items.append(items)
                print(True)
                # break
            elif linked_list.count(items) <= 1:
                unique_items.append(items)
            else:
                print(False)
            
    except:
        raise ValueError("Enter a number dude!")

linked_list_duplicate(list_1, list_2)
print(f'The duplicate elements are: {duplicate_items}')
print(f'The unique elements are {unique_items}')

        

