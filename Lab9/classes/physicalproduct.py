from product import Product

class PhysicalProduct(Product):
    def __init__(self, productid, name, price, stock, weight):
        super().__init__(productid, name, price, stock)
        self.weight = weight

    def get_weight(self):
        return self.weight
    
    def return_display_information(self) -> str:
        output_string = f"""==================
            Product ID: {self.productid}
            Name: {self.name}
            Price: {self.price}
            Stock: {self.stock}
            Weight: {self.weight}
=================="""
        return output_string