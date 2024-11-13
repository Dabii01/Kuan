import tkinter as tk
from tkinter import ttk

gui=tk.Tk()
gui.title("Space Impact")
gui.geometry("500x700")

ttk.Label(gui, background = "#025043").pack(expand = True, fill = "both")

gui.mainloop()