# Import the random module to generate random values
import random 

# Display a welcome message for the password generator
print("Welcome to the password generator!")

# Define lists of characters that can be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Prompt the user to enter the number of letters, symbols, and numbers for the password
num_letters = int(input("Enter the number of letters: "))
num_symbols = int(input("Enter the number of symbols: "))
num_numbers = int(input("Enter the number of numbers: "))

# Create a list of characters for the password by randomly selecting from the defined character sets
password_chars = (
    [random.choice(letters) for _ in range(num_letters)] +
    [random.choice(numbers) for _ in range(num_numbers)] +
    [random.choice(symbols) for _ in range(num_symbols)]
)

# Shuffle the characters in the password list to randomize their order
random.shuffle(password_chars)

# Join the characters to form the final password
password = ''.join(password_chars)

# Display the generated password to the user
print(f"Your password is: {password}")


