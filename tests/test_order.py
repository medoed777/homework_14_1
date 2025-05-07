import pytest


def test_order_full_price(setup_orders):
    order1, order2 = setup_orders
    assert order1.full_price == 540000.0
    assert order2.full_price == 1050000.0


def test_order_quantity(setup_orders):
    order1, order2 = setup_orders
    assert order1.quantity == 3
    assert order2.quantity == 5


def test_order_product(setup_orders):
    order1, order2 = setup_orders
    assert order1.product.name == "Samsung Galaxy S23 Ultra"
    assert order2.product.name == "Iphone 15"
