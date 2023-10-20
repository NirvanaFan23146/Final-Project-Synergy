import tkinter as tk
from DataBase.database_controller import database
from application.main_window import Main_window

if __name__ == '__main__':
    root = tk.Tk()
    db = database()
    app = Main_window(root = root, db=db)
    app.pack()
    root.title('Список сотрудников компании')
    root.geometry('665x450')
    root.resizable(False, False)
    root.mainloop()