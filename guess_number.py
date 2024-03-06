import random

# Print initial instructions for the user
print("Computer has chosen a number between 1 and 50. Try to guess it! You have 10 guesses.")

def guess_number():
    # Generate a random number between 1 and 50
    secret_number = random.randint(1,50)
    number_guess = 0 

    # Allow the user to guess up to 10 times
    while number_guess < 10:
        guess = int(input("Enter the guess number: "))  # Prompt the user to enter their guess
        number_guess += 1  # Increment the number of guesses made

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {number_guess} guesses!")
            break  # Exit the loop if the guess is correct
        # Provide hints if the guess is too high or too low
        elif guess < secret_number:
            print("Too low! Try guessing a higher number.")
        else:
            print("Too high! Try guessing a lower number.")
    else:
        print("You have used all your guesses!")  # Inform the user that they have exhausted all their guesses

# Call the function to start the game
guess_number()
