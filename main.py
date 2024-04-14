# Задание: Применение Принципа Открытости/Закрытости (Open/Closed Principle)
# в Разработке Простой Игры.
# Цель: Закрепить понимание и навыки применения принципа открытости/закрытости
# (Open/Closed Principle), одного из пяти SOLID принципов объектно-ориентированного
# программирования. Принцип гласит, что программные сущности (классы, модули, функции и т.д.)
# должны быть открыты для расширения, но закрыты для модификации.
# Задача: Разработать простую игру, где игрок может использовать различные типы оружия
# для борьбы с монстрами. Программа должна быть спроектирована таким образом, чтобы легко
# можно было добавлять новые типы оружия, не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

# Абстрактный класс Weapon
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Классы конкретных типов оружия
class Меч(Weapon):
    def attack(self):
        return "удар мечом"

class Лук(Weapon):
    def attack(self):
        return "выстрел из лука"

# Класс Fighter
class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def attack(self):
        return self.weapon.attack()

# Класс Monster
class Monster:
    def is_defeated(self):
        return True

# Демонстрация боя
fighter = Fighter(Меч())
monster = Monster()

weapons = [Меч(), Лук()]

for weapon in weapons:
    fighter.change_weapon(weapon)
    print(f"Боец выбирает {type(weapon).__name__}.")
    print(f"Боец наносит {fighter.attack()}.")
    if monster.is_defeated():
        print("Монстр побежден!")
    else:
        print("Монстр атакует бойца!")