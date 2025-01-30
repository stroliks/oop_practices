from __future__ import annotations

class Wizard:
    def __init__(self, name: str, house: str, magic_level: int, status: str, spells=[]):

        self.__name = name
        self.__house = house
        if magic_level < 0:
            raise ValueError(" магическая сила не может быть отрицательной")
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

    def add_spell(self, spell):
        self.__spells.append(spell)

    def remove_spell(self, spell):
        if spell not in self.__spells:
            return "такого заклинания у волшебника нет. удалить невозможно"
        self.__spells.remove(spell)

    def increase_magic_level(self, amount: int):
        if amount > 0:
            self.__magic_level += amount
        return "введено неверное значение"

    def __str__(self):
        return (f"Волшебник:  {self.__name} \n "
                f"Факультет:  {self.__house} \n "
                f"Магическая сила:{self.__magic_level} \n "
                f"Владеет заклинаниями: {self.__spells} \n "
                f"Статус обучения: {self.__status} \n")

### Задача №1.2. **`Spell` (Заклинание)**

# Создайте класс **`Spell`** для моделирования заклинания в Хогвартсе.
# В классе **`Spell`** задаются приватные поля: название заклинания, уровень сложности (по шкале от 1 до 10), тип заклинания (боевое, лечебное и т.д.), описание.
# Все поля должны быть приватными.
# Реализуйте методы: геттеры и сеттеры для каждого приватного поля. Операция вывода на экран (**`__str__`**) должна аккумулировать состояние полей объекта.

class Spell:
    def __init__(self, title: str, dif_level: int, type: str, description: str):
        self.__title = title
        if dif_level<1 and dif_level>10:
            raise ValueError ("только значения от 1 до 10")
        self.__dif_level = dif_level
        self.__type = type
        self.__description = description

    def get_title(self):
        return self.__title
    def get_dif_level(self):
        return self.__dif_level
    def get_type(self):
        return self.__type
    def get_description(self):
        return self.__description

    def set_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Только строковое значение")
        self.__title = title

    def set_type(self, type):
        if not isinstance(type, str):
            raise ValueError("Только строковое значение")
        self.__type = type

    def set_dif_level(self, dif_level):
        if dif_level<1 and dif_level>10:
            raise ValueError ("только значения от 1 до 10")
        self.__dif_level = dif_level

    def set_title(self, description):
        self.__description = description

    def __str__(self):
        return (f"Название: {self.__title} \n"
                f"Уровень сложности: {self.__dif_level} \n"
                f"Тип заклинания: {self.__type} \n"
                f"Описание заклинания: {self.__description}")


spell_water = Spell("Вода", 5, "боевое", "смерч")
spell_fire = Spell("Огонь", 8, "боевое", "ураган")
spell_doctor = Spell("Доктор", 2, "лечебное", "здоровье улучшает")


w1 = Wizard("Эль", "РП-10", 15, "выпущен")
print(w1)
w1.add_spell(spell_doctor.get_title())
print(w1)
w1.add_spell(spell_water.get_title())
print(w1)
w1.remove_spell(spell_water.get_title())
print(w1)

w1.remove_spell(spell_doctor.get_title())
print(w1)