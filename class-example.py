# __init_ used as a constructor or dunder method and will be called first
# Self is default which is used to access the object after instantiated.
# Self points the variable instantiated to an object and not the class name. Ex: self -> Player1, Player2....
# Self can append paramters as well.. Ex: player1.age, player1.gender
# Class takes the init parameters.

name = input("Enter Player Name: ")
scores = input("Enter Player Score: ")
age = int(input("Enter player age: "))

class CricketStats:
    # Class Object Attribute and it's static; Cannot be mutated
    is_legend = True
    is_retired = False
    def __init__(self, name, scores, age):
        if age < 40:
            self.name = name # Regular Class attribute and it's dynamic; Can be mutated
            self.scores = scores
            self.age = age
    def retired(self):
        print("Player Retired: ", self.is_retired)
        return self.is_retired

player1 = CricketStats(name, scores, age)
print("The player name is: ", player1.name)
print("The player score is: ", player1.scores)
print("Enter Player age: ", player1.age)
player1.age = 36
print("Is the player a legend? ", player1.is_legend)
print("Is the player retired: ", player1.retired())

species = input("Enter Animal Species: ")
animal_name = input("Enter Animal Name: ")
animal_age = int(input("Enter Animal Age: "))

class Animal:
    type = species
    def __init__(self, animal_name, animal_age):
        self.animal_name = animal_name
        self.animal_age = animal_age  
    def find_oldest(self):
        if self.animal_age > 40:
            print(f'{self.animal_name} will be the oldest animal age')
            return self.animal_age

animal1 = Animal(animal_name, animal_age)
print("The animal 1 name is: ", animal1.animal_name)
print("The animal1 age is: ", animal1.animal_age)
print("Species Type of an Animal: ", animal1.type)
print("The oldes age of this species is: ", animal1.find_oldest())



        