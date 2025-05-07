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


def test_create_new_product(product_list):
    """Тест на создание нового продукта."""
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "Latest Samsung flagship phone",
        "price": 1200,
        "quantity": 10,
    }
    product = Product.new_product(product_data, product_list)

    assert len(product_list) == 1
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 1200
    assert product.quantity == 10


def test_update_existing_product(product_list):
    """Тест на обновление существующего продукта."""
    product_data_1 = {
        "name": "iPhone 14 Pro",
        "description": "Latest Apple flagship phone",
        "price": 1300,
        "quantity": 5,
    }
    Product.new_product(product_data_1, product_list)

    product_data_2 = {"name": "iPhone 14 Pro", "price": 1400, "quantity": 3}
    updated_product = Product.new_product(product_data_2, product_list)

    assert len(product_list) == 1
    assert updated_product.quantity == 8
    assert updated_product.price == 1400
