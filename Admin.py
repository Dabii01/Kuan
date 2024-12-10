import tkinter as tk
import pickle

PLAYER_FILE = "player_info.pkl"
HIGH_SCORE_FILE = "high_score.pkl"
max = int(5)

def load_playerinfo():
    try:
        with open(PLAYER_FILE, "rb") as file:
            player_info = pickle.load(file)
        return player_info
    except FileNotFoundError:
        return []

def load_highscore():
    try:
        with open(HIGH_SCORE_FILE, "rb") as file:
            high_score = pickle.load(file)
        return high_score
    except FileNotFoundError:
        return 0

class AdminLeaderboard:
    def __init__(self):
        self.admin_interface = tk.Tk()
        self.admin_interface.title("Admin Leaderboard")
        self.admin_interface.geometry("500x650")
        self.admin_interface.configure(bg="#008080")

        self.show_highscore()
        self.show_scores()

    def show_highscore(self):
        high_score = load_highscore()
        self.highest_score = tk.Label(self.admin_interface, text=f"Highest Score: {high_score}", bg="#03313d",fg="white", font=("Arial", 16, "bold"), padx=20, pady=10, relief="raised", bd=5).pack(pady=20)

    def show_scores(self):
        player_info = load_playerinfo()
        if player_info:
            for i in range(len(player_info)):
                self.highest_score = tk.Label(self.admin_interface, text=f"Score: {player_info[i]}", bg="#03313d",fg="white", font=("Arial", 16, "bold"), padx=20, pady=10, relief="raised", bd=5).pack(pady=20+(1+3))
        else:
            None

    def run(self):
        self.admin_interface.mainloop()

def ShowInfo():
    Admin = AdminLeaderboard()
    Admin.run()
