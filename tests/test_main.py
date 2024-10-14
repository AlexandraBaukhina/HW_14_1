import pytest

from src.main import Product, Category


def test_product_initialization():
    product = Product("Apple", "Fresh and juicy", 1.99, 100)
    assert product.name == "Apple"
    assert product.description == "Fresh and juicy"
    assert product.price == 1.99
    assert product.quantity == 100

def test_category_initialization():
    products = ["Apple", "Banana", "Orange"]
    category = Category("Fruits", "Various kinds of fruits", products)
    assert category.name == "Fruits"
    assert category.description == "Various kinds of fruits"
    assert category.products == products

def test_category_counter():
    # Сбрасываем счетчик категорий для чистого теста
    Category.category_counter = 0
    Category("Fruits", "Various kinds of fruits", ["Apple", "Banana"])
    Category("Vegetables", "Fresh vegetables", ["Carrot", "Potato"])
    assert Category.category_counter == 2

def test_product_counter():
    # Сбрасываем счетчик продуктов для чистого теста
    Category.product_counter = 0
    Category("Fruits", "Various kinds of fruits", ["Apple", "Banana"])
    Category("Vegetables", "Fresh vegetables", ["Carrot", "Potato", "Tomato"])
    assert Category.product_counter == 5
