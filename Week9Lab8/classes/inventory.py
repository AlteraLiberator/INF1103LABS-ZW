from __future__ import annotations
from typing import Any, Literal
from .product import Product
from .physicalproduct import PhysicalProduct
from .digitalproduct import DigitalProduct
from functools import singledispatchmethod

class Inventory:
    def __init__(self, _product_list=[]) -> None:
        self._product_list = _product_list
        
    @classmethod
    def from_dict(cls, data: dict) -> Inventory:
        product_list_data = data.get("_product_list", [])
        product_list = [Product.from_dict(product_data) for product_data in product_list_data]
        return cls(product_list)

    @property
    def product_list(self) -> list[Product]:
        return self._product_list

    @product_list.setter
    def product_list(self, value) -> None:
        self._product_list = value

    def get_methods(self):
        return [
            {
                "display_string": "Display all products",
                "method": self.print_all_products,
                "fields":[]
            },
            {
                "display_string": "Search for product",
                "method": self.search_product_list_by_id,
                "fields":["product_id"]
            },
            {
                "display_string": "Add new product",
                "method": self.add_product,
            },
            {
                "display_string": "Add stock to product",
                "method": self.add_to_product,
            },
        ]

    def search_product_list_by_id(self, product_id: str) -> Product | Literal[False]:
        for product in self.product_list:
            if product_id == product.productid:
                return product
        return False
    
    def replace_product(self, product_id: str, new_product: Product) -> bool:
        for i, product in enumerate(self.product_list):
            if product_id == product.productid:
                self.product_list[i] = new_product
                return True
        return False
    
    @singledispatchmethod
    def add_product(self, product) -> Any:
        raise NotImplementedError("Unsupported product type")
    
    @add_product.register
    def _(self, product: PhysicalProduct) -> None:
        duplicate = self.search_product_list_by_id(product.productid)
        if isinstance(duplicate, PhysicalProduct):
            duplicate.stock += product.stock
            return
        
        if isinstance(duplicate, Product):
            raise ValueError("Product ID already exists as a different product type.")
        self._product_list.append(product)
        return
    
    @add_product.register
    def _(self, product: DigitalProduct) -> None:
        duplicate = self.search_product_list_by_id(product.productid)
        if isinstance(duplicate, DigitalProduct):
            duplicate.stock += product.stock
            return
        
        if isinstance(duplicate, Product):
            raise ValueError("Product ID already exists as a different product type.")
        self._product_list.append(product)
        return

    def add_to_product(self, product_id: str, added_stock: int) -> None:
        product = self.search_product_list_by_id(product_id)
        if not isinstance(product, Product):
            raise ValueError("Product not found!")
        product.stock += added_stock
        return

    def delete_product(self, product_id: str) -> bool:
        product = self.search_product_list_by_id(product_id)
        if not product:
            return False
        self.product_list.remove(product)
        return True

    def get_product(
        self, product_id: str
    ) -> tuple[Literal[False], Literal["Product Not Found"]] | Product:
        product = self.search_product_list_by_id(product_id)
        if not product:
            return False, "Product Not Found"

        return product

    def print_product(self, product_id: str) -> bool:
        product = self.get_product(product_id)
        if isinstance(product, tuple):
            print(product[1])
            return False

        print(product.return_display_information())
        return True

    def print_all_products(self) -> None:
        print("""ITEMS IN INVENTORY""")
        for product in self.product_list:
            print(product.return_display_information())

        return
