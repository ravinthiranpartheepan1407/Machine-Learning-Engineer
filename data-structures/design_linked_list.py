# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

# A node in a singly linked list should have two attributes: val and next. 
# val is the value of the current node, and next is a pointer/reference to the next node.

# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. 
# Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. 

# After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 

# If index equals the length of the linked list, the node will be appended to the end of the linked list. 
# If index is greater than the length, the node will not be inserted.

# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

# Breakdown:

# 1. Create input var
# 2. Create empty list
# 3. Create head function
# 4. cretae tail function
# 5. create insert function
# 6. Create get function
# 7. create delete function
# 8. create update function

values = [5,8,9,11,2,13]

head = int(input("Enter head value: "))
tail = int(input("Enter tail value: "))

insert_index = int(input("Enter insert index: "))
insert_val = int(input("Enter a value to insert: "))

delete_index = int(input("Enter a index to delete: "))

update_index = int(input("Enter a index to update: "))
update_value = int(input("Update Value: "))

get_index = int(input("Enter a index to get: "))

linked_design = []

class Head:
    def __init__(self, head):
        self.head = head
        linked_design.append(head)
        print(f'The head created at the index {len(linked_design)-len(linked_design)} and value is {linked_design[0]}')

class Tail:
    def __init__(self, tail):
        self.tail = tail
        linked_design.append(tail)
        print(f'The tail created at the index {len(linked_design)} and value is {linked_design[-1]}')

def append(values): #O(n)
    for items in range(len(values)): 
        linked_design.append(values[items])

def insert(insert_index): #O(n)
    for _ in range(insert_index, insert_index+1,1):
        linked_design.insert(insert_index,insert_val)
        print(f'The inserted index is {insert_index} and the value is: {linked_design[insert_index]}')

def delete(delete_index): #O(n)
    for _ in range(delete_index, delete_index+1,1): 
        delete_value = linked_design.pop(delete_index)
        print(f'The deleted index is {delete_index} and the value is: {delete_value}')  
        linked_design.insert(delete_index, "NULL")  

def get(get_index): #O(1)
    print(f'The fetched index is: {linked_design[get_index]}')
    # for items in range(len(linked_design)):
    #     if linked_design[get_index] == linked_design[items]:
    #         print(linked_design[get_index])
    #         break

def update(update_index, update_value): #O(n)
    for _ in range(update_index, update_index+1,1):
        pop = linked_design.pop(update_index)
        update_values = linked_design.insert(update_index,update_value)
        print(f'Index {update_index} updated to value {linked_design[update_index]}')

head_val = Head(head)
append(values)
insert(insert_index)
delete(delete_index)
tail_val = Tail(tail)
get(get_index)
update(update_index, update_value)
print(f'The final design of this linked list is: {linked_design}')









        