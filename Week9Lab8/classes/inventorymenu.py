from typing import Union

from .menu import Menu
from .inventory import Inventory
from .product import Product
from .physicalproduct import PhysicalProduct
from .digitalproduct import DigitalProduct
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
        while True:
            productType = input("Enter product type (physical/digital): ").strip().lower()
            if productType == "physical":
                weight = input("Enter product weight: ")
                while not is_float(weight):
                    print("Invalid weight. Please enter a valid number.")
                    weight = input("Enter product weight: ")
                product = PhysicalProduct(
                    product_id, name, float(price), int(stock), float(weight)
                )
                break
            elif productType == "digital":
                file_size = input("Enter product file size (MB): ")
                while not is_float(file_size):
                    print("Invalid file size. Please enter a valid number.")
                    file_size = input("Enter product file size (MB): ")
                product = DigitalProduct(
                    product_id, name, float(price), int(stock), float(file_size)
                )
                break
            else:
                print("Invalid product type. Please enter 'physical' or 'digital'.")

        self.inventory.add_product(product)
        pass

    def remove_item(self) -> None:
        product_id = input("Enter product ID to remove: ")
        if self.inventory.delete_product(product_id):
            print(f"Product with ID {product_id} has been removed.")
        else:
            print(f"Product with ID {product_id} not found.")

        return

    @staticmethod
    def show_item(product: Union[DigitalProduct, PhysicalProduct]) -> str:
        return f"{product.return_display_information()}\n{product.get_fulfilment_information()}"

    def search_item(self) -> None:
        product_id = input("Enter product ID to search: ")
        product = self.inventory.search_product_list_by_id(product_id)
        if isinstance(product, Product):
            print("Product found:")
            print(product.return_display_information())
            print(product.get_fulfilment_information())
        else:
            print(f"Product with ID {product_id} not found.")
        return

    def view_inventory(self) -> None:
        print("Current Inventory:")
        for product in self.inventory.product_list:
            print(product.return_display_information(), "\n", product.get_fulfilment_information())
        return

    def save_data(self, file_reader: FileHandler, file_location: Path) -> None:
        try:
            file_reader.inventory_to_file(file_location, self.inventory)
            print("Data saved successfully.")
        except (OSError, TypeError) as e:
            print(f"An error occurred while saving data: {e}")
