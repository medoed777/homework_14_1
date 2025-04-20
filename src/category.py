from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Только объекты класса Product могут быть добавлены.")

    @property
    def products(self):
        """Геттер для получения списка товаров в виде строк."""
        return "\n".join([f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products])

    @property
    def products_in_list(self):
        return self.__products