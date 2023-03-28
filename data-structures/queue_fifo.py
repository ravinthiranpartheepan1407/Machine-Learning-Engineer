# Design your implementation of the circular queue. 
# The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
# In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. 
# But using the circular queue, we can use the space to store new values.

insert = int(input("Enter a value to insert: "))
queue = [14,66,8,0,3,17,43]
enQueue = []
deQueue = []

class Insert:   
    def insertion(insert):
        queue.append(insert)
        
class Delete:
    def delete(queue):
        remove_first_index = queue.pop(0)         
        deQueue.append(remove_first_index)

def get(queue):
    front_val = queue[0]
    rear_val = queue[-1] 
    print(f'The front element is: {front_val}')
    print(f'The rear element is: {rear_val}')


# Iteration 1:
insert_element = Insert.insertion(insert)
delete_element = Delete.delete(queue)
get(queue)

# Iteration 2:
    # insert_element = Insert.insertion(insert)
    # delete_element = Delete.delete(queue)
    # get(queue)

# Iteration 3:
    # insert_element = Insert.insertion(insert)
    # delete_element = Delete.delete(queue)
    # get(queue)

print(f'The deQueue element is: {deQueue}')
print(f'The final circular queue is: {queue}')


