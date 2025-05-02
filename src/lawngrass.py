from src.product import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if not isinstance(other, LawnGrass):
            raise TypeError("Нельзя складывать продукты разных классов")

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных классов")

        return (self.price * self.quantity) + (other.price * other.quantity)