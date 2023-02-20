data = int(input("Enter Numbers: "))
def highest_even(data):
    odd = []
    evens = []
    if data % 2 == 0:
        evens.append(int(data))
        print(evens)
        print("Even Number")
    else:
        odd.append(int(data))
        print(odd)
        print("Odd Number")

highest_even(data)
