from __future__ import annotations
from dataclasses import dataclass

from functions.helpers import is_number, is_float


@dataclass
class Product:

    def __init__(self, productid: str, name: str, price: float, stock: int) -> None:
        self._productid = productid
        self._name = name
        self._price = price
        self._stock = stock
        
    @classmethod
    def from_dict(cls, data: dict) -> Product:
        productid = data.get("_productid", "")
        name = data.get("_name", "")
        price = data.get("_price", 0.0)
        stock = data.get("_stock", 0)
        return cls(productid, name, price, stock)

    @property
    def productid(self)-> str:
        return self._productid

    @productid.setter
    def productid(self, value) -> None:
        self._productid = value

    @property
    def name(self)-> str:
        return self._name

    @name.setter
    def name(self, value) -> None:
        self._name = value

    @property
    def price(self)-> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        if not is_float(value):
            return
        self._price = value

    @property
    def stock(self)-> int:
        return self._stock

    @stock.setter
    def stock(self, value) -> None:
        if not is_number(value):
            return
        self._stock = value

    def update_stock(self, input) -> None:
        self.stock += input

    def return_display_information(self) -> str:
        output_string = f"""
            Product ID: {self.productid}
            Name: {self.name}
            Price: {self.price}
            Stock: {self.stock}"""

        return output_string
