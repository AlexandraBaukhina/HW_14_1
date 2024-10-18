# Создаем класс c атрибутами
class Product:
    name: str  # Здесь мы пишем название атрибута и указываем тип description: str
    _price: float  # Используем _price для хранения цены quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод для создания нового продукта из словаря."""
        return cls(
            name=product_data.get('name'),
            description=product_data.get('description'),
            price=product_data.get('price'),
            quantity=product_data.get('quantity')
        )

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price: float):
        if new_price < self._price:
            while True:
                confirmation = input(f"Вы уверены, что хотите понизить цену с {self._price} до {new_price}? (y/n): ")
                if confirmation.lower() == 'y':
                    self._price = new_price
                    print(f"Цена успешно изменена на {self._price}.")
                    break
                elif confirmation.lower() == 'n':
                    print("Изменение цены отменено.")
                    break
                else:
                    print("Некорректный ввод. Пожалуйста, введите 'y' или 'n'.")
        else:
            self._price = new_price
            print(f"Цена успешно изменена на {self._price}.")

    def __repr__(self):
        return f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"


class Category:
    category_counter: int = 0  # Счетчик категорий
    product_counter: int = 0    # Счетчик продуктов

    def __init__(self, name: str, description: str):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = []  # Инициализируем пустой список для хранения продуктов
        Category.category_counter += 1
        def add_product(self, product: Product):
            """Метод для добавления продукта в категорию."""
            if isinstance(product, Product):  # Проверяем, что передан объект класса Product
                self.__products.append(product)  # Добавляем продукт в приватный список
                Category.product_counter += 1  # Увеличиваем счетчик продуктов
            else:
                raise ValueError("Можно добавлять только экземпляры класса Product.")  # Исключение, если передан не Product

        @property
        def products(self) -> str:
            """Геттер для получения списка продуктов в категории в виде строки."""
            product_strings = [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]
            return "\n".join(product_strings) if product_strings else "Нет продуктов в категории."

    def get_products(self):
        """Метод для получения списка продуктов в категории."""
        return self.__products[:]  # Возвращаем копию списка продуктов

    def __repr__(self):
        return f"Category(name={self.name}, description={self.description}, products={self.products})"


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                         "функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим "
                         "другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
