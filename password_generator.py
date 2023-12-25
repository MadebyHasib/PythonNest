# Import the 'random' module to generate random elements.
import random

# Print a welcome message for the user.
print("Welcome to the PyPassword Generator!")

# Define lists containing letters, numbers, and symbols.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get user input for the number of letters, symbols, and numbers in the password.
num_letters = int(input("Enter the number of letters: "))
num_symbols = int(input("Enter the number of symbols: "))
num_numbers = int(input("Enter the number of numbers: "))

# Combine all the character lists into one list.
all_chars = letters + numbers + symbols

# Calculate the total password length based on user input.
password_length = num_letters + num_symbols + num_numbers

# Generate a list of randomly selected characters for the password.
password_chars = [random.choice(all_chars) for _ in range(password_length)]

# Shuffle the order of characters in the password.
random.shuffle(password_chars)

# Combine the characters into a string to create the final password.
password = ''.join(password_chars)

# Display the generated password to the user.
print(f"Your password is: {password}")


