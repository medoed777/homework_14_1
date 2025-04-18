import json
import os

from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open (full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data

def create_category_from_json(data):
    categorys = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categorys.append(Category(**category))
    return categorys
