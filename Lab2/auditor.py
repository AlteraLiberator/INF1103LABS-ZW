inventory = 0
rejectedEntries = 0

# Main Program Loop
while True:
    mainMenu = input("Enter stock quantity, or 'quit' to exit: ").lower()

    # Exit the program if the user types 'quit'
    if mainMenu == "quit":
        break

    # Check if the input is a valid number
    if mainMenu.isdigit():
        inventory += int(mainMenu)
        print(f"Current inventory: {inventory}")
    else:
        print("Invalid input. Please enter a number or 'quit'.")
