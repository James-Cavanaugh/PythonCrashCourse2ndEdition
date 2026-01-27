# 9-4 Number Served.py
class Restaurant:
    def __init__(self, name, cuisine_type, number_served=0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.name} is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self):
        self.number_served += 1

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors, number_served=0):
        super().__init__(name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self):
        print(self.flavors)


stand = IceCreamStand("Joe's Creamery", "Ice Cream", "Vanilla, Chocolate, Oreo, Strawberry")
stand.display_flavors()