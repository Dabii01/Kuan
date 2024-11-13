import tkinter as tk

def move_left(event):
    ship.move(shuttle, -10, 0)

def move_right(event):
    ship.move(shuttle, +10, 0)


interface = tk.Tk()
interface.geometry("500x670")
interface.title("Space Impact")

ship = tk.Canvas(interface, width=500, height=670, background="gray")
ship.pack()

shuttle=ship.create_rectangle(225, 600, 275, 650, fill="blue")

interface.bind("<Left>", move_left)
interface.bind("<Right>", move_right)

interface.mainloop()
