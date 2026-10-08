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

    return 0


if __name__ == "__main__":
    main()
