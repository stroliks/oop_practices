
from __future__ import annotations
from itertools import chain
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Home Work 6_2 (Account)")
icon = PhotoImage(file = "Pacman.png")
root.iconphoto(False, icon)
root.geometry("600x470")
root.resizable(False, False)

# def input_data():
#     if not (entry_name.get()=="") and ("@" in entry_mail.get()) and (int(entry_age.get()) > 0):
#         label_result = ttk.Label(text="Данные успешно введены!!!", background="#66ff33", font=("Arial", 15))
#     else:
#         label_result = ttk.Label(text="Введены неверные данные либо поле <<Имя>> не заполнено",  background="#FF033E", font=("Arial", 15))
#     label_result.grid(row=7, column=0, columnspan=3, sticky=NSEW)

for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(9): root.rowconfigure(index=r, weight=1)

label_name = ttk.Label(text="Account", font = ("Arial", 18), foreground="#FF033E")
label_name.grid(row=0, column=0, columnspan=2)

message1 = StringVar()
message1.set("Full name")
entry_name = ttk.Entry(textvariable=message1)
entry_name.grid(row=1, column=0, columnspan=5)


message2 = StringVar()
message2.set("Email address")
entry_name = ttk.Entry(textvariable=message2)
entry_name.grid(row=2, column=0, columnspan=5)

message3 = StringVar()
message3.set("Email address")
entry_name = ttk.Entry(textvariable=message3)
entry_name.grid(row=3, column=0, columnspan=5)

label_name = ttk.Label(text="Gender", font = ("Arial", 15), foreground="#FF033E")
label_name.grid(row=4, column=0)

photo1 = PhotoImage(file="male.png")
photo2 = PhotoImage(file="female.png")

mail_btn = ttk.Radiobutton(text="Male", value = "Male", image=photo1, compound="left")
mail_btn.grid(row=5, column=0)

femail_btn = ttk.Radiobutton(text="Female", value = "Female", image=photo2, compound="left")
femail_btn.grid(row=5, column=1)

label_name = ttk.Label(text="Programming languages", font = ("Arial", 15), foreground="#FF033E")
label_name.grid(row=6, column=0)




# btn_enter = ttk.Button(text="SUBMIT", command = input_data)
# btn_enter.grid(row=8, column=1, columnspan=3, sticky=NSEW)




root.mainloop()
