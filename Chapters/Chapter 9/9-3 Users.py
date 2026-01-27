class User:
    def __init__(self, firstname, lastname, age, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"{self.firstname} {self.lastname} is {self.age} years old and their email is {self.email}")

    def greet_user(self):
        print(f"Hello {self.firstname} {self.lastname}!")

user1 = User("Pat", "David", 30, "pdavid30@gmail.com")
user2 = User("Mark", "Zuckerberg", 56, "mzuckzuck@hotmail.com")
user3 = User("James", "Cavanaugh", 18, "james.arr.cavanaugh@gmail.com")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()