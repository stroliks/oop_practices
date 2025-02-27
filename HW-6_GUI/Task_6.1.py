from cProfile import label
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Home Work 6_1 (date_of_user)")
icon = PhotoImage(file = "Pacman.png")
root.iconphoto(False, icon)
root.geometry("600x300")
root.resizable(False, False)


def input_data():
    if not (entry_name.get() is None) and ("@" in entry_mail.get()) and (int(entry_age.get()) > 0):
        label_result = ttk.Label(text="Данные успешно введены!!!", background="#00322d", font=("Arial", 15))
    else:
        label_result = ttk.Label(text="Введены неверные данные либо поле <<Имя>> не заполнено",  background="#FF033E", font=("Arial", 15))
    label_result.grid(row=7, column=0, columnspan=3, sticky=NSEW)

for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(6): root.rowconfigure(index=r, weight=1)

label_name = ttk.Label(text="Введите имя", font = ("Arial", 18))
label_name.grid(row=0, column=0)

entry_name = ttk.Entry(width=30)
entry_name.grid(row=1, column=0)

label_mail = ttk.Label(text="Введите email", font = ("Arial", 18))
label_mail.grid(row=2, column=1)
entry_mail = ttk.Entry(width=30)
entry_mail.grid(row=3, column=1)

label_age = ttk.Label(text="Введите возраст", font = ("Arial", 18))
label_age.grid(row=4, column=2)
entry_age = ttk.Entry(width=30)
entry_age.grid(row=5, column=2)

btn_enter = ttk.Button(text="Отправить", command = input_data)
btn_enter.grid(row=6, column=0, columnspan=3, sticky=NSEW)

root.mainloop()