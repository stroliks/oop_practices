import math
### **Задача №6.**

# Создайте класс `Fraction` для работы с дробями.
# Класс должен включать поля:
# числитель и знаменатель, оба целочисленные значения.
# Реализуйте методы для сложения, вычитания и умножения дробей.
# Перегрузите соответствующие операторы (+, -, *) для реализации этих операций.
# Каждая операция должна возвращать новый объект класса Fraction, представляющий результат.
# Добавьте методы проверки на знаменатель равный нулю перед выполнением операций.
# Операция вывода на экран (**`__str__`**) должна отображать дробь в формате "числитель/знаменатель" или "целое число", если знаменатель равен 1.

class Fraction:
    def __init__(self, nom: int, denom: int):

        self.nom = nom
        if denom == 0:
            raise ValueError("Делитель не может быть нулём!!")
        self.denom = denom

    def __add__(self, other):
        denom = self.denom * other.denom
        nom = self.nom * (denom / self.denom) + other.nom * (denom / other.denom)
        while denom % 2 == 0 and  nom % 2 == 0:
            denom /= 2
            nom /= 2
        new_fraction = Fraction(int(nom), int(denom))
        return new_fraction

    def __sub__(self, other):
        denom = self.denom * other.denom
        nom = self.nom * (denom / self.denom) - other.nom * (denom / other.denom)
        while denom % 2 == 0 and  nom % 2 == 0:
            denom /= 2
            nom /= 2
        new_fraction = Fraction(int(nom), int(denom))
        return new_fraction

    def __mul__(self, other):
        denom = self.denom * other.denom
        nom = self.nom * other.nom
        while denom % 2 == 0 and  nom % 2 == 0:
            denom /= 2
            nom /= 2
        new_fraction = Fraction(int(nom), int(denom))
        return new_fraction


    def __str__(self):
        if self.nom == self.denom:
            return f"1"
        elif self.denom == 1:
            return f"{self.nom}"
        return f"{self.nom}/{self.denom}"

f1 = Fraction(7,16)

f2 = Fraction(8,15)

print(f1+f2)
print(f1-f2)
print(f1*f2)
