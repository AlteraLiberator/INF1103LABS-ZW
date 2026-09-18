
# Initialising global variables
inventory = 0
rejectedEntries = 0

# Functions
def get_valid_input():

    user_input = ""

    # Mini while loop to ensure that we do not return invalid input
    while True:

        # Get user input
        user_input = input("Enter stock quantity, or 'quit' to exit: ")

        # Validate input
        if user_input == "quit":
            return user_input

        if not user_input.isDigit():

            # Add failed counter to global variable rejectedEntries
            rejectedEntries += 1

            # Note isdigit() will not count -ve numbers input as number as "-1".isdigit() will count the "-" as a non digit character, thus failing the check
            print("Invalid input. Please enter a positive number or 'quit'.")
            pass

        # Return proper output (This does break the loop)
        return int(user_input)


def process_delivery(current_total, new_value):
    # Initialise variables
    overflow = False
    new_total = 0

    # Calculate the new total
    new_total = current_total + new_value

    # Check if overflow
    if new_total > 500:
        overflow = True

    # Return as tuple with overflow flag
    return (new_total, overflow)

def calculate_tax():
    pass

def generate_report():
    pass


# Main Program Loop
while True:
    mainMenu = input("Enter stock quantity, or 'quit' to exit: ").lower()

    # Exit the program if the user types 'quit'
    if mainMenu == "quit":
        break

    # Check if the input is a valid number
    if mainMenu.isdigit():
        inventory += int(mainMenu)

        # Check for inventory overflow
        if inventory > 500:
            print("Alert! Current inventory is above 500 units! Exiting...")
            break

        print(f"Current inventory: {inventory}")
    else:
        rejectedEntries += 1

        # Note isdigit() will not count -ve numbers input as number as "-1".isdigit() will count the "-" as a non digit character, thus failing the check
        print("Invalid input. Please enter a positive number or 'quit'.")

# Final report (outside loop, when client quits program)
print("Total Units Processed: {inv}\nNumber of Failed/Rejected Entries: {rejects}".format(inv = inventory, rejects = rejectedEntries))


