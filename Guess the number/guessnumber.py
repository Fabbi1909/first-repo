import random

secret_number = random.randint(1, 10)

while True:
    try:
        number = int(input("Guess the number I'm thinking of (1–10): "))

        if number < 1 or number > 10:
            print("Please enter a number between 1 and 10.")
        elif number > secret_number:
            print("Too high!")
        elif number < secret_number:
            print("Too low!")
        else:
            print("You got it! 🎉")
            break  # stop loop once guessed correctly

    except ValueError:
        print("Please enter a valid number.")
