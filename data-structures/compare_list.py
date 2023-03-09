## Clarifications:

# 1. Regarding data_1 && data_2; data_3 && data_4 the inputs are clear
# 2. Output expections are also clear for both data_1 && data_2; data_3 && data_4

## Thought Process:

# Bad Code: ()
# 1. Implementing for loop checking a match by iter thorugh data_1 and data_2 as seperate ops will create nested loop and results in O(n^2)

# Good code:
# 1. Merge data_1 and data_2 && simulatenously for data_3 and data_4
# 2. Have to implemente for loop to iteratie through the lists merged list: O(n) and if-else to check count > 1 :O(1)
# 3. If there is a match print true or false
# 4. This ops will result in O(n+n) -> O(n)

## Goals:
#1. Make it readable
#2. Excellent time and space complexity: O(n) or O(1)
#3. Find a way to balance both rule 1 and rule 2

data_1 = ['a', 'b', 'c', 'x'] #Time: O(1) #Space: O(1)
data_2 = ['z','b','i'] #Time: O(1) #Space: O(1)

match_1 = []
match_2 = []

data_3 = ['a', 'b', 'c', 'x'] #Time: O(1) #Space: O(1)
data_4 = ['z','y','a'] #Time: O(1) #Space: O(1)

def merge_1():
    for i in data_2: #Time: O(n) #Space: O(1)
        data_1.append(i) #Time: O(1) #Space: O(1)
    print(data_1) #Time: O(1) #Space: O(1)

    for i in data_1: #Time: O(n) #Space: O(1)
        if data_1.count(i) > 1: #Time: O(1) #Space: O(1)
            match_1.append(i)
            print("Match Found in data_1 and data_2: ", match_1)
            break
        else:
            match_1.append(None)
            print("No match Found")

def merge_2():
    for i in data_4: #Time: O(n) #Space: O(1)
        data_3.append(i) #Time: O(1) #Space: O(1)
    print(data_3) #Time: O(1) #Space: O(1)

    for i in data_3: #Time: O(n) #Space: O(1)
        if data_3.count(i) > 1: #Time: O(1) #Space: O(1)
            match_2.append(i) #Time: O(1) #Space: O(1)
            print("Match Found in data_3 and data_4: ", match_2)
            break
        else:
            match_2.append(None) #Time: O(1) #Space: O(1
            print("No Match Found")

merge_1()
merge_2()


print("The time complexity is: O(n+n) -> O(n)")

