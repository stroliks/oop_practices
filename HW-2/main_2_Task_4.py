import random
# ### **Задача №4.**
#
# Создайте класс ArrayUtils, который будет содержать статические методы для выполнения различных операций над массивами целых чисел.
# Этот класс будет полезен в ситуациях, когда нужно провести стандартные операции над массивами, такие как
# расчет суммы или произведения элементов, без необходимости создания экземпляра класса.
#
# Операции класса:
#
# 1. **Метод для расчёта суммы элементов массива**:
#     - Входные данные: массив чисел.
#     - Выходные данные: сумма всех элементов массива.
# 2. **Метод для расчёта произведения элементов массива**:
#     - Входные данные: массив чисел.
#     - Выходные данные: произведение всех элементов массива.
# 3. **Метод для инверсии массива**:
#     - Входные данные: массив чисел.
#     - Выходные данные: массив с элементами в обратном порядке.
# 4. **Метод для нахождения максимального элемента в массиве**:
#     - Входные данные: массив чисел.
#     - Выходные данные: максимальное значение среди элементов массива.
# 5. **Метод для нахождения минимального элемента в массиве**:
#     - Входные данные: массив чисел.
#     - Выходные данные: минимальное значение среди элементов массива.

class ArrayUtils:

    @staticmethod
    def summ(array: list) -> float:

        summ_ = 0
        for element in array:
            summ_ += element
        return summ_

    @staticmethod
    def prod(array: list) -> float:

        prod = 1
        for element in array:
            prod *= element
        return prod

    @staticmethod
    def inverse(array: list) -> list:

        for i in range(len(array)//2):
            buff = array[i]
            array[i] = array[-i-1]
            array[-i - 1] = buff
        return array

    @staticmethod
    def max_elem(array: list) -> float:

        max_ = array[0]
        for i in range(1, len(array), 1):
            if array[i] >= max_:
                max_ = array[i]
        return max_

    @staticmethod
    def min_elem(array: list) -> float:

        min_ = array[0]
        for i in range(1, len(array), 1):
            if array[i] <= min_:
                min_ = array[i]
        return min_


l1 = [random.randint(1,10) for i in range(5)]
print(f" Список изначальный: {l1}")

print(f" Сумма списка: {ArrayUtils.summ(l1)}")
print(f" Произведение списка: {ArrayUtils.prod(l1)}")
print(f" Инверсия списка: {ArrayUtils.inverse(l1)}")
print(f" Максимальный элемент списка: {ArrayUtils.max_elem(l1)}")
print(f" Минимальный элемент списка: {ArrayUtils.min_elem(l1)}")