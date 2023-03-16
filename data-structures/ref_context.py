# Reference Type: Reference a var to another var
# Context Type: Login inside a particular scope
# Instantiation: Access the referenced var from ref type instantiation

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

name_db = ["Suren", "Ravi"]
waiting_list = []

class Attrib:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
    
    def checkName(self):
        try:
            if self.name in name_db:
                print("Your have registered already dude!")
            else:
                print("Please register your name")
                # name_db.append(name)
                storage = {'name': name, 'age': age}
                waiting_list.append(storage)
                print("We have added you to our waiting list DB:", waiting_list)
        except:
            raise ValueError("Please Enter a String")

class CheckCriteria(Attrib): # Class Reference
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    def checkAge(self): # Class Scope or Context
        try:       
            if self.age > 18 and self.age < 21:
                print("You are eligible to join Group A")
            elif self.age > 21:
                print("You are eligible to join Group B")
            else:
                print("You are not eligible")
        except:
            raise ValueError("Please Enter your age in number dude!")

student = CheckCriteria(name, age) # Class Instantiation
student.checkAge()
student.checkName()