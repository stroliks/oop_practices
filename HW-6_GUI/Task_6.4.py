
from __future__ import annotations
from itertools import chain
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("6_4 Конвертер валют")
root.geometry("450x315")
root.resizable(False, False)

def selected_1():
    currency_values = [90, 1, 100, 120]
    currency_1 = combobox1.get()
    if currency_1 == 'USD':
        val_1 = 90
    if currency_1 == 'RUB':
        val_1 = 1
    if currency_1 == 'EUR':
        val_1 = 100
    if currency_1 == 'GBP':
        val_1 = 150
    amount_currency_1 = entry_currency1.get()
    currency_2 = combobox2.get()
    if currency_2 == 'USD':
        val_2 = 90
    if currency_2 == 'RUB':
        val_2 = 1
    if currency_2 == 'EUR':
        val_2 = 100
    if currency_2 == 'GBP':
        val_2 = 150
    amount_currency_2 = ((val_1 * int(amount_currency_1)) / val_2)

    entry_currency2.configure(textvariable=amount_currency_2)

def selected_2():
    currency_values = [90,1,100,120]
    currency_2 = combobox2.get()
    if currency_2=='USD':
        val_2 = 90
    if currency_2 == 'RUB':
        val_2 = 1
    if currency_2 == 'EUR':
        val_2 = 100
    if currency_2 == 'GBP':
        val_2 = 150
    amount_currency_2 = entry_currency2.get()
    currency_1 = combobox1.get()
    if currency_1 == 'USD':
        val_1 = 90
    if currency_1 == 'RUB':
        val_1 = 1
    if currency_1 == 'EUR':
        val_1 = 100
    if currency_1 == 'GBP':
        val_1 = 150
    amount_currency_1 = ((val_2 * int(amount_currency_2)) / val_1)

    entry_currency1.configure(textvariable=amount_currency_1)



label_name = ttk.Label(text="WELCOME", font = ("Arial", 18), foreground="#FF033E")
label_name.place(x=30, y=30, anchor=W)

label_name2 = ttk.Label(text="This is a currency converter", font = ("Arial", 14), foreground="#FF033E")
label_name2.place(x=30, y=80, anchor=W)


entry_currency1 = ttk.Entry(validate="key", validatecommand=selected_1)
entry_currency1.place(anchor=NW, x=40, y= 130, height=40)

entry_currency2 = ttk.Entry(validate="key", validatecommand=selected_2)
entry_currency2.place(anchor=NW, x=40, y= 210, height=40)



currency = ['USD', 'RUB', 'EUR', 'GBP']
combobox1 = ttk.Combobox(values=currency)
combobox1.place(anchor=NE, x=300, y= 130, height=40)
#combobox1.bind(selected_1)
combobox2 = ttk.Combobox(values=currency)
combobox2.place(anchor=NE, x=300, y= 210, height=40)
#combobox2.bind(selected_2)


root.mainloop()
