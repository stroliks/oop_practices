import math
### Задача №8.
# Создайте класс Time для представления и управления временем.
# Класс должен содержать поля: часы, минуты и секунды, все целочисленные значения.

# Реализуйте методы для сложения и вычитания временных интервалов, а также умножения времени на целое число.
# Перегрузите соответствующие операторы (+, -, *) для реализации этих операций.
# Включите функцию для коррекции времени, чтобы часы, минуты и секунды автоматически приводились к правильному формату
# (например, 90 минут становятся 1 часом и 30 минутами).
# Операция вывода на экран (**`__str__`**) должна отображать время в формате "ЧЧ:ММ:СС",
# где ЧЧ, ММ и СС должны быть всегда двузначными числами, даже если они меньше 10.

class Time:

    def __init__(self, hour, min, sec):
        """
        :param hour: int
        :param min: int
        :param sec: int
        """
        self.hour = hour
        self.min = min
        self.sec = sec

    def __add__(self, other):
        summ_sec = (self.hour + other.hour) * 3600 + (self.min + other.min) * 60 + self.sec + other.sec
        new_hour = summ_sec//3600
        new_min = (summ_sec % 3600) // 60
        new_sec = (summ_sec % 3600) % 60
        time = Time(new_hour, new_min, new_sec)
        return time

    def __sub__(self, other):
        summ_sec = (self.hour - other.hour) * 3600 + (self.min - other.min) * 60 + self.sec - other.sec
        new_hour = abs(summ_sec)//3600
        new_min = abs(summ_sec) % 3600 // 60
        new_sec = (abs(summ_sec) % 3600) % 60
        time = Time(new_hour, new_min, new_sec)
        if summ_sec >= 0:
            return time
        return f"-{time}"

    def __mul__(self, other):
        summ_sec = (self.hour  * 3600 + self.min * 60 + self.sec) * other
        new_hour = summ_sec//3600
        new_min = (summ_sec % 3600) // 60
        new_sec = (summ_sec % 3600) % 60
        time = Time(new_hour, new_min, new_sec)
        return time

    def __str__(self):
        if self.hour < 10:
            self.hour = f"0{self.hour}"
        if self.min < 10:
            self.min = f"0{self.min}"
        if self.sec < 10:
            self.sec = f"0{self.sec}"
        return f"{self.hour}:{self.min}:{self.sec}"


t1 = Time(1,20,2)
t2 = Time(3,22,11)

print(t1 + t2)
print(t1 - t2)
print(t1 * 9)
