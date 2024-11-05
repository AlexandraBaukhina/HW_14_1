import pytest

from src.main import Product, Category


def test_product_creation():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 10


def test_product_str_method():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 5)
    assert str(product) == "Iphone 15, 210000.0 руб. Остаток: 5 шт."


def test_product_add_method():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 5)

    combined_product = product1 + product2

    assert combined_product.name == "Сумма"
    assert combined_product.description == "Сумма продуктов"
    assert combined_product.price == (180000.0 * 10 + 210000.0 * 5) / (10 + 5)  # Средняя цена
    assert combined_product.quantity == 15  # Общее количество


def test_category_creation():
    category = Category("Смартфоны", "Современные смартфоны с высокими характеристиками.")
    assert category.name == "Смартфоны"
    assert category.description == "Современные смартфоны с высокими характеристиками."
    assert category.total_quantity() == 0  # В категории пока нет продуктов


def test_add_product_to_category():
    category = Category("Смартфоны", "Современные смартфоны с высокими характеристиками.")
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)
    category.add_product(product)

    assert category.total_quantity() == 10  # Общее количество продуктов в категории
    assert str(category) == "Смартфоны, количество продуктов: 10 шт."
    assert "Samsung Galaxy S23 Ultra" in category.products  # Проверяем, что продукт добавлен


def test_empty_category_products():
    category = Category("Смартфоны", "Современные смартфоны с высокими характеристиками.")
    assert category.products == "Нет продуктов в категории."


if __name__ == "__main__":
    pytest.main()
