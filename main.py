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