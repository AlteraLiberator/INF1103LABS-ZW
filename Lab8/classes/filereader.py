from .inventory import Inventory
import json


class FileHandler:
    def __init__(
        self,
    ) -> None:
        pass

        
    def file_to_inventory(self, file_location: str):
        try:
            with open(file_location, "r", encoding="utf-8") as file:
                inventory = json.load(file)
                return Inventory(**inventory)

        except FileNotFoundError:
            return Inventory()

    def inventory_to_file(self, file_location: str, inventory: Inventory):
        try:
            with open(file_location, "w", encoding="utf-8") as file:
                json.dump(inventory.__dict__, file, indent=4)
                return True

        except Exception:
            return False
