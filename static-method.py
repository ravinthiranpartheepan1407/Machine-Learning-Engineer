# Decorators can invoked with "@" symbol
# Decorators are used to declare static methods as same like Class object attribute for a var inside a class
# @classmethod takes cls as default
# @staticmethod takes self as default
# By using @staticmethod we can directly call the method through class name instead of object instantiation

name = input("Enter Food Name: ")
price = int(input("Enter Food Price: "))
class Food:
    has_discount = True
    is_available = True
    def __init__(self, name, price):
        self.name = name
        self.price = price
        if self.price > 20:
            print("Order must be greater than 20 Euros")
    
    @classmethod
    def check_availability(cls):
        print(f'Is the food available for serving? {cls.is_available}')
        return cls.is_available
    
    @staticmethod
    def check_discount(self):
        print(f'Does {self.name} has discount? {self.has_discount}')

order1 = Food(name, price)
print("The food name is: ", order1.name)
print("The food price is: ", order1.price)
print("Food Available: ", order1.check_availability())
print("Discount Applied: ", Food.check_discount(order1.has_discount))