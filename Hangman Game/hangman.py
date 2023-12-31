import random
from hangman_art import stages, logo

# List of words for the hangman game
word_list = ["pizza", "burger", "pasta", "chocolate", "icecream"]

# Select a random word from the word list
chosen_word = random.choice(word_list)

# Initialize the display with underscores for each letter in the chosen word
display = "_" * len(chosen_word)

# List to store guessed letters
guessed_letters = []

# Initial number of lives for the player
lives = 6

# Welcome message
print("Welcome to Hangman!")

# Display the hangman logo
print(logo)

# Main game loop
while True:
    # Display the current state of the word and remaining lives
    print(f"\nWord: {display}")
    print(f"Lives: {lives}")

    # Get a letter guess from the player
    guess = input("Guess the letters: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed the letter. Try again")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is not in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! {lives} lives remaining.")
    else:
        print("Correct guess!")

        # Update the display with correctly guessed letters
        display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

    # Display the hangman stages based on the remaining lives
    print(stages[lives])

    # Check if the player has guessed the entire word
    if "_" not in display:
        print(f"Congratulations! You guessed the word: {chosen_word}")
        break

    # Check if the player has run out of lives
    if lives == 0:
        print(f"Sorry, you ran out of lives. The word was {chosen_word}")
        break

