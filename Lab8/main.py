from pathlib import Path

from classes.filereader import FileHandler
from classes.inventorymenu import InventoryMenu
from functions.helpers import number_checker


def main():
    current_directory = Path(__file__).parent

    INVENTORY_FILE = current_directory / "inventory.json"

    file_manager = FileHandler()

    inventory = file_manager.file_to_inventory(INVENTORY_FILE)

    inventory_menu = InventoryMenu(inventory)

    while True:
        user_option = inventory_menu.display_main_menu()

        for item in inventory_menu.menu_options:
            if item["display_string"] == "Quit":
                if user_option == str(inventory_menu.menu_options.index(item)):
                    print(inventory_menu.exit_message())
                    file_manager.inventory_to_file(INVENTORY_FILE, inventory)
                    return

            elif item["display_string"] == "Save Data":
                if user_option == str(inventory_menu.menu_options.index(item)):
                    inventory_menu.save_data(file_manager, INVENTORY_FILE)
                    continue
            elif user_option == str(inventory_menu.menu_options.index(item)):
                item["method"]()


if __name__ == "__main__":
    main()
