import pytest
from src.category import Category
from src.product import Product
from src.category_iterator import CategoryIterator


def test_category_init(first_category, two_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны ок"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert two_category.category_count == 2

    assert first_category.product_count == 3
    assert two_category.product_count == 3


def test_category_products_property(first_category):
    assert first_category.products == [
        'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
        'Iphone 15, 210000.0 руб. Остаток: 8 шт.'
    ]


def test_category_add_product(first_category, product):
    assert len(first_category.products_in_list) == 2
    first_category.add_product(product)
    assert len(first_category.products_in_list) == 3

def test_category_str(two_category):
    assert str(two_category) == "Телевизоры, количество продуктов: 1 шт."


def test_category_iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    first_product = next(category_iterator)
    assert first_product == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert category_iterator.index == 1
    products = list(category_iterator)
    assert len(products) == 2
    assert products[1] == "Iphone 15, 210000.0 руб. Остаток: 8 шт."

def test_category_iterator_empty(zero_category):
    iterator = CategoryIterator(zero_category)
    assert list(iterator) == []
