from __future__ import annotations

class Library:
    def __init__(self, title: str, adress: str, books=None, employees=None):
        self.__title = title
        self.__adress = adress

        self.__books = []
        if books is not None:
            self.__books.append(books)

        self.__employees = []
        if employees is not None:
            self.__employees.append(employees)

    def get_title(self):
        return self.__title

    def get_adress(self):
        return self.__adress

    def get_books(self):
        return self.__books

    def get_employees(self):
        return self.__employees

    def set_adress(self, adress):
        self.__adress = adress

    def add_book(self, book):
        self.__books.append(book.get_title())

    def remove_book(self, book):
        self.__books.remove(book.get_title())

    def add_employee(self, employee):
        self.__employees.append(employee.get_name())

    def remove_employee(self, employee):
        self.__employees.remove(employee.get_name())

    def __str__(self):
        return f"Название библиотеки: {self.__title}, Список книг: {self.__books}, Список работников: {self.__employees}"


class Book:
    def __init__(self, title: str, id: int, year: int, genre=None):
        self.__title = title
        self.__id = id
        self.__year = year
        self.__genre = []
        if genre is not None:
            self.__genre.append(genre)

    def get_title(self):
        return self.__title
    def get_id(self):
        return self.__id
    def get_year(self):
        return self.__year
    def get_genre(self):
        return self.__genre

    def set_year(self, year):
        self.__year = year

    def add_genre(self, genre):
        self.__genre.append(genre.get_name())

    def remove_genre(self, genre):
        self.__genre.remove(genre.get_name())

    def __str__(self):
        return f"Название книги: {self.__title}, ID: {self.__id}, Год: {self.__year}, Жанры: {self.__genre}"


class Employee:
    def __init__(self, name: str, position: str, id: int):
        self.__name = name
        self.__position = position
        self.__id = id
        self.__contact_info = None


    def get_name(self):
        return self.__name
    def get_position(self):
        return self.__position

    def get_id(self):
        return self.__id

    def get_contact_info(self):
        return self.__contact_info

    def set_position(self, position):
        self.__position = position

    def add_contact_info(self, type, value):
        contact_info = ContactInfo(type, value)
        self.__contact_info = contact_info

    def remove_contact_info(self):
        self.__contact_info = None

    def __str__(self):
        return f"Имя: {self.__name}, Должность: {self.__position}, ID: {self.__id}, Контакты: {self.__contact_info}"

class Genre:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def __str__(self):
        return f"Название жанра: {self.__name}, Описание: {self.__description}"


class ContactInfo:
    def __init__(self, type: str, value: str):
        self.__type = type
        self.__value = value

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

    def __str__(self):
        return f"Тип контакта: {self.__type}, Значение: {self.__value}"

library = Library("Gorkov", "Mira 13")
book1 = Book("War and World", 5488452, 1875)
genre1 = Genre("повесть", "поветствование")
man1 = Employee("Irina", "fireman", 25485)

library.add_employee(man1)
library.add_book(book1)
book1.add_genre(genre1)

print(library.get_books())
print(library.get_employees())
print(man1)

man1.add_contact_info("tel", "9586854523")
print(man1)
print(man1.get_contact_info())
