import tkinter as tk
from tkinter import ttk
from typing import Callable

class Button():

    def __init__(self, Frame, text : str, function : Callable) -> None:
        self.body = tk.Button(Frame, command = function, text = text)

    def pack(self, side : str) -> None:
        self.body.pack(side = side)