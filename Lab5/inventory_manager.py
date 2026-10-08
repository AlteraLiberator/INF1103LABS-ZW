from pathlib import Path
import json
from pprint import pprint
import copy

current_directory = Path(__file__).parent

INVENTORY_FILE = current_directory / "inventory.json"


# Inventory functions
def get_inventory(default):

    try:
        with open(INVENTORY_FILE) as json_data:
            print("inventory.json found")
            data = json.load(json_data)
            json_data.close()
            print("Inventory loaded.")
            return data

    except FileNotFoundError:
        print("inventory.json not found, generating...")
        data = open(INVENTORY_FILE, "x")
        data.close()
        print("inventory.json created")

        return default


def main():

    # Define variables
    inventory = {"items": []}

    # Start program

    print("====" * 7)
    print("Inventory Management System")
    print("====" * 7)

    # Get Inventory
    inventory = get_inventory(inventory)
    
    while True:
        
        # Print options menu
        print(("-"*7) + "MENU" + ("-"*7))
        print("""
              1. Display all products
              2. Add product
              3. Update stock
              4. Search product
              5. Save Inventory
              6. Exit (Autosaves)
              """)
        print("-"*18 + "\n")
        
        user_input = input("Enter option: ")
        
        while not user_input.isdigit():
            user_input = input("Invalid entry, try again: ")
        
        match int(user_input):
            case 1:
                pass
            case 2: 
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _: # Default case
                print("No matching option found, returning to menu")
        
        

    return 0


if __name__ == "__main__":
    main()
