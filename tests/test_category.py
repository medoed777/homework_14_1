import pytest

from src.category_iterator import CategoryIterator


def test_category_init(first_category, two_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны ок"
    assert len(first_category.products_list) == 2

    assert first_category.category_count == 2
    assert two_category.category_count == 2

    assert first_category.product_count == 3
    assert two_category.product_count == 3


def test_category_add_product(first_category, product):
    assert len(first_category.products_list) == 2
    first_category.add_product(product)
    assert len(first_category.products_list) == 3


def test_category_str(two_category):
    assert str(two_category) == "Телевизоры, количество продуктов: 14 шт."


def test_category_iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(category_iterator).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(category_iterator)


def test_category_iterator_empty(zero_category):
    iterator = CategoryIterator(zero_category)
    assert list(iterator) == []


def test_category_add_product_error(first_category, product):
    with pytest.raises(TypeError):
        first_category.add_product(1)

def test_category_add_product_smartphone(first_category, product_smartphone1):
    first_category.add_product(product_smartphone1) == product_smartphone1
