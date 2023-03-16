# Breakdown:

# 1. Create list_1 and list_2 with typeof int
# 2. Loop through list_1 and list_2 with complexity of O(n)
# 3. merge both list
# 4. Find the max

list_1 = [-2,1,-3,4,-1,2,1,-5,4]
list_2 = [5,4,-1,7,8]

merge_arr = []
max_sub_element = []

def linked_max_subarr(list_1, list_2):
    link_list = list_1 + list_2
    print(len(link_list))
    merge_arr.append(link_list)
    for elements in range(1,len(link_list)): #Start=1 and Stop=14 O(n)
        link_list[elements] = max(link_list[elements-1] + link_list[elements], link_list[elements]) # O(n)
        print(link_list[elements])
        max_sub_element.append(link_list[elements])

linked_max_subarr(list_1, list_2)
print(f'The max element in sub array is: {max(max_sub_element)}')
print(f'The merged list is: {merge_arr}')

