from .product import Product


class DigitalProduct(Product):
    def __init__(self, productid, name, price, stock, file_size) -> None:
        super().__init__(productid, name, price, stock)
        self._file_size = file_size

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value

    def return_display_information(self) -> str:
        output_string = super().return_display_information()
        output_string += f"\nFile Size: {self._file_size} MB"
        return output_string
