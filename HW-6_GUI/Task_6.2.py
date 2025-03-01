
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



def submit():
    window = Tk()
    window.title("Результат ввода")
    window.geometry("470x300")
    languages = select()
    if "@" in entry_mail1.get() and "@" in entry_mail2.get():
        text_window = (f"Данные успешно введены!!! \n "
                    f"Имя: {entry_name.get()}\n"
                    f" Email 1: {entry_mail1.get()}\n"
                    f" Email 2: {entry_mail2.get()}\n"
                    f" Пол:   {selected_sex.get()} \n"
                    f" Изучаемые языки :\n {languages}")
    else:
        text_window = "Проверьте правильность ввода данных (в электронной почте нет символа @)!!!"

    label = ttk.Label(window, text=text_window)
    label.pack(anchor=CENTER, expand=1)

    window.mainloop()
def select():
    result = ""
    if python.get() == 1: result += "     Python\n"
    if java.get() == 1: result += "     Java\n"
    if c_.get() == 1: result += "     C++\n"
    if cs.get() == 1: result += "     C#\n"
    if js.get() == 1: result += "     JavaScript\n"
    return result


for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(9): root.rowconfigure(index=r, weight=1)

label_name = ttk.Label(text="Account", font = ("Arial", 18), foreground="#FF033E")
label_name.grid(row=0, column=0)

message1 = StringVar()
message1.set("Full name")
entry_name = ttk.Entry(textvariable=message1, width=100)
entry_name.grid(row=1, column=0, columnspan=5, padx=30, pady=10)


message2 = StringVar()
message2.set("Email address@")
entry_mail1 = ttk.Entry(textvariable=message2, width=100)
entry_mail1.grid(row=2, column=0, columnspan=5, padx=30, pady=10)

message3 = StringVar()
message3.set("Email address@")
entry_mail2 = ttk.Entry(textvariable=message3, width=100)
entry_mail2.grid(row=3, column=0, columnspan=5, padx=30, pady=10)

label_name = ttk.Label(text="Gender", font = ("Arial", 15), foreground="#FF033E")
label_name.grid(row=4, column=0)

photo1 = PhotoImage(file="male.png")
photo2 = PhotoImage(file="female.png")

selected_sex = StringVar()
mail_btn = ttk.Radiobutton(text="Male", value = "Male", variable=selected_sex, image=photo1, compound="left")
mail_btn.grid(row=5, column=0)

femail_btn = ttk.Radiobutton(text="Female", value = "Female", variable=selected_sex, image=photo2, compound="left")
femail_btn.grid(row=5, column=1)

label_name = ttk.Label(text="Programming languages", font = ("Arial", 15), foreground="#FF033E")
label_name.grid(row=6, column=0, columnspan = 2)


python = IntVar()
btn_py = ttk.Checkbutton(text="Python", variable=python, command=select)
btn_py.grid(row=7, column=0)

java = IntVar()
btn_ja = ttk.Checkbutton(text="Java", variable=java, command=select)
btn_ja.grid(row=7, column=1)

c_ = IntVar()
btn_c_ = ttk.Checkbutton(text="C++", variable=c_, command=select)
btn_c_.grid(row=7, column=2)

cs = IntVar()
btn_cs = ttk.Checkbutton(text="C#", variable=cs, command=select)
btn_cs.grid(row=7, column=3)

js = IntVar()
btn_js = ttk.Checkbutton(text="JavaScript", variable=js, command=select)
btn_js.grid(row=7, column=4, padx=20)


style2 = ttk.Style()
style2.configure("TButton", foreground='blue', background='orange')
btn_submit = ttk.Button(text="SUBMIT", style="TButton", command = submit)
btn_submit.grid(row=8, column=0, columnspan=4, sticky=NSEW,padx=20, pady=30)



root.mainloop()
