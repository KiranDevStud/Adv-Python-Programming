def get_integer_input():
    try:
        user_input = input("Enter an integer: ")
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

get_integer_input()
