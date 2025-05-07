from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):
    product: Product
    quantity: int
    full_price: float

    def __init__(self, product, quantity):
        super().__init__()
        self.product = product
        self.quantity = quantity
        self.full_price = self.calkulate_full_price()


    def __str__(self):
        return f"Заказ: {self.product.name}, Количество: {self.quantity}, Полная цена: {self.full_price}"


    def calkulate_full_price(self):
        return self.product.price * self.quantity
