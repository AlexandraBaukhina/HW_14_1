class BaseProduct:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

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
        return f"BaseProduct(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})"

    def __add__(self, other):
        """Сложение двух продуктов для получения полной стоимости всех товаров."""
        if not isinstance(other, BaseProduct):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}.")

        if type(self) is not type(other):
            raise TypeError(
                f"Нельзя складывать продукты разных классов: {type(self).__name__} и {type(other).__name__}.")

        total_price = (self.price * self.quantity) + (other.price * other.quantity)
        total_quantity = self.quantity + other.quantity
        return BaseProduct("Сумма", "Сумма продуктов", total_price / total_quantity if total_quantity > 0 else 0,
                           total_quantity)


class Smartphone(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: str, model: str,
                 memory: str, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (super().__str__() +
                f"\nПроизводительность: {self.efficiency}\n"
                f"Модель: {self.model}\n"
                f"Объем встроенной памяти: {self.memory}\n"
                f"Цвет: {self.color}")

    def __repr__(self):
        return (f"Smartphone(name={self.name}, description={self.description}, price={self.price}, "
                f"quantity={self.quantity}, efficiency={self.efficiency}, model={self.model}, "
                f"memory={self.memory}, color={self.color})")


class LawnGrass(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (super().__str__() +
                f"\nСтрана-производитель: {self.country}\n"
                f"Срок прорастания: {self.germination_period}\n"
                f"Цвет: {self.color}")

    def __repr__(self):
        return (f"LawnGrass(name={self.name}, description={self.description}, price={self.price}, "
                f"quantity={self.quantity}, country={self.country}, germination_period={self.germination_period}, "
                f"color={self.color})")


class Category:
    category_counter: int = 0  # Счетчик категорий
    product_counter: int = 0    # Счетчик продуктов

    def __init__(self, name: str, description: str):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = []  # Инициализируем пустой список для хранения продуктов
        Category.category_counter += 1

    def add_product(self, product: BaseProduct):
        """Метод для добавления продукта в категорию."""
        if isinstance(product, BaseProduct):  # Проверяем, что передан объект класса BaseProduct или его наследников
            self.__products.append(product)  # Добавляем продукт в приватный список
            Category.product_counter += 1  # Увеличиваем счетчик продуктов
        else:
            raise ValueError("Можно добавлять только экземпляры класса BaseProduct или его наследников.")  # Исключение, если передан не BaseProduct

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
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10, "Высокая",
                             "S23 Ultra", "256GB", "Серый")
    smartphone2 = Smartphone("iPhone 14 Pro", "128GB, Золотой цвет, 48MP камера", 150000.0, 5, "Высокая", "14 Pro",
                             "128GB", "Золотой")
    lawn_grass = LawnGrass("Трава газонная", "Трава для газона", 1000.0, 50, "Россия", "7-10 дней", "Зеленый")

    # Пример сложения товаров одного класса
    #try:
    #    total_smartphone = smartphone1 + smartphone2
    #    print(total_smartphone)
    #except TypeError as e:
    #    print(e)

    # Пример сложения товаров разных классов
    #try:
    #    total_mixed = smartphone1 + lawn_grass
    #    print(total_mixed)
    #except TypeError as e:
    #    print(e)

    category = Category("Электроника", "Категория для электроники")
    category.add_product(smartphone1)
    category.add_product(smartphone2)

    lawn_grass_category = Category("Сад и огород", "Категория для садовых товаров")
    lawn_grass_category.add_product(lawn_grass)

    print(category)
    print(category.products)
    print(lawn_grass_category)
    print(lawn_grass_category.products)
