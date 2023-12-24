# Import the 'random' module to generate random choices.
import random

# Define a list of choices for the game.
choices = ["rock", "paper", "scissors"]

# Prompt the user to input their choice (rock, paper, or scissors).
user_choice = input("Enter your choice (rock, paper, scissors): ")

# Check if the user's input is one of the valid choices.
if user_choice in choices:
    # Generate a random choice for the computer.
    computer_choice = random.choice(choices)
    
    # Print the computer's choice.
    print(f"Computer chose: {computer_choice}")

    # Check for the outcome of the game based on user and computer choices.
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        print("You win!" if computer_choice == "scissors" else "Computer wins")
    elif user_choice == "paper":
        print("You win!" if computer_choice == "rock" else "Computer wins")
    else:
        print("You win!" if computer_choice == "paper" else "Computer wins")
else:
    # Print a message for an invalid user choice.
    print("Invalid choice!")
