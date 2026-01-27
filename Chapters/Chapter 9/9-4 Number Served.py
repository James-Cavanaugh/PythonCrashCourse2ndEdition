# 9-1 Restaurant.py
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

restaurant1 = Restaurant("Sushi Factory", "Asian")
print(restaurant1.number_served)
restaurant1.number_served = 3
print(restaurant1.number_served)
restaurant1.set_number_served(4)
print(restaurant1.number_served)
restaurant1.increment_number_served()
print(restaurant1.number_served)