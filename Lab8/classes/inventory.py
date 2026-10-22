from typing import Literal
from functools import singledispatchmethod
from .product import Product


class Inventory:
    def __init__(self, product_list=[]) -> None:
        self._product_list = [] if product_list == [] else product_list

    @property
    def product_list(self) -> list[Product]:
        return self._product_list

    @product_list.setter
    def product_list(self, value) -> None:
        self._product_list = value

    def search_product_list_by_id(self, product_id: str) -> Product | Literal[False]:
        for product in self.product_list:
            if product_id == product.productid:
                return product
        return False

    def add_product(self, product: Product) -> None:
        duplicate = self.search_product_list_by_id(product.productid)
        if isinstance(duplicate, Product):
            duplicate.stock += product.stock
            return
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

        print(product.display_information())
        return True

    def print_all_products(self) -> None:
        print("""ITEMS IN INVENTORY""")
        for product in self.product_list:
            print(product.display_information())

        return
