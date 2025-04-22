from unittest.mock import patch

from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_class():
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product.name = "Xiaomi Redmi Note 11"
    product.description = "1024GB, Синий"
    product.price = 31000.0
    product.quantity = 14


def test_product_update(product):
    with patch("builtins.input", return_value="y"):
        product.price = 0
    assert "Цена не должна быть нулевая или отрицательная"


def test_product_price(product):
    assert product.price > 0


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_with_add1, product_with_add2):
    assert 1500000.0
