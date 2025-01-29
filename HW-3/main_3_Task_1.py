# ### **Задача №1.1. `Wizard` (Волшебник)**
#
# Создайте класс **`Wizard`** для моделирования волшебника в Хогвартсе. В классе **`Wizard`** задаются приватные поля:
# имя волшебника,
# факультет,
# уровень магической силы,
# список известных заклинаний (список объектов класса **`Spell`**),
# текущий статус (в Хогвартсе или выпущен).
#
# Все поля должны быть приватными. Реализуйте следующие методы:
#

# 4. **Другие методы**:
#     - **`add_spell(spell: Spell)`**: добавляет заклинание в список известных.
#     - **`remove_spell(spell: Spell)`**: удаляет заклинание из списка известных.
#     - **`increase_magic_level(amount: int)`**: увеличивает уровень магической силы на заданное значение (неотрицательное).
#     - **`__str__()`**: возвращает строку, аккумулирующую состояние всех полей объекта.


class Wizard:
    def __init__(self, name: str, house: str, magic_level: int, spells: list, status: str):
        self.__name = name
        self.__house = house
        self.__magic_level = magic_level
        self.__spells = spells
        self.__status = status
    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_magic_level(self):
        return self.__magic_level

    def get_spells(self):
        return self.__spells

    def get_status(self):
        return self.__status

    def set_house(self, house):
        self.__house = house

    def set_magic_level(self, magic_level):
        self.__magic_level = magic_level

    def set_status(self, status):
        self.__status = status

    def add_spell(self, spell: Spell):
        self.__spells.append(spell)

    def remove_spell(self, spell: Spell):
        if spell in self.__spells:
            self.__spells.remove(spell)
        return "такого заклинания у волшебника нет"

    def increase_magic_level(self, amount: int):
        if amount >0:
            self.__magic_level += amount
        return "введено неверное значение"


    def __str__(self):
        return (f"{self.__name} \n "
                f"{self.__house} \n "
                f"{self.__magic_level} \n "
                f"{self.__spells} \n "
                f"{self.__status} \n")
