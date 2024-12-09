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
        
        self.canvas = tk.Canvas(self.Interface, width=500, height=670, bg="black")
        self.canvas.pack()

        self.score = 0

        self.score_label = tk.Label(self.Interface, text="Score: 0", font=("Arial", 14), fg="white", bg="black")
        self.canvas.create_window(40, 20, window=self.score_label)

        self.ship = self.canvas.create_polygon(194, 633, 223, 596, 236, 546, 249, 596, 279, 633, 250, 633, 250, 638, 243, 638, 243, 633, 230, 633, 230, 638, 222, 638, 222, 633, fill="#790D0D")

        self.canvas.bind_all("<Left>", self.move_left)
        self.canvas.bind_all("<Right>", self.move_right)
        self.canvas.bind_all("<space>", self.shoot)

        self.enemies = []
        self.create_enemy()

    def move_left(self, event):
        x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13 = self.canvas.coords(self.ship)
        if x1 > 10:
            self.canvas.move(self.ship, -10, 0)

    def move_right(self, event):
        x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13 = self.canvas.coords(self.ship)
        if x5 < 490:
            self.canvas.move(self.ship, +10, 0)

    def shoot(self, event):
        x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12, x13, y13 = self.canvas.coords(self.ship)
        bullet_id = self.canvas.create_oval(x3 - 5, y3 - 10, x3 + 3, y3 +10, fill="blue")
        self.move_bullet(bullet_id)

    def move_bullet(self, bullet_id):
        coords = self.canvas.coords(bullet_id)
        if coords:
            x1, y1, x2, y2 = coords
            if y2 > 0: 
                self.canvas.move(bullet_id, 0, -10)  
                self.check_collision(bullet_id) 
                self.Interface.after(60, lambda: self.move_bullet(bullet_id)) 
            else:
                self.canvas.delete(bullet_id)

    def check_collision(self, bullet_id):
        if self.canvas.coords(bullet_id):
            bullet_x1, bullet_y1, bullet_x2, bullet_y2 = self.canvas.coords(bullet_id)
            for enemy_id in self.enemies[:]:
                enemy_x1, enemy_y1, enemy_x2, enemy_y2, enemy_x3, enemy_y3, enemy_x4, enemy_y4, enemy_x5, enemy_y5, enemy_x6, enemy_y6, enemy_x7, enemy_y7, enemy_x8, enemy_y8, enemy_x9, enemy_y9, enemy_x10, enemy_y10, enemy_x11, enemy_y11, enemy_x12, enemy_y12 = self.canvas.coords(enemy_id)
                if (bullet_x2 > enemy_x1 and bullet_x1 < enemy_x7) and (bullet_y2 < enemy_y8 and bullet_y1 > enemy_y2):
                    self.canvas.delete(bullet_id)
                    self.canvas.delete(enemy_id)
                    self.enemies.remove(enemy_id)
                    self.update_score()

    def update_score(self):
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

    def create_enemy(self):
        x1 = R.randint(20, 450)
        enemy_id = self.canvas.create_polygon(x1, 42, x1 + 13, 25, x1 + 13, 46, x1 + 23, 28, x1 + 34, 46, x1 + 34, 25, x1 + 48, 42, x1 + 34, 93, x1 + 34, 63, x1 + 24, 81, x1 + 14, 63, x1 + 13, 93, fill="gray")
        self.enemies.append(enemy_id)
        self.move_enemies(enemy_id)
        self.Interface.after(800, self.create_enemy)

    def move_enemies(self, enemy_id):
        if self.canvas.coords(enemy_id):
            x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, x10, y10, x11, y11, x12, y12 = self.canvas.coords(enemy_id)
            if y8 < 650:
                self.canvas.move(enemy_id, 0, +10)
                self.check_player_collision(enemy_id)
                self.Interface.after(100, lambda: self.move_enemies(enemy_id))
            else:
                self.canvas.delete(enemy_id)
                self.enemies.remove(enemy_id)
                self.game_over()

    def check_player_collision(self, enemy_id):
        enemy_x1, enemy_y1, enemy_x2, enemy_y2, enemy_x3, enemy_y3, enemy_x4, enemy_y4, enemy_x5, enemy_y5, enemy_x6, enemy_y6, enemy_x7, enemy_y7, enemy_x8, enemy_y8, enemy_x9, enemy_y9, enemy_x10, enemy_y10, enemy_x11, enemy_y11, enemy_x12, enemy_y12 = self.canvas.coords(enemy_id)
        player_x1, player_y1, player_x2, player_y2, player_x3, player_y3, player_x4, player_y4, player_x5, player_y5, player_x6, player_y6, player_x7, player_y7, player_x8, player_y8, player_x9, player_y9, player_x10, player_y10, player_x11, player_y11, player_x12, player_y12, player_x13, player_y13 = self.canvas.coords(self.ship)
        if (enemy_x7 > player_x1 and enemy_x1 < player_x5) and (enemy_y8 > player_y3 and enemy_y2 < player_y7):
            self.canvas.delete(enemy_id)
            self.enemies.remove(enemy_id)
            self.game_over()

    def game_over(self):
        self.Interface.after(500, lambda: self.Interface.destroy())
        mb.showinfo("Game Over", f"Game Over! Your score was {self.score}")

    def run(self):
        self.Interface.mainloop()

play()
