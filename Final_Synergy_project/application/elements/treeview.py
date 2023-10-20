import tkinter as tk
from tkinter import ttk
from typing import Tuple, Dict

class Treeview():

    def __init__(self, Frame, columns : Dict[str, str], height : float, wights : Dict[str, float]) -> None:
        self.body = ttk.Treeview(Frame, columns = tuple(list(columns.keys())), height = height, show = 'headings')

        for column_id in columns:
            self.body.column(column_id, width = wights[column_id], anchor = tk.CENTER)  
            self.body.heading(column_id, text = columns[column_id])

        self.body.pack(side = tk.LEFT)
        
    def fill_treeview(self, data : Tuple [Tuple [str]]) -> None:
        [self.body.delete(i) for i in self.body.get_children()]
        [self.body.insert('', 'end', values = row) for row in data]