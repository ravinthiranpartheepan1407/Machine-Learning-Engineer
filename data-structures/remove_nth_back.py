# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Breakdown:

# 1. Create a list with int type
# 2. Iterate through the list from range(len(int_list))
# 3. Remove the given nth element as n = input()

int_list = [1,2,3,4,5]
node = int(input("Enter an integer: "))

removed_node = []

def remove_nth_item_back(int_list, node): # The complexity is O(n)
    for _ in range(len(int_list)):
        remove = int_list[-node]
        removed_node.append(remove)
        existing_nodes = list(set(int_list) - set(removed_node))
        # if removed_node in int_list:
        #     int_list.remove()
        print(f'The removed node is {removed_node} and the remaining nodes are {existing_nodes}')
        break

remove_nth_item_back(int_list, node)

