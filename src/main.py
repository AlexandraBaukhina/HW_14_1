class Product:
    name: str  # Название продукта
    _price: float  # Цена продукта
    quantity: int

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

    def __str__(self):
        """Строковое отображение продукта в требуемом формате."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"

    def __add__(self, other):
        """Сложение двух продуктов для получения полной стоимости всех товаров."""
        if isinstance(other, Product):
            total_price = (self.price * self.quantity) + (other.price * other.quantity)
            total_quantity = self.quantity + other.quantity
            return Product("Сумма", "Сумма продуктов", total_price / total_quantity if total_quantity > 0 else 0, total_quantity)
        return NotImplemented


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
        return "\n".join(str(product) for product in self.__products) if self.__products else "Нет продуктов в категории."

    def total_quantity(self) -> int:
        """Метод для подсчета общего количества продуктов в категории."""
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        """Строковое отображение категории в требуемом формате."""
        return f"{self.name}, количество продуктов: {self.total_quantity()} шт."

    def __repr__(self):
        return f"Category(name={self.name}, description={self.description}, products={self.products})"


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10)
    product2 = Product("Iphone 15", "512GB, Gray space", 210)
