def access_list_element():
    my_list = [10, 20, 30, 40, 50]
    try:
        index = int(input("Enter an index to access (0-4): "))
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Please enter a valid integer.")

access_list_element()
