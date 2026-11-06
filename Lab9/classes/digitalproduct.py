from .product import Product


class DigitalProduct(Product):
    def __init__(self, productid, name, price, stock, file_size) -> None:
        super().__init__(productid, name, price, stock)
        self.file_size = file_size

    def return_display_information(self) -> str:
        output_string = f"""==================
            Product ID: {self.productid}
            Name: {self.name}
            Price: {self.price}
            Stock: {self.stock}
            File Size: {self.file_size} MB
=================="""
        return output_string
