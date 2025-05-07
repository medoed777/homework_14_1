from src.base_entity import BaseEntity
from src.exceptions import ZeroQuantityProduct
from src.product import Product


class Category(BaseEntity):
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        super().__init__()
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.products_in_list} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        if isinstance(product, Product):
            try:
                if product.quantity <= 0:
                    raise ZeroQuantityProduct("Нечего добавлять")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError("Только объекты класса Product могут быть добавлены.")

    @property
    def products(self):
        return self.__products

    @property
    def products_list(self):
        """Геттер для получения списка товаров в виде строк."""
        return [str(product) for product in self.__products]

    @property
    def products_in_list(self):
        return sum(product.quantity for product in self.__products)

    def middle_price(self):
        try:
            return sum(product.price for product in self.__products) / len(
                self.__products
            )
        except ZeroDivisionError:
            return 0
