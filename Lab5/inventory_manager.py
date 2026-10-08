from pathlib import Path
import json
from pprint import pprint
import copy

current_directory = Path(__file__).parent

INVENTORY_FILE = current_directory / "inventory.json"


# Option for user to exit current function
def exit_flag(data):
    if data == "-1":
        return True
    return False


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

def save_inventory(inventory):
    try:
        with open(INVENTORY_FILE, "w") as inventory_file:
            json.dump(inventory, inventory_file, indent=4)
            
        print("Inventory saved!")
    except Exception as e:
        print(f"Error occurred: {e}\nUnable to save file.")
        

# Product functions
def display_product(inventory):
    if len(inventory["items"]) == 0:
        print("No items in inventory!")
    else:

        for item in inventory["items"]:
            print(
                f"ID: {item['ID']} | Name: {item['Name']} | Price: ${item['Price']:.2f} | Current stock: {item['Stock']}"
            )
    return True


def add_product(inventory):

    item = {"ID": "", "Name": "", "Price": 0, "Stock": 0}

    while True:
        user_input = input("Enter product ID, or -1 to exit:")

        if exit_flag(user_input):
            break

        exists_flag = False

        for items in inventory["items"]:
            if items["ID"] == user_input:
                exists_flag = True
                break

        if exists_flag:
            print("Product already exists!")
            continue
        else:
            item["ID"] = user_input

            # User enters product name
            user_input = input("Enter Product Name, or -1 to exit:")
            if exit_flag(user_input):
                break
            item["Name"] = user_input

            while True:
                user_input = input("Enter Product Price, or -1 to exit:")
                if exit_flag(user_input):
                    break
                try:
                    item["Price"] = float(user_input)
                    break
                except ValueError:
                    print("Invalid price!")

            # To exit outer loop if user entered 0 from the price loop
            if exit_flag(user_input):
                break

            while True:
                user_input = input("Enter Product Stock, or -1 to exit:")
                if exit_flag(user_input):
                    break
                try:
                    item["Stock"] = int(user_input)
                    break
                except ValueError:
                    print("Invalid stock!")

            # To exit outer loop if user entered 0 from the stock loop
            if exit_flag(user_input):
                break

            inventory["items"].append(item)
            break

    return inventory


def update_product_stock(inventory):

    user_input = input("Enter product ID or -1 to exit: ")
    exists_flag = False

    if exit_flag(user_input):
        return inventory

    for items in inventory["items"]:
        if items["ID"] == user_input:
            exists_flag = True
            while True:
                user_input = input(
                    f"Current stock is {items['Stock']}. What do you want to change it to?"
                )
                if not user_input.isdigit():
                    print("That is not a positive whole number.")
                    continue
                items["Stock"] = int(user_input)
                break
            break
    if not exists_flag:
        print("Product not found, returning to menu...")

    return inventory


def search_product(inventory):

    user_input = input("Enter product ID or -1 to exit: ")
    exists_flag = False

    if exit_flag(user_input):
        return inventory

    for items in inventory["items"]:
        if items["ID"] == user_input:
            exists_flag = True
            print(f"""
Product Found!
-----------------------------
ID: {items["ID"]}
Name: {items["Name"]}
Price: {items["Price"]}
Stock: {{items["Stock"]}}
-----------------------------
                  """)
            break

    if not exists_flag:
        print("Product not found, returning to menu...")

    return True


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
        print(("-" * 7) + "MENU" + ("-" * 7))
        print("""
1. Display all products
2. Add product
3. Update stock
4. Search product
5. Save Inventory
6. Exit (Autosaves)
              """)
        print("-" * 18 + "\n")

        user_input = input("Enter option: ")

        while not user_input.isdigit():
            user_input = input("Invalid entry, try again: ")

        match int(user_input):
            case 1:
                print("\n")
                display_product(inventory)
                print("\n")
            case 2:
                print("\n")
                inventory = add_product(inventory)
                print("\n")
            case 3:
                print("\n")
                inventory = update_product_stock(inventory)
                print("\n")
            case 4:
                print("\n")
                search_product(inventory)
                print("\n")
            case 5:
                print("\n")
                save_inventory(inventory)
                print("\n")
            case 6:
                break
            case _:  # Default case
                print("No matching option found, returning to menu")

    print("Exiting app and saving inventory...")
    save_inventory(inventory)

    return 0


if __name__ == "__main__":
    main()
