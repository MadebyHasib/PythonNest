# Initialize the result variable to None.
result = None

# Continue looping indefinitely.
while True:
    # If the result is None, prompt the user to input the first number,
    # an operator, and the second number.
    if result is None:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+ - * /): ")
        num2 = float(input("Enter the second number: "))
    # If the result is not None, use the previous result as the first number,
    # and prompt the user to input an operator and the second number.
    else:
        num1 = result
        operator = input("Enter an operator (+ - * /): ")
        num2 = float(input("Enter the second number: "))

    # Perform the arithmetic operation based on the operator provided.
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Check if the second number is not zero to avoid division by zero.
        if num2 != 0:
            result = num1 / num2
        else:
            # If the second number is zero, print a message indicating it's not possible.
            print("Cannot divide by zero.")
    else:
        # If an invalid operator is provided, print a message indicating so.
        print("Invalid operation!")

    # Display the arithmetic expression and the result.
    print(f"{num1} {operator} {num2} = {result}")

    # Ask the user if they want to continue or not.
    user_input = input("Do you want to continue? (yes/no): ")
    # If the user enters 'no', break the loop to exit.
    if user_input == "no":
        break
