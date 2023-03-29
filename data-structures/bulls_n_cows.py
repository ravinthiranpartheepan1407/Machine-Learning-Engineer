# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. 
# When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
# Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
# Note that both secret and guess may contain duplicate digits.

# Breakdown:

# 1. Create a input var with int type -> Guess
# 2. Generate 8bit rand integers as secret
# 3. Iterate through secret and check if there is any digit matches with the Guess
# 4. Print the hint (For ex: If there 1 bull then it will 1A and there are 2 cows it will be 2B -> 1A2B)

from random import randint
guess = input("Enter your guess: ")
bulls = []
cows = []

def bulls_n_cows(guess): # O(n) Complexity
    _secret = str(randint(1000,9999))
    print(f'The secret is: {_secret}')
    print("The guess is: ", guess)
    try:
        for values in range(len(_secret)):
            # print(_secret[values])
            if _secret[values] == guess[values]:
                bulls.append(_secret[values])
                count_bulls = bulls.count(_secret[values])
                print(f'Value Occurence: {count_bulls}')                
            else:
                cows.append(_secret[values])
                count_cows = cows.count(_secret[values])
                print(f'Value Occurence: {count_cows}')
    except:
        raise ValueError("Enter 8-bit numbers dude!")

bulls_n_cows(guess)
print(f'Bulls: {bulls} and the cows: {cows}')
print(f'Your hint is: {len(bulls)}A{len(cows)}B')
