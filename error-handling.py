# https://docs.python.org/3/library/exceptions.html

meal = str(input("Enter Meal Name: "))

while(True):    
    try:
        pay = int(input("Pay the price: "))
        print(pay)
    except ValueError:
        print("Pay the Meal Price: ")
    except ZeroDivisionError:
        print("Your payment should not be Nil")
    else:
        print(f'Thank you for your ordering {meal}!')
        break