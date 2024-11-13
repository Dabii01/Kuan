import tkinter as tk
from tkinter import messagebox as mb

class Account_Entry:
    def __init__(self):
        self.user_account = "user"
        self.user_password = "user123"
        self.admin_account = "admin"
        self.admin_password = "admin123"

    def user_click(self):
        user_login = tk.Tk()
        user_login.title("User login")
        user_login.geometry("500x300")

        tk.Label(user_login, text="Username:").place(x=100, y=80)
        User_account = tk.Entry(user_login)
        User_account.place(x=200, y=80)

        tk.Label(user_login, text="Password:").place(x=100, y=120)
        User_password = tk.Entry(user_login, show="*")
        User_password.place(x=200, y=120)

        login_button = tk.Button(user_login, text="Login", command=lambda: self.user_login(User_account.get(), User_password.get(), user_login))
        login_button.place(x=220, y=160)

        user_login.mainloop()

    def user_login(self, User_account, User_password, user_login):
        if User_account == self.user_account and User_password == self.user_password:
            mb.showinfo("Login", "User logged in successfully!")
        else:
            mb.showinfo("Can't Log In", "Account or password incorrect")
        user_login.destroy()

    def admin_click(self):
        admin_login = tk.Tk()
        admin_login.title("Admin login")
        admin_login.geometry("500x300")

        tk.Label(admin_login, text="Username:").place(x=100, y=80)
        Admin_account = tk.Entry(admin_login)
        Admin_account.place(x=200, y=80)

        tk.Label(admin_login, text="Password:").place(x=100, y=120)
        Admin_password = tk.Entry(admin_login, show="*")
        Admin_password.place(x=200, y=120)

        login_button = tk.Button(admin_login, text="Login", command=lambda: self.admin_login(Admin_account.get(), Admin_password.get(), admin_login))
        login_button.place(x=220, y=160)

        admin_login.mainloop()

    def admin_login(self, Admin_account, Admin_password, admin_login):
        if Admin_account == self.admin_account and Admin_password == self.admin_password:
            mb.showinfo("Login", "Admin logged in successfully!")
        else:
            mb.showinfo("Can't Log In", "Account or password incorrect")
        admin_login.destroy()

class Login_Interface:
    entry = Account_Entry()
    def __init__(self):
        self.interface = tk.Tk()
        self.interface.title("Space Impact")
        self.interface.geometry("500x700")

        self.user_button = tk.Button(self.interface, text="User", command=self.user_click)
        self.admin_button = tk.Button(self.interface, text="Admin", command=self.admin_click)
        self.user_button.place(x=250, y=250)
        self.admin_button.place(x=244, y=300)

    def user_click(self):
        self.entry.user_click()

    def admin_click(self):
        self.entry.admin_click()

    def run(self):
        self.interface.mainloop()

interface = Login_Interface()
print(interface.run())
