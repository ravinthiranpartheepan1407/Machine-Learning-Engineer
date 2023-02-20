# *args -> can only takes value (Tuples)
# **kwargs(Keyword Args) -> can take dictionary (Key and values)

age = input("Enter Number1: ")
userid  = input("Enter Number2: ")

def test(*age, **userid):
    print(age)
    print(userid)

print(test(age, userid1=userid))
    