# 9-3 Users.py
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

user1 = User("Pat", "David", 30, "pdavid30@gmail.com")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
