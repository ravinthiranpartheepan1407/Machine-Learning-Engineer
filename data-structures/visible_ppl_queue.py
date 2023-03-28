# There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. 
# You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

# A person can see another person to their right in the queue if everybody in between is shorter than both of them. 
# More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

# Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

# Breakdown:

# 1. Create a list of ppl with int type
# 2. Iterate through list and process the index[0]
# 3. If index[0] < index[n+1...] then print index[0] can see the index[n+1..]
# 4. else print(not able to see)

person_index = int(input("Enter person index: "))
peoples = [4,5,2,3,7,8,1]
visibility = []
def visible_ppl_queue(peoples):
    for person_count in range(person_index,len(peoples),1):
        if peoples[person_count] < peoples[person_count+1]:
            visibility.append(peoples[person_count+1])
            print(f'The person {person_index} able to see {visibility}')
            # print(f'The person {peoples[person_count]} can see {peoples[person_count+1]}')
            continue
        else:
            print("Not able to see others")
        break
        

visible_ppl_queue(peoples)
# print(f'The person {person_index} able to see {visibility}')
