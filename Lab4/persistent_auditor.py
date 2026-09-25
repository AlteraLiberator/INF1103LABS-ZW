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
            return (0, rejected_entries)

        # If user entered a non-positive number that isnt 'quit'
        if not user_input.isdigit():
            # Add failed counter to global variable rejectedEntries
            rejected_entries += 1

            # Note isdigit() will not count -ve numbers input as number as "-1".isdigit() will count the "-" as a non digit character, thus failing the check
            print("Invalid input. Please enter a positive number or 'quit'.")
            continue

        # If user entered 0
        if int(user_input) == 0:
            # Add failed counter to global variable rejectedEntries
            rejected_entries += 1
            print("Invalid input. Please enter a positive number or 'quit'.")
            continue

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
    if new_total > INVENTORY_CAPACITY:
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
def generate_report(inventory_units, rejected_entries, successful_deliveries):

    # Initialise variables
    report = ""
    report += "\nFinal Session Report\n"
    report += "Total units in store: {}.\n".format(inventory_units)
    report += "Failed entry attempts: {}.\n".format(rejected_entries)
    report += "Successful deliveries: {}.\n".format(successful_deliveries)

    return report

def main():

    # Initialise "global" variables
    inventory = 0
    total_failed_attempts = 0
    total_successful_deliveries = 0

    # Start of main loop
    while True:

        # initialise internal variables
        overflow_check = False
        current_delivery_tax = 0

        delivery_units, rejected_user_inputs = get_valid_input()
        total_failed_attempts += rejected_user_inputs

        # get_valid_input first field returned 0 (user entered quit)
        if not delivery_units:
            break

        inventory, overflow_check = process_delivery(inventory, delivery_units)
        total_successful_deliveries += 1

        current_delivery_tax = calculate_tax(delivery_units)
        print("Tax needed to be paid for this delivery: {}".format(current_delivery_tax))

        # Inventory has overflowed
        if overflow_check:
            break

    # Print report when exiting application
    print(generate_report(inventory, total_failed_attempts, total_successful_deliveries))

main()


