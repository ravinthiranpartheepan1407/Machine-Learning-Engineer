# You are given the head of a linked list containing unique integer values and 
# an integer array nums that is a subset of the linked list values.

# Return the number of connected components in nums where two values are connected 
# if they appear consecutively in the linked list.

# Breakdown:

# 1. Create a check_list with int type
# 2. Create an input list with int type
# 3. Itertate through check_list
# 4. Check if the input_list items are in check_list if yes print the match else print the unmatched element

head = [0,5,7,9,11,13,5]
input_num = [20,13,7,9,2,5]

connected = []
not_connected = []

def linked_list_components(head, input_num):
    merge = set(head+input_num)
    for values in range(len(head)):
        if head[values] in input_num:
            connected.append(head[values])
            get_not_connected = list(set(merge) - set(connected))
            print(f'The connected nodes are: {connected} and the not connected nodes are: {get_not_connected}')
        else:
            print("No connected nodes")
        
linked_list_components(head, input_num)

