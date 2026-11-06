from .product import Product
from .canbeshipped import CanBeShipped
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, productid, name, price, stock, weight):
        super().__init__(productid, name, price, stock)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def return_display_information(self) -> str:
        output_string = super().return_display_information()
        output_string += f"\nWeight: {self._weight}"
        return output_string
    
    def can_be_shipped(self) -> bool:
        return True
    
    def calculate_shipping_cost(self) -> float:
        return self.weight * self.price
