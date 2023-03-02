from random import randint
guess_input = int(input("Enter your Guess: "))
def guess_number(guess_input):
    magic_num = randint(0,10)
    try:
        if guess_input == magic_num:
            print(f'Yo! your guess is correct: {guess_input} and the magic number is also {magic_num}')
        else:
            print(f'Your guess is not correct: {magic_num} Try again!')
    except:
        raise ValueError("Please Enter a Number Dude!")

guess_number(guess_input)