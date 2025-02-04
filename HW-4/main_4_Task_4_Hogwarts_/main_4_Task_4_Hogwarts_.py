from __future__ import annotations

import random

class Hogwarts:
    def __init__(self,students=None, spells=None):
        self.__students = students or []
        self.__spells = spells or []

    def enroll_student(self, student):
        self.__students.append(student.get_name())


    def teach_spell(self, spell: Spell):
        self.__spells.append(spell.get_title())

    def simulate_duel (self, student1, student2):
        pass


class HogwartsStudent:
    def __init__(self,name:str, house: str, mana=100, spells=None):
        self.__name = name
        self.__house = house
        self.__mana = mana
        self.__spells = spells or []

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_mana(self):
        return self.__mana

    def get_spells(self):
        return self.__spells

    def set_mana(self, new_mana):
        self.__mana = new_mana

    def learn_spell(self, spell: Spell):
        self.__spells.append(spell.get_title())

    def cast_spell(self):
        cast_spell = random.choice(self.__spells)
        return cast_spell


class Spell:
    def __init__(self, title: str, description: str, value_mana: int):
        self.__title = title
        self.__description = description
        self.__value_mana = value_mana

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def value_mana(self):
        return self.__value_mana



    def cast(self, target: HogwartsStudent):
        pass


