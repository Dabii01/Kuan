import tkinter as tk
from tkinter import messagebox as mb
import random as R

def play():
    Game().run()

class Game():
    def __init__(self):
        self.Interface = tk.Tk()
        self.Interface.geometry("500x650")
        self.Interface.title("Space Impact")
        self.score = 0
        
        self.canvas = tk.Canvas(self.Interface, width=500, height=650, bg="black")
        self.canvas.pack()
        
        self.space_color = "darkblue"
        self.player_color = "green"
        self.enemy_color = "red"
        self.bullet_color = "yellow"
        self.explosion_color = "orange"

        self.canvas.create_rectangle(0, 0, 500, 650, fill=self.space_color)

        self.score_text = self.canvas.create_text(50, 20, text=f"Score: {self.score}", fill="white", font=("Arial", 16))

        self.player_width = 125
        self.player_height = 120
        self.character_id = self.canvas.create_rectangle(250 - self.player_width // 2, 610 - self.player_height // 2, 250 + self.player_width // 2, 610 + self.player_height // 2, fill=self.player_color)

        self.enemies = []
        self.spawn_enemy()
        
        # Control bindings
        self.canvas.bind_all("<Left>", self.move_left)
        self.canvas.bind_all("<Right>", self.move_right)
        self.canvas.bind_all("<space>", self.shoot)

    def move_left(self, event):
        self.move_player(-10)

    def move_right(self, event):
        self.move_player(10)

    def move_player(self, dx):
        x1, y1, x2, y2 = self.canvas.coords(self.character_id)
        if 50 <= x1 + dx <= 450:
            self.canvas.move(self.character_id, dx, 0)

    def shoot(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.character_id)
        bullet_id = self.canvas.create_rectangle(x1 + self.player_width // 2 - 5, y1, x2 - self.player_width // 2 + 5, y1 - 25, fill="blue")
        self.animate_bullet(bullet_id)

    def animate_bullet(self, bullet_id):
        if self.canvas.coords(bullet_id):
            x1, y1, x2, y2 = self.canvas.coords(bullet_id)
            if y2 > 0:
                self.canvas.move(bullet_id, 0, -10)
                self.check_collision(bullet_id)
                self.Interface.after(80, lambda: self.animate_bullet(bullet_id))
            else:
                self.canvas.delete(bullet_id)

    def check_collision(self, bullet_id):
        if self.canvas.coords(bullet_id):
            bx1, by1, bx2, by2 = self.canvas.coords(bullet_id)
            for enemy_id in self.enemies[:]:
                ex1, ey1, ex2, ey2 = self.canvas.coords(enemy_id)
                if (bx2 > ex1 and bx1 < ex2) and (by2 > ey1 and by1 < ey2):
                    self.canvas.delete(bullet_id)
                    self.canvas.delete(enemy_id)
                    self.enemies.remove(enemy_id)
                    self.score += 1
                    self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

    def check_player_collision(self, enemy_id):
        ex1, ey1, ex2, ey2 = self.canvas.coords(enemy_id)
        px1, py1, px2, py2 = self.canvas.coords(self.character_id)
        if (px2 > ex1 and px1 < ex2) and (py2 > ey1 and py1 < ey2):
            self.canvas.delete(enemy_id)
            self.enemies.remove(enemy_id)
            self.Interface.destroy()

    def spawn_enemy(self):
        x = R.randint(50, 450)
        enemy_id = self.canvas.create_rectangle(x - 50, 50 - 50, x + 50, 50 + 50, fill=self.enemy_color)
        self.enemies.append(enemy_id)
        self.move_enemy(enemy_id)
        self.Interface.after(1000, self.spawn_enemy)

    def move_enemy(self, enemy_id):
        if self.canvas.coords(enemy_id):
            x1, y1, x2, y2 = self.canvas.coords(enemy_id)
            if y2 < 650:
                self.canvas.move(enemy_id, 0, 10)
                self.check_player_collision(enemy_id)
                self.Interface.after(100, lambda: self.move_enemy(enemy_id))
            else:
                self.canvas.delete(enemy_id)
                self.enemies.remove(enemy_id)

    def run(self):
        self.Interface.mainloop()

play()
