alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Prompt the user to choose between encryption or decryption and convert the input to lowercase
direction = input("Type 'encrypt' for encryption or 'decrypt' for decryption: ").lower()

# Prompt the user to input the message
user_text = input("Type your message: ")

# Prompt the user to input the shift value and convert it to an integer
shift_value = int(input("Enter the shift key: "))

# Define the Caesar Cipher function with parameters: text, shift, and direction
def caesar_cipher(text, shift, direction):
    # Initialize an empty list to store the result
    result = []

    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an alphabetical letter
        if char.isalpha():
            # Find the index of the character in the alphabet
            char_index = alphabet.index(char)
            
            # Check if the direction is 'encrypt' or 'decrypt' and perform the shift accordingly
            if direction == 'encrypt':
                new_index = (char_index + shift) % 26
            elif direction == 'decrypt':
                new_index = (char_index - shift) % 26
            
            # Retrieve the new character after the shift and append it to the result list
            new_char = alphabet[new_index]
            result.append(new_char)
        else:
            # If the character is not an alphabetical letter, append it as is to the result list
            result.append(char)

    # Print the result as a string after encryption or decryption
    print(f"Text after {direction}: {''.join(result)}")

# Call the Caesar Cipher function with user-input values
caesar_cipher(user_text, shift_value, direction)
