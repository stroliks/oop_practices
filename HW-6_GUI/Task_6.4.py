
from __future__ import annotations
from itertools import chain
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("6_4 Конвертер валют")
root.geometry("450x315")
root.resizable(False, False)
currency = ["USD", "RUB", "EUR", "GBP"]
courses = [90,1,100,150]

def selected_1(event):
    val_2 = courses[currency.index(text2.get())]
    amount_currency_2 = float(entry_currency2.get())
    val_1 = courses[currency.index(text1.get())]
    amount_currency_1 = ((val_2 * amount_currency_2) / val_1)
    text_entry1.set(str(amount_currency_1))
    entry_currency1.configure(textvariable=text_entry1)

def selected_2(event):
    val_1 = courses[currency.index(text1.get())]
    amount_currency_1 = float(entry_currency1.get())
    val_2 = courses[currency.index(text2.get())]
    amount_currency_2 = ((val_1 * amount_currency_1) / val_2)
    text_entry2.set(str(amount_currency_2))
    entry_currency2.configure(textvariable=text_entry2)


label_name = ttk.Label(text="WELCOME", font = ("Arial", 18), foreground="#FF033E")
label_name.place(x=30, y=30, anchor=W)

label_name2 = ttk.Label(text="This is a currency converter", font = ("Arial", 14), foreground="#FF033E")
label_name2.place(x=30, y=80, anchor=W)

text_entry1=StringVar()
entry_currency1 = ttk.Entry(textvariable=text_entry1)
entry_currency1.place(anchor=NW, x=40, y= 130, height=40)

text_entry2=StringVar()
entry_currency2 = ttk.Entry(textvariable=text_entry2)
entry_currency2.place(anchor=NW, x=40, y= 210, height=40)

text1 = StringVar()
text2 = StringVar()

combobox1 = ttk.Combobox(textvariable=text1, values=currency, state="readonly")
combobox1.place(anchor=NE, x=300, y= 130, height=40)
combobox1.bind("<<ComboboxSelected>>",selected_1)
combobox2 = ttk.Combobox(textvariable=text2, values=currency, state="readonly")
combobox2.place(anchor=NE, x=300, y= 210, height=40)
combobox2.bind("<<ComboboxSelected>>", selected_2)


root.mainloop()
