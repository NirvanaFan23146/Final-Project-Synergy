import tkinter as tk
from tkinter import ttk
from application.elements.label import Entry
from application.elements.button import Button
from typing import List

class Sub_Window(tk.Toplevel):

    def __init__(self, root, app, type, db, title) -> None:
        super().__init__(root)

        self.title(title)
        self.geometry('400x260')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        self.db = db
        self.type = type
        self.init_sub_window(type = self.type)
        self.view = app

    def init_sub_window(self, type : str) -> None:

        if type == "ADD":
            self.label1 = Entry(self, text = "Имя", label_position = (50, 20), entry_position = (200, 20))
            self.label2 = Entry(self, text = "Фамилия", label_position = (50, 50), entry_position = (200, 50))
            self.label3 = Entry(self, text = "Отчество", label_position = (50, 80), entry_position = (200, 80))
            self.label4 = Entry(self, text = "Телефон", label_position = (50, 110), entry_position = (200, 110))
            self.label5 = Entry(self, text = "Почта", label_position = (50, 140), entry_position = (200, 140))
            self.label6 = Entry(self, text = "Зарплата", label_position = (50, 170), entry_position = (200, 170))

            self.btn_close = Button(self, text = 'Закрыть', function = self.destroy)
            self.btn_close.body.place(x = 300, y = 200)

            self.btn_ok = Button(self, text = 'Добавить', function = self.create)
            self.btn_ok.body.place(x = 220, y = 200)

        elif type == "DELETE":
            self.label1 = Entry(self, text = "ID", label_position = (50, 20), entry_position = (200, 20))

            self.btn_close = Button(self, text = 'Закрыть', function = self.destroy)
            self.btn_close.body.place(x = 300, y = 200)

            self.btn_ok = Button(self, text = 'Удалить', function = self.delete)
            self.btn_ok.body.place(x = 220, y = 200)


        elif type == "UPDATE":
            self.label1 = Entry(self, text = "Имя", label_position = (50, 20), entry_position = (200, 20))
            self.label2 = Entry(self, text = "Фамилия", label_position = (50, 50), entry_position = (200, 50))
            self.label3 = Entry(self, text = "Отчество", label_position = (50, 80), entry_position = (200, 80))
            self.label4 = Entry(self, text = "Телефон", label_position = (50, 110), entry_position = (200, 110))
            self.label5 = Entry(self, text = "Почта", label_position = (50, 140), entry_position = (200, 140))
            self.label6 = Entry(self, text = "Зарплата", label_position = (50, 170), entry_position = (200, 170))
            self.label7 = Entry(self, text = "ID", label_position = (50, 200), entry_position = (200, 200))

            self.btn_close = Button(self, text = 'Закрыть', function = self.destroy)
            self.btn_close.body.place(x = 300, y = 230)

            self.btn_ok = Button(self, text = 'Изменить', function = self.update)
            self.btn_ok.body.place(x = 220, y = 230)


        elif type == "FIND":
            self.label1 = Entry(self, text = "Имя", label_position = (50, 20), entry_position = (200, 20))
            self.label2 = Entry(self, text = "Фамилия", label_position = (50, 50), entry_position = (200, 50))
            self.label3 = Entry(self, text = "Отчество", label_position = (50, 80), entry_position = (200, 80))

            self.btn_close = Button(self, text = 'Закрыть', function = self.destroy)
            self.btn_close.body.place(x = 300, y = 230)

            self.btn_ok = Button(self, text = 'Найти', function = self.find)
            self.btn_ok.body.place(x = 220, y = 230)


    
    def create(self) -> None:
        data = []
        data.append(self.label1.entry.get())
        data.append(self.label2.entry.get())
        data.append(self.label3.entry.get())
        data.append(self.label4.entry.get())
        data.append(self.label5.entry.get())
        data.append(self.label6.entry.get())
        self.db.create_staff(data)
        self.view.tree.fill_treeview(self.db.find_all_staff())


    def delete(self) -> None:
        data = self.label1.entry.get()
        self.db.delete_staff(data)
        self.view.tree.fill_treeview(self.db.find_all_staff())


    def update(self) -> None:
        data = []
        data.append(self.label1.entry.get())
        data.append(self.label2.entry.get())
        data.append(self.label3.entry.get())
        data.append(self.label4.entry.get())
        data.append(self.label5.entry.get())
        data.append(self.label6.entry.get())
        data.append(self.label7.entry.get())
        self.db.update_staff(data)
        self.view.tree.fill_treeview(self.db.find_all_staff())

    def find(self) -> None:
        data = []
        data.append(self.label1.entry.get())
        data.append(self.label2.entry.get())
        data.append(self.label3.entry.get())
        staff = self.db.find_staff(data)
        self.view.tree.fill_treeview(staff)
        self.destroy()
