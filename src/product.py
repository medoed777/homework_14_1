from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Нельзя складывать продукты разных классов")

        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных классов")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict, product_list: list):
        """Создает новый экземпляр Product или обновляет существующий."""
        name = product_data.get("name")

        for product in product_list:
            if product.name == name:
                product.quantity += product_data.get("quantity", 0)
                product.price = max(product.price, product_data.get("price", 0))
                return product

        new_product = cls(
            name=name,
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
        )
        product_list.append(new_product)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        """Сеттер для установки цены с проверкой и подтверждением."""
        if value < self.__price:
            confirmation = input(
                f"Вы уверены, что хотите понизить цену с {self.__price} до {value}? (y/n): "
            )
            if confirmation.lower() != "y":
                print("Изменение цены отменено.")
                return
        elif value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        self.__price = value
