active = True
contacts = {}

while active:
    user_input = input("Welcome to the Contact Book!\n\t1. Add Contact\n\t2. Remove Contact\n\t3. Search for Contact\n\t4. View All Contacts\n\t5. Exit\n")
    if user_input == "1" or user_input == "1.":
        name = input("Enter the Contact Name: ").title()
        if name in contacts:
            print("Contact Name Already Exists!")
            continue
        number = input("Enter the Contact Number: ")
        if number in contacts.values():
            print("Contact Number Already Exists!")
            continue
        contacts[name] = number
    elif user_input == "2" or user_input == "2.":
        name = input("Enter the Contact Name: ").title()
        if name in contacts:
            del contacts[name]
        else:
            print("Contact Name Not Found!")
    elif user_input == "3" or user_input == "3.":
        name = input("Enter the Contact Name: ").title()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact Name Not Found!")
    elif user_input == "4" or user_input == "4.":
        for name, contact in contacts:
            print(f"{name}: {contact}")
    elif user_input == "5" or user_input == "5.":
        print("Thank you for using the Contact Book!")
        active = False
    else:
        print("Invalid Input, Try Again!")