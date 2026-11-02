from .inventory import Inventory
import json
from pathlib import Path


class FileHandler:
    def __init__(
        self,
    ) -> None:
        pass

        
    def file_to_inventory(self, file_location: Path):
        try:
            with open(file_location, "r", encoding="utf-8") as file:
                inventory = json.load(file)
                return Inventory.from_dict(inventory)

        except FileNotFoundError:
            return Inventory()

    def inventory_to_file(self, file_location: Path, inventory: Inventory):
        try:
            with open(file_location, "w", encoding="utf-8") as file:
                json.dump(inventory.__dict__, file, default=lambda o: o.__dict__, indent=4)
                return True

        except Exception:
            return False
