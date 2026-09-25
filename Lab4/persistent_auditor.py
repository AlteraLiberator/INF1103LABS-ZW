# Imports
from pathlib import Path

# Get current directory
current_directory = Path(__file__).parent

INVENTORY_FILE = current_directory / "inventory.txt"

# Initialising global constants
INVENTORY_CAPACITY = 500
TAX_RATE = 0.09     # 9% GST lul
VALUE_PER_UNIT_ITEM = 120   # Has to have value to be taxed


INVENTORY_ITEM_FORMAT = {
    "id":0,
    "name":1,
    "quantity":2,
    "transaction_history":3
}

TRANSACTION_HISTORY_LIMITER = "|"

# Functions

# Data logic
def load_inventory():

    inventory = []

    # Open file
    try:
        data = open(INVENTORY_FILE, "r")
    except FileNotFoundError:
        data = open(INVENTORY_FILE, "x")
        data.close()
        return []

    for line in data:
        inventory_item = line.split(",")
        inventory.append(inventory_item)

    # Return file contents as list of lists
    return inventory

# Business logic
# Get user input (Returns either boolean or tuple)
def get_valid_input():

    # Initialise variables
    user_input_item_name = ""
    user_input_item_quantity = ""
    item = []
    rejected_entries = 0

    # Mini while loop to ensure that we do not return invalid input
    
    while True:
        # Get item name
        user_input_item_name = input("Enter item name, or 'quit' to exit: ")

            # Validate input
        if user_input_item_name == "quit":
            return ([], rejected_entries, True)

        item[0] = user_input_item_name
        
        while True:
            # Get item quantity
            user_input_item_quantity = input("Enter item stock quantity, or 'c' to re-enter item name: ")

            # Validate input
            if user_input_item_name == "c":
                break

            # If user entered a non-positive number that isnt 'c'
            if not user_input_item_quantity.isdigit():
                # Add failed counter to global variable rejectedEntries
                rejected_entries += 1

                # Note isdigit() will not count -ve numbers input as number as "-1".isdigit() will count the "-" as a non digit character, thus failing the check
                print("Invalid input. Please enter a positive number or 'c'.")
                continue

            # If user entered 0
            if int(user_input_item_quantity) == 0:
                # Add failed counter to global variable rejectedEntries
                rejected_entries += 1
                print("Invalid input. Please enter a positive number or 'quit'.")
                continue

            item[1] = user_input_item_quantity

            # Return resulting item
            return (item, rejected_entries, False)


# Adds delivery to current inventory (returns new total)
def process_delivery(current_inventory, new_input):
    # Initialise variables
    overflow = False
    new_total = 0
    exists_flag = False
    total_items = 0
    initial_id = 1

    for item in current_inventory:
        exists_flag = True
        total_items += item[INVENTORY_ITEM_FORMAT["quantity"]]
        if new_input[0] == item[INVENTORY_ITEM_FORMAT["name"]]:
            item[INVENTORY_ITEM_FORMAT["quantity"]] += new_input[1]
            total_items += new_input[1]
            item[INVENTORY_ITEM_FORMAT["transaction_history"]] += f"|{new_input[1]}"

    if not exists_flag:
        if len(current_inventory) == 0:
            new_item = []
            new_item[INVENTORY_ITEM_FORMAT["id"]] = 1
            new_item[INVENTORY_ITEM_FORMAT["name"]] = new_input[0]
            new_item[INVENTORY_ITEM_FORMAT["quantity"]] = new_input[1]
            new_item[INVENTORY_ITEM_FORMAT["transaction_history"]] = f"{new_input[1]}"
            current_inventory.append(new_item)
        else:
            new_item = []
            new_item[INVENTORY_ITEM_FORMAT["id"]] = current_inventory[-1][INVENTORY_ITEM_FORMAT["id"]] + 1
            new_item[INVENTORY_ITEM_FORMAT["name"]] = new_input[0]
            new_item[INVENTORY_ITEM_FORMAT["quantity"]] = new_input[1]
            new_item[INVENTORY_ITEM_FORMAT["transaction_history"]] = f"{new_input[1]}"
            current_inventory.append(new_item)

    if total_items > INVENTORY_CAPACITY:
        overflow = True

    # Return inventory
    return (current_inventory, overflow)

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


# Main program logic
def main():

    # Initialise "global" variables
    inventory = []
    inventory_item = []
    total_failed_attempts = 0
    total_successful_deliveries = 0

    # Start of main loop
    while True:

        # initialise internal variables
        overflow_check = False
        current_delivery_tax = 0

        inventory = load_inventory()

        inventory_item, rejected_user_inputs, exit_flag = get_valid_input()
        total_failed_attempts += rejected_user_inputs

        # get_valid_input first field returned 0 (user entered quit)
        if exit_flag:
            break

        inventory, overflow_check = process_delivery(inventory, inventory_item)
        total_successful_deliveries += 1

        current_delivery_tax = calculate_tax(inventory_item)
        print("Tax needed to be paid for this delivery: {}".format(current_delivery_tax))

        # Inventory has overflowed
        if overflow_check:
            break

    # Print report when exiting application
    print(generate_report(inventory, total_failed_attempts, total_successful_deliveries))

main()


