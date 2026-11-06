from product import Product

class PhysicalProduct(Product):
    def __init__(self, productid, name, price, stock, weight):
        super().__init__(productid, name, price, stock)
        self.weight = weight

    def get_weight(self):
        return self.weight
    
    def return_display_information(self) -> str:
        output_string = super().return_display_information()
        output_string += f"\nWeight: {self.weight}"
        return output_string