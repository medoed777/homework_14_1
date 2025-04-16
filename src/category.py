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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

if __name__ == "__main__":
    products1 = Product("Samsung", "Samsung ok", 10000, 5)
    products2 = Product("Iphone", " ok", 12000, 6)
    products3 = Product("Телевизоры", "ok", 4000, 8)
    products4 = Product("Nokia", "no ok", 1000.50, 0)

    category = Category("aaaaaa", "fasfasfaf", [products1, products2, products3, products4])

    print(category.name)
    print(category.description)
    print(category.products)
    print(category.category_count)
    print(category.product_count)