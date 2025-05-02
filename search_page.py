from tkinter import *
import tkinter as tk

from searcher import expand_item, found_items


def search():
    found_list.delete(0,END)
    found_items.clear()
    expand_item(search_field.get())
    for item in found_items:
        add_string = ''
        for element in item:
            add_string += element
            add_string += ' -> '
        add_string = add_string[0:-3]
        found_list.insert(END, add_string)


app = tk.Tk()
app.title('Поиск')
app.geometry('600x300+600+200')
app.resizable(False, False)

search_label = tk.Label(text='Введите искомое значение')
search_label.grid(row=0, column=1, columnspan=2, padx=30, pady=10, ipadx=2, ipady=2)

search_field = tk.Entry(width=50)
search_field.grid(row=1, column=1, padx=30, pady=10, ipadx=2, ipady=2)

search_button = tk.Button(text='Найти', width=10, command=search)
search_button.grid(row=1, column=2, padx=10, pady=10, ipadx=2, ipady=2)

found_list = tk.Listbox(width=80)
found_list.grid(row=2, column=1, columnspan=2, padx=50, pady=10, ipadx=2, ipady=2)


app.mainloop()