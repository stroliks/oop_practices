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
    def summ_list(list):
        """
        :param list: []
        :return: float
        """
        summ_ = 0
        for element in list:
            summ_ += element
        return summ_

    @staticmethod
    def prod_list(list):
        """
        :param list: []
        :return: float
        """
        prod = 1
        for element in list:
            prod *= element
        return prod

    @staticmethod
    def inverse_list(list):
        """
        :param list: []
        :return: []
        """
        for i in range(len(list)//2):
            buff = list[i]
            list[i] = list[-i-1]
            list[-i - 1] = buff
        return list

    @staticmethod
    def max_elem_list(list):
        """
        :param list: []
        :return: []
        """
        max_ = list[0]
        for i in range(1, len(list), 1):
            if list[i] >= max_:
                max_ = list[i]
        return max_

    @staticmethod
    def min_elem_list(list):
        """
        :param list: []
        :return: []
        """
        min_ = list[0]
        for i in range(1, len(list), 1):
            if list[i] <= min_:
                min_ = list[i]
        return min_


l1 = [random.randint(1,10) for i in range(5)]
print(f" Список изначальный: {l1}")

print(f" Сумма списка: {ArrayUtils.summ_list(l1)}")
print(f" Произведение списка: {ArrayUtils.prod_list(l1)}")
print(f" Инверсия списка: {ArrayUtils.inverse_list(l1)}")
print(f" Максимальный элемент списка: {ArrayUtils.max_elem_list(l1)}")
print(f" Минимальный элемент списка: {ArrayUtils.min_elem_list(l1)}")