from tkinter import *


def Add():
    listbox.insert(END, entry.get())
    entry.delete(0, END)


def Delete():
    select = list(listbox.curselection())
    select.reverse()
    for i in select:
        listbox.delete(i)


def Save():
    with open("hello.txt", "w") as file:
        file.writelines(str(req))


def on_selected(evt):
    value = listbox.get(listbox.curselection())
    output.delete(0, END)
    output.insert('0', value)


req = Tk()
req.title("Программа - имя")
req.geometry("450x180")

main_menu = Menu()
main_menu.add_cascade(label="Файл")
main_menu.add_cascade(label="Вид")
main_menu.add_cascade(label="Справка")

listbox = Listbox(req)
listbox.selectmode = EXTENDED
listbox.pack(side=LEFT)
listbox.bind('<<ListboxSelect>>', on_selected)

f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)

output = Entry(req)
output.pack(side=LEFT, padx=40)

button_1 = Button(f, text="Добавить", command=Add).pack(fill=X)
button_2 = Button(f, text="Удалить", command=Delete).pack(fill=X)
button_3 = Button(f, text="Сохранить", command=Save).pack(fill=X)

req.config(menu=main_menu)
req.mainloop()
