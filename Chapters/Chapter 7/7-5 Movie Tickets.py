while True:
    age = int(input("Enter your age\n(Enter '-1' to quit): "))
    if age == -1:
        break
    if age < 3:
        print("Your ticket is 0$!")
    elif age < 12:
        print("Your ticket is 10$!")
    else:
        print("Your ticket is 15$!")