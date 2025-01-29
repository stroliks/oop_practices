import math
### **Задача №5.**

# Разработайте класс Vector для представления и манипуляции векторами в трехмерном пространстве.
# В классе должны быть поля для координат x, y и z, все типа float.
# Включите методы для сложения, вычитания, скалярного произведения и векторного произведения векторов.
# Перегрузите операторы (+, -, *) для соответствующих операций:
        # + для сложения векторов,
        # - для вычитания,
        # * может использоваться как для скалярного произведения, так и для векторного в зависимости от типа аргумента (вектор или число).
# Реализуйте также метод для вычисления нормы (длины) вектора.
# Операция вывода на экран (**`__str__`**) должна представлять вектор в форме "(x, y, z)".

class Vector:
    def __init__(self, x: float, y: float, z: float):

        self.x = x
        self.y = y
        self.z = z


    def len_vector(self) -> float:
        len_ = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return len_

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return f"({x}, {y}, {z})"

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return f"({x}, {y}, {z})"

    def __mul__(self, other):
            x_m = self.y * other.z - self.z * other.y
            y_m = self.z * other.x - self.x * other.z
            z_m = self.x * other.y - self.y * other.x
            return f"({x_m}, {y_m}, {z_m})"

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

p1 = Vector(2,5,6)

p2 = Vector(8,16,2)

print(p1)
print(p2)
print(p1.len_vector())
print(p2.len_vector())
print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
