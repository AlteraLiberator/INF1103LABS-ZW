from .menu import Menu
from .inventory import Inventory
from .product import Product
from .physicalproduct import PhysicalProduct
from .filereader import FileHandler
from functions.helpers import is_number, is_float

from pathlib import Path


class InventoryMenu(Menu):
    def __init__(self, inventory: Inventory) -> None:
        super().__init__()
        self._inventory = inventory
        self._menu_options = [
            {
                "display_string": "Add Item",
                "method": self.add_item,
            },
            {
                "display_string": "Remove Item",
                "method": self.remove_item,
            },
            {
                "display_string": "View Inventory",
                "method": self.view_inventory,
            },
            {
                "display_string": "Search Item",
                "method": self.search_item,
            },
            {
                "display_string": "Save Data",
                "method": self.save_data,
            },
            {
                "display_string": "Quit",
                "method": None,
            },
        ]

    @property
    def inventory(self) -> Inventory:
        return self._inventory

    @inventory.setter
    def inventory(self, value) -> None:
        self._inventory = value

    def add_item(self) -> None:
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        while not is_float(price):
            print("Invalid price. Please enter a valid number.")
            price = input("Enter product price: ")
        stock = input("Enter product stock: ")
        while not is_number(stock):
            print("Invalid stock. Please enter a valid number.")
            stock = input("Enter product stock: ")
        productType = input("Enter product type (physical/digital): ").strip().lower()
        if productType == "physical":
            weight = input("Enter product weight: ")
            while not is_float(weight):
                print("Invalid weight. Please enter a valid number.")
                weight = input("Enter product weight: ")
            product = PhysicalProduct(product_id, name, float(price), int(stock), float(weight))
        else:
            product = Product(product_id, name, float(price), int(stock))
        self.inventory.add_product(product)
        pass

    def remove_item(self) -> None:
        product_id = input("Enter product ID to remove: ")
        if self.inventory.delete_product(product_id):
            print(f"Product with ID {product_id} has been removed.")
        else:
            print(f"Product with ID {product_id} not found.")

        return

    def search_item(self) -> None:
        product_id = input("Enter product ID to search: ")
        product = self.inventory.search_product_list_by_id(product_id)
        if isinstance(product, Product):
            print("Product found:")
            print(product.return_display_information())
        else:
            print(f"Product with ID {product_id} not found.")
        return

    def view_inventory(self) -> None:
        print("Current Inventory:")
        for product in self.inventory.product_list:
            print(product.return_display_information())
        return

    def save_data(self, file_reader: FileHandler, file_location: Path) -> None:
        try:
            print(self.inventory.product_list)
            file_reader.inventory_to_file(file_location, self.inventory)
            print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")
