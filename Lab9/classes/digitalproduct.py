from .product import Product


class DigitalProduct(Product):
    def __init__(self, productid, name, price, stock, file_size) -> None:
        super().__init__(productid, name, price, stock)
        self.file_size = file_size

    def return_display_information(self) -> str:
        output_string = super().return_display_information()
        output_string += f"\nFile Size: {self.file_size} MB"
        return output_string
