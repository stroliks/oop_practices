from __future__ import annotations

class Library:
    def __init__(self, title: str, adress: str, books=None, users=None):
        self.__title = title
        self.__adress = adress

        self.__books = []
        if books is not None:
            self.__books.append(books)

        self.__users = []
        if users is not None:
            self.__users.append(users)

    def add_book(self, book):
        self.__books.append(book.get_title())

    def remove_book(self, book):
        self.__books.remove(book)

    def add_user(self, user):
        self.__users.append(user.get_name())

    def give_book(self, book, user):
        if book.get_status() == "выдана":
            return "книги нет в наличии"
        book.set_status("выдана")
        book.set_user(user)
        user.set_books(book)

    def return_book(self, book, user):
        if book.get_status() == "в наличии":
            return "книга не выдавалась"
        book.set_status("в наличии")
        book.set_user(None)
        user.remove_books(book)

    def get_books(self):
        return self.__books

    def get_users(self):
        return self.__users

    def __str__(self):
        return f"Название библиотеки: {self.__title}, Список книг: {self.__books}, Список читателей: {self.__users}"


class Book:
    def __init__(self, title: str, author: str, year: int, status="в наличии", user=None):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = status
        self.__user = user

    def get_title(self):
        return self.__title
    def get_status(self):
        return self.__status

    def set_user(self, user):
        self.__user = user
    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Название книги: {self.__title}, Автор: {self.__books}, Год: {self.__users}, Статус: {self.__status}, Читатель: {self.__user}"


class User:
    def __init__(self, name: str, number: int, books=None):
        self.__name = name
        self.__number = number

        self.__books = []
        if books is not None:
            self.__books.append(books)

    def get_name(self):
        return self.__name
    def get_books(self):
        return self.__books

    def set_books(self, book):
        self.__books.append(book.get_title())

    def remove_books(self, book):
        self.__books.remove(book.get_title())

    def __str__(self):
        return f"Имя: {self.__name}, Билет: {self.__number}, Список взятых книг: {self.__books}"

Lib = Library("Gorkov", "Mira 13")
print(Lib)
reader1 = User("Fred", 505)
reader2 = User("Bob", 58)
reader3 = User("Snak", 12)
book1 = Book("Addy", "Tolstoy", 1958)
book2 = Book("Bobby", "Bob", 1754)
book3 = Book("Celly", "Claud", 2021)
book4 = Book("Daddy", "Dunkan", 1201)

Lib.add_book(book1)
Lib.add_book(book2)
Lib.add_book(book3)
Lib.add_book(book4)
print(Lib)
Lib.add_user(reader1)
Lib.add_user(reader2)
Lib.add_user(reader3)
print(Lib)

Lib.give_book(book2, reader2)

print(book2.get_status())
print(reader2.get_books())

Lib.give_book(book4, reader2)

print(book4.get_status())
print(reader2.get_books())

Lib.return_book(book4, reader2)

print(reader2.get_books())