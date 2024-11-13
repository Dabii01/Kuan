import tkinter as tk
from tkinter import ttk

class main_interface():
    def __init__(self):
        self.Interface = tk.Tk()
        self.Interface.title("Space Impact")
        self.Interface.geometry("500x700")
        ttk.Label(self.Interface, background= "#025043").pack(expand = True, fill = "both")

    def print_self(self):
        self.Interface.mainloop()

interface=main_interface()

print(interface.print_self())