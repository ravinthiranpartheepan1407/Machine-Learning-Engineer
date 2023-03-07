# O(1) : Process only one item in the list no matter how many items are there in a list.
# O(1): Has excellent Big-O complexity
# No.of elements Process = 1 (Only one) and the ops going to be flat; it cannot concurrenlty run iterative process for the elements

# O(1): assignments

def big_O_1():
    list = ["Red", "Blue", "Green"]
    # One op: #O(1)
    print(list[0]) 
    # One op: #O(1)
    print(list[1]) # Totally O(2) -> Two ops (Constant time per elements: O(1): list[0] + O(1): list[1] = O(2))

big_O_1()
print("Totally O(2) -> Two ops (Constant time per elements: O(1): list[0] + O(1): list[1] = O(2))")
    

