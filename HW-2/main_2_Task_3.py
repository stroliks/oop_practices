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
    def __init__(self, name, x, y, lenght, high, color, visible = True, frame = True):
        """
        :param name: str
        :param x: int
        :param y: int
        :param lenght: int
        :param high: int
        :param color: str
        :param visible: bool
        :param frame: bool
        """

        self.name = name
        self.x = x
        self.y = y
        self.lenght = lenght
        self.high = high
        self.color = color
        self.visible = visible
        self.frame = frame

    def move_horiz(self, delta_x):
        x_right = self.x + self.lenght
        if x_right + delta_x <= 1960 and self.x + delta_x >= 0:
            self.x += delta_x
        else:
            print(f"невозможно передвинуть окно по горизонтали на {delta_x} (выход за границу!!)")

    def move_vert(self, delta_y):
        y_low = self.y - self.high
        if y_low + delta_y >= 0 and self.y + delta_y <= 1080:
            self.y += delta_y
        else:
            print(f"невозможно передвинуть окно по вертикали на {delta_y} (выход за границу!!)")

    def change_size(self):
        delta_len = int(input("Изменить длину на :   "))
        delta_high = int(input("Изменить высоту на :   "))
        x_right = self.x + self.lenght
        if x_right + delta_len <= 1960 and self.y + delta_high <= 1080:
            self.lenght += delta_len
            self.high += delta_high
        else:
            print(f"невозможно увеличить окно (выход за границы экрана!!)")

    def change_color(self, new_color):
        self.color = new_color

    def change_visible(self):
        buff = self.visible
        self.visible = not buff

    def change_frame(self):
        buff = self.frame
        self.frame = not buff

    def __str__(self):
        return (f"заголовок:  {self.name}\nкоординаты верхнего левого угла: х = {self.x}, у = {self.y} \nразмеры: {self.lenght} х {self.high} \n"
                f"цвет: {self.color} \nвидимость: {"Да" if self.visible == True else "Нет"} \nрамка: {"Да" if self.frame == True else "Нет"}   ")




p1 = ModelWindow("Окно1", 300,600, 600, 300, "green", True, True)

print()
print(p1)
p1.change_size()
print(p1)
