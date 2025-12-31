people = int(input("How many people are in your dinner group? "))
if people <= 0:
    print("Invalid")
elif people >= 8:
    print("You will have to wait for a table")
else:
    print("Alright, your table is ready")