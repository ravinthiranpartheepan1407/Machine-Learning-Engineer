# Generator functions are faster than range
# Which can be invoked with gen_functionName

num = int(input("Enter Numbers: "))
def gen_cook(num):
    for i in range(num):
        yield i

g = gen_cook(num)
print(g)
