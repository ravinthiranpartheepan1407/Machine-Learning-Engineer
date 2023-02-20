# It Start with local
# Set Parent local
# Then set golbal 
# Parameters considered as local
# use GLOBAL keyword to inovke a global variable inside a local

a = int(input("Enter Value: ")) # a is global
def sum(a):
    print("Sum of A is: ")
    return int(a+a)
def parent(a): # Parent is a local
    print("Number shown below :") #local
    def child():
        return int(a)
    return child()

print(parent(a))
print(sum(a))
x = "  hello world"
print(x.strip()) # Strin removes whitespaces