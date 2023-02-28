from random import randint
value = int(input("Enter a number: "))
guess = randint(0,10)
while True:
    try:
        if value > 0 and value < 11:
            print("Valid number range!")
            if value == guess:
                print(f'Your Guess is Correct! {guess} == {value}')
                break
            else:
                print(f'Your Guess is not Correct. The number is {guess}')
        break
    except:
        raise ValueError("Please Enter a Number")
    