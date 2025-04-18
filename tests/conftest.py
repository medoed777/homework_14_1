import pytest

from src.category import Category
from src.product import Product


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
