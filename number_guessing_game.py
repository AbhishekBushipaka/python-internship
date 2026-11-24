
# Number Guessing Game
# CodeOrbit Tech - Python Internship

import random

print("===== NUMBER GUESSING GAME =====")

while True:
    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    # Allow the user to guess
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")

            elif guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("Congratulations! You guessed correctly.")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break
