
from __future__ import annotations
from itertools import chain
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Home Work 6_3 (Array Calculator)")
icon = PhotoImage(file = "Pacman.png")
root.iconphoto(False, icon)
root.geometry("600x470")
root.resizable(False, False)


def window_error():
    window = Tk()
    window.title("Ошибка")
    window.geometry("500x200")
    text_window = "Проверьте правильность ввода данных (введены не числовые значения)!!!"

    label = ttk.Label(window, text=text_window)
    label.pack(anchor=CENTER, expand=1)
    btn = ttk.Button(window, text="Хорошо, я проверю)))", command=lambda: window.destroy())
    btn.pack(anchor=CENTER, expand=1)

    window.mainloop()


def hendler_array():
    values = []
    str_array = entry_array.get()
    try:
        if (all(isinstance(int(i), int) for i in str_array)):
            array = []
            array = [int(a) for a in str_array]
            value_even = 0
            for i in array:
                if i % 2 == 0:
                    value_even += 1
            values.extend([len(array), max(array), min(array), (sum(array) / len(array)), value_even, (len(array) - value_even)])
            lable_len.configure(text=values[0])
            lable_max.configure(text=values[1])
            lable_min.configure(text=values[2])
            lable_avg.configure(text=values[3])
            lable_even.configure(text=values[4])
            lable_uneven.configure(text=values[5])

    except:
        window_error()




for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(7): root.rowconfigure(index=r, weight=1)

label_name = ttk.Label(text="Calculator Arrays", font = ("Arial", 16), foreground="#FF033E")
label_name.grid(row=0, column=0, padx=30, sticky=W)

message1 = StringVar()
message1.set("input array")
entry_array = ttk.Entry(textvariable=message1, width=100)
entry_array.grid(row=1, column=0, columnspan=3, padx=30, pady=10)

list_name = ["Lenght:", "Max elem:", "Min elem:","Avg:", "Number of even:", "Number of uneven:",]

for element in list_name:
    label = ttk.Label(text=element)
    label.grid(row=(list_name.index(element)+2), column=0, padx=30, sticky=W)

lable_len = ttk.Label(text=" (result) ")
lable_len.grid(row= 2, column=2, padx=30, sticky=E)

lable_max = ttk.Label(text=" (result) ")
lable_max.grid(row= 3, column=2, padx=30, sticky=E)

lable_min = ttk.Label(text=" (result) ")
lable_min.grid(row= 4, column=2, padx=30, sticky=E)

lable_avg = ttk.Label(text=" (result) ")
lable_avg.grid(row= 5, column=2, padx=30, sticky=E)

lable_even = ttk.Label(text=" (result) ")
lable_even.grid(row= 6, column=2, padx=30, sticky=E)

lable_uneven = ttk.Label(text=" (result) ")
lable_uneven.grid(row= 7, column=2, padx=30, sticky=E)


btn_submit = ttk.Button(text="SUBMIT", command = hendler_array)
btn_submit.grid(row=8, column=0, columnspan=2, sticky=NSEW,padx=20, pady=30)

root.mainloop()
