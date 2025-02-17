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
    def __init__(self, type_el):
        self._type_el = type_el

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self, element):
        pass


class Client(Element):
    def __init__(self, name, accounts=None):
        super().__init__()
        self._name = name
        self._accounts = [] or accounts

    def add(self):
        acc = Account()
        self._accounts.append(acc)

    def remove(self, account):
        self._accounts.remove(account)


class Employee(Element):
    def __init__(self, post):
        super().__init__()
        self._post = post or []

    def add(self):
        post = Manager()
        self._post.append(post)

    def remove(self, post):
        self._post.remove(post)


class Cashier(Employee):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def open_shift(self):
        return True

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
    def __init__(self, number, type_account):
        self._number = number
        self.__type_account = type_account
        self.__client = Client()







