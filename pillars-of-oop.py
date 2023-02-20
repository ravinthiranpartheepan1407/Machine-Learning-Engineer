# Encapsulation: Binding Data and access them from another function
# Abstraction: Hiding the internals of a function
# Scope of Abstraction: Public and Private... Ex: _ used to specify private scope and it tells don't modify it.
# Inheritance: Used to Inherit another class features from a different class; Inherit features and pass it into another class parameters
# Polymorphism: Same function with different features
# Use SUPER to extend the features inside a class when passing another class as a parameter
# Super inherits the class passed as a parameter

_sellername = input("Enter Seller Name: ")
_sellerorg = input("Enter Seller Org: ")
selleritem = input("Create an item: ")

_username = input("Enter User Name: ")
_userorg = input("Enter user org: ")
useritem = input("Create user item: ")

class MerchantCentre:
    def __init__(self):
        print("Account Setup Processing")
    def seller_account_created(self):
        print("Setting Your Seller Account")
        return "Seller Account Created"
    def user_account_created(self):
        print("Setting Your User Account")
        return "User Account Created"

class CreateSeller(MerchantCentre):
    def __init__ (self, _sellername, _sellerorg, selleritem):
        self._sellername = _sellername
        self._sellerorg = _sellerorg
        self.selleritem = selleritem
    def create_seller(self):
        print(f'Created {self._username} for {self._sellerorg} organization')
    def create_item(char):
        print(f'{char._sellername} has created an item called {char.selleritem}')

class CreateUser(MerchantCentre):
    def __init__(self, _username, _userorg, useritem):
        self._username = _username
        self._userorg = _userorg
        self.useritem = useritem
    def create_user(self):
        print(f'Created {self._username} with {self._userorg}')
    def create_item(char):
        print(f'{char._username} has created an item called {char.useritem}')

create_seller_account = CreateSeller(_sellername, _sellerorg, selleritem)
create_user_account = CreateUser(_username, _userorg, useritem)

print("The Seller Name is: ", create_seller_account._sellername)
print("The Seller Org Name is: ", create_seller_account._sellerorg)

print("Status: ", create_seller_account.seller_account_created())

print("The User Name is: ", create_user_account._username)
print("The User Org Name is: ", create_user_account._userorg)

print("Status: ", create_user_account.user_account_created())

# Polymorphism
for char in [create_seller_account, create_user_account]:
    char.create_item()





