# Brekadown:

# 1. Create an empty dict
# 2. create var for storing target
# 3. Create list with non negative int
# 4. use enum to index each elements in list

target = int(input("Enter a number: "))
list = [4,8,7,6,3]
def tw_eq_sum(target, list):
    pairs = {}
    for key, value in enumerate(list):
        sum = target - value # 9-4 = 5; 9-8 = 1; 9-7 = 2; 9-6 = 3; 9-3 = 6
        print(sum)
        if sum in pairs:
            print(pairs[sum], key)
        pairs[value] = key

tw_eq_sum(target, list)

