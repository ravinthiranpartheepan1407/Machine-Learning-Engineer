# Given the head of a linked list and an integer val, 
# remove all the nodes of the linked list that has Node.val == val, and return the new head

index = int(input("Enter a value to remove from the node: "))
head = [1,2,6,3,4,5,6,6,6]

def remove_linked_list(index):
    for _ in range(len(head)):
        if index in head:
            head.remove(index)
            continue
        break

remove_linked_list(index)
print(head)
