
# Initialising variables
inventory = 0
rejectedEntries = 0

# Functions
def get_valid_input():
    pass

def process_delivery():
    pass

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


