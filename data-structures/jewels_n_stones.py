# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
# Each character in stones is a type of stone you have. 
# You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Breakdown

# 1. Create a list for jewels
# 2. Create a input var for stones
# 3. Iterate through jewels list
# 4. Check if input "stone" elements match with the jewels then print the Found elements
# 5. Else not stones found

jewels = "aA"
stones = str(input("Enter the stones you have: "))

your_stones = []

def jewels_n_stones(jewels, stones):
    for items in range(len(stones)):
        print(stones[items])
        if stones[items] in jewels:
            print(f'Your stones: {stones[items]}')
            your_stones.append(stones[items])
            continue
        else:
            print("No Stones")

jewels_n_stones(jewels, stones)
print(f'You have {len(your_stones)} stones with you')
