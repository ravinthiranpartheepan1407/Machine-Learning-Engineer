#Map: Takes Func as 1st param and Iterables as 2nd param
#Filter: Used to Filter Specific Data; Takes Func as 1st param and Iterables as 2nd param
#Zip: Used to Merge Two Data, List, Tuples...; Takes data as 1st param and another data Iterables as 2nd param
#Reduce:

# Maps
game = str(input("Enter Games: "))
price = int(input("Enter Game Price: "))
check = str(input("Search Game: "))
new_game = []
def add_games(game):
    new_game.append([game])
def check_price(price):
    return price*4
print(list(map(add_games, [game])))
print(list(map(check_price, [price])))

#Filter
def is_game_available(new_game):
    if game == new_game:
        print("Game Available")
        return new_game
    else:
        print("Game not found")
        print("Enter Game To Library")
        add_games(game)
        print("Game Added")
print(list(filter(is_game_available, [check])))

#Zip
print(list(zip(game, str(price))))




