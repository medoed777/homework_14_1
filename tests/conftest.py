import pytest

from src.category import Category
from src.product import Product
from src.category_iterator import CategoryIterator

@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны ок",
        products=[
            Product(
                "Samsung Galaxy S23 Ultra",
                "256GB, Серый цвет, 200MP камера",
                180000.0,
                5,
            ),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def two_category():
    return Category(
        name="Телевизоры",
        description="Телевизоры ок",
        products=[Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)],
    )


@pytest.fixture
def product():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

@pytest.fixture
def category_iterator(first_category):
    return CategoryIterator(first_category)

@pytest.fixture
def zero_category():
    return Category("Пустая категория", "Описание", [])

@pytest.fixture
def product_with_add1():
    return Product(name="Samsung Galaxy S23 Ultra", description="Флагманский смартфон от Samsung", price=180000.0, quantity=5)

@pytest.fixture
def product_with_add2():
    return Product(name="iPhone 14 Pro", description="Флагманский смартфон от Apple", price=200000.0, quantity=3)