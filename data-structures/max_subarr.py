# Given an integer array list, find the subarray with the largest sum, and return its sum.

# Breakdown:

# 1. Create a list
# 2. Create a max number var
# 3. Create a current element var
# 4. Iterate through list
# 5. if the current ele is < 0 then set it to 0 else set it to the value
# 6. if current > max the set the max = current

list = [-2,1,-3,4,-1,2,1,-5,4]
total = []

def max_subarr(list):
    # for i in list: # O(n) sum  of an array
    #     total.append(i)
    #     print(sum(total))

    for i in range(1,len(list)): # Start = 1  and Stop = 9
        list[i]=max(list[i-1]+list[i],list[i]) # list[1] = 1; max(list[0] + list[1], list[1]) -> (1,1) -> (1,1): 1
        print(list[i])
        # max((list[1] + list[2]), lis[2] -> -2
        # max((list[2] + list[3]), lis[3] -> 4
        # max((list[3] + list[4]), lis[4] -> 3
        # max((list[4] + list[5]), lis[5] -> 5
        # max((list[5] + list[6]), lis[6] -> 6
        # max((list[6] + list[7]), lis[7] -> 1
        # max((list[7] + list[8]), lis[8] -> 5
        # max((list[8] + list[9]), lis[9] -> 6
        total.append(list[i])

    # for j in list:
    #     if j > 0:
    #         total.append(j)
    #         print(total)
    #     else:
    #         list.remove(j)
    #         total.append(j)
    # print(sum(total)) 


max_subarr(list)
print(f'The max value of sub list is: {max(total)}')
