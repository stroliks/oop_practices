from __future__ import annotations

class Athlete:
    def __init__(self, name: str, age: int, sport: str, status:str, achievements = None):

        self.__name = name
        if age < 0:
            raise ValueError(" возраст не может быть отрицательным")
        self.__age = age
        self.__sport = sport
        self.__status = status
        self.__achievements = []
        if achievements is not None:
            self.__achievements.append(achievements)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_sport(self):
        return self.__sport

    def get_status(self):
        return self.__status

    def get_achievements(self):
        return self.__achievements


    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_sport(self, sport):
        self.__sport = sport

    def set_status(self, status):
        self.__status = status

    def add_achievement(self, achievement):
        self.__achievements.append(achievement)

    def remove_achievement(self, achievement):
        if achievement not in self.__achievements:
            return "такого достижения нет. удалить невозможно"
        self.__achievements.remove(achievement)

    def __str__(self):
        return (f"Имя:  {self.__name} \n "
                f"Возраст:  {self.__age} \n "
                f"Вид спорта:  {self.__sport} \n "
                f"Статус: {self.__status} \n "
                f"Список достижений: {self.__achievements} \n")


class Achievement:
    def __init__(self, title: str, sport: str):
        self.__title = title
        self.__sport = sport

    def get_title(self):
        return self.__title

    def __str__(self):
        return (f"Название: {self.__title} \n"
                f"Вид спорта: {self.__sport} \n")

dos1 = Achievement("1 место","бег")
dos2 = Achievement("3 место","плаванье")

a1 = Athlete("вася", 35, "бег", "пенсия", dos1.get_title())
a2 = Athlete("Рома", 22, "стрельба", "в работе")



print(a1)
print(a2)
a2.add_achievement(dos2.get_title())
a1.remove_achievement(dos1.get_title())
print(a1)
print(a2)
