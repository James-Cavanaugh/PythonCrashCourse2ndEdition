while True:
    topping = input("Enter a topping for your pizza\n(Type 'quit' to exit): ")
    if topping == "quit":
        break
    else:
        print(f"Adding {topping.title()} to your pizza!")
