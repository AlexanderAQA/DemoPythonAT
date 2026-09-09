# Занятие 4. ООП - объектно-ориентированное программирование
# Классы, объекты, наследование, инкапсуляция

# ==============================================================================
# 1. Классы и Объекты
# ==============================================================================
class Character:
    """
    Класс — это шаблон или схема для создания объектов.
    Он определяет атрибуты (данные) и методы (функции), которыми будут обладать объекты.
    """
    # Атрибут класса (общий для всех экземпляров)
    game_name = "Fantasy RPG"

    # Метод-конструктор для инициализации атрибутов экземпляра.
    def __init__(self, name, health):
        self.name = name          # Атрибут экземпляра
        self.health = health      # Атрибут экземпляра

    # Метод экземпляра /функция экземпляра
    def introduce(self):
        return f"\nЯ {self.name}, и у меня {self.health} HP. Добро пожаловать в {self.game_name}!"


# Создание объектов (экземпляров класса)
hero_1 = Character("Aragorn", 100)
hero_2 = Character("Legolas", 85)

# print(hero_1.introduce())
# print(hero_2.introduce())


# ==============================================================================
# 2. Наследование
# ==============================================================================
class Mag(Character):
    """
    Маг наследует от Персонажа. Он получает все атрибуты и методы Персонажа,
    а также может вводить свои собственные уникальные особенности.
    """
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana          # Уникальный атрибут Мага

    # Переписываем родительский метод
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} у меня также {self.mana} очков маны!"

    # Уникальный метод Мага
    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"\n{self.name} кастит Fireball! Осталось маны: {self.mana}"
        return f"\n{self.name} не осталось маны!!!"


mage_hero = Mag("Gandalf", 90, 50)
#print(mage_hero.introduce())
#print(mage_hero.cast_spell())


# ==============================================================================
# 3. Инкапсуляция
# ==============================================================================
class BankAccount:
    """
    Инкапсуляция — это практика сокрытия внутренних деталей и защиты данных.
    В Python рекомендуют использовать одинарные (_) или двойные (__) подчеркивания для обеспечения конфиденциальности.
    """
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Приватный атрибут (недоступен напрямую извне класса)

    # Метод-геттер для безопасного доступа к приватному атрибуту.
    def get_balance(self):
        return self.__balance

    # Метод-сеттер для безопасного обновления приватного атрибута с проверкой.
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"В кошелек добавлено {amount}. Новый баланс: {self.__balance}")
        else:
            print("Неверное количество монет!!!")


account = BankAccount("Alice", 1000)
print(f"Владелец аккаунта: {account.owner}")
# print(account.__balance) # Эта строка вызовет ошибку AttributeError, поскольку переменная __balance скрыта!
print(f"Баланс аккаунта (через геттер - безопасный доступ к приватному параметру): {account.get_balance()}")
account.deposit(250)

"""
ДЗ на ЧТ:
1. Создать класс Фрукты. Добавить инициализацию класса. Указать параметры: название, вес, цвет
2. Создать 3 экземпляра класса Фрукты. Вывести на печать все их параметры в формате:
Название: ***
Вес: ***
Цвет: ***
3. Создать дочерний класс Ягоды (который наследует класс Фрукты). Для ягод указать новый параметр  - размер (фракция).
4. Создать функцию в классе Фрукты print_info - с выводом на печать всей информации об экземпляре класса.
5. Создать функцию в классе Ягоды print_berries_info - с выводом на печать всей информации об экземпляре класса.
6. Вызвать функции 5 и 6 для конкретных экземпляров классов.
"""

class Fruits:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
    def introduce(self):
        return f"Название: {self.name}\n Вес: {self.weight}\n Цвет: {self.color}"

    def print_info(self):
        pass


fruit1 = Fruits("Apple", 5, "Red")
fruit2 = Fruits("Banana", 3, "Yellow")
fruit3 = Fruits("Watermelon", 10, "Green")
print(fruit1.introduce())
print(fruit2.introduce())
print(fruit3.introduce())

class Berries(Fruits):
    def __init__(self, name, weight, color, size):
        super().__init__(name, weight, color)
        self.size = size
    def print_info(self):
        print(f"Название: {self.name}")
        print(f"Вес: {self.weight}")
        print(f"Цвет: {self.color}")

    def print_berries_info(self):
        print(f"Название: {self.name}")
        print(f"Вес: {self.weight}")
        print(f"Цвет: {self.color}")
        print(f"Размер: {self.size}")
        print("-" * 20)

print ("Информация о фруктах: ")
fruit1.print_info()
fruit2.print_info()
fruit3.print_info()

print("Информация о ягодах: ")
raspberry = Berries("raspberry", 5 , "Red", "Small" )
raspberry.print_berries_info()