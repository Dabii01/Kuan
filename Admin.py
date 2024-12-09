import tkinter as tk
import random as R

class AdminLeaderboard:
    def __init__(self):
        self.admin_interface = tk.Tk()
        self.admin_interface.title("Admin Leaderboard")
        self.admin_interface.geometry("400x500")
        self.admin_interface.configure(bg="#008080")
        
        self.player_scores = [
            ("Player 1", 0),
            ("Player 2", 0),
            ("Player 3", 0),
            ("Player 4", 0),
            ("Player 5", 0),
        ]

        self.create_widgets()
        self.display_leaderboard()

    def create_widgets(self):
        
        self.highest_score_label = tk.Label(
            self.admin_interface,
            text="Highest Score: ",
            bg="#03313d",  
            fg="white",
            font=("Arial", 16, "bold"),
            padx=20,
            pady=10,
            relief="raised",  
            bd=5
        )
        self.highest_score_label.pack(pady=20)
        self.highest_player_label = tk.Label(
            self.admin_interface,
            text="Player: ",
            bg="#03313d",  
            fg="white",
            font=("Arial", 16, "bold"),
            padx=20,
            pady=10,
            relief="raised",
            bd=5
        )
        self.highest_player_label.pack(pady=10)

        self.leaderboard_frame = tk.Frame(self.admin_interface, bg="#03313d", relief="raised", padx=10, pady=10)
        self.leaderboard_frame.pack(pady=20)

        self.leaderboard_text = tk.Label(
            self.leaderboard_frame,
            bg="#03313d",  
            fg="white",
            font=("Arial", 20, "bold"),
            justify="left",
            padx=20,
            pady=30,
            relief="raised",
            bd=5
        )
        self.leaderboard_text.pack()

    def display_leaderboard(self):
        
        highest_player, highest_score = max(self.player_scores, key=lambda x: x[1])

        self.highest_score_label.config(text=f"Highest Score: {highest_score}")
        self.highest_player_label.config(text=f"Player: {highest_player.split()[1]}")  
        randomized_scores = R.sample([score for _, score in self.player_scores], len(self.player_scores))
        leaderboard_display = "\n".join(
            [f"{player}: {randomized_scores[i]}" for i, (player, _) in enumerate(self.player_scores)]
        )

        self.leaderboard_text.config(text=leaderboard_display)

    def run(self):
        self.admin_interface.mainloop()

interface = AdminLeaderboard()
interface.run()
