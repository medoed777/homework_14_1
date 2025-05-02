import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="Флагманский смартфон от Samsung",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product_with_add2():
    return Product(
        name="iPhone 14 Pro",
        description="Флагманский смартфон от Apple",
        price=200000.0,
        quantity=3,
    )


@pytest.fixture
def product_list():
    return []


@pytest.fixture
def product_smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def product_smartphone2():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def product_lawngrass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def product_lawngrass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
