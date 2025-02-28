from __future__ import annotations
from abc import ABC, abstractmethod
import random

class Client:

    def __init__(self, name):
        self.__name = name
        self._accounts = []
        self._accounts.append(Account())

    def get_name(self):
        return self.__name

    def get_account(self):
        return self._accounts

    def add_accounts(self):
        acc = Account()
        self._accounts.append(acc)

    def remove_account(self, account):
        self._accounts.pop(account)

    def __repr__(self):
        return f" имя {self.get_name()} счет {self._accounts}"


class Account:
    def __init__(self):

        self.__number = random.randint(100, 1000)


    def get_number(self):
        return self.__number

    def __repr__(self):
        return f" {self.__number}"

client1 = Client("Bob")

client1.add_accounts()
client1.add_accounts()
print(client1)
client1.remove_account(1)

print(client1)




