def test_category_init(first_category, two_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны ок"
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert two_category.category_count == 2

    assert first_category.product_count == 3
    assert two_category.product_count == 3


def test_category_products_property(first_category):
    assert first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    )


def test_category_add_product(first_category, product):
    assert len(first_category.products_in_list) == 2
    first_category.add_product(product)
    assert len(first_category.products_in_list) == 3
