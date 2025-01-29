### **Задача №3.**

# Создайте класс `ModelWindow` для работы с моделями экранных окон.
# В качестве полей задаются:
        # заголовок окна,
        # координаты левого верхнего угла,
        # размер по горизонтали,
        # размер по вертикали,
        # цвет окна,
        # состояние “видимое/невидимое”,
        # состояние “с рамкой/без рамки”.
# Координаты и размеры указываются в целых числах.
# Реализовать операции:
        # передвижения окна по горизонтали,
        # по вертикали;
        # изменение высота и/или ширины окна;
        # изменение цвет окна;
        # изменение состояния;
        # опрос состояния. Операция вывода на экран (`__str__`) должна аккумулировать состояние полей объекта.
# Операции передвижения и изменения размера должны осуществлять проверку на пересечение границ экрана. Границы экрана принять 1960х1080.

class ModelWindow:
    def __init__(self, name: str, x: int, y: int, lenght: int, high: int, color: str, is_visible: bool = True, frame: bool = True):


        self.__name = name
        self.__x = x
        self.__y = y
        self.__lenght = lenght
        self.__high = high
        self.__color = color
        self.__is_visible = is_visible
        self.__frame = frame

    def move_horiz(self, delta_x):
        x_right = self.__x + self.__lenght
        if x_right + delta_x <= 1960 and self.__x + delta_x >= 0:
            self.__x += delta_x
        else:
            print(f"невозможно передвинуть окно по горизонтали на {delta_x} (выход за границу!!)")

    def move_vert(self, delta_y):
        y_low = self.__y - self.__high
        if y_low + delta_y >= 0 and self.__y + delta_y <= 1080:
            self.__y += delta_y
        else:
            print(f"невозможно передвинуть окно по вертикали на {delta_y} (выход за границу!!)")

    def change_size(self, delta_len, delta_high):
        x_right = self.__x + self.__lenght
        if x_right + delta_len <= 1960 and self.__y + delta_high <= 1080:
            self.__lenght += delta_len
            self.__high += delta_high
        else:
            print(f"невозможно увеличить окно (выход за границы экрана!!)")

    def change_color(self, new_color):
        self.__color = new_color

    def change_visible(self):
        buff = self.__visible
        self.__visible = not buff

    def change_frame(self):
        buff = self.__frame
        self.__frame = not buff

    def __str__(self):
        return (f"заголовок:  {self.__name}\nкоординаты верхнего левого угла: х = {self.__x}, у = {self.__y} \nразмеры: {self.__lenght} х {self.__high} \n"
                f"цвет: {self.__color} \nвидимость: {"Да" if self.__is_visible == True else "Нет"} \nрамка: {"Да" if self.__frame == True else "Нет"}   ")




p1 = ModelWindow("Окно1", 300,600, 600, 300, "green", True, True)

print()
print(p1)
p1.change_size(50, 80)
print(p1)
