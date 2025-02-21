from __future__ import annotations
from abc import ABC, abstractmethod

class Bank:
    def __init__(self, name: str, elements: list):
        self._name = name
        self._elements = elements or []

    def add_element(self, element):
        self._elements.append(element)

    def remove_element(self, element):
        self._elements.remove(element)

class Element(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self, element):
        pass


class Client(Element):
    def __init__(self, name, accounts=None):
        super().__init__(name)
        self._accounts = [] or accounts

    def add(self):
        acc = Account()
        self._accounts.append(acc)

    def get_name(self):
        return self._name
    def remove(self, account):
        self._accounts.remove(account)

    def add_account(self, acc):
        self._accounts.append(acc)

    def __repr__(self):
        return f" имя {self.get_name()} счет {self._accounts}"

class Employee(Element):
    def __init__(self, name, post):
        super().__init__(name)
        self._post = post or []

    def add(self):
        post = Manager()
        self._post.append(post)

    def remove(self, post):
        self._post.remove(post)


class Cashier(Employee):
    def __init__(self, name):
        super().__init__(name)

    def open_shift(self):
        return True

    def get_name(self):
        return self._name

    def close_shift(self):
        return False

class Manager(Employee):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def open_account(self, account):
        pass

    def close_account(self):
        pass


class Account():
    def __init__(self, number, type_account, client):
        self._number = number
        self.__type_account = type_account
        self.__client = client


    def set_client(self,client):
        self.__client = client

    def __repr__(self):
        return f" номер счета {self._number} клиент {self.__client}"

client1 = Client("Bob")


deb = Account(254, "debit", client1)

print(deb)


print(client1)




