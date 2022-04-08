from tkinter import *


class RdButton:
    def __init__(self, func, mode, x_pos, y_pos, var):
        Radiobutton(value=mode,
                    text=mode,
                    font=("Arial", 15),
                    variable=var,
                    command=func).place(x=x_pos, y=y_pos)
