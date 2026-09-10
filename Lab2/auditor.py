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

        # Check if the number is non-negative
        if int(mainMenu) < 0:
            print("Please enter a non-negative number.")
            rejectedEntries += 1
            # Re-prompt the user for input in next iteration of the loop
            continue

        inventory += int(mainMenu)

        # Check for inventory overflow
        if inventory > 500:
            print("Alert! Current inventory is above 500 units! Exiting...")
            break

        print(f"Current inventory: {inventory}")
    else:
        print("Invalid input. Please enter a number or 'quit'.")