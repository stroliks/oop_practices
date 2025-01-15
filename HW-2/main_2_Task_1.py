### **Задача №1.**

# Сформировать класс **`Patient`** для представления сущности «Пациент» в программе.
# В качестве полей задаются: ФИО пациента (строка), возраст (число), и текущее заболевание (строка).
# Реализовать операции: «записать на прием», которая принимает дату и время и выводит уведомление о записи на прием.
# Реализовать метод вывода информации о пациенте на экран, который аккумулирует состояние полей объекта.

class Date:
    def __init__(self, month, day, hours, minute):
        self.month = month
        self.day = day
        self.hours = hours
        self.minute = minute

    def date(self):
        return f"{self.day}.{self.month}"

    def time(self):
        return f"{self.hours}:{self.minute}"


class Patient:
    def __init__(self, name, age, illness):
        """
        :param name: str
        :param age: int
        :param illness: str
        """
        self.name = name
        self.age = age
        self.illness = illness

    def record(self):
        date = input("Введите дату приема в формате ДД.ММ:   ")
        time = input("Введите время приема в формате ЧЧ.ММ:   ")
        month = date[0:2]
        day = date[3:]
        hours = time[0:2]
        minute = time[3:]
        d1 = Date(month, day, hours, minute)

        print(f"Клиент {self.name} записан на прием на дату: {d1.date()}, на время: {d1.time()}")

    def __str__(self):
        return f"Пациент: {self.name} \n Возраст:  {self.age} лет \n Заболевание:  {self.illness}"

p1 = Patient("Коля", 35,"грипп")

p1.record()
print()
print(p1)
