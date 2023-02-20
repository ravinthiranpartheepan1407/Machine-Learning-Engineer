name = input("Enter Your Name: ")
health = int(input("Enter Player A Health: "))
BHealth = int(input("Enter Player B Health: "))

bullets = int(input("Enter Player A bullets: "))
Bbullets = int(input("Enter Player B bullets: "))

class SuperList(list):
    def __name__(self, name) -> str:
        self.name = name
        return self.name

super_list_1 = SuperList(name)
super_list_1_append = super_list_1.append("Suren")
print("The name is: ", super_list_1.name)
print("The Appended name is: ", super_list_1_append[0])

class PlayerA:
    def __init__(self, bullets, health):
        print("Added Player A Power")
        self.bullets = bullets
        self.health = health
    def health_check(self):
        if self.health < 10:
            print("Player B wins")
        else:
            print("Player A won the game")

class PlayerB:
    def __init__(self, Bbullets, Bhealth):
        print("Added Player B Power")
        self.Bbullets = Bbullets
        self.Bhealth = Bhealth
    def Bhealth_check(self):
        if self.BHealth < 10:
            print("Player A wins")
        else:
            print("Player B won the game")

class Attack(PlayerA, PlayerB):
    def __init__(self, bullets, health, Bbullets, Bhealth):
        PlayerA.__init__(self, bullets, health)
        PlayerB.__init__(self, Bbullets, Bhealth)
        print("Fight Started")

attacking = Attack(health, bullets, BHealth, Bbullets)
print(f'The Player A attacking with {attacking.bullets} bullets')
print(f'The Player B attacking with {attacking.Bbullets} bullets')