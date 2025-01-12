# ## **Задача №1.**
#
# Сформировать класс "Animal" для представления сущности «Животное» в программе.
# В качестве полей задаются: имя животного (строка), вид животного (строка), возраст (число).
# Реализовать следующие операции: вывести звук, который издает животное (строка).
# Реализовать метод вывода информации о животном на экран.
# Метод вывода на экран должен аккумулировать состояние полей объекта.

class Animal:
    def __init__(self, name, type, age):
        """
        :param name: str
        :param type: str
        :param age: int
        """
        self.name = name
        self.type = type
        self.age = age

    def make_sound(self):
        print("Мяу")

    def info(self):
        print(f"Имя : { self.name}, вид:  {self.type}, возраст: {self.age}")


# ## **Задача №2.**
#
# Сформировать класс «Book» для представления сущности «Книга» в программе.
# В качестве полей задаются: наименование книги (строка), автор книги (строка), количество страниц (число).
# Реализовать операции: «отрыть» указанную страницу (на вход в метод передается номер страницы и выводится строка,
# открылась страница или нет). Реализовать метод вывода информации о книге на экран.
# Метод вывода на экран должен аккумулировать состояние полей объекта.

class Book:
    def __init__(self, name, author, count_page):
        """
        :param name: str
        :param author: str
        :param count_page: int
        """
        self.name = name
        self.author = author
        self.count_page = count_page

    def open_book(self, num_page):
        if num_page > 0 and num_page <= self.count_page:
            print(f"книга открылась на странице под номером {num_page}")
        else:
            print("книга НЕ открылась")

    def info(self):
        print(f"Название : { self.name}, автор:  {self.type}, страниц: {self.age}")


# ## **Задача №3.**
#
# Сформировать класс «**PassengerPlane**» для представления сущности «Пассажирский Самолет» в программе.
# В качестве полей задаются: производитель самолета, модель самолета, вместимость, пассажиров, текущая высота,
# текущая скорость.
# Реализовать следующие операции:
# взлет самолета,
# посадка самолета,
# изменение высоты,
# изменение скорости.
# Реализовать метод вывода информации о пассажирском самолете на экран.
# Метод вывода на экран должен аккумулировать состояние полей объекта.
#
# Примечание:
#
# Взлет самолета – операция, которая выводит сообщение на консоль «Самолет взлетел!».
# Посадка самолета – операция, которая выводит сообщение на консоль «Самолет приземлился!».
# Изменение высоты – операция, которая на вход принимает новое значение высоты и заменяет старое.

class PassengerPlane:
    def __init__(self, creator, model, capacity, current_height, current_speed):
        """

        :param creator: str
        :param model: str
        :param capacity: int
        :param current_height: float
        :param current_speed: float
        """
        self.creator = creator
        self.model = model
        self.capacity = capacity
        self.current_height = current_height
        self.current_speed = current_speed

    def rise(self):
        print("Самолет взлетел!")

    def landing(self):
        print("Самолет приземлился!")

    def change_height(self, delta_height):
        self.current_height += delta_height

    def change_speed(self, delta_speed):
        self.current_speed += delta_speed


    def info(self):
        print(f"Информация о самолете: производитель : {self.creator}, модель:  {self.model}, вместимость: {self.capacity}, "
              f"текущая высота: {self.current_height}, текущая скорость: {self.current_speed}")


# ## **Задача №4.**
#
# Сформировать класс «**MusicAlbum**» для представления сущности «Музыкальный Альбом» в программе.
# В качестве полей задаются: исполнитель, название альбома, жанр, список треков.
# Реализовать следующие операции:
# добавить трек в альбом,
# удалить трек из альбома,
# воспроизвести указанный трек.
# Реализовать метод вывода информации о музыкальном альбоме на экран. Метод вывода на экран должен аккумулировать
# состояние полей объекта.
#
# Примечание:
#
# Добавить трек в альбом – операция принимает на вход трек в формате строки и добавляет в список треков.
# Удалить трек из альбома – операция, принимает на вход название трека в формате строки и удаляет трек, если он имеется.
# Воспроизвести трек – операция, принимает на вход название трека и имитирует его воспроизведение выводом информации
# на консоль.

class MusicAlbum:
    def __init__(self, singer, album, genre, list_tracs):
        """

        :param singer: str
        :param album: str
        :param genre: str
        :param list_tracs: list
        """
        self.singer = singer
        self.album = album
        self.genre = genre
        self.list_tracs = list_tracs

    def add_track(self, new_track):
        self.list_tracs.append(new_track)

    def del_track(self, del_track):
        self.list_tracs.remove(del_track)

    def play_track(self, name_track):
        if name_track in self.list_tracs:
            print(f"СЕЙЧАС ИГРАЕТ ТРЕК <<{name_track}>>")
        else:
            print(f"Такой трек отсутствует в списке,  воспроизвести невозможно")
    def info(self):
        print(f"Информация о альбоме: исполнитель : {self.singer}, альбом:  {self.album}, жанр: {self.genre}, "
                f"трэки: {self.list_tracs}")

