import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import random as R

def play():
    Game().run()

class Game():
    def __init__(self):
        self.Interface = tk.Tk()
        self.Interface.geometry("500x650")
        self.Interface.title("Space Impact")
        self.score = 0
        
        self.canvas = tk.Canvas(self.Interface, width=500, height=670)
        self.canvas.pack()
        
        self.Space = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Pictures\smoother_pixelated_image.jpg").resize((500, 670)))
        self.Main_player = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Pictures\transparent_ufo.png").resize((125, 120)))
        self.enemy_image = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Pictures\ship_image.png").resize((100, 100)))
        self.bullet_image = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Pictures\new_bullet.png").resize((10, 25)))
        self.explosion_image = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Pictures\explosion-removebg-preview.png").resize((100, 100)))
        
        self.canvas.create_image(250, 335, image=self.Space)
        self.score_text = self.canvas.create_text(50, 20, text=f"Score: {self.score}", fill="white", font=("Arial", 16))
        self.character_id = self.canvas.create_image(250, 610, image=self.Main_player)
        self.enemies = []
        
        self.spawn_enemy()
        self.canvas.bind_all("<Left>", lambda e: self.move_player(-10))
        self.canvas.bind_all("<Right>", lambda e: self.move_player(10))
        self.canvas.bind_all("<space>", self.shoot)

    def move_player(self, dx):
        x, _ = self.canvas.coords(self.character_id)
        if 50 <= x + dx <= 450:
            self.canvas.move(self.character_id, dx, 0)

    def shoot(self, _):
        x, y = self.canvas.coords(self.character_id)
        bullet_id = self.canvas.create_image(x, y, image=self.bullet_image, anchor="center")
        self.animate_bullet(bullet_id)

    def animate_bullet(self, bullet_id):
        if self.canvas.coords(bullet_id):
            y = self.canvas.coords(bullet_id)[1]
            if y > 0:
                self.canvas.move(bullet_id, 0, -10)
                self.check_collision(bullet_id)
                self.Interface.after(80, lambda: self.animate_bullet(bullet_id))
            else:
                self.canvas.delete(bullet_id)

    def check_collision(self, bullet_id):
        if self.canvas.coords(bullet_id):
            bx, by = self.canvas.coords(bullet_id)
            for enemy_id in self.enemies[:]:
                ex, ey = self.canvas.coords(enemy_id)
                if abs(bx - ex) < 50 and abs(by - ey) < 50:
                    self.destroy_objects(bullet_id, enemy_id)
                    self.score += 1
                    self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

    def spawn_enemy(self):
        x = R.randint(50, 450)
        enemy_id = self.canvas.create_image(x, 50, image=self.enemy_image, anchor="center")
        self.enemies.append(enemy_id)
        self.move_enemy(enemy_id)
        self.Interface.after(1000, self.spawn_enemy)

    def move_enemy(self, enemy_id):
        if self.canvas.coords(enemy_id):
            y = self.canvas.coords(enemy_id)[1]
            if y < 670:
                self.canvas.move(enemy_id, 0, 10)
                self.check_player_collision(enemy_id)
                self.Interface.after(100, lambda: self.move_enemy(enemy_id))
            else:
                self.enemies.remove(enemy_id)
                self.canvas.delete(enemy_id)

    def check_player_collision(self, enemy_id):
        ex, ey = self.canvas.coords(enemy_id)
        px, py = self.canvas.coords(self.character_id)
        if abs(px - ex) < 50 and abs(py - ey) < 50:
            self.destroy_objects(enemy_id, None)
            self.end_game()

    def destroy_objects(self, *ids):
        for obj_id in ids:
            if obj_id:
                self.canvas.delete(obj_id)
                if obj_id in self.enemies:
                    self.enemies.remove(obj_id)

    def end_game(self):
        x, y = self.canvas.coords(self.character_id)
        self.canvas.create_image(x, y, image=self.explosion_image)
        self.Interface.after(500, lambda: self.Interface.destroy())
        mb.showinfo("Game Over", "You have been destroyed!")

    def run(self):
        self.Interface.mainloop()

play()