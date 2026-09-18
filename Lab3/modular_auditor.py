# Initialising global constants
INVENTORY_CAPACITY = 500
TAX_RATE = 0.09     # 9% GST lul
VALUE_PER_UNIT_ITEM = 120   # Has to have value to be taxed


# Functions

# Get user input (Returns either boolean or tuple)
def get_valid_input():

    # Initialise variables
    user_input = ""
    rejected_entries = 0

    # Mini while loop to ensure that we do not return invalid input
    while True:

        # Get user input
        user_input = input("Enter stock quantity, or 'quit' to exit: ")

        # Validate input
        if user_input == "quit":
            return False

        # If user entered a non-positive number that isnt 'quit'
        if not user_input.isDigit():
            # Add failed counter to global variable rejectedEntries
            rejected_entries += 1

            # Note isdigit() will not count -ve numbers input as number as "-1".isdigit() will count the "-" as a non digit character, thus failing the check
            print("Invalid input. Please enter a positive number or 'quit'.")
            pass

        # If user entered 0
        if int(user_input) == 0:
            # Add failed counter to global variable rejectedEntries
            rejected_entries += 1
            print("Invalid input. Please enter a positive number or 'quit'.")
            pass

        # Return proper(This does break the loop)
        return (int(user_input), rejected_entries)

# Adds delivery to current inventory (returns new total)
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

# Calculates and returns the tax on the delivery
def calculate_tax(delivery_amount):
    # initialise variables
    tax = 0

    tax = delivery_amount * VALUE_PER_UNIT_ITEM * TAX_RATE

    return tax

# Generates the text string for the report (DOES NOT PRINT)
def generate_report(inventory_units, rejected_entries):

    # Initialise variables
    report = ""
    report += "Final Session Report\n"
    report += "Total units in store: {}.\n".format(inventory_units)
    report += "Failed entry attempts: {}.\n".format(rejected_entries)

    return report

def main():

    # Initialise variables
    inventory = 0
    total_failed_attempts = 0

    # Start of main loop
    while True:
        user_input = get_valid_input()

        # get_valid_input returned false (user entered quit)
        if not user_input:
            print(generate_report(inventory, total_failed_attempts))
            break

        delivery_units, rejected_user_inputs = user_input
        total_failed_attempts += rejected_user_inputs

        process_delivery(inventory, delivery_units)



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


