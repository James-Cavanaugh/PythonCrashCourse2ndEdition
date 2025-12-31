# 7-4 Pizza Toppings
active = True
count = 0
while active:
    topping = input("Enter a topping for your pizza\n(Type 'quit' to exit): ")
    if topping == "quit":
        break
    else:
        print(f"Adding {topping.title()} to your pizza!")
        count += 1
    if count >= 3:
        active = False
        print("You have the maximum amount of toppings now!")
