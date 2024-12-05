import tkinter as tk
from tkinter import messagebox as mb
import customtkinter as ctk
import Game as SI


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Account_Entry:
    def __init__(self):
        self.user_account = "user"
        self.user_password = "user123"
        self.admin_account = "admin"
        self.admin_password = "admin123"

    def user_click(self):
        user_login = tk.Toplevel()
        user_login.title("User Login")
        user_login.geometry("500x300")
        user_login.configure(bg="#008080")  

        tk.Label(user_login, text="Username:", bg="#008080", fg="white").place(x=100, y=80)
        User_account = tk.Entry(user_login)
        User_account.place(x=200, y=80)

        tk.Label(user_login, text="Password:", bg="#008080", fg="white").place(x=100, y=120)
        User_password = tk.Entry(user_login, show="*")
        User_password.place(x=200, y=120)

        login_button = tk.Button(user_login, text="Login", command=lambda: self.user_login(User_account.get(), User_password.get()))
        login_button.place(x=220, y=160)

    def user_login(self, User_account, User_password):
        if User_account == self.user_account and User_password == self.user_password:
            SI.play()
        else:
            mb.showinfo("Can't Log In", "Account or password incorrect")

    def admin_click(self):
        admin_login = tk.Toplevel()
        admin_login.title("Admin Login")
        admin_login.geometry("500x300")
        admin_login.configure(bg="#008080")  

        tk.Label(admin_login, text="Username:", bg="#008080", fg="white").place(x=100, y=80)
        Admin_account = tk.Entry(admin_login)
        Admin_account.place(x=200, y=80)

        tk.Label(admin_login, text="Password:", bg="#008080", fg="white").place(x=100, y=120)
        Admin_password = tk.Entry(admin_login, show="*")
        Admin_password.place(x=200, y=120)

        login_button = tk.Button(admin_login, text="Login", command=lambda: self.admin_login(Admin_account.get(), Admin_password.get()))
        login_button.place(x=220, y=160)

    def admin_login(self, Admin_account, Admin_password):
        if Admin_account == self.admin_account and Admin_password == self.admin_password:
            mb.showinfo("Login", "Admin logged in successfully!")
        else:
            mb.showinfo("Can't Log In", "Account or password incorrect")

class Login_Interface:
    entry = Account_Entry()
    
    def __init__(self):
        self.interface = tk.Tk()
        self.interface.title("Select")
        self.interface.geometry("500x700")
        self.interface.configure(bg="#008080")  

        self.create_button("user", 0.4, self.user_click)
        self.create_button("admin", 0.6, self.admin_click)

    def create_button(self, text, rel_y, command):
        
        button = ctk.CTkButton(
            self.interface, 
            text=text, 
            font=("Arial", 20), 
            fg_color="#03313d",       
            hover_color="#044a5a",    
            text_color="white",       
            command=command,
            width=200,
            height=50,
            corner_radius=20,         
            border_width=0            
        )
        button.place(relx=0.5, rely=rel_y, anchor="center")

    def user_click(self):
        self.entry.user_click()

    def admin_click(self):
        self.entry.admin_click()

    def run(self):
        self.interface.mainloop()

interface = Login_Interface()
interface.run()