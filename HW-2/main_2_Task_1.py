### **Задача №1.**

# Сформировать класс **`Patient`** для представления сущности «Пациент» в программе.
# В качестве полей задаются: ФИО пациента (строка), возраст (число), и текущее заболевание (строка).
# Реализовать операции: «записать на прием», которая принимает дату и время и выводит уведомление о записи на прием.
# Реализовать метод вывода информации о пациенте на экран, который аккумулирует состояние полей объекта.

class Date:
    def __init__(self, month, day, hours, minute):
        self.__month = month
        self.__day = day
        self.__hours = hours
        self.__minute = minute

    def date(self):
        return f"{self.__day}.{self.__month}"

    def time(self):
        return f"{self.__hours}:{self.__minute}"


class Patient:
    def __init__(self, name: str, age: int, illness: str):

        self.__name = name
        self.__age = age
        self.__illness = illness

    def record(self, date, time):
        month = date[0:2]
        day = date[3:]
        hours = time[0:2]
        minute = time[3:]
        d1 = Date(month, day, hours, minute)

        print(f"Клиент {self.__name} записан на прием на дату: {d1.date()}, на время: {d1.time()}")

    def __str__(self):
        return f"Пациент: {self.__name} \n Возраст:  {self.__age} лет \n Заболевание:  {self.__illness}"

p1 = Patient("Коля", 35,"грипп")

p1.record("15.03", "15.35")
print()
print(p1)
