from functions.helpers import number_checker


class Product:

    def __init__(self, productid: str, name:str, price:int, stock:int) -> None:
        self._productid = productid
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def productid(self):
        return self._productid

    @productid.setter
    def productid(self, value):
        self._productid = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        number_checker(value)
        self._price = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value) -> None:
        number_checker(value)
        self._stock = value

    def update_stock(self, input) -> None:
        self.stock += input
        
    def display_information(self) -> str:
        output_string = f"""==================
            Product ID: {self.productid}
            Name: {self.name}
            Price: {self.price}
            Stock: {self.stock}
=================="""
        return output_string
        
