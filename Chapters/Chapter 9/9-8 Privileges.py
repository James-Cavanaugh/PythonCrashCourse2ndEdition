# 9-5 Login Attempts.py
class User:
    def __init__(self, firstname, lastname, age, email, login_attempts=0):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.firstname} {self.lastname} is {self.age} years old and their email is {self.email}")

    def greet_user(self):
        print(f"Hello {self.firstname} {self.lastname}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, firstname, lastname, age, email, privileges, login_attempts=0):
        super().__init__(firstname, lastname, age, email, login_attempts)
        self.privileges = privileges

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

admin = Admin("John", "Doe", 30, "jdoe@gmail.com", Privileges(["get post", "create post", "remove post"]))
admin.privileges.show_privileges()
