# Breakdown:

# 1. Create list_1 and list_2
# 2. Implement for loop to iterate thorugh each lists and store the merge in a list if the complexity req is O(m+n)
# 3. If the complexity is O(1) then concat the two lists

list_1 = [0,3,4,31]
list_2 = [4,6,30]

merged_list = []

def merge_sorted_arr(list_1, list_2): # O(1)
    sort = list_1 + list_2
    merged_list.append(sort)

def merge_sort_arr(list_1, list_2): # O(m+n)
    for i in list_1: # O(m)
        merged_list.append(i)
    for j in list_2: # O(n)
        merged_list.append(j)

    print(sorted(merged_list))
    
def merge_sorted_array(list_1, list_2): # O(n^2)
    for i in list_1:
        for i in list_2:
            sort = sorted(i)
            merged_list.append(i)            
            break

merge_sort_arr(list_1, list_2)
merge_sorted_arr(list_1, list_2)
merge_sorted_array(list_1, list_2)
# print(merged_list)