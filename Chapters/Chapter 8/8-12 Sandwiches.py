def sandwich_order(*items):
    print("Your Sandwich will have:")
    for item in items:
        print(f"- {item}")

sandwich_order("beef", "cheese")
sandwich_order("chicken", "bacon", "ranch")
sandwich_order("chicken", "bacon", "ranch", "lettuce", "tomato", "pickles", "fried onions")