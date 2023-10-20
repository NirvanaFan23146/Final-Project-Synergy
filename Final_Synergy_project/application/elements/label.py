import tkinter as tk
from tkinter import ttk
from typing import Tuple

class Entry():

    def __init__(self, Frame, text : str, label_position : Tuple [int], entry_position : Tuple [int]) -> None:
        self.label = tk.Label(Frame, text = text)
        self.label.place(x = label_position[0], y = label_position[1])

        self.entry = tk.Entry(Frame)
        self.entry.place(x = entry_position[0], y = entry_position[1])
