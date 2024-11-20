import Space_impact as S_I

class Log_in():
    def __init__(self):
        self.user_email="user"
        self.user_pass="user123"
        self.admin_email="admin"
        self.admin_pass="admin123"

    def user_login(self, email, password):
        if email == self.user_email and password == self.user_pass:
            S_I.play()
        else:
            print("Email or password is incorrect.")
            print()

    def admin_login(self, email, password):
        if email == self.user_email and password == self.user_pass:
            print("Sawadheeka")
        else:
            print("Email or password is incorrect.")
            print()

login=Log_in()
while True:
    print("---------------------------------------------- SELECT -------------------------------------------------")
    print("                  1. USER                        |                         2. ADMIN")
    choice=int(input("\nCHOOSE:  "))

    if choice==1:
        email=input("Enter user email: ")
        password=input("Enter user password: ")
        login.user_login(email, password)

    elif choice==1:
        email=input("Enter user email: ")
        password=input("Enter user password: ")
        login.admin_login(email, password)
