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

    def simulate_duel(self, student1, student2):
        while student1.get_mana() > 0 or student2.get_mana() > 0 or student2.get_health() > 0 or student1.get_health() > 0:
            spell_1 = student1.cast_spell()
            student1.set_mana(student1.get_mana() - spell_1.get_mana())
            student2.take_spell(spell_1)
            spell_2 = student2.cast_spell()
            student2.set_mana(student2.get_mana() - spell_2.get_mana())
            student1.take_spell(spell_2)
            # вывод значений  чтобы отследить процесс сражения
            print(f"игрок_1 мана {student1.get_mana()}, здоровье {student1.get_health}   игрок_2 мана {student2.get_mana()}, здоровье {student2.get_health}")
        if student1.get_mana() < 0 or student1.get_health() < 0:
            return f"победитель {student2.get_name()}"
        return f"победитель {student1.get_name()}"


class HogwartsStudent:
    def __init__(self, name: str, house: str, health=100, mana=100, spells=None):
        self.__name = name
        self.__house = house
        self.__health = health
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

    def get_health(self):
        return self.__health

    def set_mana(self, new_mana):
        self.__mana = new_mana

    def set_health(self, health):
        self.__health = health

    def learn_spell(self, spell: Spell):
        self.__spells.append(spell.get_title())

    def cast_spell(self):
        spell = random.choice(self.__spells)
        return spell

    def take_spell(self, spell):
        if spell.cast() == self.__name:
            if spell.get_title() == "damage":
                self.set_health(self.__health - 10)



class Spell:
    def __init__(self, title: str, description: str, mana: int):
        self.__title = title
        self.__description = description
        self.__mana = mana

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_mana(self):
        return self.__mana

    def cast(self, target):
        return target

damage = Spell("damage", "Урон", 10)
simple_spell = Spell("damage", "Урон", 15)
bob = HogwartsStudent("Bob", "FAT")
coc = HogwartsStudent("Coc", "FEVT")
ror = HogwartsStudent("Roc", "ATF")

hogwarts = Hogwarts()

hogwarts.teach_spell(damage)
hogwarts.teach_spell(simple_spell)
hogwarts.enroll_student(bob)
hogwarts.enroll_student(coc)
hogwarts.enroll_student(ror)
bob.learn_spell(damage)
bob.learn_spell(simple_spell)
coc.learn_spell(damage)
coc.learn_spell(simple_spell)
ror.learn_spell(damage)
ror.learn_spell(simple_spell)

hogwarts.simulate_duel(bob,coc)
