import tkinter as tk
import random as r

class Player():
    def __init__(self):
        self.interface = tk.Tk()
        self.interface.geometry("500x670")
        self.interface.title("Space Impact")

        self.ship = tk.Canvas(self.interface, width=500, height=670, background="gray")
        self.ship.place(x=0, y=0)

        self.shuttle=self.ship.create_rectangle(225, 600, 275, 650, fill="blue")

        self.interface.bind("<Left>", self.move_left)
        self.interface.bind("<Right>", self.move_right)

    def move_left(self,event):
        x1, y1, x2, y2 = self.ship.coords(self.shuttle)
        if x1>0:
            self.ship.move(self.shuttle, -10, 0)


    def move_right(self,event):
        x1, y1, x2, y2 = self.ship.coords(self.shuttle)
        if x2<500:
            self.ship.move(self.shuttle, +10, 0)

    def run(self):
        self.interface.mainloop()

game=Player()

print(game.run())
