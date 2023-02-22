# Lambda is an anonymous function.
# Lamba takes param in the 1st field and results the action.

game =  input("Enter Game Title: ")
library = ["Halo"]
validate_game_title = print(map(lambda g: game in library, game))
print(game in library)

# Sort according to 3nd field
price = [(10,20,5),(10,50,10),(5,5,2),(25,5,7)]
price.sort(key=lambda val: val[2])
print(price)