username = input("Enter username: ").strip()
if len(username) <= 3:
    print("Invalid username")
else:
    print(f"Lowercase: {username.lower()}")
    print(f"Uppercase: {username.upper()}")
    print(f"Title: {username.title()}")
    print(f"Length: {len(username)}")