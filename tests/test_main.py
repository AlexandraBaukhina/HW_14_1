import pytest

from src.main import Product, Category


@pytest.fixture
def product_data():
    """Фикстура для тестовых данных продукта."""
    return {
        'name': 'Smartphone',
        'description': 'Latest model smartphone',
        'price': 699.99,
        'quantity': 50
    }

@pytest.fixture
def product(product_data):
    """Фикстура для создания экземпляра продукта."""
    return Product.new_product(product_data)

@pytest.fixture
def category():
    """Фикстура для создания экземпляра категории."""
    return Category("Electronics", "Devices and gadgets")

def test_product_initialization(product, product_data):
    """Тестируем инициализацию продукта."""
    assert product.name == product_data['name']
    assert product.description == product_data['description']
    assert product.price == product_data['price']
    assert product.quantity == product_data['quantity']

def test_category_initialization(category):
    """Тестируем инициализацию категории."""
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert len(category.get_products()) == 0  # Должно быть пусто

def test_add_product(category, product):
    """Тестируем добавление продукта в категорию."""
    category.add_product(product)
    assert len(category.get_products()) == 1  # Теперь должен быть один продукт
    assert category.get_products()[0].name == product.name

def test_add_invalid_product(category):
    """Тестируем добавление некорректного продукта."""
    with pytest.raises(ValueError):
        category.add_product("Not a product")  # Передаем строку вместо объекта Product

def test_products_property(category, product):
    """Тестируем свойство products для получения списка продуктов."""
    category.add_product(product)
    products_list = category.products
    assert "Smartphone" in products_list  # Проверяем, что имя продукта есть в строке

def test_category_counter():
    """Тестируем счетчик категорий."""
    initial_counter = Category.category_counter
    new_category = Category("Home Appliances", "Appliances for home")
    assert Category.category_counter == initial_counter + 1  # Проверяем, что счетчик увеличился

def test_product_counter(category, product):
    """Тестируем счетчик продуктов."""
    initial_counter = Category.product_counter
    category.add_product(product)
    assert Category.product_counter == initial_counter + 1  # Проверяем, что счетчик увеличился
