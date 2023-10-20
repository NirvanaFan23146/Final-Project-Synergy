import tkinter as tk
from application.elements.treeview import Treeview
from application.elements.button import Button
from application.application_data import treeview_columns_names, treeview_columns_shapes
from application.sub_window import Sub_Window

class Main_window(tk.Frame):
    def __init__(self, root, db) -> None:

        self.root = root
        super().__init__(root)
        self.db = db
        self.init_main()


    def init_main(self):
        # Создаем панель инструментов
        self.toolbar = tk.Frame(self)
        self.toolbar.pack(side = tk.TOP, fill = tk.X)

        btn_open_add = Button(self.toolbar, function = self.create_sub_window1, text = "Add")
        btn_open_add.pack(side = tk.LEFT)

        btn_open_del = Button(self.toolbar, function = self.create_sub_window2, text = "Delete")
        btn_open_del.pack(side = tk.LEFT)

        btn_open_update = Button(self.toolbar, function = self.create_sub_window3, text = "Update")
        btn_open_update.pack(side = tk.LEFT)

        btn_open_find = Button(self.toolbar, function = self.create_sub_window4, text = "Find")
        btn_open_find.pack(side = tk.LEFT)


        btn_open_refresh = Button(self.toolbar, function = self.refresh, text = "Refresh")
        btn_open_refresh.pack(side = tk.RIGHT)

        self.tree = Treeview(self, columns = treeview_columns_names, height = 45, wights = treeview_columns_shapes)
        self.tree.fill_treeview(self.db.find_all_staff())
        

    def create_sub_window1(self) -> None:
        self.create_sub_window(type = "ADD", title = "Добавить")
        
    def create_sub_window2(self) -> None:
        self.create_sub_window(type = "DELETE", title = "Удалить")

    def create_sub_window3(self) -> None:
        self.create_sub_window(type = "UPDATE", title = "Изменить")

    def create_sub_window4(self) -> None:
        self.create_sub_window(type = "FIND", title = "Найти")


    def create_sub_window(self, type : str, title : str) -> None:
        Sub_Window(root = self.root, app = self, type = type, db = self.db, title = title)

    def refresh(self) -> None:
        self.tree.fill_treeview(self.db.find_all_staff())
